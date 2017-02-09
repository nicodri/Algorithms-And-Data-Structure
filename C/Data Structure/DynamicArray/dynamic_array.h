#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int CAPACITY_INIT = 1;
int GROWTH_FACTOR = 2;

typedef struct DArray {
    int upto;
    int size;
    int *array;
} DArray;

DArray DArray_init();
int append(DArray* arr, int i);
int get(DArray* arr, int index);
int get_index(DArray* arr, int value);
int set(DArray* arr, int index, int value);
int delete(DArray* arr, int value);
void DArray_free(DArray* arr);