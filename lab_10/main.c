#include <io.h>

#include "func.h"
#include "work.h"

int main(int argc, char *argv[])
{
    if (argc > 3)
    {
        FILE *f_in = fopen(argv[2], "r");
        FILE *f_out = fopen(argv[3], "w");
        if ((f_in) && (f_out))
            do_func(f_in, f_out, argv);
        else
            printf("File error\n");
        fclose(f_in);
        fclose(f_out);
    }
    else
        printf("Argv error\n");
}
