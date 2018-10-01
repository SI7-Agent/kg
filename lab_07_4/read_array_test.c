#include <stdio.h>
#include <stdlib.h>

/**
 Заполняет массив array_orig данными из файла f.

 * @param f
 * @param array_orig
 */

void read_array(FILE *f, int *array_orig, int *array_orig_end)
{
    int num;
    fseek(f, 0, SEEK_SET);

    int i = 0;
    while(fscanf(f, "%d", &num) == 1)
    {
        *array_orig = num;
        if (array_orig != array_orig_end)
            array_orig++;
    }
}
