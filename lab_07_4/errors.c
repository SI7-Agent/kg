#include "errors.h"

void print_error(index code, char *argv[])
{
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