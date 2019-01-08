#ifndef FUNC_H
#define FUNC_H

#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>

typedef struct node_type
{
    void *data;
    struct node_type *next;
}node_type;

void add_elem(node_type **head, void *data);
void *pop_back(node_type **head);
void *pop_front(node_type **head);
void append(node_type **head_a, node_type **head_b);
int comp_int(const void *i, const void *j);
void sorted_insert(node_type **head, node_type *element,
int (*comparator)(const void *, const void *));
void sort(node_type **head);
void list_print(node_type *head);
void free_list(node_type *head);
void get_list_copy(node_type *orig, node_type **copy);
node_type *delete_head(node_type *head);

#endif
