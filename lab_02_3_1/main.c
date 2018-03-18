#include <stdio.h>

int nod_c(int a, int b)
{
    while (b)
    {
        int c = a % b;
        a = b;
        b = c;
    }
    return (a);
}

int main(void)
{
    int a, b, r1, r2;
    printf("vvedi chislo a\n");

    r1 = scanf("%d", &a);

    while ((r1 != 1)  || (!floor(a)))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r1 = scanf("%d", &a);
    }

    printf("vvedi chislo b\n");

    r2 = scanf("%d", &b);

    while ((r2 != 1)  || (!floor(b)))
    {
        fflush(stdin);
        printf("Nevernie dannie, povtorite vvod\n");
        r2 = scanf("%d", &b);
    }

    printf("NOD - %d", nod_c(a, b));
}
