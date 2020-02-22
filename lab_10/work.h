#ifndef WORK_H
#define WORK_H

#include <stdio.h>
#include "func.h"

int get_size(FILE *f);
void fill_list_mas(int **mas1, int **mas2, node_type **head1, node_type **head2, FILE *f);
void task(FILE *out, node_type *head1, node_type *head2);
void print_in_file(FILE *f_out, node_type *head);
void do_func(FILE *f1, FILE *f2, char *argv[]);

#endif
