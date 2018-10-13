#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

/**
 Преобразует исходную матрицу в матрицу без i-ой строки и j-ого столбца.
 * @brief get_matr
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
 * @brief determinant
 * @param matr
 * @param m
 * @param size
 * @return возвращает значение определтеля.
 */

float static **p;

float determinant(float **matr, int m, int size)
{
    int i, d, k, n;
    if (m == size)
    {
        p = (float**)malloc(m*sizeof(float*));
        for (i = 0; i<m; i++)
            p[i] = (float*)malloc(m*sizeof(float));
    }
    else if (m > 2)
    {
        for (int i = 0; i<m; i++)
            free(p[i]);
        free(p);

        p = (float**)malloc(m*sizeof(float*));
        for (i = 0; i<m; i++)
            p[i] = (float*)malloc(m*sizeof(float));
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
    for (int i = 0; i<m; i++)
        free(p[i]);
    free(p);
    return d;
}
