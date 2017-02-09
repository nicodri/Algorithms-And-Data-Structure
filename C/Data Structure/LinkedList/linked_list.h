#include <stdlib.h>
#include <stdio.h>

typedef struct item {
    int value;
    struct item* next;
} Item;

void free_all(Item* list);
Item* remove_item(Item* list, int value);
int get_index(Item *list, int value);
int get(Item *list, int index);
Item *insert_front(Item *list, int value);
Item *new_item(int value);