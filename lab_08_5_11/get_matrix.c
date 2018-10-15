#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

/**
 Выделяет память под динамическую матрицу.

 * @param rows
 * @param cols
 * @return возвращает указатель на начало массива указателей.
 */

float **allocate_matrix(int rows, int cols)
{
    float **ptrs, *data;

    ptrs = malloc(rows * sizeof(float*));
    data = malloc(rows * cols * sizeof(float));

    for (int i = 0; i < rows; i++)
        ptrs[i] = data + i * cols;

    return ptrs;
}

/**
 Считывает матрицу из файла.

 * @param f
 * @param matr
 * @param rows
 * @param cols
 */

void fill_matrix(FILE *f, float **matr, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
        {
            float tmp;
            fscanf(f, "%f", &tmp);
            matr[i][j] = tmp;
        }
}
