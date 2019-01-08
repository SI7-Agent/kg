#include "func.h"

/**
 Добавляет элемент в конец списка.

 * @param head
 * @param data
 */

void add_elem(node_type **head, void *data)
{
    node_type *tmp = (node_type*)malloc(sizeof(node_type));
    tmp->data = data;
    tmp->next = NULL;

    if (!(*head))
    {
        *head = tmp;
    }
    else
    {
        node_type *start = *head;
        for (; start->next; start = start->next);
        start->next = tmp;
    }
}

/**
 Извлекает элемент с конца списка.

 * @param head
 * @return возвращает адрес, хранящийся в инфо части последнего элемента.
 */

void *pop_back(node_type **head)
{
    node_type *cur_node = NULL;
    node_type *prev_node = NULL;

    void *end_node = NULL;

    if (head)
    {
        if (*head)
        {
            cur_node = *head;
            while (cur_node->next)
            {
                prev_node = cur_node;
                cur_node = cur_node->next;
            }

            if (prev_node == NULL)
            {
                end_node = (*head)->data;
                free(*head);
                *head = NULL;
            }
            else
            {
                end_node = cur_node->data;
                free(cur_node->next);
                prev_node->next = NULL;
            }
        }
    }
    return end_node;
}

/**
 Извлекает элемент с начала списка.

 * @param head
 * @return возвращает адрес, хранящийся в инфо части первого элемента.
 */


void *pop_front(node_type **head)
{
    node_type *cur_node = NULL;
    node_type *prev_node = NULL;

    void *start_node = NULL;

    if (head)
    {
        if (*head)
        {
            cur_node = *head;
            if (cur_node->next)
            {
                prev_node = cur_node;
                cur_node = prev_node->next;
                start_node = prev_node->data;
                free(*head);
                *head = cur_node;
            }
            else
            {
                start_node = cur_node->data;
                free(*head);
                *head = NULL;
            }
        }
    }
    return start_node;
}

/**
 Объединяет два списка в один, в то же время очищает второй список.

 * @param head_a
 * @param head_b
 */

void append(node_type **head_a, node_type **head_b)
{
    node_type *iter = *head_a;
    if (*head_a)
        for (; iter->next != NULL; iter = iter->next);

    if (*head_b)
    {
        while (*head_b)
        {
            void *data = pop_front(head_b);
            add_elem(head_a, data);
        }
    }
}

/**
 Сравнивает два элемента.

 * @param i
 * @param j
 * @return возвращает значение, большее нуля, если первый элемент больше второго,
 * в противном случае возвращает значение, меньшее нуля.
 */

int comp_int(const void *i, const void *j)
{
    return *(int*)i - *(int*)j;
}

/**
 Вставляет элемент в отсортированный список, чтобы список пролжать быть отсортированным.

 * @param head
 * @param element
 */

void sorted_insert(node_type **head, node_type *element,
int (*comparator)(const void *, const void *))
{
    node_type *tmp = *head, *prev_tmp;
    for(prev_tmp = NULL; (tmp) && (comparator(element->data, tmp->data) > 0); )
    {
        prev_tmp = tmp;
        tmp = tmp->next;
    }

    if(!prev_tmp)
    {
        element->next = *head;
        *head = element;
    }
    else
    {
        element->next = tmp;
        prev_tmp->next = element;
    }
}

/**
 Сортирует список методом вставок.

 * @param root
 */

void sort(node_type **head)
{
    node_type *element_to_insert, *new_root = NULL;

    for(node_type *current_element = *head; current_element; )
    {
        element_to_insert = current_element;
        current_element = current_element->next;
        sorted_insert(&new_root, element_to_insert, comp_int);
    }
    if(new_root)
        *head = new_root;
}

/**
 Выводит список на экран.

 * @param head
 */

void list_print(node_type *head)
{
    if (head)
    {
        node_type *cur;
        cur = head;
        do
        {
            printf("%d ", *(int*)(cur->data));
            cur = cur->next;
        }
        while(cur);
    }
    else
        printf("Empty list\n");
}

/**
 Удаляет (с очисткой) головной элемент.

 * @param root
 * @return возвращает список без первого элемента.
 */

node_type *delete_head(node_type *head)
{
  node_type *temp;
  temp = head->next;
  free(head);
  return(temp);
}

/**
 Очищает список.

 * @param head
 */

void free_list(node_type *head)
{
    if (head)
        while (head)
            head = delete_head(head);
}

/**
 Создает копию списка.

 * @param orig
 * @param copy
 */

void get_list_copy(node_type *orig, node_type **copy)
{
    while (orig)
    {
        add_elem(copy, orig->data);
        orig = orig->next;
    }
}
