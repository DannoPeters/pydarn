/*
 *
 *
 *Author: Marina Schmidt 
 */

#include <Python.h>
//#include <stdio.h>
#include <datetime.h>
//#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
//#include <errno.h>
#include <sys/time.h>
#include <unistd.h>
//#include <string.h>
#include <fcntl.h>
#include "rtypes.h"
#include "rconvert.h"
#include "rtime.h"
#include "dmap.h"
#include "structmember.h"

/*
 *Read dmap record:
 *              Reads a record 
 *
 *
 */
static PyObject *
read_dmap_rec(PyObject *self, PyObject *args)
{
    (void) self;
    (void) args;
    int fd; // file descriptor 
    FILE* fp=NULL;
    PyObject *error;
    /*Each fitacf record contains subrecords of data for each beam divided
     * by times 
     *
     *
     */
    PyObject *beam_record = PyDict_New();
    int nrange = 0;

    fp = fdopen(fd,"r"); // fp - file pointer
    if ( fp == NULL)
    {
        error = Py_BuildValue("i",&errno);
        return PyErr_SetFromErrno(error);
    }

    // dmap structures for scalar data and array data for each beam 
    struct DataMap *beamdata;
    struct DataMapScalar *scalardata; 
    struct DataMapArray *arraydata;

    beamdata = DataMapRead(fd);
    if ( beamdata == NULL)
    {
        error = Py_BuildValue("i",&errno);
        return PyErr_SetFromErrno(error);
    }
    PyObject *value;
   
    // snum - number of scalar values
    for(int i=0; i < beamdata->snum; i++)
    {
        scalardata = beamdata->scl[i];
        

        if (scalardata->type == DATASHORT)
        {   
            if ( strcmp(scalardata->name, "nrang") == 0 )
            {
                nrange = *(scalardata->data.sptr); // need this value for the vector arrays
            }
            value = Py_BuildValue("i",&(scalardata->data.sptr));   
        }    
        else if (scalardata->type == DATACHAR)
        {    
            value = Py_BuildValue("c",scalardata->data.cptr);
        }
        else if (scalardata->type == DATAINT)
        {    
            value = Py_BuildValue("i",*(scalardata->data.iptr));
        }
        else if (scalardata->type == DATAFLOAT)
        {    
            value = Py_BuildValue("f",*(scalardata->data.fptr));
        }
        else if (scalardata->type == DATAFLOAT)
        {    
            value = Py_BuildValue("d",*(scalardata->data.dptr));
            }
        else if (scalardata->type == DATASTRING)
        {
            value = Py_BuildValue("s",*((char **)scalardata->data.vptr));
        }
        else
        {
            Py_DECREF(value);
            Py_DECREF(beam_record);
            error = Py_BuildValue("i",-1);
            return PyErr_SetFromErrno(error);
        }
        
        if ( PyDict_SetItemString(beam_record,scalardata->name,value) < 0 )
        {
            Py_DECREF(value);
            Py_DECREF(beam_record);
            error = Py_BuildValue("i",-1);
            return PyErr_SetFromErrno(error);
        }
        PyCLEAR(value);
    }

    PyObject *vector_list = PyList_New(0);
    // Parse the vectors now
    for(int i=0; i < beamdata->anum;i++)
    {
        arraydata = beamdata->arr[i];
         // special case 
        if ( arraydata->dim <= 2 )
        {
            if (strcmp(arraydata->name,"ltab") == 0 && arraydata->type == DATASHORT)
            {
                for (int j=0; j < arraydata->rng[1]-1; j++)
                {
                    value = Py_BuildValue("[i,i]", arraydata->data.sptr[j+2], arraydata->data.sptr[j*2+1]);
                    PyList_Append(vector_list,value);
                    PyCLEAR(value);
                }
            }
            else
            {
                for(int j=0; j < arraydata->rng[0]; j++)
                {
                    if(arraydata->type == DATASHORT)
                    {
                        value = Py_BuildValue("i", arraydata->data.sptr[j]);
                    }
                    else if (scalardata->type == DATACHAR)
                    {    
                        value = Py_BuildValue("c",scalardata->data.cptr);
                    }
                    else if (scalardata->type == DATAINT)
                    {    
                        value = Py_BuildValue("i",*(scalardata->data.iptr));
                    }
                    else if (scalardata->type == DATAFLOAT)
                    {    
                        value = Py_BuildValue("f",*(scalardata->data.fptr));
                    }
                    else if (scalardata->type == DATAFLOAT)
                    {    
                        value = Py_BuildValue("d",*(scalardata->data.dptr));
                        }
                    else if (scalardata->type == DATASTRING)
                    {
                        value = Py_BuildValue("s",scalardata->data.vptr);
                    }
                    else
                    {
                                Py_DECREF(value);
                                Py_DECREF(vector_list);
                                Py_DECREF(beam_record);
                                error = Py_BuildValue("i",-1);
                                return PyErr_SetFromErrno(error);
                    }
                }
            }
        }
        else if (arraydata->dim ==  3) // parses acfd and xcfd
        {
            for(int j=0; j < nrange; j++)
            {
                for(int k=0; k < arraydata->rng[1]; k++)
                {
                    for (int m=0; m < 2; m++)
                    {
                            if(arraydata->type == DATAFLOAT)
                            {
                                value = Py_BuildValue("f",arraydata->data.fptr[(j*arraydata->rng[1]+k)*2+m]);
                            }
                            else
                            {
                                Py_DECREF(value);
                                Py_DECREF(vector_list);
                                Py_DECREF(beam_record);
                                error = Py_BuildValue("i",-1);
                                return PyErr_SetFromErrno(error);
                            }
                            PyList_Append(vector_list, value);
                            PyCLEAR(value);
                    }
                }
            }

        }
        if ( PyDict_SetItemString(beam_record,arraydata->name,vector_list) < 0 )
        {
            Py_DECREF(value);
            Py_DECREF(beam_record);
            Py_DECREF(vector_list);
            error = Py_BuildValue("i",-1);
            return PyErr_SetFromErrno(error);
        }
        PyCLEAR(value);
        PyCLEAR(vector_list);


    }
    Py_DECREF(value);
    Py_DECREF(vector_list);
   
    return beam_record;
}

static PyMethodDef dmapMethods[] = 
{
    {"read_dmap_rec", read_dmap_rec, METH_VARARGS, "reads a dmap record"},
    {NULL, 0, NULL, NULL} /* Sentinel */
};

static struct PyModuleDef dmapreader =
{
    PyModuleDef_HEAD_INIT,
    "dmapreader",
    "",
    -1,
    dmapMethods
};

PyMODINIT_FUNC PyInit_dampreader(void)
{
    return PyModule_Create(&dmapreader);
}
