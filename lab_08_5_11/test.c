#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>
#include <math.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"

void determ_test(FILE *f)
{
    float num;
    fscanf(f, "%f", &num);
    if (fabs(num - (-4)) <= 0.0001)
        printf("Test passed\n\n");
    else
        printf("Test didn't passed\n\n");
}

void sum_test(FILE *f)
{
    float num;
    int flag = 0;
    int flag1 = 0;
    fscanf(f, "%f", &num);
    fscanf(f, "%f", &num);
    while (fscanf(f, "%f", &num) == 1)
    {
        flag1++;
        if ((fabs(num - 0) <= 0.0001) && (flag1 == 1))
        {
            continue;
        }
        if ((fabs(num - 1) <= 0.0001) && (flag1 == 2))
        {
            continue;
        }
        if ((fabs(num - 1) <= 0.0001) && (flag1 == 3))
        {
            continue;
        }
        if ((fabs(num - 1) <= 0.0001) && (flag1 == 4))
        {
            continue;
        }
        if ((fabs(num - 9) <= 0.0001) && (flag1 == 5))
        {
            continue;
        }
        if ((fabs(num - 5) <= 0.0001) && (flag1 == 6))
        {
            continue;
        }
        if ((fabs(num - 6) <= 0.0001) && (flag1 == 7))
        {
            continue;
        }
        if ((fabs(num - 3) <= 0.0001) && (flag1 == 8))
        {
            continue;
        }
        if ((fabs(num - 3) <= 0.0001) && (flag1 == 9))
        {
            continue;
        }
        if ((fabs(num - (-2)) <= 0.0001) && (flag1 == 10))
        {
            continue;
        }
        if ((fabs(num - 0) <= 0.0001) && flag1 == 11)
        {
            continue;
        }
        if ((fabs(num - 2) <= 0.0001) && (flag1 == 12))
        {
            continue;
        }
        flag = 1;
        if (flag == 1)
            break;
    }
    if (flag == 0)
        printf("Test passed\n\n");
    else
        printf("Test didn't passed\n\n");
}

void mult_test(FILE *f)
{
    float num;
    int flag = 0;
    int flag1 = 0;
    fscanf(f, "%f", &num);
    fscanf(f, "%f", &num);
    while (fscanf(f, "%f", &num) == 1)
    {
        flag1++;
        if ((fabs(num - (-1)) <= 0.0001) && (flag1 == 1))
        {
            continue;
        }
        if ((fabs(num - 2) <= 0.0001) && (flag1 == 2))
        {
            continue;
        }
        if ((fabs(num - 1) <= 0.0001) && (flag1 == 3))
        {
            continue;
        }
        if ((fabs(num - (-6)) <= 0.0001) && (flag1 == 4))
        {
            continue;
        }
        if ((fabs(num - 9) <= 0.0001) && (flag1 == 5))
        {
            continue;
        }
        if ((fabs(num - 8) <= 0.0001) && (flag1 == 6))
        {
            continue;
        }
        if ((fabs(num - 15) <= 0.0001) && (flag1 == 7))
        {
            continue;
        }
        if ((fabs(num - 34) <= 0.0001) && (flag1 == 8))
        {
            continue;
        }
        if ((fabs(num - 3) <= 0.0001) && (flag1 == 9))
        {
            continue;
        }
        if ((fabs(num - 1) <= 0.0001) && (flag1 == 10))
        {
            continue;
        }
        if ((fabs(num - 5) <= 0.0001) && flag1 == 11)
        {
            continue;
        }
        if ((fabs(num - 18) <= 0.0001) && (flag1 == 12))
        {
            continue;
        }
        if ((fabs(num - (-3)) <= 0.0001) && (flag1 == 13))
        {
            continue;
        }
        if ((fabs(num - (-10)) <= 0.0001) && (flag1 == 14))
        {
            continue;
        }
        if ((fabs(num - (-13)) <= 0.0001) && (flag1 == 15))
        {
            continue;
        }
        if ((fabs(num - (-10)) <= 0.0001) && (flag1 == 16))
        {
            continue;
        }
        flag = 1;
        if (flag == 1)
            break;
    }
    if (flag == 0)
        printf("Test passed\n\n");
    else
        printf("Test didn't passed\n\n");
}

int main()
{
    FILE *f1 = fopen("res_out1.txt", "r");
    printf("Summing up testing...\n");
    sum_test(f1);
    fclose(f1);
    //-------
    FILE *f2 = fopen("res_out2.txt", "r");
    printf("Multipling testing...\n");
    mult_test(f2);
    fclose(f2);
    //-------
    FILE *f3 = fopen("res_out3.txt", "r");
    printf("Determinant testing...\n");
    mult_test(f3);
    fclose(f3);
    return 0;
}
