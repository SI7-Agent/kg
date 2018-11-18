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
	
    if (ptrs)
    {
        data = malloc(rows * cols * sizeof(float));

        if (!data)
            free(ptrs);
        else
            for (int i = 0; i < rows; i++)
                ptrs[i] = data + i * cols;
    }

    return ptrs;
}

/**
 Считывает матрицу из файла.

 * @param f
 * @param matr
 * @param rows
 * @param cols
 */

float **fill_matrix(FILE *f, int *rows, int *cols)
{
    int row;
    int col;

    fscanf(f, "%d", &row);
    fscanf(f, "%d", &col);

    float **matrix = allocate_matrix(row, col);

    if (matrix)
    {
        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
            {
                float tmp;
                fscanf(f, "%f", &tmp);
                matrix[i][j] = tmp;
            }

        *rows = row;
        *cols = col;
    }

    return matrix;
}

/**
 Очищает память под матрицу.

 * @param matr
 */

void free_matrix(float **matr)
{
    if ((matr == NULL) || (matr[0] == NULL))
        printf("Error in free function\n");
    else
    {
        free(matr[0]);
        free(matr);
    }
}
