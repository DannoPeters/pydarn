/*
 *
 *
 *Author: Marina Schmidt 
 */

#include <Python.h>
#include <stdio.h>
#include <datetime.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
#include <errno>
#include <sys/time.h>
#include <unistd.h>
#include <string.h>
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
    int fd; // file descriptor 
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
        return PyErr_SetFromErrno(errno);
    }

    // dmap structures for scalar data and array data for each beam 
    DataMap *beamdata;
    DataMapScalar *scalardata; 
    DataMapArray *arraydata;

    beamdata = DataMapRead(fd);
    if ( beamdata == NULL)
    {
        return PyErr_SetFromErrno(errno);
    }
    
    // snum - number of scalar values
    for(int i=0; i < beamdata->snum; i++)
    {
        s = beamdata->scl[i];
        PyObject *value;
        

        if (scalardata->type == DATASHORT)
        {   
            if ( strcmp(scalardata->name, "nrang") == 0 )
            {
                nrange = scalaradata->data.sptr; // need this value for the vector arrays
            }
            value = Py_BuildValue(("i",*(scalardata->data.sptr));   
        }    
        else if (scalardata->type == DATACHAR)
        {    
            value = Py_BuildValue("c"scalardata->data.cptr);
        }
        else if (scalardata->type == DATAINT)
        {    
            value = Py_BuildValue("i",*(scalardata->data.iptr))
        }
        else if (scalardata->type == DATAFLOAT)
        {    
            value = Py_BuildValue("f",*(scalardata->data.fptr))
        }
        else if (scalardata->tyoe == DATAFLOAT)
        {    
            value = Py_BuildValue("d",*(scalardata->data.dptr))
            }
        else if (scalardata->type == DATASTRING)
        {
            value = Py_BuildValue("s",*((char **)scalardata->data.vptr))
        }
        else
        {
            Py_DECREF(value);
            Py_DECREF(beam_record);
            return -1;
        }
        
        if ( PyDict_SetItemString(beam_record,scalardata->name,value) < 0 )
        {
            Py_DECREF(value);
            Py_DECREF(beam_record);
            return -1;

        }
        PyCLEAR(value)
    }

    // Parse the vectors now
    for(int i=0; i < beamdata->anum;i++)
    {
        arraydata = deamdata->arr[i];
        PyObject *vector_list = PyListNew(0);

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
                        value = Py_BuildValue("c"scalardata->data.cptr);
                    }
                    else if (scalardata->type == DATAINT)
                    {    
                        value = Py_BuildValue("i",*(scalardata->data.iptr))
                    }
                    else if (scalardata->type == DATAFLOAT)
                    {    
                        value = Py_BuildValue("f",*(scalardata->data.fptr))
                    }
                    else if (scalardata->tyoe == DATAFLOAT)
                    {    
                        value = Py_BuildValue("d",*(scalardata->data.dptr))
                        }
                    else if (scalardata->type == DATASTRING)
                    {
                        value = Py_BuildValue("s",data->data.vptr))
                    }
                    else
                    {
                                Py_DECREF(value);
                                Py_DECREF(vector_list);
                                Py_DECREF(beam_record);
                                return -1;

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
                            if(arraydata->type == DATAFlOAT)
                            {
                                value = Py_BuildValue("f",arraydata->fptr[(j*arraydata->rng[1]+k)*2+m]);
                            }
                            else
                            {
                                Py_DECREF(value);
                                Py_DECREF(vector_list);
                                Py_DECREF(beam_record);
                                return -1;

                            }
                            PyList_Append(vector_list, value);
                            PyClear(value);


                    }
                }
            }

        }
        if ( PyDict_SetItemString(beam_record,arraydata->name,vector_list) < 0 )
        {
            Py_DECREF(value);
            Py_DECREF(beam_record);
            Py_DECREF(vector_list);
            return -1;

        }
        PyCLEAR(value);
        PyCLEAR(vector_list);


    }
    Py_DECREF(value);
    Py_DECREF(vector_list);
   
    return beam_record;
}


