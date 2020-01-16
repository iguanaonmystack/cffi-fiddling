/* plotter.h */

extern void plot(int *** data, size_t xdepth, size_t ydepth, size_t zdepth);
extern void hello(char * name);
extern void numbers(int * data, size_t size);

void *mymalloc(size_t size);
void myfree(void *ptr);
