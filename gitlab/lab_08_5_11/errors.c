#include "errors.h"

/**
 Выводит тип ошибки, если таковая имеется.
  
  @param code
  @param argv
 */

void print_error(index code)
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
            break;
        case -3:
            printf("Info_file failed\n");
            break;
        case -4:
            printf("\nError while summing\n");
            break;
        case -5:
            printf("\nError while multiplicating\n");
            break;
        case -6:
            printf("\nError while determinating\n");
            break;
        case -7:
            printf("\nAllocation error\n");
            break;
        default:
            printf("\n");
            break;
    }
}