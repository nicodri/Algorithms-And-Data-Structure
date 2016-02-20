#include <stdint.h>
#include <stdio.h>

void merge(int list[], int down, int middle, int top){
    int size = top - down + 1;
    // Copying list
    int templist[size];
    for (int i=0; i < size; i++) templist[i] = list[i + down];

    // Going through the sublists
    int ileft = down;
    int iright = middle + 1;
    int i = down;
    while ((ileft <= middle) && (iright <= top)){
        if (templist[ileft - down] > templist[iright - down]){
            list[i++] = templist[iright++ - down];
        }
        else{
            list[i++] = templist[ileft++ - down];
        }
    }

    // Finishing the filling
    while (ileft <= middle) list[i++] = templist[ileft++ - down];
    while (iright <= top) list[i++] = templist[iright++ - down];

}

void merge_sort(int list[], int down, int top){
    if (top - down > 0) {
        int middle = (top + down) / 2;
        // Sorting left
        merge_sort(list, down, middle);
        // Sorting right
        merge_sort(list, middle + 1, top);
        // Merging
        merge(list, down, middle, top);
    }
}

int main(){
    int test[] = {5, 2, 3, 1 , 8, 7, 6, 4};
    for (int i=0; i<8; i++) printf("%i, ", test[i]);
    printf("\n");
    merge_sort(test, 0, 7);
    for (int i=0; i<8; i++) printf("%i, ", test[i]);
    printf("\n");

}