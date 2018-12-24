#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"
#include "process.h"
#include "errors.h"

int main(int argc, char *argv[])
{
	index code;
    if (argc > 3)
        process(argv, argc, &code);
    else
        code = wrong_argv;
    print_error(code);

    return 0;
}
