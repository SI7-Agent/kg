#ifndef ERRORS_H
#define ERRORS_H

#include <stdio.h>

typedef enum errors_index
{
    mem_error = -7,
    bad_determ,
    bad_multy,
    bad_sum,
    no_info,
    no_file,
    wrong_argv,	
    ok
} index;

void print_error(index code);

#endif