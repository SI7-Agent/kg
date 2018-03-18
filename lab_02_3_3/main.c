#include <stdio.h>
#include <math.h>

int main()
{
    float eps, x, r1, r2;

    printf("vvedi eps\n");
    r1 = scanf("%f", &eps);

    while (r1 != 1 || (eps == 0))
    {
        if (eps == 0)
        {
            fflush(stdin);
            printf("eps ne mozhet ravnyatsya 0\n");
            r1 = scanf("%f", &eps);
        }
        else
        {
            fflush(stdin);
            printf("Nevernie dannie, povtorite vvod\n");
            r1 = scanf("%f", &eps);
        }
    }

    printf("\n");
    printf("vvedi x\n");
    fflush(stdin);
    r2 = scanf("%f", &x);

    while ((r2 != 1) || (fabs(x) > 1))
    {
        if (fabs(x) > 1)
        {
            fflush(stdin);
            printf("|x| ne mozhet > 1\n");
            r2 = scanf("%f", &x);
        }
        else
        {
            fflush(stdin);
            printf("Nevernie dannie, povtorite vvod\n");
            r2 = scanf("%f", &x);
        }
    }

    printf("\n");
    int koef = 1;
    float t = x/koef;
    float mnoz = -x*x*koef/(koef + 2);
    float sum = t;
    while (t > eps)
    {
        t = t*mnoz;
        sum = sum + t;
        koef = koef + 2;
    }

    printf("zhnachenie funkzii s(x) = %f \n", sum);
    printf("zhnachenie funkzii f(x) = %f \n", atan(x));

    float absol = fabs(atan(x) - sum);
    printf("absolutanaya oshibka = %f \n", absol);

    float otnos = fabs(absol/atan(x));

    if (x == 0)
    {
        printf("pri x = 0 otnositelnaya osibka ne vozmozhna");
    }
    else
    {
        printf("otnositelnaya oshibka = %f ", otnos);
    }
}
