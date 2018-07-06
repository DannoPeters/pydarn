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

        // Go through all possible scalar values and add them to the dictionary
        if ((strcmp(s->name,"radar.revision.major")==0) && (s->type==DATACHAR))
        {
            value = PyChar_FromChar((char)s->data.cptr);
            if ( PyDict_SetItemString(beam_record, "radar revision major", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
        if ((strcmp(s->name,"radar.revision.minor")==0) && (s->type==DATACHAR))
        {
            value = PyChar_FromChar((char)s->data.cptr);
            if ( PyDict_SetItemString(beam_record, "radar revision minor", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
        else if ((strcmp(s->name,"origin.code")==0) && (s->type==DATACHAR))
         {
            value = PyChar_FromChar((char)s->data.cptr);
            if ( PyDict_SetItemString(beam_record, "origin code", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        } 
        else if ((strcmp(s->name,"origin.time")==0) && (s->type==DATASTRING))
          {
            value = PyString_((char **)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "day", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
      
        else if ((strcmp(s->name,"time.hr")==0) && (s->type==DATASHORT))
           {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "hour", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
     
        else if ((strcmp(s->name,"time.mt")==0) && (s->type==DATASHORT))
            {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "minute", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
    
        else if ((strcmp(s->name,"time.sc")==0) && (s->type==DATASHORT))
             {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "seconds", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
   
        else if ((strcmp(s->name,"time.us")==0) && (s->type==DATAINT))
        {
            // Does this actually work? should we store it as a double?
            value = PyInt_FromInt(((int)(((int)(*(s->data.iptr)*1e-3))*1e3)));
            if ( PyDict_SetItemString(beam_record, "us", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
        if ((strcmp(s->name,"nrang")==0) && (s->type==DATASHORT))
        {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "nrang", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
        if ((strcmp(s->name,"time.yr")==0) && (s->type==DATASHORT))
        {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "year", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
        else if ((strcmp(s->name,"time.mo")==0) && (s->type==DATASHORT))
         {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "month", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        } 
        else if ((strcmp(s->name,"time.dy")==0) && (s->type==DATASHORT))
          {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "day", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
      
        else if ((strcmp(s->name,"time.hr")==0) && (s->type==DATASHORT))
           {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "hour", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
     
        else if ((strcmp(s->name,"time.mt")==0) && (s->type==DATASHORT))
            {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "minute", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
    
        else if ((strcmp(s->name,"time.sc")==0) && (s->type==DATASHORT))
             {
            value = PyInt_FromShort((short)s->data.sptr);
            if ( PyDict_SetItemString(beam_record, "seconds", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
   
        else if ((strcmp(s->name,"time.us")==0) && (s->type==DATAINT))
        {
            // Does this actually work? should we store it as a double?
            value = PyInt_FromInt(((int)(((int)(*(s->data.iptr)*1e-3))*1e3)));
            if ( PyDict_SetItemString(beam_record, "us", value) < 0 )
            {
                Py_DECREF(value);
                return -1; 
            }
        }
 

}


