#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"
#include "process.h"

int main(int argc, char *argv[])
{
    FILE *matr1 = fopen(argv[2], "r");
	
    if (!matr1)
        printf("Error opening file\n");
    else
    {
        int rows1;
        int cols1;

        float **matrix1 = fill_matrix(matr1, &rows1, &cols1);
        if (matrix1 != NULL)
        {
            if ((argc > 4) && (strcmp(argv[1], "a") == 0))
            {
                FILE *matr2 = fopen(argv[3], "r");
                if (!matr2)
                    printf("Error opening file\n");
                else
                {
                    int rows2;
                    int cols2;

                    float **matrix2 = fill_matrix(matr2, &rows2, &cols2);
                    if (matrix2 != NULL)
                    {
                        make_sum(matrix1, matrix2, rows1, cols1, rows2, cols2, argv);
                        free_matrix(matrix2);
                    }
                    else
                        printf("Allocation error\n");
                }

                fclose(matr2);
            }

            if ((argc > 4) && (strcmp(argv[1], "m") == 0))
            {
                FILE *matr2 = fopen(argv[3], "r");
                if (!matr2)
                    printf("Error opening file\n");
                else
                {
                    int rows2;
                    int cols2;

                    float **matrix2 = fill_matrix(matr2, &rows2, &cols2);
                    if (matrix2 != NULL)
                    {
                        make_multy(matrix1, matrix2, rows1, cols1, rows2, cols2, argv);
                        free_matrix(matrix2);
                    }
                    else
                        printf("Allocation error\n");
                }

                fclose(matr2);
            }

            if ((argc > 3) && (strcmp(argv[1], "o") == 0))
                make_det(matrix1, rows1, cols1, argv);

            if ((argc > 4) && (strcmp(argv[1], "h") == 0))
                make_info();

            free_matrix(matrix1);
        }
        else
            printf("Allocation error\n");

        fclose(matr1);
    }

    return 0;
}
