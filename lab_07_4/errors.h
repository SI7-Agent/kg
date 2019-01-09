#ifndef ERRORS_H
#define ERRORS_H

#include <stdio.h>
#include "read_array_test.h"

typedef enum errors_index
{
    mem_error = -6,
    bad_data_file,
    bad_filter,
    empty_file,
    no_file,
    wrong_argv,	
    ok
} index;

void print_error(index code, char *argv[]);

#endif