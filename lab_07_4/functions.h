#ifndef FUNCTION_H
#define FUNCTION_H

int key(int *array_start, int *array_end, int *array2_start, int *array2_end);
void mysort(int *array_start, int *array_end);
void output(int *array_start, int *array_end);
void record (FILE *f, int *array_start, int *array_end);
unsigned long long tick(void);

#endif
