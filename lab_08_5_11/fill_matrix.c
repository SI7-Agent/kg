#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

/**
 Cчитывает матрицу из файла.
 * @brief fill_matrix
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
