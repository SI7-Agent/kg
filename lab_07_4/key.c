#include <stdlib.h>
#include <stdio.h>

int key(int *array_start, int *array_end, int *array2_start, int *array2_end)
{
    int start_orig = array_start;
    int size = array_end - array_start;

    int average = 0;
    int ready_to_filter = 0;

    if (size == 0)
    {
        printf ("Incorrect Data");
        return -1;
    }

    array_start = start_orig;
    for (int i = 0; i < size; i++)
    {
        average = average + *array_start;
        if (array_start != array_end)
            array_start++;
    }

    average = average/size;

    array_start = start_orig;
    for (int i = 0; i < size; i++)
    {
        if (*array_start > average)
            ready_to_filter++;

        if (array_start != array_end)
            array_start++;
    }

    if (ready_to_filter == 0)
        return -1;

    array2_start = (int *)realloc(array2_start, ready_to_filter*sizeof(int));
    array2_end = array2_start+ready_to_filter;

    int start_orig2 = array2_start;

    array_start = start_orig;
    int size2 = 0;
    for (int i = 0; i < size; i++)
    {
        if (*array_start > average)
        {
            int temp = *array_start;
            *array2_start = temp;
            size2++;

            if (array2_start != array2_end)
                array2_start++;
        }

        if (array_start != array_end)
            array_start++;
    }

    array2_start = start_orig2;

    return ready_to_filter;
}
