#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

int main()
{
    int size;
    printf("Input size of matrix:\n");

    while ((scanf("%d", &size) != 1)||(size <= 0))
    {
        fflush(stdin);
        printf("Try again:\n");
    }

    char split[2];
    printf("\nInput split:\n");
    scanf("%s", &split[0]);

    while (isalpha(split[0]) != 0)
    {
        fflush(stdin);
        printf("Try again:\n");
        scanf("%s", &split[0]);
    }

    char *mas;
    mas = (char*)malloc(size*size*sizeof(char));

    int i;
    int j;
    int mas1[size+1];
    srand(time(NULL));
    for (i = 0; i < size; i++)
    {
        int verh, niz;
        verh = 0;
        niz = 0;
        int pos = 0 + rand()%size;

        for (j = 0; j < size; j++)
        {
            if (j != pos)
            {
                int reg = 0 + rand()%2;
                if (reg == 0)
                {
                    *(mas + i*size + j) = rand()%('z' - 'a' + 1) + 'a';
                    if (j < pos)
                        niz++;
                }
                else
                {
                    *(mas + i*size + j) = rand()%('Z' - 'A' + 1) + 'A';
                    verh++;
                }
            }
            else
                *(mas + i*size + j) = split[0];
        }
        if (verh > niz)
        {
            mas1[i] = -1;
        }
    }

    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            printf("%5c", *(mas + i*size + j));
        }
        printf("\n");
    }

    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            if (mas1[i] == -1)
            {
                *(mas+i*size + j) = NULL;
            }
        }
    }

    printf("\n");

    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            if (*(mas + i*size + j) != NULL)
            {
                printf("%5c", *(mas + i*size + j));
                if (j == size - 1)
                    printf("\n");
            }
        }
    }
}
