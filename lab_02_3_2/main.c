#include <stdio.h>

int main()
{
    int x, y, k, b, r1, r2, r3, r4;

    printf("x\n");
    r1 = scanf("%d", &x);
    printf("\n");

    while ((r1 != 1) && (x != 0))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r1 = scanf("%d", &x);
    }

    printf("y\n");
    fflush(stdin);
    r2 = scanf("%d", &y);
    printf("\n");

    while (r2 != 1 && (y != 0))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r2 = scanf("%d", &y);
    }

    printf("k\n");
    fflush(stdin);
    r3 = scanf("%d", &k);
    printf("\n");

    while (r3 != 1 && (k != 0))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r3 = scanf("%d", &k);
    }

    printf("b\n");
    fflush(stdin);
    r4 = scanf("%d", &b);
    printf("\n");

    while (r4 != 1 && (b != 0))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r4 = scanf("%d", &b);
    }

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
        printf("nad grafikom");
    }
}
