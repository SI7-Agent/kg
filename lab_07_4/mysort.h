#ifndef MYSORT_H
#define MYSORT_H

void swap(char **newElement, char **location, void **member);
void mysort(void* array_start, size_t num, size_t size, int (*compar)(const void*, const void*));
int comp_int (const void *i, const void *j);

#endif