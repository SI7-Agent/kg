#include "func.h"
#include "test.h"

/**
 Печатает информацию о проводимом тесте.

 * @param val
 * @param id
 */

void answer(int val, int id)
{
    if (val == OK)
       printf("%s %d %s\n", "test", id, "PASSED");

    else
        printf("%s %d %s\n", "test", id, "FAILED");
}

/**
 Проводит мульти-тестирование 1

 * @return возвращает статус тестирования.
 */

int test1()
{
    char *buf1 = (char*)malloc(MAX_BUF_LEN);
    char *buf2 = (char*)malloc(MAX_BUF_LEN);
    int flag;

    if (buf1 && buf2)
    {
        char sym = 'B';

        int read_byte1 = my_snprintf(buf1, MAX_BUF_LEN, "%c olo %i %hx", sym, -70, -170);
        int read_byte2 = snprintf(buf2, MAX_BUF_LEN, "%c olo %i %hx", sym, -70, -170);
        flag = compare(buf1, buf2, read_byte1, read_byte2);

        free(buf1);
        free(buf2);
    }
    else
        flag = FAIL;

    return flag;
}

/**
 Проводит мульти-тестирование 2.

 * @return возвращает статус тестирования.
 */

int test2()
{
    char *buf1 = (char*)malloc(MAX_BUF_LEN);
    char *buf2 = (char*)malloc(MAX_BUF_LEN);
    int flag;

    if (buf1 && buf2)
    {
        int read_byte1 = my_snprintf(buf1, MAX_BUF_LEN, "My %c%c%c%c is %c. I am %i (%hx) years old.", 'n', 'a', 'm', 'e', 'K', 197, 197);
        int read_byte2 = snprintf(buf2, MAX_BUF_LEN, "My %c%c%c%c is %c. I am %i (%hx) years old.", 'n', 'a', 'm', 'e', 'K', 197, 197);
        flag = compare(buf1, buf2, read_byte1, read_byte2);
        free(buf1);
        free(buf2);
    }
    else
        flag = FAIL;

    return flag;
}

/**
 Сравнивает результат работы библиотечной функции snprintf и реализованной функции my_snprintf.

 * @param buf1
 * @param buf2
 * @param read_byte1
 * @param read_byte2
 * @return возвращает статус сравнения.
 */

int compare(char *buf1, char *buf2, int read_byte1, int read_byte2)
{
    int flag = OK;
    if(read_byte1 != read_byte2)
        flag = FAIL;

    if(memcmp(buf1, buf2, strlen(buf2)) != 0)
        flag = FAIL;

    if(flag == FAIL)
    {
        printf("%s\n",buf1);
        printf("%s\n",buf2);
    }
    return flag;
}
