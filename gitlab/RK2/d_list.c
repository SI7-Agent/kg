#include <stdio.h>
#include <stdlib.h>

#include "d_list.h"

name *add(name *start, Student *data)
{
    name *head = start;
    name *tmp = malloc(sizeof(name));
    tmp->guy = data;
    tmp->next = NULL;
    if (!start)
    {
        head = tmp;
        head->prev = NULL;
    }
    else
    {
        for (; start->next; start = start->next);
        name *prev_tmp = start;
        start->next = tmp;
        tmp->prev = prev_tmp;
    }
    return head;
}

marks *add_m()
{
    int flag = 0;
    marks *head = NULL;
    marks *start;
    int flag2 = 0;
    while (!flag)
    {
        marks *new_node = malloc(sizeof(marks));
        printf("\nInput mark (1 to 5)\n");
        int mark;
        fflush(stdin);
        int check = scanf("%d", &mark);
        while ((mark < 1) || (mark > 5) || (!check))
        {
            printf("\nError. Try again\n");
            fflush(stdin);
            check = scanf("%d", &mark);
        }
        new_node->mark = mark;
        new_node->next = NULL;
        if (!head)
        {
            head = new_node;
            head->prev = NULL;
        }
        else
        {
            marks *tmp_prev = head;
            new_node->mark = mark;
            head->next = new_node;
            head = head->next;
            head->prev = tmp_prev;
        }
        if (!flag2)
        {
            start = head;
            flag2 = 1;
        }
        printf("\nFinish? 0/1\n");
        fflush(stdin);
        check = scanf("%d", &flag);
        while ((flag > 1) || (flag < 0) || (!check))
        {
            printf("\nError. Try again\n");
            fflush(stdin);
            check = scanf("%d", &flag);
        }
    }
    return start;
}

Student *add_st()
{
    Student *data = malloc(sizeof(Student));

    printf("\nInput name (up to 20 syms)\n");
    char *name_buf = (char*)malloc(20);
    gets(name_buf);
    data->name_st = name_buf;

    printf("\nInput age\n");
    int age;
    int check = scanf("%d", &age);
    while ((age < 1) || (age > 130) || (!check))
    {
        printf("\nError. Try again\n");
        fflush(stdin);
        check = scanf("%d", &age);
    }
    data->age = age;

    data->mark = add_m();

    return data;
}

void print_big_struct(name *all)
{
    while (all)
    {
        printf("\nName: %s\n\nAge: %d\n", all->guy->name_st, all->guy->age);
        print_marks(all->guy->mark);
        all = all->next;
    }
}

void print_marks(marks *all)
{
    printf("\nMark list:");
    while (all)
    {
        printf(" %d", all->mark);
        all = all->next;
    }
    printf("\n\n");
}
