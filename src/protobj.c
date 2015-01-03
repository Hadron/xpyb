#include "module.h"
#include "except.h"
#include "protobj.h"


/*
 * Infrastructure
 */

static PyObject *
xpybProtobj_new(PyTypeObject *self, PyObject *args, PyObject *kw)
{
    return PyType_GenericNew(self, args, kw);
}

static int
xpybProtobj_init(xpybProtobj *self, PyObject *args, PyObject *kw)
{
    static char *kwlist[] = { "parent", "offset", "size", NULL };
    Py_ssize_t offset = 0, size = -1;
    PyObject *parent;

    if (!PyArg_ParseTupleAndKeywords(args, kw, "O|nn", kwlist,
				     &parent, &offset, &size))
	return -1;

    self->buf = PyBuffer_FromObject(parent, offset, size);
    if (self->buf == NULL)
	return -1;
    
    return 0;
}

static void
xpybProtobj_dealloc(xpybProtobj *self)
{
    Py_CLEAR(self->buf);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

#if PY_MAJOR_VERSION < 3
#define BUFFER_TYPE PyBuffer_Type
#else
#define BUFFER_TYPE PyMemoryView_Type
#endif

#if PY_MAJOR_VERSION < 3
static Py_ssize_t
xpybProtobj_readbuf(xpybProtobj *self, Py_ssize_t s, void **p)
{
    return BUFFER_TYPE.tp_as_buffer->bf_getreadbuffer(self->buf, s, p);
}

static Py_ssize_t
xpybProtobj_segcount(xpybProtobj *self, Py_ssize_t *s)
{
    return BUFFER_TYPE.tp_as_buffer->bf_getsegcount(self->buf, s);
}

static Py_ssize_t
xpybProtobj_charbuf(xpybProtobj *self, Py_ssize_t s, char **p)
{
    return BUFFER_TYPE.tp_as_buffer->bf_getcharbuffer(self->buf, s, p);
}
#endif /* PY_MAJOR_VERSION < 3 */

#if PY_MAJOR_VERSION >= 3
static int
xpybProtobj_getbuffer(xpybProtobj *self, Py_buffer *buf, int i)
{
    return BUFFER_TYPE.tp_as_buffer->bf_getbuffer(self->buf, buf, i);
}

static void
xpybProtobj_releasebuffer(xpybProtobj *self, Py_buffer *buf)
{
    BUFFER_TYPE.tp_as_buffer->bf_releasebuffer(self->buf, buf);
}
#endif /* PY_MAJOR_VERSION >= 3 */

static Py_ssize_t
xpybProtobj_length(xpybProtobj *self)
{
    return PyMapping_Length(self->buf);
}

static PyObject *
xpybProtobj_concat(xpybProtobj *self, PyObject *arg)
{
    return BUFFER_TYPE.tp_as_sequence->sq_concat(self->buf, arg);
}

static PyObject *
xpybProtobj_repeat(xpybProtobj *self, Py_ssize_t arg)
{
    return BUFFER_TYPE.tp_as_sequence->sq_repeat(self->buf, arg);
}

static PyObject *
xpybProtobj_item(xpybProtobj *self, Py_ssize_t arg)
{
    return BUFFER_TYPE.tp_as_sequence->sq_item(self->buf, arg);
}

static int
xpybProtobj_ass_item(xpybProtobj *self, Py_ssize_t arg1, PyObject *arg2)
{
    return BUFFER_TYPE.tp_as_sequence->sq_ass_item(self->buf, arg1, arg2);
}

#if PY_MAJOR_VERSION >= 3
static PyObject *
xpybProtobj_subscript(xpybProtobj *self, PyObject *item)
{
    return BUFFER_TYPE.tp_as_mapping->mp_subscript(self->buf, item);
}

static int
xpybProtobj_ass_subscript(xpybProtobj *self, PyObject *item1, PyObject *item2)
{
    return BUFFER_TYPE.tp_as_mapping->mp_ass_subscript(self->buf, item1, item2);
}
#endif /* PY_MAJOR_VERSION >= 3 */

#if PY_MAJOR_VERSION < 3
static PyObject *
xpybProtobj_slice(xpybProtobj *self, Py_ssize_t arg1, Py_ssize_t arg2)
{
    return BUFFER_TYPE.tp_as_sequence->sq_slice(self->buf, arg1, arg2);
}

static int
xpybProtobj_ass_slice(xpybProtobj *self, Py_ssize_t arg1, Py_ssize_t arg2, PyObject *arg3)
{
    return BUFFER_TYPE.tp_as_sequence->sq_ass_slice(self->buf, arg1, arg2, arg3);
}
#endif /* PY_MAJOR_VERSION < 3 */

static int
xpybProtobj_contains(xpybProtobj *self, PyObject *arg)
{
    return BUFFER_TYPE.tp_as_sequence->sq_contains(self->buf, arg);
}

static PyObject *
xpybProtobj_inplace_concat(xpybProtobj *self, PyObject *arg)
{
    return BUFFER_TYPE.tp_as_sequence->sq_inplace_concat(self->buf, arg);
}

static PyObject *
xpybProtobj_inplace_repeat(xpybProtobj *self, Py_ssize_t arg)
{
    return BUFFER_TYPE.tp_as_sequence->sq_inplace_repeat(self->buf, arg);
}


/*
 * Members
 */


/*
 * Methods
 */


/*
 * Definition
 */

static PyBufferProcs xpybProtobj_bufops = {
#if PY_MAJOR_VERSION >= 3
    .bf_getbuffer = (getbufferproc)xpybProtobj_getbuffer,
    .bf_releasebuffer = (releasebufferproc)xpybProtobj_releasebuffer
#else
    .bf_getreadbuffer = (readbufferproc)xpybProtobj_readbuf,
    .bf_getsegcount = (segcountproc)xpybProtobj_segcount,
    .bf_getcharbuffer = (charbufferproc)xpybProtobj_charbuf
#endif
};

static PySequenceMethods xpybProtobj_seqops = {
    .sq_length = (lenfunc)xpybProtobj_length,
    .sq_concat = (binaryfunc)xpybProtobj_concat,
    .sq_repeat = (ssizeargfunc)xpybProtobj_repeat,
    .sq_item = (ssizeargfunc)xpybProtobj_item,
#if PY_MAJOR_VERSION < 3
    .sq_slice = (ssizessizeargfunc)xpybProtobj_slice,
#endif
    .sq_ass_item = (ssizeobjargproc)xpybProtobj_ass_item,
#if PY_MAJOR_VERSION < 3
    .sq_ass_slice = (ssizessizeobjargproc)xpybProtobj_ass_slice,
#endif
    .sq_contains = (objobjproc)xpybProtobj_contains,
    .sq_inplace_concat = (binaryfunc)xpybProtobj_inplace_concat,
    .sq_inplace_repeat = (ssizeargfunc)xpybProtobj_inplace_repeat
};

#if PY_MAJOR_VERSION >= 3
static PyMappingMethods xpybProtobj_mapops = {
    .mp_length = (lenfunc)xpybProtobj_length,
    .mp_subscript = (binaryfunc)xpybProtobj_subscript,
    .mp_ass_subscript = (objobjargproc)xpybProtobj_ass_subscript
};
#endif /* PY_MAJOR_VERSION >= 3 */

PyTypeObject xpybProtobj_type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "xcb.Protobj",
    .tp_basicsize = sizeof(xpybProtobj),
    .tp_init = (initproc)xpybProtobj_init,
    .tp_new = xpybProtobj_new,
    .tp_dealloc = (destructor)xpybProtobj_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_doc = "XCB generic X protocol object",
#if PY_MAJOR_VERSION >= 3
    .tp_as_mapping = &xpybProtobj_mapops,
#endif
    .tp_as_sequence = &xpybProtobj_seqops,
    .tp_as_buffer = &xpybProtobj_bufops
};

/*
 * Module init
 */
int xpybProtobj_modinit(PyObject *m)
{
    if (PyType_Ready(&xpybProtobj_type) < 0)
        return -1;
    Py_INCREF(&xpybProtobj_type);
    if (PyModule_AddObject(m, "Protobj", (PyObject *)&xpybProtobj_type) < 0)
	return -1;

    return 0;
}
