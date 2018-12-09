#ifndef READ_ARRAY_TEST_H
#define READ_ARRAY_TEST_H

void read_array(FILE *f, int *array_orig, int *array_orig_end);
void output(int *array_start, int *array_end);
void record (FILE *f, int *array_start, int *array_end);
void record_empty(char *argv[]);

#endif