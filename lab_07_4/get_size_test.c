#include <stdio.h>
#include <stdlib.h>

int get_size(FILE *f)
{
    int size = 0;
    int num;
    fseek(f, 0, SEEK_SET);

    while(fscanf(f, "%d", &num) == 1)
        size++;

    return size;
}
