#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"

/**
 Выполняет операцию сложения матриц со всеми проверками от получения файла второй матрицы до печати результата в файл.

 * @param matrix1
 * @param rows1
 * @param cols1
 * @param argv
 */

void make_sum(float **matrix1, int rows1, int cols1, char *argv[])
{
    output(matrix1, rows1, cols1);
    FILE *matr2 = fopen(argv[3], "r");
		
    if (!matr2)
    {
        printf("Error opening file\n");
        free_matrix(matrix1);
    }
    else
    {
        int rows2;
        int cols2;

        printf("\n");

        float **matrix2 = fill_matrix(matr2, &rows2, &cols2);
        output(matrix2, rows2, cols2);
        printf("\n");

        if ((rows1 != rows2) || (cols1 != cols2))
        {
            printf("\nERROR! Wrong sizes of matrixes\n");

            free_matrix(matrix2);
            fclose(matr2);
        }
        else
        {
            float **res = get_sum(matrix1, matrix2, rows1, cols1);

            if (res == NULL)
                printf("Result allocation error\n");
            else
            {
                output(res, rows1, cols1);
                record_matr(argv, res, rows1, cols1);
                free_matrix(res);
            }

            free_matrix(matrix2);
            fclose(matr2);
        }
    }
}

/**
 Выполняет операцию умножения матриц со всеми проверками от получения файла второй матрицы до печати результата в файл.

 * @param matrix1
 * @param rows1
 * @param cols1
 * @param argv
 */

void make_multy(float **matrix1, int rows1, int cols1, char *argv[])
{
    output(matrix1, rows1, cols1);
    FILE *matr2 = fopen(argv[3], "r");
	
    if (!matr2)
        printf("Error opening file\n");
    else
    {
        int rows2;
        int cols2;

        printf("\n");

        float **matrix2 = fill_matrix(matr2, &rows2, &cols2);
        output(matrix2, rows2, cols2);
        printf("\n");

        if (cols1 != rows2)
        {
            printf("\nERROR! Wrong sizes of matrixes\n");

            free_matrix(matrix2);
        }
        else
        {
            float **res2 = get_multy(matrix1, matrix2, rows1, cols2, rows2);

            if (res2 == NULL)
                printf("Result allocation error\n");
            else
            {
                output(res2, rows1, cols2);
                record_matr(argv, res2, rows1, cols2);
                free_matrix(res2);
            }

            free_matrix(matrix2);
            fclose(matr2);
        }
    }
}

/**
 Выполняет операцию вычисления детерминанта со всеми проверками до печати результата в файл.

 * @param matrix1
 * @param rows1
 * @param cols1
 * @param argv
 */

void make_det(float **matrix1, int rows1, int cols1, char *argv[])
{
    output(matrix1, rows1, cols1);
    if (rows1 != cols1)
    {
        printf("\nERROR! Nums of rows not equal nums of cols\n");
        free_matrix(matrix1);
    }
    else
    {
        int err = 0;
        float determ = determinant(matrix1, rows1, rows1, &err);
        if (err == 1)
            printf("Error in determinator function\n");
        else
            record_num(argv, determ);
    }
}

/**
 Выполняет операцию вывода справочной информации.

 */

void make_info()
{
    FILE *f_info = fopen("info.txt", "r");
		
    if (!f_info)
        printf("Error opening info file\n");
    else
    {
        char string[200];
        while (!(feof(f_info)))
        {
            fgets(string, 199, f_info);
            printf("%s", string);
        }
        fclose(f_info);
    }
}
