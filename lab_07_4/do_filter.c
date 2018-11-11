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

void sort_with_filt(int *array_for_filter, int *array_for_filter_end, char *argv[])
{
    unsigned long long tb, te;
    tb = tick();
    mysort(array_for_filter, array_for_filter_end, sizeof(int), comp_int);
    te = tick();

    printf("\nSorted array:\n");
    output(array_for_filter, array_for_filter_end);

    printf("\nSort time: %llu nsec\n", (te - tb) / CLOCKS_PER_SEC);

    FILE *f_out = fopen(argv[2], "w");
    record(f_out, array_for_filter, array_for_filter_end);
    fclose(f_out);
}

void sort_with_no_filt(int *array_orig, int *array_orig_end,int *array_start, char *argv[])
{
    unsigned long long tb, te;
    array_orig = array_start;
    tb = tick();
    mysort(array_orig, array_orig_end, sizeof(int), comp_int);
    te = tick();

    array_orig = array_start;
    printf("\nSorted array:\n");
    output(array_orig, array_orig_end);

    printf("\nSort time: %llu nsec\n", (te - tb) / CLOCKS_PER_SEC);

    array_orig = array_start;
    FILE *f_out = fopen(argv[2], "w");
    record(f_out, array_orig, array_orig_end);
    fclose(f_out);
}

void work(int *code, char *argv[], int argc, int *array_orig, int *array_orig_end, int *array_start, int *array_for_filter, int *array_for_filter_end)
{
    int flag = 0;
    if ((argc > 3) && (strcmp(argv[3], "f") == 0))
    {
        flag = 1;
        array_orig = array_start;
        int size2 = key(array_orig, array_orig_end, &array_for_filter, &array_for_filter_end);

        if (size2 < 0)
            *code = -4;
    }

    if ((flag == 1)&&(*code != -4))
        sort_with_filt(array_for_filter, array_for_filter_end, argv);
    else if ((argc > 2)&&(flag == 0))
        sort_with_no_filt(array_orig, array_orig_end, array_start, argv);
}
