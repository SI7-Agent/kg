#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"

int main(int argc, char *argv[])
{
    FILE *matr1 = fopen(argv[2], "r");
    int rows1; int cols1;

    fscanf(matr1, "%d", &rows1);
    fscanf(matr1, "%d", &cols1);

    float **matrix1 = allocate_matrix(rows1, cols1);
    fill_matrix(matr1, matrix1, rows1, cols1);

    if ((argc > 4) && (strcmp(argv[1], "a") == 0))
    {
        output(matrix1, rows1, cols1);
        FILE *matr2 = fopen(argv[3], "r");
        int rows2; int cols2;

        fscanf(matr2, "%d", &rows2);
        fscanf(matr2, "%d", &cols2);

        printf("\n");
        float **matrix2 = allocate_matrix(rows2, cols2);
        fill_matrix(matr2, matrix2, rows2, cols2);
        output(matrix2, rows2, cols2);
        printf("\n");

        if ((rows1 != rows2) || (cols1 != cols2))
        {
            printf("\nERROR! Wrong sizes of matrixes\n");
            free(matrix1[0]);
            free(matrix1);
            fclose(matr1);

            free(matrix2[0]);
            free(matrix2);
            fclose(matr2);
            return -1;
        }
        float **res = get_sum(matrix1, matrix2, rows1, cols1);
        output(res, rows1, cols1);
        record_matr(argv, res, rows1, cols1);

        free(res[0]);
        free(res);

        free(matrix2[0]);
        free(matrix2);
        fclose(matr2);
    }

    if ((argc > 4) && (strcmp(argv[1], "m") == 0))
    {
        output(matrix1, rows1, cols1);
        FILE *matr2 = fopen(argv[3], "r");
        int rows2; int cols2;

        fscanf(matr2, "%d", &rows2);
        fscanf(matr2, "%d", &cols2);

        printf("\n");
        float **matrix2 = allocate_matrix(rows2, cols2);
        fill_matrix(matr2, matrix2, rows2, cols2);
        output(matrix2, rows2, cols2);
        printf("\n");

        if (cols1 != rows2)
        {
            printf("\nERROR! Wrong sizes of matrixes\n");
            free(matrix1[0]);
            free(matrix1);
            fclose(matr1);

            free(matrix2[0]);
            free(matrix2);
            fclose(matr2);
            return -1;
        }
        float **res2 = get_multy(matrix1, matrix2, rows1, cols2, rows2);
        output(res2, rows1, cols2);
        record_matr(argv, res2, rows1, cols2);

        free(res2[0]);
        free(res2);

        free(matrix2[0]);
        free(matrix2);
        fclose(matr2);
    }

    if ((argc > 3) && (strcmp(argv[1], "o") == 0))
    {
        output(matrix1, rows1, cols1);
        if (rows1 != cols1)
        {
            printf("ERROR! Nums of rows not equal nums of cols\n");
            free(matrix1[0]);
            free(matrix1);
            fclose(matr1);
            return -1;
        }

        float determ = determinant(matrix1, rows1, rows1);
        record_num(argv, determ);
    }

    if ((argc > 4) && (strcmp(argv[1], "h") == 0))
    {
        FILE *f_info = fopen("info.txt", "r");
        char string[200];
        while (f_info)
        {
            char * str = fgets(string, 199, f_info);
            if (str == NULL)
                break;
            printf("%s", string);
        }
        fclose(f_info);
    }

    free(matrix1[0]);
    free(matrix1);
    fclose(matr1);

    return 0;
}
