#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "functions.h"

void main()
{
    printf("Reading normal file\n");
    FILE *f1 = fopen("in_1.txt", "r");

    int size = get_size(f1);

    int *array_orig1 = (int*)malloc(size*sizeof(int));
    int *array_orig_end1 = array_orig1 + size;

    read_array(f1, array_orig1, array_orig_end1);

    int *array_for_filter1 = (int*)malloc(size*sizeof(int));
    int *array_for_filter_end1 = array_for_filter1 + size;

    int key_item = key(array_orig1, array_orig_end1, array_for_filter1, array_for_filter_end1);

    if ((key_item != -1) && (key_item != -2))
        printf("Test passed\n\n");
    else
        printf("\nTest failed\n\n");

    free(array_orig1);
    free(array_for_filter1);
    fclose(f1);

    //-----------------------------

    printf("Reading empty file\n");
    FILE *f2 = fopen("in_2.txt", "r");

    size = get_size(f2);

    if (size == 0)
        printf("Test passed\n\n");
    else
        printf("\nTest failed\n\n");
    fclose(f2);

    //-----------------------------

    printf("Filtered array is empty\n");
    FILE *f3 = fopen("in_3.txt", "r");

    size = get_size(f3);

    int *array_orig2 = (int*)malloc(size*sizeof(int));
    int *array_orig_end2 = array_orig2 + size;

    read_array(f3, array_orig2, array_orig_end2);

    int *array_for_filter2 = (int*)malloc(size*sizeof(int));
    int *array_for_filter_end2 = array_for_filter2 + size;

    key_item = key(array_orig2, array_orig_end2, array_for_filter2, array_for_filter_end2);

    if (key_item == -2)
        printf("Test passed\n\n");
    else
        printf("Test failed\n\n");

    free(array_orig2);
    free(array_for_filter2);
    fclose(f3);

    //-----------------------------

    printf("Reading file with incorrect data \n");
    FILE *f4 = fopen("in_4.txt", "r");

    int pos = 0;
    pos = get_pos(f4);
    fseek(f4, 0, SEEK_END);
    int pos_end = 0;
    pos_end = ftell(f4);

    if (pos != pos_end)
        printf("Test passed\n");
    else
        printf("\nTest failed\n");
    fclose(f4);
}
