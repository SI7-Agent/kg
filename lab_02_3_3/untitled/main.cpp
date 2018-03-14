#include <stdio.h>
#include <math.h>

int main()
{
    float eps, x;

    printf("vvedi eps\n");
    scanf("%f", &eps);

    printf("vvedi x\n");
    scanf("%f", &x);

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
    printf("otnositelnaya oshibka = %f ", otnos);
}
