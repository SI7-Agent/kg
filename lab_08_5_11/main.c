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

        if ((argc > 4) && (strcmp(argv[1], "a") == 0))
            make_sum(matrix1, rows1, cols1, argv);

        if ((argc > 4) && (strcmp(argv[1], "m") == 0))
            make_multy(matrix1, rows1, cols1, argv);

        if ((argc > 3) && (strcmp(argv[1], "o") == 0))
            make_det(matrix1, rows1, cols1, argv);

        if ((argc > 4) && (strcmp(argv[1], "h") == 0))
            make_info();

        free_matrix(matrix1);
        fclose(matr1);
    }

    return 0;
}
