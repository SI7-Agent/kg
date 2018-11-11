#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "read_array_test.h"
#include "tick.h"
#include "key.h"
#include "get_size_test.h"
#include "mysort.h"
#include "do_filter.h"

int main(int argc, char *argv[])
{
    int code = 0;
    if (argc < 3)
        code = -1;
    else
    {
        FILE *f = fopen(argv[1], "r");
        if (f == NULL)
            code = -2;
        else
        {
            int size = get_size(f);
            if (size == 0)
                code = -3;
            else
            {
                long pos, pos_end;
                fseek(f, 0, SEEK_END);
                pos_end = ftell(f);
                pos = get_pos(f);

                if (pos != pos_end)
                    code = -5;
                else
                {
                    int *array_orig = (int *)malloc(size*sizeof(int));
                    int *array_orig_end = array_orig+size;
                    int *array_start = array_orig;

                    fseek(f, 0, SEEK_SET);

                    int *array_for_filter = (int *)malloc(size*sizeof(int));
                    int *array_for_filter_end = array_for_filter+size;
                    if ((array_orig == NULL)||(array_for_filter == NULL))
                        code = -6;
                    else
                    {
                        printf("Read array:\n");
                        read_array(f, array_orig, array_orig_end);
                        output(array_orig, array_orig_end);
                        work(&code, argv, argc, array_orig, array_orig_end, array_start, array_for_filter, array_for_filter_end);

                        free(array_for_filter);
                        free(array_orig);
                    }
                }
            }
            fclose(f);
        }
    }
    switch (code)
    {
    case 0:
        break;

    case -1:
        printf("Arguments failed\n");
        break;

    case -2:
        printf("In_file failed\n");
        record_empty(argv);
        break;

    case -3:
        printf("File is empty/contains incorrect data.\n");
        record_empty(argv);
        break;

    case -4:
        printf("\nError in filter func\n");
        break;

    case -5:
        printf("\nFile contains incorrect data\n");
        record_empty(argv);
        break;

    case -6:
        printf("\nAllocation error\n");
        break;

    default:
        printf("\n");
    }
}
