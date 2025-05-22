// C program to demonstrate dynamic memory allocation
#include <stdio.h>
#include <stdlib.h>

int* arr = malloc(3 * sizeof(int));
arr[0] = 1; arr[1] = 2; arr[2] = 3;

int* temp = malloc(6 * sizeof(int));
for (int i = 0; i < 3; i++) temp[i] = arr[i];
free(arr);
arr = temp;
arr[3] = 4;