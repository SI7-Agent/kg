#include <stdio.h>

int main()
{
    float x, y, k, b, r1, r2, r3, r4;

    printf("x\n");
    r1 = scanf("%f", &x);
    printf("\n");

    while ((r1 != 1) && (x != 0))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r1 = scanf("%f", &x);
    }

    printf("y\n");
    fflush(stdin);
    r2 = scanf("%f", &y);
    printf("\n");

    while (r2 != 1 && (y != 0))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r2 = scanf("%f", &y);
    }

    printf("k\n");
    fflush(stdin);
    r3 = scanf("%f", &k);
    printf("\n");

    while (r3 != 1 && (k != 0))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r3 = scanf("%f", &k);
    }

    printf("f\n");
    fflush(stdin);
    r4 = scanf("%f", &b);
    printf("\n");

    while (r4 != 1 && (b != 0))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r4 = scanf("%f", &b);
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
