#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include "test_func.h"
#include "my_libstr.h"

char *answer(int val)
{
    char *answer = "FAIL";
    if (val == OK)
        answer = "\nTest passed";
    else
        answer = "\nTest didn't pass";

    return answer;
}

int test_getline(const char *file_name)
{
    FILE *file_in1 = fopen(file_name, "r");
    FILE *file_in2 = fopen(file_name, "r");
    int result = OK;
    int code_error = 0;

    char *string = NULL;
    char str[256];
    size_t length = 0;

    while((code_error = getline(&string, &length, file_in1) != -1)&&(string != NULL))
    {
        fgets(str, sizeof(str), file_in2);

        if (!strcmp(string, str))
            result = OK;
        else
            result = FAIL;

        if (strlen(string) != strlen(str))
            result = FAIL;

        if(string != NULL)
            free(string);
        string = NULL;
    }

    fclose(file_in2);
    fclose(file_in1);
    return result;
}

int test_replace(const char *line, const char *replace_what, const char *replace_with, char *answer)
{
    int result = OK;
    char *answer_to_check = str_replace(line, replace_what, replace_with);

    if (!strcmp(answer_to_check, answer))
        result = OK;
    else
        result = FAIL;

    if(answer_to_check != NULL)
        free(answer_to_check);
    return result;
}
