#include <stdlib.h>
#include <stdio.h>

void mysort(int *array_start, int *array_end)
{
    int *array_start_flag1;
    int *array_start_flag2;
    array_start_flag1 = array_start;
    array_start_flag2 = array_start;

    int size = array_end - array_start;
    int newElement, location;

    for (int i = 1; i < size; i++)
    {
        array_start_flag1 = array_start+i;

        newElement = *array_start_flag1;
        location = i - 1;

        array_start_flag1 = array_start+location+1;
        array_start_flag2 = array_start+location;
        while(location >= 0 && *array_start_flag2 > newElement)
        {
            *array_start_flag1 = *array_start_flag2;
            location = location - 1;
            array_start_flag1 = array_start+location+1;
            array_start_flag2 = array_start+location;
        }
        *array_start_flag1 = newElement;
    }
}
