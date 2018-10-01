#include <stdio.h>
#include <stdlib.h>

/**
 Узнает местоположение курсора после
 последнего удачно считанного числа.

 * @param f
 * @return возвращает местоположение курсора после
 последнего удачно считанного числа.
 */

int get_pos(FILE *f)
{
    int num;
    int pos;
    fseek(f, 0, SEEK_SET);

    while(fscanf(f, "%d", &num) == 1)
        pos = ftell(f);

    return pos;
}
