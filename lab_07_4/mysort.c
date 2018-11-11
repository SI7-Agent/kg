#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 Cортирует по возрастанию массив array_start.

 * @param array_start
 * @param array_end
 * @param size
 */

void mysort (void* array_start, void* array_end, size_t size, int (*compar)(const void*, const void*))
{
    void *member = malloc(size*sizeof(void*)), *base = array_start;
    char *newElement, *location;
    char *start = (char*)array_start;
    char *end = (char*)array_end;
    start += size;
    for (; start < end; start += size)
    {
        newElement = start;
        memcpy(member, newElement, size);
        location = start - size;
        while((void*)location >= base && compar(location, newElement) > 0)
        {
            memcpy(member, newElement, size);
            memcpy(newElement, location, size);
            memcpy(location, member, size);
            location -= size;
            newElement -= size;
        }
    }
    free(member);
}

/**
 Сравнивает два элемента.

 * @param i
 * @param j
 * @return возвращает либо число, большее 0, либо меньшее 0, либо 0.
 */

int comp_int (const void *i, const void *j)
{
    return *(int*)i - *(int*)j;
}

