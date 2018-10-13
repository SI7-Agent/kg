#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "functions.h"

/**
 Выполняет умножение двух матриц.
 * @brief get_multy
 * @param matr1
 * @param matr2
 * @param rows
 * @param cols
 * @param num1
 * @return возвращает указатель на результирующую матрицу.
 */

float **get_multy(float **matr1, float **matr2, int rows, int cols, int num1)
{
    float **result = allocate_matrix(rows, cols);

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
        {
            float tmp = 0;
            for (int k = 0; k < num1; k++)
                tmp += matr1[i][k] * matr2[k][j];
            result[i][j] = tmp;
        }

    return result;
}
