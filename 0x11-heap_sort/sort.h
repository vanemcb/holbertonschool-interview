#ifndef SORT_H
#define SORT_H

void print_array(const int *array, size_t size);
void sift_down(int *array, size_t start, size_t end, size_t size);
void heapify(int *array, size_t size);
void heap_sort(int *array, size_t size);

#endif /*SORT_H*/
