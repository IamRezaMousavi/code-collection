/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-30 19:08:00
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 19:23:43
 */
#include <stdio.h>

typedef struct Student {
  int   id;
  char *first_name;
  char *last_name;
  float gpa;
  int (*someFunction)();
} Student;

void displayStudent(Student std) {
  printf("        ID: %d\n", std.id);
  printf("First Name: %s\n", std.first_name);
  printf(" Last Name: %s\n", std.last_name);
  printf("       GPA: %.2f\n", std.gpa);
}

int func() {
  return 20;
}

Student studentConstructor() {
  Student c = {.id = 9710, .first_name = "Reza", .last_name = "Mousavi", .someFunction = &func};
  return c;
}

int main(int argc, const char *argv[]) {
  Student one = studentConstructor();
  displayStudent(one);
  printf("Resut is %d\n", one.someFunction());

  return 0;
}
