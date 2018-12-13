#include <stdio.h>
#include <stdlib.h>

/**
 Создает массив и заполняет его данными из файла f.

 * @param f
 * @param size
 
 * @return возвращает указатель на начало заполненного массива.
 */

int *read_array(FILE *f, int size)
{
    int num;
    fseek(f, 0, SEEK_SET);

    int *array_orig = (int*)malloc(size * sizeof(int));
    int *array_orig_flag = array_orig;
    if (array_orig)
    {		
        int *array_orig_end = array_orig + size;
        while(fscanf(f, "%d", &num) == 1)
        {
            *array_orig = num;
            if (array_orig != array_orig_end)
                array_orig++;
        }
        array_orig = array_orig_flag;
    }
    return array_orig;
}

/**
 Выводит на экран массив array_start.

 * @param array_start
 * @param array_end
 */

void output(int *array_start, int *array_end)
{
    while (array_start != array_end)
    {
        printf("%d\n", *array_start);
        array_start++;
    }
}

/**
 Записывает массив array_start в файл f.

 * @param f
 * @param array_start
 * @param array_end
 */

void record(FILE *f, int *array_start, int *array_end)
{
    while (array_start != array_end)
    {
        fprintf(f, "%d ", *array_start);
        array_start++;
    }
}

/**
 Создает пустой выходной файл в случаях ошибок, предусмотренных в программе.

 * @param argv
 */

void record_empty(char *argv[])
{
    FILE *f_out_error = fopen(argv[2], "w");
    if (f_out_error)
    {
        fprintf(f_out_error, "%s", "");
        fclose(f_out_error);
    }
}
