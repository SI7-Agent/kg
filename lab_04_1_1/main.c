#include <stdio.h>
#include <malloc.h>

int main()
{
    int N;
    printf("Input N (not more 10): ");
    while ((scanf("%d", &N) == 0)||(N>10)||(N<0))
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
            printf("Input 0 < N <= 10\n");
            fflush(stdin);
        }

    int b;
    int proizv = 1;
    for (b = 0; b < i; b++)
    {
        if (mass[b]%2 == 1)
        {
            proizv = proizv*mass[b];
        }
    }

    printf("Your multiple: %d", proizv);
}
