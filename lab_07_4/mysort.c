#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 Сортирует по возрастанию массив array_start.

 * @param array_start
 * @param array_end
 * @param size
 */

void mysort (void* array_start, void* array_end, size_t size, int (*compar)(const void*, const void*))
{
    void *newElement, *member = malloc(size*sizeof(void*)), *location, *base = array_start;
    array_start += size;
    for (; array_start < array_end; array_start += size)
    {
        newElement = array_start;
        memcpy(member, newElement, size);
        location = array_start - size;
        while(location >= base && compar(location, newElement) > 0)
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
