#include <stdlib.h>
#include <stdio.h>

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
