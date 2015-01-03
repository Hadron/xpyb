#include "module.h"
#include "except.h"
#include "response.h"

/*
 * Helpers
 */


/*
 * Infrastructure
 */


/*
 * Members
 */

#if PY_MAJOR_VERSION >= 3
#define Py_CompareWithASCIIString(obj, s) (PyUnicode_CompareWithASCIIString(obj, s))
#else
#define Py_CompareWithASCIIString(obj, s) (strcmp(PyString_AsString(obj), s))
#endif

static PyObject *
xpybResponse_getattro(PyObject *self, PyObject *obj)
{
    const xcb_generic_event_t *data;
    Py_ssize_t size;

    if (PyObject_AsReadBuffer(self, (const void **)&data, &size) < 0)
	return NULL;

    if (Py_CompareWithASCIIString(obj, "response_type") == 0)
	return Py_BuildValue("B", data->response_type);
    if (Py_CompareWithASCIIString(obj, "sequence") == 0)
	return Py_BuildValue("H", data->sequence);

    return xpybResponse_type.tp_base->tp_getattro(self, obj);
}


/*
 * Definition
 */

PyTypeObject xpybResponse_type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "xcb.Response",
    .tp_basicsize = sizeof(xpybResponse),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_doc = "XCB generic response object",
    .tp_base = &xpybProtobj_type,
    .tp_getattro = xpybResponse_getattro
};


/*
 * Module init
 */
int xpybResponse_modinit(PyObject *m)
{
    if (PyType_Ready(&xpybResponse_type) < 0)
        return -1;
    Py_INCREF(&xpybResponse_type);
    if (PyModule_AddObject(m, "Response", (PyObject *)&xpybResponse_type) < 0)
	return -1;

    return 0;
}
