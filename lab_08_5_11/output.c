#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

/**
 Выводит матрицу на экран.
 * @brief output
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
