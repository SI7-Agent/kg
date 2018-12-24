#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

/**
 Выводит матрицу на экран.

 * @param matr
 * @param rows
 * @param cols
 */

void output(float **matr, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
            printf("%8.2f", matr[i][j]);
        printf("\n");
    }
}

/**
 Записывает матрицу в файл.

 * @param name_res
 * @param matr
 * @param rows
 * @param cols
 */

void record_matr(char *name_res, float **matr, int rows, int cols)
{
    FILE *f_res = fopen(name_res, "w");
	
    if (!f_res)
        printf("Error opening file\n");
    else
    {
        fprintf(f_res, "%d ", rows);
        fprintf(f_res, "%d\n", cols);

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
                fprintf(f_res, "%8.2f", matr[i][j]);
            fprintf(f_res, "\n");
        }

        fclose(f_res);
    }
}

/**
 Записывает число в файл.

 * @param name_res
 * @param num
 */

void record_num(char *name_res, float num)
{
    FILE *f_res = fopen(name_res, "w");
	
    if (!f_res)
        printf("Error opening file\n");
    else
    {
        fprintf(f_res, "%.2f", num);
        fclose(f_res);
    }
}
