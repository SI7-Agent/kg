#include <stdlib.h>
#include <stdio.h>

void output(int *array_start, int *array_end)
{
    int size = array_end - array_start;
    for (int i = 0; i < size; i++)
    {
        printf("%d\n", *array_start);
        if (array_start != array_end)
            array_start++;
    }
}
