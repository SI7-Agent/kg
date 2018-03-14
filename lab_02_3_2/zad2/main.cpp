#include <stdio.h>

int main()
{
    int x, y, k, b;

    printf("x\n");
    scanf("%d", &x);

    printf("y\n");
    scanf("%d", &y);

    printf("k\n");
    scanf("%d", &k);

    printf("b\n");
    scanf("%d", &b);

    if (y == k*x + b)
    {
        printf("na grafike");
    }
    if (y < k*x + b)
    {
        printf("pod grafikom");
    }
    if (y > k*x + b)
    {
        printf("nad grafikm");
    }
}
