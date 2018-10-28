#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"

void make_sum(FILE *matr1, float **matrix1, int rows1, int cols1, char *argv[])
{
	output(matrix1, rows1, cols1);
        FILE *matr2 = fopen(argv[3], "r");
		
		if (!matr2)
		{
			printf("Error opening file\n");
			free_matrix(matrix1);
			return ;
		}
		
        int rows2; int cols2;

        fscanf(matr2, "%d", &rows2);
        fscanf(matr2, "%d", &cols2);

        printf("\n");
        float **matrix2 = allocate_matrix(rows2, cols2);
		
		if (matrix2 == NULL)
		{
			printf("Allocation error\n");
			free_matrix(matrix1);
			return ;
		}
	
        fill_matrix(matr2, matrix2, rows2, cols2);
        output(matrix2, rows2, cols2);
        printf("\n");

        if ((rows1 != rows2) || (cols1 != cols2))
        {
            printf("\nERROR! Wrong sizes of matrixes\n");
            free_matrix(matrix1);
            fclose(matr1);

            free_matrix(matrix2);
            fclose(matr2);
            return ;
        }
        float **res = get_sum(matrix1, matrix2, rows1, cols1);
		
		if (res == NULL)
		{
			printf("Allocation error\n");
			return ;
		}
		
        output(res, rows1, cols1);
        record_matr(argv, res, rows1, cols1);

        free_matrix(res);

        free_matrix(matrix2);
        fclose(matr2);
}

void make_multy(FILE *matr1, float **matrix1, int rows1, int cols1, char *argv[])
{
	output(matrix1, rows1, cols1);
    FILE *matr2 = fopen(argv[3], "r");
	
	if (!matr2)
	{
		printf("Error opening file\n");
		return ;
	}
		
    int rows2; int cols2;

    fscanf(matr2, "%d", &rows2);
    fscanf(matr2, "%d", &cols2);

    printf("\n");
    float **matrix2 = allocate_matrix(rows2, cols2);
		
	if (matrix2 == NULL)
	{
		printf("Allocation error\n");
		return ;
	}
		
    fill_matrix(matr2, matrix2, rows2, cols2);
    output(matrix2, rows2, cols2);
    printf("\n");

    if (cols1 != rows2)
    {
        printf("\nERROR! Wrong sizes of matrixes\n");
        free_matrix(matrix1);
        fclose(matr1);

        free_matrix(matrix2);
        fclose(matr2);
        return ;
    }
    float **res2 = get_multy(matrix1, matrix2, rows1, cols2, rows2);
		
	if (res2 == NULL)
	{
		printf("Allocation error\n");
		return ;
	}
		
    output(res2, rows1, cols2);
    record_matr(argv, res2, rows1, cols2);

    free_matrix(res2);

    free_matrix(matrix2);
    fclose(matr2);	
}

void make_det(FILE *matr1, float **matrix1, int rows1, int cols1, char *argv[])
{
	output(matrix1, rows1, cols1);
    if (rows1 != cols1)
    {
        printf("ERROR! Nums of rows not equal nums of cols\n");
        free_matrix(matrix1);
        fclose(matr1);
        return ;
    }

	FILE *f_error = fopen("error.txt", "w");
	fclose(f_error);
    float determ = determinant(matrix1, rows1, rows1);
	
	f_error = fopen("error.txt", "r");
	
	char error[15];
	fscanf(f_error, "%s", error);
	if (strcmp(error, "allocat_error") == 0)
	{
		printf("Error while computing determinator\n");
		return;
	}
	
    record_num(argv, determ);
}

void make_info(char *argv[])
{
	FILE *f_info = fopen("info.txt", "r");
		
	if (!f_info)
	{
		printf("Error opening file\n");
		return ;
	}
		
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