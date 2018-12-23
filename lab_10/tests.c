#include "tests.h"

void test1(node_type *list, int *data)
{
    int counter = 0;
    int flag = 0;
    while (list)
    {
        if (!flag)
        {
            if (*(int*)list->data == data[counter])
                flag = 0;
            else
                flag = 1;
            counter++;
        }
        list = list->next;
    }
    if (flag)
        printf("Test failed\n");
    else
        printf("Test passed\n");
}

void test2(node_type *list1, node_type *list2, int *data)
{
    append(&list1, &list2);
    int counter = 0;
    int flag = 0;
    while (list1)
    {
        if (!flag)
        {
            if (*(int*)list1->data == data[counter])
                flag = 0;
            else
                flag = 1;
            counter++;
        }
        list1 = list1->next;
    }
    if (flag)
        printf("Test failed\n");
    else
        printf("Test passed\n");
}

void test3(node_type *list, int *data)
{
    sort(&list);
    int counter = 0;
    int flag = 0;
    while (list)
    {
        if (!flag)
        {
            if (*(int*)list->data == data[counter])
                flag = 0;
            else
                flag = 1;
            counter++;
        }
        list = list->next;
    }
    if (flag)
        printf("Test failed\n");
    else
        printf("Test passed\n");
}

void test4(node_type *list, int *data)
{
    int flag = 0;

    void *data_f_test = pop_front(&list);
    void *data_b_test = pop_back(&list);

    if ((*(int*)data_f_test == data[0]) && (*(int*)data_b_test == data[1]))
        flag = 0;
    else
        flag = 1;

    if (flag)
        printf("Test failed\n");
    else
        printf("Test passed\n");
}
