#ifndef READ_ARRAY_TEST_H
#define READ_ARRAY_TEST_H

int *read_array(FILE *f, int size);
void output(int *array_start, int *array_end);
void record (FILE *f, int *array_start, int *array_end);
void record_empty(char *argv[]);

#endif