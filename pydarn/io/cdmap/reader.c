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
    PyObject *fitacf_record = PyList_New(); 
    PyObject *beam_record = PyDict_New();
    

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
        

        if (s->type == DATASHORT)
        {    
            value = Py_BuildValue(("i",*(s->data.sptr));   
        }    
        else if (s->type == DATACHAR)
        {    
            value = Py_BuildValue("c"s->data.cptr);
        }
        else if (s->type == DATAINT)
        {    
            value = Py_BuildValue("i",*(s->data.iptr))
        }
        else if (s->type == DATAFLOAT)
        {    
            value = Py_BuildValue("f",*(s->data.fptr))
        }
        else if (s->tyoe == DATAFLOAT)
        {    
            value = Py_BuildValue("d",*(s->data.dptr))
            }
        else if (s->type == DATASTRING)
        {
            value = Py_BuildValue("s",*((char **)s->data.vptr))
        }
        else
        {
            Py_DECREF(value);
            Py_DECREF(fitacf_record);
            Py_DECREF(beam_record);
            return -1;
        }
        
        if ( PyDict_SetItemString(beamData,s->name,value) < 0 )
        {
            Py_DECREF(value);
            Py_DECREF(fitacf_record);
            Py_DECREF(beam_record);
            return -1;

        }
        PyCLEAR(value)
    }
    return 0;
}


