/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-07-23 01:26:36
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-09-25 17:49:13
 */
#include <conio.h>
#include <stdio.h>

int main(int argc, const char *argv[]) {
  char *names[] = {"Ali", "Reza", "Mohammad"};

  printf("Names:\n");
  for (int i = 0; i < 3; i++)
    printf("\t%s\n", names[i]);

  getch();
  return 0;
}
