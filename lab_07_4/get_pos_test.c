#include <stdio.h>
#include <stdlib.h>

int get_pos(FILE *f)
{
    int num;
    int pos;
    fseek(f, 0, SEEK_SET);

    while(fscanf(f, "%d", &num) == 1)
        pos = ftell(f);

    return pos;
}
