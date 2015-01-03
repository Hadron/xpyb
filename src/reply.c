#include "module.h"
#include "except.h"
#include "response.h"
#include "reply.h"

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
xpybReply_getattro(PyObject *self, PyObject *obj)
{
    xcb_generic_reply_t *data;
    Py_ssize_t size;

    if (PyObject_AsReadBuffer(self, (const void **)&data, &size) < 0)
	return NULL;

    if (Py_CompareWithASCIIString(obj, "length") == 0)
        return Py_BuildValue("I", data->length);

    return xpybReply_type.tp_base->tp_getattro(self, obj);
}


/*
 * Definition
 */

PyTypeObject xpybReply_type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "xcb.Reply",
    .tp_basicsize = sizeof(xpybReply),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_doc = "XCB generic reply object",
    .tp_base = &xpybResponse_type,
    .tp_getattro = xpybReply_getattro
};


/*
 * Module init
 */
int xpybReply_modinit(PyObject *m)
{
    if (PyType_Ready(&xpybReply_type) < 0)
        return -1;
    Py_INCREF(&xpybReply_type);
    if (PyModule_AddObject(m, "Reply", (PyObject *)&xpybReply_type) < 0)
	return -1;

    return 0;
}
