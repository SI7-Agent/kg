#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include "test_func.h"

int main()
{
    printf("Test str_replace 1 %s\n", answer(test_replace("caac","aa","cc","cccc")));
    printf("Test str_replace 2 %s\n", answer(test_replace("aacc","aa","cc","cccc")));
    printf("Test str_replace 3 %s\n", answer(test_replace("ccaa","aa","cc","cccc")));
    printf("Test str_replace 4 %s\n", answer(test_replace("ccaaaa","aa","cc","cccccc")));
    printf("Test str_replace 5 %s\n", answer(test_replace("aaccaa","aa","cc","cccccc")));
    printf("Test str_replace 6 %s\n", answer(test_replace("aaaacc","aa","cc","cccccc")));
    printf("Test str_replace 7 %s\n", answer(test_replace("aaaaaa","aa","cc","cccccc")));
    printf("Test str_replace 8 %s\n", answer(test_replace("aaaaaa","aaa","cc","cccc")));
    printf("Test str_replace 9 %s\n", answer(test_replace("aaaaaa","aaa","cccc","cccccccc")));
    printf("Test str_replace 10 %s\n", answer(test_replace("aaaaaa","aaa","","")));

    printf("Test getline 1 %s\n", answer(test_getline("in_2.txt")));
    printf("Test getline 2 %s\n", answer(test_getline("in_3.txt")));
    printf("Test getline 3 %s\n", answer(test_getline("in_4.txt")));
    printf("Test getline 4 %s\n", answer(test_getline("in_6.txt")));
    printf("Test getline 5 %s\n", answer(test_getline("in_7.txt")));
    printf("Test getline 6 %s\n", answer(test_getline("in_5.txt")));

    return 0;
}
