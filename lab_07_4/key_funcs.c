#include <stdio.h>

/**
 Вычисляет среднее значение элементов данного массива.

 * @param array_start
 * @param array_end
 * @return возвращает среднее значение элементов данного массива.
 */

int get_average(int *array_start, int *array_end, int size)
{
    int average = 0;
    while (array_start != array_end)
    {
        average = average + *array_start;
        array_start++;
    }

    average = average / size;
    return average;
}

/**
 Вычисляет число элементов, пригодных для фильтрации.

 * @param array_start
 * @param array_end
 * @param average
 * @return возвращает число элементов, пригодных для фильтрации.
 */

int get_filt_elems(int *array_start, int *array_end, int average)
{
    int ready_to_filter = 0;
    while (array_start != array_end)
    {
        if (*array_start > average)
            ready_to_filter++;

        array_start++;
    }
    return ready_to_filter;
}

/**
 Копирует элементы, пригодные для фильтрации, в отдельный массив.

 * @param array_start
 * @param array_end
 * @param average
 * @param start_orig2
 * @param array2_end
 */

void get_array_for_filter(int *array_start, int *array_end, int average, int *start_orig2, int *array2_end)
{
    int size = 0;
    while (array_start != array_end)
    {
        if (*array_start > average)
        {
            int temp = *array_start;
            *(start_orig2) = temp;
            size++;

            if (start_orig2 != array2_end)
                start_orig2++;
        }
		
        array_start++;
    }
}
