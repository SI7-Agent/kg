#include <stdlib.h>
#include <stdio.h>

void mysort(int *array_start, int *array_end)
{
    int newElement, location;

    for (int i = 1; i < array_end - array_start; i++)
    {
        newElement = *(array_start+i);
        location = i - 1;
        while(location >= 0 && *(array_start+location) > newElement)
        {
            *(array_start+location+1) = *(array_start+location);
            location = location - 1;
        }
        *(array_start+location+1) = newElement;
    }
}
