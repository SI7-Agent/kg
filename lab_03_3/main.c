#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

# define N 10

void output(FILE *f)
{
    int num;
    fseek(f, 0, SEEK_SET);
    for (int i = 0; i < N; i++)
    {
        fread(&num, sizeof(int), 1, f);
        printf("%d ", num);
    }
}

void rand_f(FILE *f)
{
    int rn;
    fseek(f, 0, SEEK_SET);
    srand(time(NULL));
    for (int i = 0; i < N; i++)
    {
        rn = rand() % 1000 + 1;
        fwrite(&rn, sizeof(int), 1, f);
    }
}

int get_number_by_pos(FILE *f, int pos)
{
    int num;
    fseek(f, sizeof(int)*pos, SEEK_SET);
    fread(&num, sizeof(int), 1, f);
    return num;
}

void put_number_by_pos(FILE *f, int pos, int val)
{
    fseek(f, sizeof(int)*pos, SEEK_SET);
    fwrite(&val, sizeof(int), 1, f);
}

void sort(FILE *f)
{
    int a, b;
    for (int i = 0; i < N - 1; i++)
    {
        for (int ii = i; ii < N; ii++)
        {
            a = get_number_by_pos(f, i);
            b = get_number_by_pos(f, ii);
            if (a > b)
            {
                put_number_by_pos(f, ii, a);
                put_number_by_pos(f, i, b);
            }
        }
    }
}


int main(void)
{
    FILE *f;
    int pos, val;
    char im[30];
    printf("File name \n");
    gets(im);
    f = fopen(im,"w+b");
    rand_f(f);
    output(f);
    puts("\ninput position of element you want to get");
    if ((scanf("%d", &pos) != 1)|| (pos < 0))
    {
        puts("Wrong position.");
        return -2;
    }
    printf("%d", get_number_by_pos(f, pos));
    puts("\ninput position of element you want to change");
    if ((scanf("%d", &pos) != 1)|| (pos < 0))
    {
        puts("Wrong position.\n");
        return -2;
    }
    puts("Input value of element");
    if (scanf("%d", &val) != 1)
    {
        puts("Wrong value.\n");
        return -2;
    }
    put_number_by_pos(f, pos, val);
    output(f);
    sort(f);
    puts("\nSorted file data");
    output(f);
    return 0;
}
