#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

/**
 Выделяет память под динамическую матрицу.

 * @param rows
 * @param cols
 * @return возвращает указатель на начало массива указателей, в случае, если память не выделилась, возвращает NULL.
 */

float **allocate_matrix(int rows, int cols)
{
    float **ptrs, *data;

    ptrs = malloc(rows * sizeof(float*));
	
	if (!ptrs)
		return NULL;
	
    data = malloc(rows * cols * sizeof(float));
	
	if (!data)
	{
		free(ptrs);
		return NULL;
	}

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

/**
 Очищает память под матрицу.

 * @param matr
 */

void free_matrix(float **matr)
{
	if (matr == NULL)
		return;
	
	free(matr[0]);
	free(matr);
}
