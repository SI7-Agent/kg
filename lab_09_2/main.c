#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include "my_libstr.h"

int main(int argc, char *argv[])
{
    int code_error = NO_ERROR;

    if (argc < 5)
        code_error = ARGV_ERROR;
    else
    {
        FILE *file_in = fopen(argv[1], "r");

        if (!file_in)
           code_error = IN_FILE_ERROR;
        else
        {
            FILE *file_out = fopen(argv[2], "w");
            if (!file_out)
                code_error = OUT_FILE_ERROR;
            else
                replace_strings_in_file(file_in, file_out, argv[3], argv[4]);

            fclose(file_out);
        }
        fclose(file_in);
    }

    get_error(code_error);
    return 0;
}
