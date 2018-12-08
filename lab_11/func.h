#ifndef FUNC_H
#define FUNC_H

#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <math.h>

#define N 15
#define MAX_BUF_LEN 100
#define K -199
#define OK 0
#define FAIL 1

char *print(char *format_buffer, size_t *size, const char cur_sym, int *global_counter);
char *print_hex_id(char *format_buffer, size_t *size, const unsigned short toconvert, int *global_counter, char sym);
int digit_len(int num);
char get_n_char(int num, int k);
char *print_int(char *format_buffer, size_t *size, const int toprint, int *global_counter);
char *print_char_sym(char *format_buffer, size_t *size, const int toprint, int *global_counter);
size_t my_vsnprintf(char *buffer, size_t buff_size, const char *format, va_list ap);
int my_snprintf(char *buffer, size_t size, const char *format, ...);

#endif
