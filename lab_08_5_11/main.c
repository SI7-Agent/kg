#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

#include "get_matrix.h"
#include "print_matrix.h"
#include "operations.h"
#include "process.h"

int main(int argc, char *argv[])
{
    if (argc > 3)
        process(argv);
    else
        printf("Arguments error\n");

    return 0;
}
