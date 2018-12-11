#include "func.h"
#include "test.h"

int main()
{
    int test_counter = 1;
    char string1[25], string2[25];
    {
        const char *command = "hex %hx";
        int buff_s = 25;
        int data_array[] = {-65431, -32769, -32768, 100, 32766, 32768, 654321, -100, 0, 32767};
        for (int i = 0; i < 10; ++i)
        {
            int n = data_array[i];
            int read_byte1 = snprintf(string1, buff_s, command, n);
            int read_byte2 = my_snprintf(string2, buff_s, command, n);
            answer(compare(string1, string2, read_byte1, read_byte2), test_counter);
            test_counter++;
        }
    }

    {
        const char *command = "hex %X";
        int buff_s = 25;
        int data_array[] = {-65431, 32234769, -323768, 100, 32743466, -32768, -63354321, 0, -327234647};
        for (int i = 0; i < 9; ++i)
        {
            int n = data_array[i];
            int read_byte1 = snprintf(string1, buff_s, command, n);
            int read_byte2 = my_snprintf(string2, buff_s, command, n);
            answer(compare(string1, string2, read_byte1, read_byte2), test_counter);
            test_counter++;
        }
    }

    answer(test1(), test_counter);
    test_counter++;
    answer(test2(), test_counter);

    return 0;
}
