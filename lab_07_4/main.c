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
#include "errors.h"

int main(int argc, char *argv[])
{
    index code = 0;
    if (argc < 3)
        code = wrong_argv;
    else
    {
        FILE *f = fopen(argv[1], "r");
        if (!f)
            code = no_file;
        else
        {
            int size = get_size(f);
            if (size == 0)
                code = empty_file;
            else
            {
                long pos, pos_end;
                fseek(f, 0, SEEK_END);
                pos_end = ftell(f);
                pos = get_pos(f);

                if (pos != pos_end)
                    code = bad_data_file;
                else
                {
                    int *array_orig = (int *)malloc(size * sizeof(int));
                    int *array_orig_end = array_orig + size;
                    int *array_start = array_orig;

                    fseek(f, 0, SEEK_SET);

                    int *array_for_filter = (int *)malloc(size * sizeof(int));
                    int *array_for_filter_end = array_for_filter + size;
                    if ((!array_orig) || (!array_for_filter))
                        code = mem_error;
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
    print_error(code, argv);
}
