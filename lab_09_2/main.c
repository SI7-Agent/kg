#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include "my_libstr.h"

/**
 Заменяет все вхождения указанной подстроки во всех строках входного файла и записывает результат в выходной файл.

 * @param file_in
 * @param file_out
 * @param search
 * @param replace
 * @return возвращает код ошибки.
 */

int work(FILE *file_in, FILE *file_out, const char *search, const char *replace)
{
    char *string = NULL;
    char *newstring = NULL;
    int code_error = 0;
    size_t length = 0;

    while((code_error = getline(&string, &length, file_in) != MALLOC_ERROR) && (string != NULL))
    {
        newstring = str_replace(string, search, replace);
        fprintf(file_out, "%s", newstring);

        if(newstring != NULL)
            free(newstring);

        if(string != NULL)
            free(string);

        length = 0;
    }

    return code_error;
}

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
                work(file_in, file_out, argv[3], argv[4]);

            fclose(file_out);
        }
        fclose(file_in);
    }

    switch(code_error)
    {
        case ARGV_ERROR:
            printf("Arguments failed\n");
            break;

        case IN_FILE_ERROR:
            printf("In_file failed\n");
            break;

        case OUT_FILE_ERROR:
            printf("Out_file failed\n");
            break;

        case MALLOC_ERROR:
            printf("Allocation failed\n");
            break;

        case NO_ERROR:
            break;

        default:
            printf("All's BAD\n");
    }
    return 0;
}
