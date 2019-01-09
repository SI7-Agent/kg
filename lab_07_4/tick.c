#include <stdlib.h>
#include <stdio.h>

/**
 Подсчитывает число тактов процессора в момент вызова.

 * @return возвращает число тактов процессора в момент вызова.
 */

unsigned long long tick(void)
{
    unsigned long long d;
    __asm__ __volatile__ ("rdtsc" : "=A" (d) );
    return d;
}
