#include <stdio.h>

int func(FILE *f)
{
    int num;
    int num1;
    int num99;
    int kol = 0;
    if (fscanf(f, "%d", &num99) == 1)
    {
        fseek(f, 0, SEEK_SET);
        fscanf(f, "%d", &num);
        while (fscanf(f, "%d", &num1) == 1)
        {
            if ((num*num1<0) || ((num1 < 0) && (num == 0)) || ((num < 0) && (num1 == 0)))
            {
                kol = kol +1;
            }
            num = num1;
        }
        return kol;
    }
    return -1;
}

int main(void)
{
    FILE *f = fopen("test1.txt", "w");
    printf("Input or data by 1\n");
    int num1;
    int p;
    int num2;
    int kol;
    do
    {
        p = scanf("%d", &num2);
        if (p == 1)
            fprintf(f, "%d\n", num2);
        fflush(stdin);
    }
    while(p == 1);
    fclose(f);
    f = fopen("test1.txt", "r");
    kol = func(f);
    if (kol == -1)
        printf("Error I/O");
    else
        printf("Changes of sign: %d", kol);
    fclose(f);
}
