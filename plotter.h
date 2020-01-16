/* plotter.h */

extern int ** data[2];
extern char * mystring;

extern void plot(size_t xdepth, size_t ydepth, size_t zdepth);
extern void hello(char * name);
extern void numbers(int * data, size_t size);

void *mymalloc(size_t size);
void myfree(void *ptr);
