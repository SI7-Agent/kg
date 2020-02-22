#include "func.h"

/**
 Записывает символ cur_sym в массив символов (строку) format_buffer.

 * @param format_buffer
 * @param size
 * @param cur_sym
 * @param global_counter
 * @return возвращает указатель на строку format_buffer с записанным символом cur_sym.
 */

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
 
/**
 Проверяет тип модификатора (использование строчных или прописных букв алфавита).

 * @param sym
 * @return возвращает указатель на массив с подходящим алфавитом.
 */
 
char *get_alphabet(char sym)
{
	char *hex_big = "0123456789ABCDEF\0";
   	char *hex_small = "0123456789abcdef\0";
	char *hexDigits = NULL;
	if (sym == 'x')
   		hexDigits = hex_small;
    else
		hexDigits = hex_big;
	return hexDigits;
}

/**
 Заполняет массив result символами конвертированного short int числа.

 * @param tmp
 * @param size
 * @param hexDigits
 * @param result
 */

void get_hex_num(int tmp, int size, char *hexDigits, char result[size])
{
	for (int i = size - 2; i >= 0; i--)
    {
       	result[i] = hexDigits[tmp % 16];
       	tmp = tmp / 16;
    }
}

/**
 Заполняет массив result символами конвертированного unsigned int числа.

 * @param tmp
 * @param size
 * @param hexDigits
 * @param result
 */

void get_hex_num_unsigned(unsigned int tmp, int size, const char *hexDigits, char result[size])
{
	for (int i = size - 2; i >= 0; i--)
    {
       	result[i] = hexDigits[tmp % 16];
        tmp = tmp / 16;
    }
}

/**
 Проверяет число на ноль, попутно пишет символ, если число персталоявляться нулевым согласно признакам.

 * @param size_mas
 * @param result
 * @param format_buffer
 * @param size
 * @param global_counter
 * @return возвращает ноль, если число - на ноль, единицу - в противном случае.
 */

int check_for_zero(int size_mas, char result[size_mas], char **format_buffer, size_t *size, int *global_counter)
{
	int flag_no_zero = 0;
	for (int i = 0; i < size_mas; ++i)
    {
       	if (result[i] != '0')
           	flag_no_zero = 1;

        if (flag_no_zero)
          	*format_buffer = print(*format_buffer, size, result[i], global_counter);
    }
	return flag_no_zero;
}

/**
 Выполняет полную запись аргумента toconvert в виде hex-числа, размера unsigned short int, в строку format_buffer.

 * @param format_buffer
 * @param size
 * @param toconvert
 * @param global_counter
 * @param sym
 * @return возвращает указатель на строку format_buffer с записанным hex-числом toconvert.
 */

char *print_short_hex(char *format_buffer, size_t *size, const unsigned short toconvert, int *global_counter, char sym)
{
    int tmp = toconvert;
    char *hexDigits = get_alphabet(sym);

    char result[5];	
	get_hex_num(tmp, 5, hexDigits, result);

    int flag_no_zero = check_for_zero(4, result, &format_buffer, size, global_counter);
    if (!flag_no_zero)
        format_buffer = print(format_buffer, size, '0', global_counter);
    return format_buffer;
}

/**
 Выполняет полную запись аргумента toconvert в виде hex-числа, размера unsigned int, в строку format_buffer.

 * @param format_buffer
 * @param size
 * @param toconvert
 * @param global_counter
 * @param sym
 * @return возвращает указатель на строку format_buffer с записанным hex-числом toconvert.
 */

char *print_full_hex(char *format_buffer, size_t *size, const unsigned int toconvert, int *global_counter, char sym)
{
    unsigned int tmp = toconvert;
    if (tmp < 0)
        tmp += 4294967295;
	
    const char *hexDigits = get_alphabet(sym);
	
    char result[9];
	get_hex_num_unsigned(tmp, 9, hexDigits, result);

    int flag_no_zero = check_for_zero(8, result, &format_buffer, size, global_counter);
    if (!flag_no_zero)
        format_buffer = print(format_buffer, size, '0', global_counter);
    return format_buffer;
}

/**
 Высчитывает длину записываемого целого числа.

 * @param num
 * @return возвращает длину записываемого целого числа.
 */

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

/**
 Конвертирует цифру записываемого целового числа в символ.

 * @param num
 * @param k
 * @return возвращает цифру числа как символ.
 */

char get_n_char(int num, int k)
{
    int n = (num / (pow(10, k - 1)));
    return n % 10 + '0';
}

/**
 Выполняет полную запись аргумента toprint в виде целого числа в строку format_buffer.

 * @param format_buffer
 * @param size
 * @param toconvert
 * @param global_counter
 * @param sym
 * @return возвращает указатель на строку format_buffer с записанным целым числом toprint.
 */

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

/**
 Выполняет запись аргумента toprint в виде символа в строку format_buffer.

 * @param format_buffer
 * @param size
 * @param toconvert
 * @param global_counter
 * @param sym
 * @return возвращает указатель на строку format_buffer с записанным символом toprint.
 */

char *print_char_sym(char *format_buffer, size_t *size, const int toprint, int *global_counter)
{
    const char sym = (const char)toprint;

    format_buffer = print(format_buffer, size, sym, global_counter);
    return format_buffer;
}

/**
 Записывает в строку buffer аргументы из списка ap в соответствии со спецификаторами и модификатором.

 * @param buffer
 * @param buff_size
 * @param format
 * @param ap
 * @return возвращает длину полученной строки, не учитывая заключительный нуль.
 */

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
                    case 'x':
                    case 'X':
                        format_buffer = print_full_hex(format_buffer, &n, va_arg(ap, unsigned int), &global_counter, cur_sym);
                        break;
                    case 'h':
                        if ((cur_sym = *flag_sym++))
                        {
                            if ((cur_sym == 'x') || (cur_sym == 'X'))
                                format_buffer = print_short_hex(format_buffer, &n, (unsigned short)va_arg(ap, unsigned int), &global_counter, cur_sym);
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

/**
 Реализуемая функция snprintf.

 * @param buffer
 * @param size
 * @param format
 * @return возвращает длину полученной строки, не учитывая заключительный нуль.
 */

int my_snprintf(char *buffer, size_t size, const char *format, ...)
{
    va_list ap;
    va_start(ap, format);
    int read_byte = my_vsnprintf(buffer, size, format, ap);
    va_end(ap);
    return read_byte;
}
