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

    if ((!f1 && f2) || (f1 && !f2))
        flag = 1;
    else if (!f1 && !f2)
        flag = 0;
    else
        do
        {
            ch1 = getc(f1);
            ch2 = getc(f2);
			
            if (!(feof(f1) && !feof(f2)) && (feof(f1) || feof(f2)))
                flag = 1;
        }
        while ((feof(f1) && feof(f2)) || feof(f1) || feof(f2) || ch1 != ch2);	
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
    }
    else
    {
        fclose(res);

        int rows1;
        int cols1;

        float **matrix1 = fill_matrix(matr1, &rows1, &cols1);

        make_det(matrix1, rows1, cols1, argv[3]);
        free_matrix(matrix1);
        fclose(matr1);

        res = fopen("out_0.txt", "r");

        if (compare_err(f, res) == 0)
        {
            printf("Test passed\n\n");
        }
        else
        {
            printf("Test didn't passed\n\n");
        }
        fclose(res);
    }
}

void sum_test(FILE *f, char *argv[])
{
    FILE *matr1 = fopen(argv[2], "r");
    FILE *matr2 = fopen(argv[3], "r");
    FILE *res = fopen("out_0.txt", "w");
	
    if ((!matr1) || (!matr2))
    {
        printf("Error opening file\n");
        printf("Test passed\n\n");
	
        fclose(res);
    }
    else
    {
        fclose(res);

        int rows1, rows2;
        int cols1, cols2;

        float **matrix1 = fill_matrix(matr1, &rows1, &cols1);
        float **matrix2 = fill_matrix(matr2, &rows2, &cols2);
		
        make_sum(matrix1, matrix2, rows1, cols1, rows2, cols2, argv[4]);
        free_matrix(matrix1);
        fclose(matr1);
        free_matrix(matrix2);
        fclose(matr2);

        res = fopen("out_0.txt", "r");

        if (compare_err(f, res) == 0)
        {
            printf("Test passed\n\n");
        }
        else
        {
            printf("Test didn't passed\n\n");
        }
        fclose(res);
    }
}

void mult_test(FILE *f, char *argv[])
{
    FILE *matr1 = fopen(argv[2], "r");
    FILE *matr2 = fopen(argv[3], "r");
    FILE *res = fopen("out_0.txt", "w");
	
    if ((!matr1) || (!matr2))
    {
        printf("Error opening file\n");
        printf("Test passed\n\n");
	
        fclose(res);
    }
    else
    {
        fclose(res);

        int rows1, rows2;
        int cols1, cols2;

        float **matrix1 = fill_matrix(matr1, &rows1, &cols1);
        float **matrix2 = fill_matrix(matr2, &rows2, &cols2);

        make_multy(matrix1, matrix2, rows1, cols1, rows2, cols2, argv[4]);
        free_matrix(matrix1);
        fclose(matr1);
        free_matrix(matrix2);
        fclose(matr2);

        res = fopen("out_0.txt", "r");

        if (compare_err(f, res) == 0)
        {
            printf("Test passed\n\n");
        }
        else
        {
            printf("Test didn't passed\n\n");
        }
        fclose(res);
    }
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
    printf("Files testing for concatination...\n");
    FILE *f7 = fopen("out_7.txt", "r");
    char *test7_argv[] = {"test.exe", "a", "in_711.txt", "in_712.txt", "out_0.txt"};
    sum_test(f7, test7_argv);
    fclose(f7);
    //-------
    printf("Files testing for multiplication...\n");
    FILE *f8 = fopen("out_8.txt", "r");
    char *test8_argv[] = {"test.exe", "m", "in_811.txt", "in_812.txt", "out_0.txt"};
    mult_test(f8, test8_argv);
    fclose(f8);
    //-------
    printf("Files testing for determinator...\n");
    FILE *f9 = fopen("out_9.txt", "r");
    char *test9_argv[] = {"test.exe", "o", "in_911.txt", "out_0.txt"};
    determ_test(f9, test9_argv);
    fclose(f9);
    //-------
    return 0;
}
