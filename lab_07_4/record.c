#include <stdlib.h>
#include <stdio.h>

/**
 Записывает массив array_start в файл f.

 * @param f
 * @param array_start
 * @param array_end
 */

void record (FILE *f, int *array_start, int *array_end)
{
    int size = array_end - array_start;
    for (int i = 0; i < size; i++)
    {
        fprintf(f, "%d ", *array_start);
        if (array_start != array_end)
            array_start++;
    }
}
