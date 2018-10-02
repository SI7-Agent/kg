#ifndef FUNCTION_H
#define FUNCTION_H

int key(int *array_start, int *array_end, int *array2_start, int *array2_end);
int get_pos(FILE *f);
int get_size(FILE *f);
int comp_int(const void *i, const void *j);
void mysort(int *array_start, int *array_end);
void output(int *array_start, int *array_end);
void record (FILE *f, int *array_start, int *array_end);
void read_array(FILE *f, int *array_orig, int *array_orig_end);
unsigned long long tick(void);

#endif
