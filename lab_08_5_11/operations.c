#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"

float static **p = NULL;

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
		return NULL;

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            result[i][j] = matr1[i][j] + matr2[i][j];

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
	
	if (result == NULL)
		return NULL;

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

/**
 Преобразует исходную матрицу в матрицу без i-ой строки и j-ого столбца.

 * @param matr
 * @param p
 * @param i
 * @param j
 * @param m
 */

void get_matr(float **matr, float **p, int i, int j, int m)
{
    int ki, kj, di, dj;
    di = 0;
    for (ki = 0; ki< m-1 ; ki++)
    {
        if (ki == i)
            di = 1;
        dj = 0;
        for (kj = 0; kj< m-1; kj++)
        {
            if (kj == j)
                dj = 1;
            p[ki][kj] = matr[ki + di][kj + dj];
        }
    }
}

/**
 Вычисляет определитель матрицы.

 * @param matr
 * @param m
 * @param size
 * @return возвращает значение определителя, в случае, если под вспомогательную матрицу память не выделилась, возвращает -1.
 */

float determinant(float **matr, int m, int size)
{
    int i, d, k, n;
    if (m == size)
        p = allocate_matrix(m, m);

    else if (m > 2)
    {
        free(p[0]);
        free(p);

        p = allocate_matrix(m, m);
    }
	
	if (p == NULL)
	{
		FILE *f_error = fopen("error.txt", "w");
		fprintf(f_error, "%s", "allocat_error");
		fclose(f_error);
		return -1;
	}

    d = 0;
    k = 1;
    n = m - 1;
    if (m == 1)
    {
        d = matr[0][0];
        return d;
    }
    if (m == 2)
    {
        d = matr[0][0] * matr[1][1] - (matr[1][0] * matr[0][1]);
        return d;
    }
    if (m>2)
    {
        for (i = 0; i<m; i++)
        {
            get_matr(matr, p, i, 0, m);
            d = d + k * matr[i][0] * determinant(p, n, m);
            k = -k;
        }
    }

    free(p[0]);
    free(p);
    return d;
}
