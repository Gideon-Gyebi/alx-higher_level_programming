#include <Python.h>

/**
 * print_python_list_info - Printing basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

  /* Get & print the size and allocated size of the list. */
	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

  /* Iterate through the list and print the type of each element. */
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

    /* Get the element at index `i`. */
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
