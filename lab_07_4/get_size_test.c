#include <stdio.h>
#include <stdlib.h>

#include "errors.h"

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

/**
 Проверяет файл на пригодность к считыванию данных.

 * @param f
 * @return возвращает код ошибки.
 */

int check_file(FILE *f)
{
    int code = ok;
    if (!f)
        code = no_file;
    else
    {
        int size = get_size(f);
        if (size == 0)
            code = empty_file;
        else
        {
            long pos, pos_end;
            fseek(f, 0, SEEK_END);
            pos_end = ftell(f);
            pos = get_pos(f);

            if (pos != pos_end)
                code = bad_data_file;
        }
    }
    return code;
}