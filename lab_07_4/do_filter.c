#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>
#include <time.h>

#include "read_array_test.h"
#include "tick.h"
#include "key.h"
#include "get_size_test.h"
#include "mysort.h"
#include "do_filter.h"
#include "errors.h"

/**
 Выполняет сортировку отфильтрованного массива.

 * @param array_for_filter
 * @param array_for_filter_end
 * @param argv
 */

void sort_with_filt(int *array_for_filter, int *array_for_filter_end, char *argv[])
{
    mysort(array_for_filter, array_for_filter_end, sizeof(int), comp_int);

    printf("\nSorted array:\n");
    output(array_for_filter, array_for_filter_end);

    FILE *f_out = fopen(argv[2], "w");
    record(f_out, array_for_filter, array_for_filter_end);
    fclose(f_out);
}

/**
 Выполняет сортировку неотфильтрованного (исходного) массива.

 * @param array_orig
 * @param array_orig_end
 * @param array_start
 * @param argv
 */

void sort_with_no_filt(int *array_orig, int *array_orig_end,int *array_start, char *argv[])
{
    array_orig = array_start;
    mysort(array_orig, array_orig_end, sizeof(int), comp_int);

    array_orig = array_start;
    printf("\nSorted array:\n");
    output(array_orig, array_orig_end);

    array_orig = array_start;
    FILE *f_out = fopen(argv[2], "w");
    record(f_out, array_orig, array_orig_end);
    fclose(f_out);
}

/**
 Выполняет работу программы после окончания проверок файлов и выделения памяти.

 * @param code
 * @param argv
 * @param argc
 * @param array_orig
 * @param array_orig_end
 * @param array_start
 * @param array_for_filter
 * @param array_for_filter_end
 */

void work(int *code, char *argv[], int argc, int *array_orig, int *array_orig_end, int *array_start, int *array_for_filter, int *array_for_filter_end)
{
    int flag = 0;
    int size2;
    if ((argc > 3) && (strcmp(argv[3], "f") == 0))
    {
        flag = 1;
        array_orig = array_start;
        size2 = key(array_orig, array_orig_end, &array_for_filter, &array_for_filter_end);

        if (!array_for_filter)
            *code = mem_error;
        else if (size2 < 0)
            *code = bad_filter;
    }

    if ((flag == 1) && (size2 > 0) && (array_for_filter))
        sort_with_filt(array_for_filter, array_for_filter_end, argv);
    else if ((argc > 2) && (flag == 0))
        sort_with_no_filt(array_orig, array_orig_end, array_start, argv);
}
