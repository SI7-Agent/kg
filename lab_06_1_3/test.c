#include <stdio.h>
#include <assert.h>
#include "func.h"

int main()
{
    FILE *f;
    f = fopen("test_data.txt", "r");
    int mas[100];
    int i = 0;
    int num;
    int plus = 0;
    int minus = 0;
    int *p;
    p = mas;
    while (fscanf(f, "%d", &num) == 1)
    {
        if (i > 99)
        {
            break;
        }

        *(p+i) = num;
        i++;
    }
    int b = 0;

    int k = get_k(&p, i);
    assert(k == 2);
    int res = get_num(&p, k, i);
    assert(res == -7460);
    printf("Tests passed.");
}
