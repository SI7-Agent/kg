#include <stdio.h>
#include <stdlib.h>

void read_array(FILE *f, int *array_orig)
{
    int num;
    fseek(f, 0, SEEK_SET);

    int i = 0;
    while(fscanf(f, "%d", &num) == 1)
    {
        *(array_orig+i) = num;
        i++;
    }
}
