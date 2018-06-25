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
#include <sys/time.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include "rtypes.h"
#include "rconvert.h"
#include "rtime.h"
#include "dmap.h"
#include "structmember.h"


static PyObject *
read_dmap_rec(PyObject *self, PyObject *args)
