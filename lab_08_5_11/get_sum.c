#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "functions.h"

/**
 Выполняет суммироование двух матриц.
 * @brief get_sum
 * @param matr1
 * @param matr2
 * @param rows
 * @param cols
 * @return возвращает указатель на результирующую матрицу.
 */

float **get_sum(float **matr1, float **matr2, int rows, int cols)
{
    float **result = allocate_matrix(rows, cols);

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            result[i][j] = matr1[i][j] + matr2[i][j];

    return result;
}
