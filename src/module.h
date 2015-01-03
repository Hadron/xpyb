#ifndef XPYB_MODULE_H
#define XPYB_MODULE_H

#include <Python.h>
#include <structmember.h>

#include <xcb/xcb.h>
#include <xcb/xcbext.h>

extern PyTypeObject *xpybModule_core;
extern PyTypeObject *xpybModule_setup;
extern PyObject *xpybModule_core_events;
extern PyObject *xpybModule_core_errors;

extern PyObject *xpybModule_extdict;
extern PyObject *xpybModule_ext_events;
extern PyObject *xpybModule_ext_errors;

PyMODINIT_FUNC
#if PY_MAJOR_VERSION >= 3
PyInit_xcb(void);
#else
initxcb(void);
#endif

#if PY_MAJOR_VERSION < 3
PyObject *
PyMemoryView_FromMemory(char *mem, Py_ssize_t size, int flags);
#endif

#if PY_MAJOR_VERSION >= 3
PyObject *
PyBuffer_FromObject(PyObject *object, Py_ssize_t offset, Py_ssize_t size);
#endif

#endif
