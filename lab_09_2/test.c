#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include "my_libstr.h"

#define OK 0
#define FAIL -1

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
	    
	    if(result == FAIL)
	    	return result;		
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