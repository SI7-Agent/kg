#include<stdio.h>
int main(void)
{
    int a, b, c;
    printf("vvedi chislo a\n");
    scanf("%d",&a);

    printf("vvedi chislo b\n");
    scanf("%d",&b);

    while (b)
    {
        c = a % b;
        a = b;
        b = c;
    }
printf("NOD - %d", a);
}
