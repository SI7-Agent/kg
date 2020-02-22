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
    index code = ok;
    FILE *f = NULL;
    int *array_orig = NULL;
    int *array_orig_end = NULL;

    if (argc < 3)
        code = wrong_argv;

    if (!code)
    {
        f = fopen(argv[1], "r");
        code = check_file(f);
    }

    if (!code)
    {
        int size = get_size(f);
        array_orig = read_array(f, size);
        array_orig_end = array_orig + size;
        if (!array_orig)
            code = mem_error;
    }

    if (!code)
        code = work(argv, argc, array_orig, array_orig_end);

    if (f)
        fclose(f);

    print_error(code, argv);
}
