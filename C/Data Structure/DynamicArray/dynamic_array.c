#include "dynamic_array.h"

DArray DArray_init(){
    DArray arr;
    arr.array = (int *) malloc(CAPACITY_INIT*sizeof(int));
    if (arr.array == NULL) {
        printf("Memory Error\n");
        return arr;
    }
    arr.upto = 0;
    arr.size = CAPACITY_INIT;
    return arr;
}

int append(DArray* arr, int i){
    int *iptr;
    if (arr->upto >= arr->size) {
        /* tmp pointer needed below as if allocation failed, original array would be lost */
        iptr = (int *) realloc(arr->array, arr->size*GROWTH_FACTOR*sizeof(int));
        if (iptr == NULL) {
            return -1;
        }
        arr->array = iptr;
        arr->size *= GROWTH_FACTOR;
    }
    arr->array[arr->upto] = i;
    return arr->upto++;
    
        
}

int set(DArray* arr, int index, int value){
    if (index >= arr->upto || index < 0) {
        return -1;
    }
    arr->array[index] = value;
    return arr->upto;
    
}
// Decision to swap the deleted element with the last one to keep the dynamic array
// continuous and as small as possible (order will not be preserved)
int delete(DArray* arr, int value){
    int i;
    int *iptr;
    for (i=0; i< arr->upto; i++){
        if (arr->array[i]==value) {
            arr->array[i] = arr->array[arr->upto--];
            break;
        }
    }
    /* Deallocate memory if too few elements */
    if (arr->upto <= arr->size / 2) {
        /* tmp pointer needed below as if allocation failed, original array would be lost */
        iptr = (int *) realloc(arr->array, (arr->size/GROWTH_FACTOR)*sizeof(int));
        if (iptr == NULL) {
            return -1;
        }
        arr->array = iptr;
        arr->size /= GROWTH_FACTOR;
    }
    return arr->upto;
}

int get(DArray* arr, int index) {
    if (index >= arr->upto || index < 0) {
        return -1;
    }
    return arr->array[index];
}

int get_index(DArray* arr, int value) {
    int i;
    for (i=0; i< arr->upto; i++){
        if (arr->array[i]==value) {
            return i;
        }
    }
    return -1;
}

void DArray_free(DArray *arr) {
    if(arr) {
        if(arr->array)free(arr->array);
        arr->array = NULL;
    }
}

int main() {
    DArray dynarray = DArray_init();

    printf("Filling the dynamic array with 200 first integers\n");
    printf("%d %d\n", dynarray.upto, dynarray.size);
    int i;
    for (i = 0; i < 200; i++) {
        append(&dynarray, i);
        printf("upto %d size %d val %d\n", dynarray.upto, dynarray.size, get(&dynarray, i));
    }
    printf("Test of the set function, set i+1 to index i \n");
    for (i = 185; i < 190; i++) {
        set(&dynarray, i, i+1);
        printf("i %d val %d\n", i, get(&dynarray, i));
    }
    printf("Test of the delete function on index i\n");
    for (i = 180; i < 182; i++) {
        delete(&dynarray, i);
        printf("i %d val %d upto %d\n", i, get(&dynarray, i), dynarray.upto);
    }
    printf("Test of the get index function on value i\n");
    for (i = 180; i < 195; i++) {
        printf("val %d index %d\n", i, get_index(&dynarray, i));
    }
    DArray_free(&dynarray);
    printf("Test of free function\n");
    printf("val %d index %d\n", 181, get_index(&dynarray, 181));
}