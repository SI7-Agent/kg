#include <stdlib.h>
#include <stdio.h>

void record (FILE *f, int *array_start, int *array_end)
{
    for (int i = 0; i < array_end - array_start; i++)
        fprintf(f, "%d ", *(array_start+i));
}
