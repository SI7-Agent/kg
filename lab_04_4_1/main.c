#include <stdio.h>
#include <malloc.h>

void InsertionSort(int n, int mass[])
{
    int newElement, location;
    int i;
    for (i = 1; i < n; i++)
    {
        newElement = mass[i];
        location = i - 1;
        while(location >= 0 && mass[location] > newElement)
        {
            mass[location+1] = mass[location];
            location = location - 1;
        }
        mass[location+1] = newElement;
    }
}

int main()
{
    int N;
    printf("Input N (not more 10): ");
    while (scanf("%d", &N) == 0)
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

    InsertionSort(N, mass);

    printf("Sorted array:\n");
    for (i = 0; i < N; i++)
        printf("%d ", mass[i]);
    printf("\n");

    return 0;
}
