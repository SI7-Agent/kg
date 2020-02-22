#include <stdio.h>
#include <math.h>

int hours1(int seconds)
{
    int hours = seconds / 10000;
    return (hours);
};

int minutes1(int seconds)
{
    int minutes = (seconds - hours1(seconds)*10000) / 100;
    return (minutes);
};

int seconds1(int seconds)
{
    int seconds2 = seconds - hours1(seconds)*10000 - minutes1(seconds)*100;
};

int main()
{
    int seconds;
    scanf("%d", &seconds);
    printf("%d:%d:%d", hours1(seconds), minutes1(seconds), seconds1(seconds));
}
