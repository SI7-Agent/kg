#include <stdlib.h>
#include <stdio.h>

int key(int *array_start, int *array_end, int *array2_start, int *array2_end)
{
    int average = 0;
    int ready_to_filter = 0;

    if (array_end - array_start == 0)
    {
        printf ("Incorrect Data");
        return -1;
    }

    for (int i = 0; i < array_end - array_start; i++)
        average = average + *(array_start+i);

    average = average/(array_end - array_start);

    for (int i = 0; i < array_end - array_start; i++)
        if (*(array_start+i) > average)
            ready_to_filter++;

    printf("\nAfter filter %d object(-s):\n", ready_to_filter);

    if (ready_to_filter == 0)
    {
        printf("No elements to filter\n");
        return -1;
    }

    array2_start = (int *)realloc(array2_start, ready_to_filter*sizeof(int));
    array2_end = array2_start+ready_to_filter;

    int size2 = 0;
    for (int i = 0; i < array_end - array_start; i++)
    {
        if (*(array_start+i) > average)
        {
            int temp = *(array_start+i);
            *(array2_start+size2) = temp;
            size2++;
        }
    }

    for(int b = 0; b < size2; b++)
        printf("%d\n", *(array2_start+b));

    return ready_to_filter;
}
