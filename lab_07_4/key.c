#include <stdlib.h>
#include <stdio.h>
#include "key_funcs.h"
#include "errors.h"

/**
 Фильтрует указанным способом массив array_start,
 под полученное число элементов создается массив array2_start,
 в который копируются элементы, удовлетворяющие фильтру.

 * @param array_start
 * @param array_end
 * @param array2_start
 * @param array2_end

 * @return возвращает размер отфильтрованного массива
 * или код ошибки в случае некорректных данных
 */

int key(int *array_start, int *array_end, int **array2_start, int **array2_end)
{
    int size = array_end - array_start;
    int ready_to_filter = 0;
	int code = ok;

    if (size == 0)
        code = bad_filter;
    else
    {
        int average = get_average(array_start, array_end, size);
        ready_to_filter = get_filt_elems(array_start, array_end, average);

        if (ready_to_filter == 0)
            code = bad_filter;
        else
        {
            *array2_start = (int *)malloc(ready_to_filter * sizeof(int));		
            if (array2_start)
            {
                *array2_end = *array2_start + ready_to_filter;
                get_array_for_filter(array_start, array_end, average, *array2_start, *array2_end);
            }
            else
                code = mem_error;
        }
    }
    
    return code;
}
