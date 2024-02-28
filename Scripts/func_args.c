#include <stdarg.h>
#include <stdio.h>

float average(int size, ...) {
  va_list valist;
  float   sum = 0;

  va_start(valist, size);
  for (int i = 0; i < size; i++)
    sum += va_arg(valist, double);
  va_end(valist);

  return sum / size;
}

int main() {
  printf("%.2f", average(3, 3.0, 2.0, 1.0));
  return 0;
}
