#ifndef MY_LIBSTR_H
#define MY_LIBSTR_H
#define NO_ERROR 0
#define MALLOC_ERROR -1
#define ARGV_ERROR -2
#define IN_FILE_ERROR -3
#define OUT_FILE_ERROR -4
#define BAD_LENGHT -5

int realloc_str(char** string, int cur_len, int new_len);
ssize_t getline(char **lineptr, size_t *n, FILE *stream);
int replace(char **string, const char *search, const char *replace);
char* str_replace(const char *source, const char *search, const char *replacement);
char *strdup(const char *str);
int replace_strings_in_file(FILE *file_in, FILE *file_out, const char *search, const char *replace);
void get_error(int code_error);
size_t my_strnlen(const char *s);
#endif