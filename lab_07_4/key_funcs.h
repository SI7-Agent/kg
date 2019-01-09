#ifndef KEY_FUNCS_H
#define KEY_FUNCS_H

int get_average(int *array_start, int *array_end, int size);
int get_filt_elems(int *array_start, int *array_end, int average);
void get_array_for_filter(int *array_start, int *array_end, int average, int *start_orig2, int *array2_end);

#endif