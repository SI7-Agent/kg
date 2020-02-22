#include <stdio.h>

float **allocate_matrix(int rows, int cols);
float **fill_matrix(FILE *f, int *rows, int *cols);
void free_matrix(float **matr);
