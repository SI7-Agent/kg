#include <stdio.h>
#include <math.h>

int metrs1(int millimetrs)
{
    int metrs = millimetrs / 1000;
};

int santimetres1(int millimetrs)
{
    int santimetres = (millimetrs - metrs1(millimetrs)*1000) / 10;
};

int millimetrs1(int millimetrs)
{
    int millimetrs2 = millimetrs - metrs1(millimetrs)*1000 - santimetres1(millimetrs)*10;
};

int main()
{
    int millimetrs;
    scanf("%d", &millimetrs);
    printf("%d:%d:%d", metrs1(millimetrs), santimetres1(millimetrs), millimetrs1(millimetrs));
}
