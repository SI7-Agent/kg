#ifndef D_LIST_H
#define D_LIST_H

typedef struct marks
{
    struct marks *prev;
    struct marks *next;
    int mark;
}marks;

typedef struct Student
{
    char* name_st;
    int age;
    marks *mark;
}Student;

typedef struct name
{
    struct name *prev;
    struct name *next;
    Student *guy;
}name;

name *add(name *start, Student *data);
marks *add_m();
Student *add_st();
void print_big_struct(name *all);
void print_marks(marks *all);


#endif // D_LIST_H
