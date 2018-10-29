#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include "my_libstr.h"

/**
 Создает копию строки и выделяет под нее память.

 * @param str
 * @return возвращает указатель на копию строки.
 */

char *strdup(const char *str)
{
    int n = strlen(str) + 1;
    char *dup = malloc(n);
    if (dup)
        strcpy(dup, str);

    return dup;
}

/**
 Перевыделяет память под считываемую строку.

 * @param string
 * @param cur_len
 * @param new_len
 * @return возвращает код ошибки.
 */

int realloc_str(char** string, int cur_len, int new_len)
{
    char *temp_string;
    temp_string = malloc(new_len);

    if (!temp_string)
        return MALLOC_ERROR;

    else
    {
        memset(temp_string, '\0', new_len);
        memcpy(temp_string, *string, cur_len);

        if (*string != NULL)
            free(*string);

        *string = temp_string;
        return NO_ERROR;
    }
}

/**
 Считывает строку из файла.

 * @param lineptr
 * @param n
 * @param stream
 * @return количество считанных байт.
 */

ssize_t getline(char **lineptr, size_t *n, FILE *stream)
{
    int code_error = 0;
    int current_length = 0;
    char buf[10];
    *n = 0;
    char *string = NULL;

    while(fgets(buf, 10, stream) != NULL)
    {
        int read = strlen(buf);
        code_error = realloc_str(&string, current_length , current_length + read + 1);

        if (code_error != NO_ERROR)
            break;

        memcpy(string + current_length, buf, read + 1);
        current_length += read;

        if(string[current_length - 1] == '\n')
            break;
    }

    *lineptr = string;
    *n = current_length;
    return current_length;
}

/**
 Заменяет первое вхождение указанной подстроки в данной строке.

 * @param string
 * @param search
 * @param replace
 * @return возвращает код ошибки.
 */

int replace(char **string, const char *search, const char *replace)
{
    int size_line = strlen(*string);
    int size_search = strlen(search);
    int size_replace = strlen(replace);

    if (strstr(*string, search) == NULL)
        return BAD_LENGHT;

    char *newstring = (char*)malloc(sizeof(char)*(size_line + size_replace - size_search + 1));

    if (!newstring)
        return MALLOC_ERROR;

    newstring[size_line + size_replace - size_search] = '\0';
    int len_left_copy = strstr(*string, search) - *string;

    memcpy(newstring, *string, len_left_copy);
    memcpy(newstring + len_left_copy, replace, size_replace);

    char *right_part_write = newstring + len_left_copy + size_replace;
    char *right_part_read = *string + len_left_copy + size_search;

    memcpy(right_part_write, right_part_read, *string + size_line - right_part_read + 1);

    if (*string)
        free(*string);

    *string = newstring;
    return NO_ERROR;
}

/**
 Заменяет все вхождения указанной подстроки в данной строке.

 * @param source
 * @param search
 * @param replacement
 * @return возвращает указатель на измененную строку.
 */

char* str_replace(const char *source, const char *search, const char *replacement)
{
    int code_error = NO_ERROR;
    char *linetmp = strdup(source);
    while ((code_error = replace(&linetmp, search, replacement)) != BAD_LENGHT);

    if (code_error == MALLOC_ERROR)
        printf("Allocation failed\n");

    return linetmp;
}
