#include <stdio.h>

int get_num(int *p, int k, int i)
{
    int x, y;
    int chislo = 0;
    int b = 0;
    for (b; b < k; b++)
    {
        int schit = 0;
        int b1 = 0;
        for (b1; b1 < i; b1++)
        {
            if (*(p+b1+2) < 0)
            {
                if (schit == b)
                {
                    x = *(p+b1+2);
                    break;
                }
                schit++;
            }
        }
        schit = 0;
        b1 = 0;
        for (b1; b1 < i; b1++)
        {
            if (*(p+i+1-b1) >= 0)
            {
                if (schit == b)
                {
                    y = *(p+i+1-b1);
                    break;
                }
                schit++;
            }
        }
        chislo += x*y;
    }
    return chislo;
}

int get_k(int *p, int razmer)
{
    int k;
    int pl = 0;
    int min = 0;
    int i = 0;
    for (i; i < razmer; i++)
    {
        if (*(p+i+2)>= 0)
        {
            pl++;
        }
        else
        {
            min++;
        }
    }
    if (pl >= min)
        return min;
    else
        return pl;
}

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
