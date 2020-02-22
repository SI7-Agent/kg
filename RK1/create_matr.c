#include <stdio.h>
#include <malloc.h>

float **allocate_matrix(int rows, int cols)
{
    float **ptrs, *data;

    ptrs = malloc(rows * sizeof(float*));

    if (!ptrs)
        return NULL;

    data = malloc(rows * cols * sizeof(float));

    if (!data)
    {
        free(ptrs);
        return NULL;
    }

    for (int i = 0; i < rows; i++)
        ptrs[i] = data + i * cols;

    return ptrs;
}

float **fill_matrix(FILE *f, int *rows, int *cols)
{
    int row;
    int col;

    fscanf(f, "%d", &row);
    fscanf(f, "%d", &col);

    float **matrix = allocate_matrix(row, col);

    if (matrix)
    {
        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
            {
                float tmp;
                fscanf(f, "%f", &tmp);
                matrix[i][j] = tmp;
            }

        *rows = row;
        *cols = col;
    }

    return matrix;
}

void print_matrix(int rows, int cols, float **matrix)
{
    for (int i = 0; i< rows; i++)
    {
        for (int j = 0; j< cols; j++)
            printf("%.3f ", matrix[i][j]);
        printf("\n");
    }
}
