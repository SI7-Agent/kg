#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "functions.h"

unsigned long long tick(void)
{
    unsigned long long d;
    __asm__ __volatile__ ("rdtsc" : "=A" (d) );
    return d;
}

int main(int argc, char *argv[])
{
    unsigned long long tb, te;
    long pos, pos_end;
    FILE *f = fopen(argv[1], "r");

    if (f == NULL)
    {
        printf("I/O error\nFile is not found\n");

        FILE *f_out_error = fopen(argv[2], "w");
        fclose(f_out_error);
        return -1;
    }

    int num;
    int size = 0;

    while(fscanf(f, "%d", &num) == 1)
    {
        pos = ftell(f);
        size++;
    }

    if (size == 0)
    {
        printf("File is empty/contains incorrect data.\n");

        FILE *f_out_error = fopen(argv[2], "w");
        fclose(f_out_error);
        return -1;
    }

    fseek(f, 0, SEEK_END);
    pos_end = ftell(f);

    if (pos != pos_end)
    {
        printf("File contains incorrect data");

        FILE *f_out_error = fopen(argv[2], "w");
        fclose(f_out_error);
        return -1;
    }

    int *array_orig = (int *)malloc(size*sizeof(int));
    int *array_orig_end = array_orig+size;

    fseek(f, 0, SEEK_SET);

    int *array_for_filter = (int *)malloc(size*sizeof(int));
    int *array_for_filter_end = array_for_filter+size;

    printf("Read array:\n");
    int i = 0;
    while(fscanf(f, "%d", &num) == 1)
    {
        *(array_orig+i) = num;
        printf("%d\n", *(array_orig+i));
        i++;
    }
    fclose(f);

    if (strcmp(argv[3], "f") == 0)
    {
        int size2 = key(array_orig, array_orig_end, array_for_filter, array_for_filter_end);

        if (size2 == -1)
        {
            printf("\nError in filter func");
            return -1;
        }

        array_for_filter = (int *)realloc(array_for_filter, size2*sizeof(int));
        array_for_filter_end = array_for_filter+size2;

        tb = tick();
        mysort(array_for_filter, array_for_filter_end);
        te = tick();

        printf("\nSorted array:\n");
        for (int i = 0; i < size2; i++)
            printf("%d\n", *(array_for_filter+i));

        printf("\nSort time: %llu nsec\n", (te - tb) / 2);

        tb = tick();
        qsort(array_for_filter, size2, sizeof(int), mysort);
        te = tick();

        printf("\nQsort time: %llu nsec\n", (te - tb) / 2);

        FILE *f_out = fopen(argv[2], "w");

        for (int i = 0; i < size2; i++)
            fprintf(f_out, "%d ", *(array_for_filter+i));

        fclose(f_out);
    }
    else
    {
        tb = tick();
        mysort(array_orig, array_orig_end);
        te = tick();

        printf("\nSorted array:\n");
        for (int i = 0; i < size; i++)
            printf("%d\n", *(array_orig+i));

        printf("\nSort time: %llu nsec\n", (te - tb) / 2);

        tb = tick();
        qsort(array_orig, size, sizeof(int), mysort);
        te = tick();

        printf("\nQsort time: %llu nsec\n", (te - tb) / 2);

        FILE *f_out = fopen(argv[2], "w");

        for (int i = 0; i < size; i++)
            fprintf(f_out, "%d ", *(array_orig+i));

        fclose(f_out);
    }

    free(array_for_filter);
    free(array_orig);
}
