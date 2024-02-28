/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-04-27 03:21:20
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-04-27 03:26:22
 */
#include <stdio.h>
#include <windows.h>

int main(int argc, const char *argv[]) {
  COORD c;
  c.X = 40;
  c.Y = 16;

  SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);

  printf("HELLO");

  return 0;
}
