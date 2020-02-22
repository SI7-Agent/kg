#include <stdio.h>
int fibo(int n)
{
    int flag = 0;
    int s = 0;
    int s1 = 1;
    int sum;

    if (n == 0)
        return 0;
    else
    {
        while (flag < n)
        {
            sum = s + s1;
            s = s1;
            s1 = sum;
            flag++;
        }
        return sum;
    }
}

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
            printf("Wrong data");
            fflush(stdin);
        }
    }
    int mass1[N*2];
    int b = 0;
    int kkk = 0;
    for (b = 0; b < N*2; b = b + 2)
    {
        if (mass[b/2] % 3 == 0)
        {
            mass1[b] = mass[b/2];
            mass1[b+1] = fibo(kkk);
            kkk++;
        }
        else
        {
            mass1[b] = mass[b/2];
            mass1[b+1] = "";
        }
    }
    int size = N*2;
    int m;
    for (i = 0;i < size;i++)
    {
        if (mass1[i] == 4210859)
        {
           for (m = i;m < size - 1;m++)
            mass1[m] = mass1[m + 1];
           size--;
           i--;
        }
    }
    for (b = 0; b < size; b++)
        printf("%d ", mass1[b]);
}
