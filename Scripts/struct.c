/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:29
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 21:55:48
 */
#include <conio.h>
#include <stdio.h>

typedef struct {
  int   id;
  char *first_name;
  char *last_name;
  float gpa;
} Student;

void displayStudent(Student std);

int main(int argc, const char *argv[]) {
  Student std1 = {9710, "Reza", "Mousavi", 19.75};
  displayStudent(std1);

  getch();
  return 0;
}

void displayStudent(Student std) {
  printf("        ID: %d\n", std.id);
  printf("First Name: %s\n", std.first_name);
  printf(" Last Name: %s\n", std.last_name);
  printf("       GPA: %.2f\n", std.gpa);
}
