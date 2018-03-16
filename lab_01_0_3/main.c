#include <math.h>
#include <stdio.h>

int main(float h, float m, float t)
{
    printf("rost (sm):\n");
    scanf("%f", &h);

    printf("ves (kg):\n");
    scanf("%f", &m);

    printf("grudnaya kletka dlina okruzhnosti (sm):\n");
    scanf("%f", &t);

    float indeks = m/(h/100)/(h/100);
    printf("indeks: %f\n", indeks);

    float norm_ves = h*t/240;
    printf("normalnii ves: %f", norm_ves);
}
