#include "work.h"

/**
 Считает количество данных для массива для задачи.

 * @param f
 * @return количество данных для массива.
 */

int get_size(FILE *f)
{
    int size = 0;
    int num;

    while(fscanf(f, "%d", &num) == 1)
        size++;

    return size;
}

/**
 Заполняет списки и массивы данных из файла.

 * @param mas1
 * @param mas2
 * @param head1
 * @param head2
 * @param f
 */

void fill_list_mas(int **mas1, int **mas2, node_type **head1, node_type **head2, FILE *f)
{
    int data1;
    int size1 = get_size(f);
    fseek(f, 1, SEEK_CUR);
    int size2 = get_size(f);
    *mas1 = (int*)malloc(sizeof(int)*size1);
    *mas2 = (int*)malloc(sizeof(int)*size2);

    if ((mas1) && (mas2))
    {
        fseek(f, 0, SEEK_SET);
        for (int i = 0; i < size1; i++)
        {
            fscanf(f, "%d", &data1);
            *(*mas1 + i) = data1;
            add_elem(head1, (*mas1 + i));
        }

        fseek(f, 3, SEEK_CUR);

        for (int i = 0; i < size1; i++)
        {
            fscanf(f, "%d", &data1);
            *(*mas2 + i) = data1;
            add_elem(head2, (*mas2 + i));
        }
    }
}

/**
 Выполняет задачу, описанную в файле.

 * @param out
 * @param head1
 * @param head2
 * @param mas1
 * @param mas2
 */

void task(FILE *out, node_type *head1, node_type *head2)
{
    void *min_1 = NULL, *min_2 = NULL, *max_1 = NULL, *max_2 = NULL, *max_global = NULL, *min_global = NULL;
    sort(&head1);
    sort(&head2);
    node_type *tmp1 = NULL;
    node_type *tmp2 = NULL;
    get_list_copy(head1, &tmp1);
    get_list_copy(head2, &tmp2);

    append(&tmp1, &tmp2);
    sort(&tmp1);

    min_1 = pop_front(&head1);
    min_2 = pop_front(&head2);

    max_1 = pop_back(&head1);
    max_2 = pop_back(&head2);

    printf("Sorted united:\n");
    fprintf(out, "Sorted united:\n");
    list_print(tmp1);
    print_in_file(out, tmp1);

    printf("\nMax 1: %d, Min 1: %d, Max 2: %d, Min 2: %d\n", *(int*)max_1, *(int*)min_1, *(int*)max_2, *(int*)min_2);
    fprintf(out, "\nMax 1: %d, Min 1: %d, Max 2: %d, Min 2: %d\n", *(int*)max_1, *(int*)min_1, *(int*)max_2, *(int*)min_2);
    if (*(int*)min_1 >= *(int*)min_2)
        min_global = min_2;
    else
        min_global = min_1;

    if (*(int*)max_1 >= *(int*)max_2)
        max_global = max_1;
    else
        max_global = max_2;
    printf("Max global: %d, Min global: %d\n", *(int*)max_global, *(int*)min_global);
    fprintf(out, "Max global: %d, Min global: %d\n", *(int*)max_global, *(int*)min_global);
    free_list(tmp1);
    free_list(head1);
    free_list(head2);
}

/**
 Печатает список в файл.

 * @param f_out
 * @param head
 */

void print_in_file(FILE *f_out, node_type *head)
{
    node_type *cur;
    cur = head;
    do
    {
        fprintf(f_out, "%d ", *(int*)cur->data);
        cur = cur->next;
    }
    while(cur);
}

/**
 Выполняет основную программу в зависимости от аргументов командной строки.

 * @param f1
 * @param f2
 * @param argv
 */

void do_func(FILE *f1, FILE *f2, char *argv[])
{
    node_type *list1 = NULL;
    node_type *list2 = NULL;
    int *data1 = NULL;
    int *data2 = NULL;
    fill_list_mas(&data1, &data2, &list1, &list2, f1);

    if ((data1) && (data2))
    {
        if (strcmp("pop_f", argv[1]) == 0)
        {
            printf("Start list:\n");
            list_print(list1);
            void *data = pop_front(&list1);
            printf("\nPoped element: %d\n", *(int*)data);
            printf("Final list:\n");
            list_print(list1);
            print_in_file(f2, list1);
            free_list(list1);
        }
        if (strcmp("pop_b", argv[1]) == 0)
        {
            printf("Start list:\n");
            list_print(list1);
            void *data = pop_back(&list1);
            printf("\nPoped element: %d\n", *(int*)data);
            printf("Final list:\n");
            list_print(list1);
            print_in_file(f2, list1);
            free_list(list1);
        }
        if (strcmp("append", argv[1]) == 0)
        {
            printf("Start list 1:\n");
            list_print(list1);
            printf("\nStart list 2:\n");
            list_print(list2);
            append(&list1, &list2);
            printf("\n\nList 1 after append:\n");
            list_print(list1);
            printf("\nStart list 2 after append:\n");
            list_print(list2);
            print_in_file(f2, list1);
            free_list(list1);
        }
        if (strcmp("sort", argv[1]) == 0)
        {
            printf("Start list 1:\n");
            list_print(list1);
            sort(&list1);
            printf("\nList 1 after sort:\n");
            list_print(list1);
            print_in_file(f2, list1);
            fprintf(f2, "\n");
            printf("\n\nStart list 2:\n");
            list_print(list2);
            sort(&list2);
            printf("\nList 2 after sort:\n");
            list_print(list2);
            print_in_file(f2, list2);
            free_list(list1);
            free_list(list2);
        }
        if (strcmp("task", argv[1]) == 0)
            task(f2, list1, list2);
    }
    else
        printf("Data error\n");

    if (data1)
        free(data1);

    if (data2)
        free(data2);
}
