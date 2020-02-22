#include <stdio.h>
#include <string.h>
#include "my_strcspn.h"

int main()
{
    int test = my_strcspn("Hello", "aye");
    printf("%d", test);
    return 0;
}
