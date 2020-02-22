#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"
#include "errors.h"

/**
 Выполняет операцию сложения матриц со всеми проверками от получения файла второй матрицы до печати результата в файл.

 * @param matrix1
 * @param rows1
 * @param cols1
 * @param argv
 */

int make_sum(float **matrix1, float **matrix2, int rows1, int cols1, int rows2, int cols2, char *out)
{
    int code;
    output(matrix1, rows1, cols1);
    printf("\n");
    output(matrix2, rows2, cols2);

    if ((rows1 != rows2) || (cols1 != cols2))
        code = bad_sum;
    else
    {
        float **res = get_sum(matrix1, matrix2, rows1, cols1);

        if (!res)
            code = mem_error;
        else
        {
            printf("\n");
            output(res, rows1, cols1);
            record_matr(out, res, rows1, cols1);
            free_matrix(res);
        }
    }
    return code;
}

/**
 Выполняет операцию умножения матриц со всеми проверками от получения файла второй матрицы до печати результата в файл.

 * @param matrix1
 * @param rows1
 * @param cols1
 * @param argv
 */

int make_multy(float **matrix1, float **matrix2, int rows1, int cols1, int rows2, int cols2, char *out)
{
    int code = ok;
    output(matrix1, rows1, cols1);
    printf("\n");
    output(matrix2, rows2, cols2);

    if (cols1 != rows2)
        code = bad_multy;
    else
    {
        float **res2 = get_multy(matrix1, matrix2, rows1, cols2, rows2);

        if (!res2)
            code = mem_error;
        else
        {
            printf("\n");
            output(res2, rows1, cols2);
            record_matr(out, res2, rows1, cols2);
            free_matrix(res2);
        }
    }
    return code;
}

/**
 Выполняет операцию вычисления детерминанта со всеми проверками до печати результата в файл.

 * @param matrix1
 * @param rows1
 * @param cols1
 * @param argv
 */

int make_det(float **matrix1, int rows1, int cols1, char *argv)
{
    int code;
    output(matrix1, rows1, cols1);
    if (rows1 != cols1)
        code = bad_determ;
    else
    {
        int err = 0;
        float determ = determinant(matrix1, rows1, rows1, &err);
        if (err == 1)
            code = bad_determ;
        else
            record_num(argv, determ);
    }
    return code;
}

/**
 Выполняет операцию вывода справочной информации.

 */

int make_info()
{
    int code = ok;
    FILE *f_info = fopen("info.txt", "r");
		
    if (!f_info)
        code = no_info;
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
    return code;
}

/**
 Выполненяет программу.

 * @param argv
 */

void process(char *argv[], int argc, int *code)
{
    FILE *matr1 = fopen(argv[2], "r");

    if (!matr1)
        *code = no_file;
    else
    {
        int rows1 = 0, cols1 = 0;
        float **matrix1 = fill_matrix(matr1, &rows1, &cols1);
	
        if (matrix1)
        {
            if (argc > 4)
            {
                int rows2 = 0, cols2 = 0;
                FILE *matr2 = fopen(argv[3], "r");
                if (matr2)
                {
                    float **matrix2 = fill_matrix(matr2, &rows2, &cols2);

                    if (matrix2)
                    {
                        if (strcmp(argv[1], "a") == 0)
                            *code = make_sum(matrix1, matrix2, rows1, cols1, rows2, cols2, argv[4]);

                        if (strcmp(argv[1], "m") == 0)
                            *code = make_multy(matrix1, matrix2, rows1, cols1, rows2, cols2, argv[4]);
						
                        free_matrix(matrix2);
                    }
                    else
                        *code = mem_error;
                    fclose(matr2);
                }
                else
                    *code = no_file;
            }		    
			
            if (strcmp(argv[1], "o") == 0)
                *code = make_det(matrix1, rows1, cols1, argv[3]);

            if (strcmp(argv[1], "h") == 0)
                *code = make_info();

            free_matrix(matrix1);
        }
        else
            *code = mem_error;

        fclose(matr1);
    }
}
