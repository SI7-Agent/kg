#include <stdio.h>
#include <stdlib.h>

/**
 Вычисляет размер массива, хранящийся в файле f.

 * @param f
 * @return возвращает размер массива, хранящийся в файле f.
 */

int get_size(FILE *f)
{
    int size = 0;
    int num;
    fseek(f, 0, SEEK_SET);

    while(fscanf(f, "%d", &num) == 1)
        size++;

    return size;
}

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