#include <math.h>
#include <stdio.h>


int main(float osnova1, float osnova2, float visota)
{
    printf("osnovanie 1:\n");
    scanf("%f", &osnova1);

    printf("osnovanie 2:\n");
    scanf("%f", &osnova2);

    printf("visota:\n");
    scanf("%f", &visota);

    float p = osnova1 + osnova2 + 2*sqrt((osnova1-osnova2)*(osnova1-osnova2)/4 + visota*visota);
    printf("perimetr: %f", p);

}
