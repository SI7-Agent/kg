#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>
#include <math.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"
#include "process.h"

int compare_err(FILE *f1, FILE *f2)
{
    int flag = 0;

    char ch1;
    char ch2;

    if ((f1 == NULL && f2 != NULL) || (f1 != NULL && f2 == NULL))
        flag = 1;
    else if (f1 == NULL && f2 == NULL)
        flag = 0;
    else
        while (1)
        {
            ch1 = getc(f1);
            ch2 = getc(f2);

            if (feof(f1) && feof(f2))
                break;
            else if (feof(f1) || feof(f2) || ch1 != ch2)
            {
                flag = 1;
                break;
            }
        }
    return flag;
}

void determ_test(FILE *f, char *argv[])
{
	FILE *matr1 = fopen(argv[2], "r");
	FILE *res = fopen("out_0.txt", "w");
	
	if (!matr1)
	{
		printf("Error opening file\n");
		printf("Test passed\n\n");
	
		fclose(res);
		return ;
	}
	else

	fclose(res);
	
    int rows1; int cols1;

    fscanf(matr1, "%d", &rows1);
    fscanf(matr1, "%d", &cols1);

    float **matrix1 = allocate_matrix(rows1, cols1);
	
	if (matrix1 == NULL)
	{
		printf("Allocation error\n");
		return ;
	}
	
    fill_matrix(matr1, matrix1, rows1, cols1);
	
    make_det(matr1, matrix1, rows1, cols1, argv);
	free_matrix(matrix1);
    fclose(matr1);

	res = fopen("out_0.txt", "r");
	
    if (compare_err(f, res) == 0)
	{printf("Test passed\n\n");}
    else
	{printf("Test didn't passed\n\n");}
	fclose(res);
}

void sum_test(FILE *f, char *argv[])
{
	FILE *matr1 = fopen(argv[2], "r");
	FILE *res = fopen("out_0.txt", "w");
	
	if (!matr1)
	{
		printf("Error opening file\n");
		printf("Test passed\n\n");
	
		fclose(res);
		return ;
	}
	else

	fclose(res);
	
    int rows1; int cols1;

    fscanf(matr1, "%d", &rows1);
    fscanf(matr1, "%d", &cols1);

    float **matrix1 = allocate_matrix(rows1, cols1);
	
	if (matrix1 == NULL)
	{
		printf("Allocation error\n");
		return ;
	}
	
    fill_matrix(matr1, matrix1, rows1, cols1);
	
    make_sum(matr1, matrix1, rows1, cols1, argv);
	free_matrix(matrix1);
    fclose(matr1);

	res = fopen("out_0.txt", "r");
	
    if (compare_err(f, res) == 0)
	{printf("Test passed\n\n");}
    else
	{printf("Test didn't passed\n\n");}
	fclose(res);
}

void mult_test(FILE *f, char *argv[])
{
	FILE *matr1 = fopen(argv[2], "r");
	FILE *res = fopen("out_0.txt", "w");
	
	if (!matr1)
	{
		printf("Error opening file\n");
		printf("Test passed\n\n");
	
		fclose(res);
		return ;
	}

	fclose(res);
	
    int rows1; int cols1;

    fscanf(matr1, "%d", &rows1);
    fscanf(matr1, "%d", &cols1);

    float **matrix1 = allocate_matrix(rows1, cols1);
	
	if (matrix1 == NULL)
	{
		printf("Allocation error\n");
		return ;
	}
	
    fill_matrix(matr1, matrix1, rows1, cols1);
	
    make_multy(matr1, matrix1, rows1, cols1, argv);
	free_matrix(matrix1);
    fclose(matr1);
	
	res = fopen("out_0.txt", "r");
	
    if (compare_err(f, res) == 0)
	{printf("Test passed\n\n");}
    else
	{printf("Test didn't passed\n\n");}
	
	fclose(res);
}

int main()
{
    FILE *f1 = fopen("out_3.txt", "r");
    printf("Summing up testing...\n");
	char *test1_argv[] = {"test.exe", "a", "in_31.txt", "in_32.txt", "out_0.txt"};
    sum_test(f1, test1_argv);
    fclose(f1);
    //-------
    FILE *f2 = fopen("out_2.txt", "r");
    printf("Multipling testing...\n");
	char *test2_argv[] = {"test.exe", "m", "in_21.txt", "in_22.txt", "out_0.txt"};
    mult_test(f2, test2_argv);
    fclose(f2);
    //-------
    FILE *f3 = fopen("out_1.txt", "r");
    printf("Determinant testing...\n");
	char *test3_argv[] = {"test.exe", "o", "in_11.txt", "out_0.txt"};
    determ_test(f3, test3_argv);
    fclose(f3);
	//-------
	printf("Data testing for concatination...\n");
	FILE *f4 = fopen("out_4.txt", "r");
	char *test4_argv[] = {"test.exe", "a", "in_41.txt", "in_42.txt", "out_0.txt"};
    sum_test(f4, test4_argv);
    fclose(f4);
	//-------
	printf("Data testing for multiplication...\n");
	FILE *f5 = fopen("out_5.txt", "r");
	char *test5_argv[] = {"test.exe", "m", "in_51.txt", "in_52.txt", "out_0.txt"};
    mult_test(f5, test5_argv);
    fclose(f5);
	//-------
	printf("Data testing for determinator...\n");
	FILE *f6 = fopen("out_6.txt", "r");
	char *test6_argv[] = {"test.exe", "o", "in_61.txt", "out_0.txt"};
    determ_test(f6, test6_argv);
    fclose(f6);
	//-------
	printf("Files testing for concatination...\n");
	FILE *f7 = fopen("out_7.txt", "r");
	char *test7_argv[] = {"test.exe", "a", "in_711.txt", "in_712.txt", "out_0.txt"};
    sum_test(f7, test7_argv);
    fclose(f7);
	//-------
	printf("Data testing for multiplication...\n");
	FILE *f8 = fopen("out_8.txt", "r");
	char *test8_argv[] = {"test.exe", "m", "in_811.txt", "in_812.txt", "out_0.txt"};
    mult_test(f8, test8_argv);
    fclose(f8);
	//-------
	printf("Data testing for determinator...\n");
	FILE *f9 = fopen("out_9.txt", "r");
	char *test9_argv[] = {"test.exe", "o", "in_911.txt", "out_0.txt"};
    determ_test(f9, test9_argv);
    fclose(f9);
	//-------
    return 0;
}
