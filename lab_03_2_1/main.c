#include <stdio.h>
int get_max(FILE *f, int *max)
{
    int num;
    if (fscanf(f, "%d", max) == 1)
    {
        while (fscanf(f, "%d", &num) == 1)
            if (num > *max)
                *max = num;
        return 0;
    }
    return -1;
}

int get_min(FILE *f, int *min)
{
    fseek(f, 0, SEEK_SET);
    int num;
    if (fscanf(f, "%d", min) == 1)
    {
        while (fscanf(f, "%d", &num) == 1)
            if (num < *min)
                *min = num;
        return 0;
    }
    return -1;
}

int get_sr(FILE *f, int *per, float sr)
{
    fseek(f, 0, SEEK_SET);
    int num;
    int kol = 0;
    if (fscanf(f, "%d", per) == 1)
    {
        while (fscanf(f, "%d", &num) == 1)
            if (num > sr)
                kol = kol + 1;
    }
    return kol;
}

int main(void)
{
    FILE *f;
    int max;
    int min;
    int per;
    char name[80];
    printf("File name\n");
    gets(name);
    f = fopen(name, "r");
    if (f == NULL)
    {
        printf("I/O error\n");
        return -1;
    }

    if (get_max(f, &max) == 0)
        printf("max is %d\n", max);
    else
        printf("There are not enough data.\n");
    if (get_min(f, &min) == 0)
        printf("min is %d\n", min);
    else
        printf("There are not enough data.\n");

    float s = 2;
    float sr = (max+min)/s;

    printf("sr is %f\n", sr);

    int kol = get_sr(f, &per, sr);

    printf("num is %d\n", kol);

    fclose(f);
    return 0;
}
