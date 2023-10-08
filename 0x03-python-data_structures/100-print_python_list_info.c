#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - f
 * @p: arg
 * 
 *Return: type 
 */
void print_python_list_info(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *pyObj;

    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", size);
    list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        
        pyObj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(pyObj)->tp_name);
        
    }
    
}
