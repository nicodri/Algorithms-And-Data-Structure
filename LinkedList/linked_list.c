#include "linked_list.h"

Item *new_item(int value){
    Item *newitem = (Item *) malloc(sizeof(Item));
    newitem->value = value;
    newitem->next = NULL;
    return newitem;
}

Item *insert_front(Item *list, int value){
    Item *newitem = new_item(value);
    newitem->next = list;
    return newitem;
}

int get(Item *list, int index){
    int ctr = 0;
    Item* p;
    for(p = list; p!= NULL; p = p->next){
        if (ctr == index){
            return p->value;
        }
        ctr++;
    }
    return -1;
}

int get_index(Item *list, int value){
    int index = 0;
    Item* p;
    for(p = list; p!= NULL; p = p->next){
        if (p->value == value){
            return index;
        }
        index++;
    }
    return -1;    
}


Item* remove_item(Item* list, int value){
    Item *previous = NULL;
    /* Case we remove the first item */
    if (list->value == value){
        previous = list->next;
        free(list);
        return previous;
    }
    for(Item *current = list; current!= NULL; current = current->next){
        if (current->value == value){
            previous->next = current->next;
            return list;
        }
        previous = current;
    }
    return NULL;    
}

void free_all(Item* list) {
    Item *next;
    for(Item *p = list; p!= NULL; p = next){
        next = p->next;
        free(p);
    }
}

int main(){
    int i;
    Item *list = new_item(0);
    printf("Inserting 6 first integers\n");
    for (i=1; i < 6; i++){
        list=insert_front(list, i);
    }
    printf("Getting 6 first integers\n");
    for (i=0; i < 6; i++){
        printf("i %d Item %d\n", i, get(list, i));
    }
    printf("Getting all elements with 3 removed\n");
    list = remove_item(list, 3);
    for (i=0; i <= 5; i++){
        printf("i %d Item %d\n", i, get(list, i));
    }
    printf("Try to retrieve the index of 3\n");
    printf("Index for 3 %d\n", get_index(list, 3));
    free_all(list);
    printf("Check of the free_all function\n");
    printf("%d\n", get(list, 1));
}