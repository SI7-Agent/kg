#ifndef NO_ERROR
#define NO_ERROR 0
#endif

#ifndef MALLOC_ERROR
#define MALLOC_ERROR -1
#endif

#ifndef ARGV_ERROR
#define ARGV_ERROR -2
#endif

#ifndef IN_FILE_ERROR
#define IN_FILE_ERROR -3
#endif

#ifndef OUT_FILE_ERROR
#define OUT_FILE_ERROR -4
#endif

#ifndef BAD_LENGHT
#define BAD_LENGHT -5
#endif

int realloc_str(char** string, int cur_len, int new_len);
ssize_t getline(char **lineptr, size_t *n, FILE *stream);
int replace(char **string, const char *search, const char *replace);
char* str_replace(const char *source, const char *search, const char *replacement);
char *strdup(const char *str);
int replace_strings_in_file(FILE *file_in, FILE *file_out, const char *search, const char *replace);
void get_error(int code_error);
size_t my_strnlen(const char *s);
