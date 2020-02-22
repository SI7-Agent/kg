#include <stdio.h>
#include <get_num.c>
#include <get_k.c>

int main()
{
    FILE *f;
    char name[80];
    printf("File name\n");
    gets(name);
    f = fopen(name, "r");
    if (f == NULL)
    {
        printf("I/O error\n");
        return -1;
    }
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
            printf("\nFile has more than 100 elements");
            break;
        }

        *(p+i) = num;
        i++;
    }
    int b = 0;

    int k = get_k(&p, i);
    if (k == 0)
    {
        printf("list has only positive or negative elements"
               "\ncontinuous countations are impossible");
        return -1;
    }
    int res = get_num(&p, k, i);
    printf("\n%d", res);
}
