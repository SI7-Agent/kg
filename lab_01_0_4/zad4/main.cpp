#include <stdio.h>

int main()
{
    int s;
    printf("vvedite, skolko u nas denel (v kopeikah)\n");
    scanf("%d", &s);

    if (s < 45)
    {
        printf("mozhem kupit 0 butilok");
    }
    else
    {
        int schet = 0;
        while (s >= 45)
        {
            int kolvo = s/45;
            int ostatok = s%45;
            schet = schet + kolvo;
            s = ostatok + kolvo*20;
        };
        printf("mozhem kupit %d butilok", schet);
    }
}
