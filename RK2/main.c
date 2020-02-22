#include <stdio.h>
#include <stdlib.h>

#include "d_list.h"

//4.2

int main()
{
    name *university = NULL;
    while (1)
    {
        printf("1) Add to the end\n");
        printf("2) Sort (not working)\n");
        printf("3) Print\n");
        printf("0) Exit\n");
        int code;
        scanf("%d", &code);
        switch (code)
        {
            case 0:
                exit(0);
            case 1:
            {
                fflush(stdin);
                Student *data = NULL;
                data = add_st();
                university = add(university, data);
                break;
            }
            case 2:
            {

                break;
            }
            case 3:
            {
                print_big_struct(university);
                break;
            }
            default:
            {
                printf("Unknown argument\n");
                break;
            }
        }
    }
}
