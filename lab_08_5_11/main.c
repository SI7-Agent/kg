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
	{
		printf("Error opening file\n");
		return -1;
	}
	
    int rows1; int cols1;

    fscanf(matr1, "%d", &rows1);
    fscanf(matr1, "%d", &cols1);

    float **matrix1 = allocate_matrix(rows1, cols1);
	
	if (matrix1 == NULL)
	{
		printf("Allocation error\n");
		return -1;
	}
	
    fill_matrix(matr1, matrix1, rows1, cols1);

    if ((argc > 4) && (strcmp(argv[1], "a") == 0))
        make_sum(matr1, matrix1, rows1, cols1, argv);

    if ((argc > 4) && (strcmp(argv[1], "m") == 0))
        make_multy(matr1, matrix1, rows1, cols1, argv);

    if ((argc > 3) && (strcmp(argv[1], "o") == 0))
		make_det(matr1, matrix1, rows1, cols1, argv);
  
    if ((argc > 4) && (strcmp(argv[1], "h") == 0))
        make_info(argv);

    free_matrix(matrix1);
    fclose(matr1);

    return 0;
}
