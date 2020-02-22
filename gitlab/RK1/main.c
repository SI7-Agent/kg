#include <stdio.h>
#include <malloc.h>
#include "create_matr.h"
#include "work.h"

//Задача 1.2

int main()
{
    int code = 0;
    FILE *f = fopen("work.txt", "r");
    if (f == NULL)
        code = -1;
    else
    {
        int rows;
        int cols;
        float **matrix = fill_matrix(f, &rows, &cols);
        if (matrix == NULL)
            code = -2;
        else
        {
            print_matrix(rows, cols, matrix);
            transmit(rows, cols, matrix);

            printf("\n");
            print_matrix(rows, cols, matrix);
            free (matrix[0]);
            free (matrix);
        }
    }
    switch (code)
    {
        case 0:
            break;
        case -1:
            printf("\nFile error\n");
            break;
        case -2:
            printf("\nAllocation error\n");
            break;
        default:
            printf("\n");
            break;
    }
    return 0;
}
