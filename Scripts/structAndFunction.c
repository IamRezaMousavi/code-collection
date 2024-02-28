/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-30 19:08:00
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 19:23:43
 */
#include <stdio.h>

typedef struct Class {
  int (*someFunction)();
} Class;

int function() {
  return 0;
}

Class classConstructor() {
  Class c;
  c.someFunction = &function;
  return c;
}

int main(int argc, const char *argv[]) {
  Class one = classConstructor();
  printf("Print result: %d\n", one.someFunction());

  return 0;
}
