#include <stdio.h>
#include <string.h>

int my_strcspn(char *string, char *key)
{
    for (int i = 0; i<sizeof(string)+1; i++)
    {
        for (int j = 0; j<sizeof(key); j++)
        {
            if (string[i] == key[j])
            {
                if ((string[i] == "\0") && (key[j] == "\0"))
                    return 0;
                else
                    return i;
            }
        }
    }
    return 0;
}

int main()
{
    int test = my_strcspn("Hello", "aye");
    printf("%d", test);
    return 0;
}
