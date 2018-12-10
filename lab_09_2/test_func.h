#ifndef TEST_FUNC_H
#define TEST_FUNC_H
#define OK 0
#define FAIL -1

char *answer(int val);
int test_getline(const char *file_name);
int test_replace(const char *line, const char *replace_what, const char *replace_with, char *answer);
#endif