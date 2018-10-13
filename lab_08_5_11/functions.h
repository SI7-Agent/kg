#ifndef FUNCTIONS_H
#define FUNCTIONS_H

void fill_matrix(FILE *f, float **matr, int rows, int cols);
void output(float **matr, int rows, int cols);
void record_matr(char *name_res[], float **matr, int rows, int cols);
void record_num(char *name_res[], float num);
void get_matr(float **matr, float **p, int i, int j, int m);
float determinant(float **matr, int m, int size);
float **allocate_matrix(int rows, int cols);
float **get_multy(float **matr1, float **matr2, int rows, int cols, int num1);
float **get_sum(float **matr1, float **matr2, int rows, int cols);

#endif // FUNCTIONS_H
