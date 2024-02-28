/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:28
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 21:44:26
 */
#include <conio.h>
#include <stdio.h>

void getDouble(int number);
void getDoubleByPointer(int *numberPtr);

int main(int argc, const char *argv[]) {
  int number;
  printf("Please type a number:");
  scanf("%d", &number);

  printf("The number is %d\n", number);
  getDouble(number);
  printf("The number After getDouble is %d\n\n", number);

  printf("The number is %d\n", number);
  getDoubleByPointer(&number);
  printf("The number After getDoubleByPointer is %d\n", number);

  getch();
  return 0;
}

void getDouble(int number) {
  number *= 2;
  printf("Number in getDouble function = %d\n", number);
}

void getDoubleByPointer(int *numberPtr) {
  (*numberPtr) *= 2;
  printf("Number in getDoubleByPointer function = %d\n", *numberPtr);
}
