#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct people
{
    size_t size;
    size_t size2;
    char *name;
    char *adress;
    char phone[15];
}
people;


people* insert(people *person, char *name, char *adress, char phone[], int i)
{
    people* new_person=(people*)realloc(person, (i+1)*sizeof(people));
    if (new_person)
    {
        size_t size = strlen(name)*sizeof(char);
        new_person[i].size = size;
        new_person[i].name = malloc(size +1);
        strcpy(new_person[i].name, name);

        size_t size2 = strlen(adress)*sizeof(char);
        new_person[i].size = size2;
        new_person[i].adress = malloc(size2 +1);
        strcpy(new_person[i].adress, adress);

        strcpy(new_person[i].phone, phone);
    }
    return (new_person);
}

int main()
{
    FILE *f;
    f = fopen("data.txt", "w");

    people *person = NULL;

    int count = 0;
    int amount;

    char name[15];
    char adress[15];
    char phone[15];

    printf("Input size of info book:\n");
    scanf("%d", &amount);

    while (count < amount)
    {
        printf("Input name:\n");
        scanf("%s", name);

        printf("Input adress:\n");
        scanf("%s", adress);

        printf("Input phone number:\n");
        scanf("%s", phone);

        people* new_person = insert(person, name, adress, phone, count);
        if (new_person)
        {
            person = new_person;
            fprintf(f, "%s, %s, %s\n", person[count].name, person[count].adress, person[count].phone);
        }
        else
            break;
        count++;
   }

    for (int k=0; k<count; k++)
    {
        free(person[k].name);
        free(person[k].adress);
    }
    free(person);

    fclose(f);
    printf("\nMemory free, task complited");
    return 0;
}
