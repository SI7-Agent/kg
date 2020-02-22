#include <stdio.h>

#include "work.h"
#include "tests.h"

int main()
{
    node_type *list_test1 = NULL;
    node_type *list_test2 = NULL;
    node_type *list_test3 = NULL;

    int data1 = 10, data2 = 30, data3 = 20, data4 = 15, data5 = 9, data6 = 0, data7 = 15;
    int expected1[] = {30, 20, 10, 15, 9, 0, 15};
    int expected2[] = {30, 20, 10, 15, 9, 0, 15, 10, 30, 20, 15, 9, 0, 15};
    int expected3[] = {0, 0, 9, 9, 10, 10, 15, 15, 15, 15, 20, 20, 30, 30};
    int expected4[] = {15, 10};

    add_elem(&list_test1, &data2);
    add_elem(&list_test1, &data3);
    add_elem(&list_test1, &data1);
    add_elem(&list_test1, &data7);
    add_elem(&list_test1, &data5);
    add_elem(&list_test1, &data6);
    add_elem(&list_test1, &data4);

    add_elem(&list_test2, &data1);
    add_elem(&list_test2, &data2);
    add_elem(&list_test2, &data3);
    add_elem(&list_test2, &data4);
    add_elem(&list_test2, &data5);
    add_elem(&list_test2, &data6);
    add_elem(&list_test2, &data7);

    add_elem(&list_test3, &data7);
    add_elem(&list_test3, &data6);
    add_elem(&list_test3, &data5);
    add_elem(&list_test3, &data4);
    add_elem(&list_test3, &data3);
    add_elem(&list_test3, &data2);
    add_elem(&list_test3, &data1);

    printf("Adding elements test\n");
    test1(list_test1, expected1);

    printf("\nAppending lists test\n");
    test2(list_test1, list_test2, expected2);

    printf("\nSorting test\n");
    test3(list_test1, expected3);

    printf("\nPopping front and back test\n");
    test4(list_test3, expected4);
}
