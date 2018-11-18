#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"

/**
 Выполняет суммироование двух матриц.

 * @param matr1
 * @param matr2
 * @param rows
 * @param cols
 * @return возвращает указатель на результирующую матрицу.
 */

float **get_sum(float **matr1, float **matr2, int rows, int cols)
{
    float **result = allocate_matrix(rows, cols);

    if (!result)
        result = NULL;
    else
    {
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
                result[i][j] = matr1[i][j] + matr2[i][j];
    }

    return result;
}

/**
 Выполняет умножение двух матриц.

 * @param matr1
 * @param matr2
 * @param rows
 * @param cols
 * @param num1
 * @return возвращает указатель на результирующую матрицу, в случае, если память не выделилась, возвращает NULL.
 */

float **get_multy(float **matr1, float **matr2, int rows, int cols, int num1)
{
    float **result = allocate_matrix(rows, cols);

    if (!result)
        result = NULL;
    else
    {
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
            {
                float tmp = 0;
                for (int k = 0; k < num1; k++)
                    tmp += matr1[i][k] * matr2[k][j];
                result[i][j] = tmp;
            }
    }

    return result;
}

/**
 Преобразует исходную матрицу в матрицу без i-ой строки и j-ого столбца.

 * @param matr
 * @param p
 * @param i
 * @param j
 * @param m
 */

void get_minor(float **matr, float **p, int i, int j, int m)
{
    int current_i, current_j, flag_i, flag_j;
    flag_i = 0;
    for (current_i = 0; current_i < m - 1 ; current_i++)
    {
        if (current_i == i)
            flag_i = 1;
        flag_j = 0;
        for (current_j = 0; current_j < m - 1; current_j++)
        {
            if (current_j == j)
                flag_j = 1;
            p[current_i][current_j] = matr[current_i + flag_i][current_j + flag_j];
        }
    }
}

/**
 Вычисляет определитель матрицы.

 * @param matr
 * @param m
 * @param size
 * @return возвращает значение определтеля.
 */

float determinant(float **matr, int m, int size, int *err)
{
    float **p = NULL;
    int i, d, k, n;

    if (m == size)
        p = allocate_matrix(m, m);
    else if (m > 2)
    {
        free_matrix(p);
        p = allocate_matrix(m, m);
    }

    d = 0;
    k = 1;
    n = m - 1;
    if (m == 1)
        d = matr[0][0];
    if (m == 2)
        d = matr[0][0] * matr[1][1] - (matr[1][0] * matr[0][1]);
    if (m > 2)
    {
        if (p)
        {
            for (i = 0; i<m; i++)
            {
                get_minor(matr, p, i, 0, m);
                d = d + k * matr[i][0] * determinant(p, n, m, err);
                k = -k;
            }
        }
        else
            *err = 1;
    }
    if (p)
        free_matrix(p);
    return d;
}
