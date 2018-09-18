#include <stdlib.h>
#include <stdio.h>

void output(int *array_start, int *array_end)
{
    for (int i = 0; i < array_end - array_start; i++)
        printf("%d\n", *(array_start+i));
}
