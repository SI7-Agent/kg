#include "func.h"

char *print(char *format_buffer, size_t *size, const char cur_sym, int *global_counter)
{
    *global_counter = *global_counter + 1;
    if(*size > 1)
    {
        *format_buffer = cur_sym;
        *size = *size - 1;
        format_buffer++;
    }
    return format_buffer;
}

char *print_hex_id(char *format_buffer, size_t *size, const unsigned short toconvert, int *global_counter, char sym)
{
    int tmp = toconvert;
    const char hex_big[] = "0123456789ABCDEF";
    const char hex_small[] = "0123456789abcdef";

    const char *hexDigits = NULL;
    if (sym == 'x')
        hexDigits = hex_small;
    else
        hexDigits = hex_big;
    char result[] = "0000\0";
    for (int i = 3; i >= 0; i--)
    {
        result[i] = hexDigits[tmp % 16];
        tmp = tmp / 16;
    }

    int flag = 0;

    for (int i = 0; i < 4; ++i)
    {
        if (result[i] != '0')
            flag = 1;
        else
            if (flag == 0)
                continue;

        format_buffer = print(format_buffer, size, result[i], global_counter);
    }

    if (flag == 0)
        format_buffer = print(format_buffer, size, '0', global_counter);

    return format_buffer;
}

int digit_len(int num)
{
    int num_len = 0;
    if (num == 0)
        num_len = 1;

    else
        while (abs(num) != 0)
        {
            num = num / 10;
            num_len++;
        }
    return num_len;
}

char get_n_char(int num, int k)
{
    int n = (num / (pow(10, k - 1)));
    return n % 10 + '0';
}

char *print_int(char *format_buffer, size_t *size, const int toprint, int *global_counter)
{
    const int num = toprint;
    int num_len = digit_len(toprint);

    if ((num < 0))
        format_buffer = print(format_buffer, size, '-', global_counter);

    for (int i = 0; i < num_len; ++i)
        format_buffer = print(format_buffer, size, get_n_char(abs(num), num_len - i), global_counter);

    return format_buffer;
}

char *print_char_sym(char *format_buffer, size_t *size, const int toprint, int *global_counter)
{
    const char sym = (const char)toprint;

    format_buffer = print(format_buffer, size, sym, global_counter);
    return format_buffer;
}

size_t my_vsnprintf(char *buffer, size_t buff_size, const char *format, va_list ap)
{
    size_t n = buff_size;
    const char *flag_sym = format;
    char *format_buffer = buffer;
    char cur_sym;
    int global_counter = 0;

    while ((cur_sym = *flag_sym++))
    {
        if (cur_sym == '%')
        {
            if ((cur_sym = *flag_sym++))
            {
                switch (cur_sym)
                {
                    case 'i':
                        format_buffer = print_int(format_buffer, &n, va_arg(ap, int), &global_counter);
                        break;
                    case 'c':
                        format_buffer = print_char_sym(format_buffer, &n, va_arg(ap, int), &global_counter);
                        break;
                    case 'h':
                        if ((cur_sym = *flag_sym++))
                        {
                            if (cur_sym == 'x')
                                format_buffer = print_hex_id(format_buffer, &n, (unsigned short)va_arg(ap, unsigned int), &global_counter, cur_sym);
                            else if (cur_sym == 'X')
                                format_buffer = print_hex_id(format_buffer, &n, (unsigned short)va_arg(ap, unsigned int), &global_counter, cur_sym);
                            else
                            {
                                format_buffer = print(format_buffer, &n, '%', &global_counter);
                                format_buffer = print(format_buffer, &n, 'h', &global_counter);
                                format_buffer = print(format_buffer, &n, cur_sym, &global_counter);
                            }
                        }
                        break;
                }
            }
        }
        else
            format_buffer = print(format_buffer, &n, cur_sym, &global_counter);
    }
    *format_buffer = '\0';
    return global_counter;
}

int my_snprintf(char *buffer, size_t size, const char *format, ...)
{
    va_list ap;
    va_start(ap, format);
    int read_byte = my_vsnprintf(buffer, size, format, ap);
    va_end(ap);
    return read_byte;
}
