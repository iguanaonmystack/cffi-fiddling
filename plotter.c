#include <stdlib.h>
#include <stdio.h>

#include "plotter.h"

char * mystring;

void *mymalloc(size_t size) {
    void * mem = malloc(size);
    fprintf(stderr, "allocated %zd bytes at %p\n", size, mem);
    return mem;
}
void myfree(void *ptr) {
    fprintf(stderr, "freeing memory at %p\n", ptr);
    free(ptr);
}

void plot(int *** data, size_t xdepth, size_t ydepth, size_t zdepth) {
    size_t i, j, k;
    for (i = 0; i < xdepth; i ++) {
        printf("x = %2zd |      z\n", i);
        printf("       |");
        for (k = 0; k < zdepth; k ++) {
            printf(" %3zd ", k);
        }
        printf("\n-------|------------------------\n");
        printf("  y    |\n");

        for (j = 0; j < ydepth; j ++) {
            printf("    %2zd |", j);
            for (k = 0; k < zdepth; k ++) {
                printf("  %03d", data[i][j][k]);
            }
            printf("\n");
        }
        printf("\n");
    }
}

void hello(char * name) {
    printf("hello %s\n", name);
}

void numbers(int * data, size_t size) {
    size_t i;
    for (i = 0; i < size; i ++) {
        if (i != 0) {
            printf(", ");
        }
        printf("%d", data[i]);
    }
    printf("\n");
}

/* A main with some test data, so we can compile just this file with `gcc plotter.c -o test` and run ./test */
int main(int argc, char ** argv) {
    size_t xdepth = 2, ydepth = 3, zdepth = 4;
    size_t i, j, k;

    /* allocate memory and assign xyz values */
    int *** data = malloc(sizeof(int **) * xdepth);
    for (i = 0; i < xdepth; i ++) {
        data[i] = malloc(sizeof(int *) * ydepth);
        for (j = 0; j < ydepth; j ++) {
            data[i][j] = malloc(sizeof(int) * zdepth);
            for (k = 0; k < zdepth; k ++) {
                data[i][j][k] = (i * 100) + (j * 10) + (k);
            }
        }
    }

    plot(data, xdepth, ydepth, zdepth);

    /* cleanup */
    for (i = 0; i < xdepth; i ++) {
        for (j = 0; j < ydepth; j ++) {
            for (k = 0; k < zdepth; k ++) {
                /* data[i][j][k] is just an int */
            }
            free(data[i][j]); data[i][j] = NULL;
        }
        free(data[i]); data[i] = NULL;
    }
    free(data); data = NULL;
}
