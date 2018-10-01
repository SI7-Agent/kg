#include <stdlib.h>
#include <stdio.h>

/**
 Сравнивает два элемента.

 * @param i
 * @param j
 * @return возвращает либо число, большее 0, либо меньшее 0, либо 0.
 */

int comp (const int *i, const int *j)
{
    return *i - *j;
}
