#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int chislo()
{
    int p;
    int aa;
    do
    {
        p = scanf("%d", &aa);
        if ((p!=1)||(aa < 10))
        {
            printf("neverniy vvod\n");
            p = scanf("%d", &aa);
        }
        fflush(stdin);
    }
    while(((p != 1)&&(aa < 10)));

    int a1 = aa%10;
    while (aa>10)
    {
        aa = aa/10;
    }
    int a2 = aa;
    int s = a1+a2;
    printf("%d\n", s);
}

int posled()
{
    int mas;
    int sum = 0;
    int p;
    int max = -100;
    do
    {
        do
        {
            p = scanf("%d", &mas);
            if ((p != 1)||(abs(mas) < 100)||(abs(mas) > 1000))
            {
                printf("neverniy vvod\n");
                p = scanf("%d", &mas);
            }
            fflush(stdin);
        }
        while ((p != 1)||(abs(mas) < 100)||(abs(mas) > 1000));

        if (mas < 0)
        {
            sum = sum + mas;
        }
        if ((mas%2 == 1) && (mas>max))
        {
            max = mas;
        }
    }
    while ((p != 1)||(mas != 349));
    printf("sum = %d\nmax = %d\n", sum, max);
}

int file()
{
    int num;
    FILE *file;
    file = fopen("1.txt", "r");
    while (fscanf(file, "%d", &num) == 1)
    {
        if (num%7 == 0)
            printf("%d\n", num);
    }
}

int main()
{
    printf("Summa pervoi i poslednei cifr vvedennogo chisla\n");
    chislo();
    printf("Summa otricatelnih chisel i maksimalnoe nechetnoe chislo\n");
    posled();
    printf("Chisla kratnie 7 iz faila\n");
    file();
}
