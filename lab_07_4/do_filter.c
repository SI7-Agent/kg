#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "read_array_test.h"
#include "key.h"
#include "get_size_test.h"
#include "mysort.h"
#include "do_filter.h"
#include "errors.h"

/**
 Выполняет работу программы после окончания проверок файлов и выделения памяти.

 * @param argv
 * @param argc
 * @param array_orig
 * @param array_orig_end
 * @param array_for_filter
 * @param array_for_filter_end
 
 * @return возвращает код ошибки.
 */

int work(char *argv[], int argc, int *array_orig, int *array_orig_end, int *array_for_filter, int *array_for_filter_end)
{
    int code = ok;
    printf("Read array:\n");
    output(array_orig, array_orig_end);
	
    if ((argc > 3) && (strcmp(argv[3], "f") == 0))
    {
        code = key(array_orig, array_orig_end, &array_for_filter, &array_for_filter_end);
		free(array_orig);
        array_orig = array_for_filter;
        array_orig_end = array_for_filter_end;
    }

    if (code == ok)
    {
        mysort(array_orig, array_orig_end - array_orig, sizeof(int), comp_int);
        printf("\nSorted array:\n");
        output(array_orig, array_orig_end);
        FILE *f_out = fopen(argv[2], "w");
        if (f_out)
        {
            record(f_out, array_orig, array_orig_end);
            fclose(f_out);
        }
        free(array_orig);
    }
    return code;
}
