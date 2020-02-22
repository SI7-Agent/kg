#include <stdio.h>
#include <math.h>

int prost(chislo)
{
    int k;
    for (k = 2; k < sqrt(chislo) + 1; k++)
    {
        if (((chislo % k == 0)&&(chislo > 2))||(chislo == 1))
        {
            return -1;
        }
    }
    return 0;
}

int main()
{
    int N;
    printf("Input N (not more 10): ");
    while ((scanf("%d", &N) == 0)||(N > 10)||(N < 0))
    {
        printf("Input 0 < N <= 10\n");
        fflush(stdin);
    }

    int* mass;
    mass = (int *)malloc(N * sizeof(int));

    printf("Input the array elements:\n");
    int i;
    for (i = 0; i < N; i++)
    {
        while(scanf_s("%d", &mass[i]) == 0)
        {
            printf("Wrong data\n");
            fflush(stdin);
        }
    }

    int num = 0;
    int b1 = 0;
    int b;
    for (b = 0; b < i; b++)
    {
        if (prost(mass[b]) == 0)
            num = num + 1;
    }
    printf("\n");
    int mass1[num];
    for (b=0;b<i;b++)
    {
        if (prost(mass[b]) == 0)
        {
            mass1[b1] = mass[b];
            printf("%d ", mass1[b1]);
            b1 = b1 + 1;
        }
    }
}
