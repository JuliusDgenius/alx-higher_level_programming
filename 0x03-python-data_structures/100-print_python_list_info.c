

/**
 * print_python_list_info - Function prints basic info about Python lists.
 * @p: This parameter is a PyObject list
 */
void print_python_list_info(PyObject *p)
{
    int size, allocate, i;
    PyObject *obj;

    size = Py_SIZE(p);
    allocate = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocate);

    for (i = 0; i < size; i++)
    {
        printf("[*] Size of the {ython List = %d\n", size);
        printf("[*] Allocated = %d\n", allocate);

        for (int i = 0; i < size; i++)
        {
            printf("Element %d: ", i);
            
            obj = PyList_GetItem(p, i);
            printf("%s\n", Py_TYPE(obj)->tp_name);
        }
    }
}
