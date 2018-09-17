#ifndef FUNCTION_H
#define FUNCTION_H

int key(int *array_start, int *array_end, int *array2_start, int *array2_end);
int get_pos(FILE *f);
int get_size(FILE *f);
void mysort(int *array_start, int *array_end);
void read_array(FILE *f, int *array_orig);

#endif

