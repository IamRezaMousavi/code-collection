/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-03-11 16:09:45
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-03-11 16:20:01
 */
#include <stdio.h>

int main(int argc, const char *argv[]) {
  printf("Type      = %%c\t%%d\t%%f\n");

  char character;
  character = 'c';
  printf("Character = %c\t%d\t%f\n", character, character, character);
  character = 36;
  printf("Character = %c\t%d\t%f\n", character, character, character);
  character = 40.75;
  printf("Character = %c\t%d\t%f\n", character, character, character);

  int integer;
  integer = 'c';
  printf("Integer   = %c\t%d\t%f\n", integer, integer, integer);
  integer = 36;
  printf("Integer   = %c\t%d\t%f\n", integer, integer, integer);
  integer = 40.75;
  printf("Integer   = %c\t%d\t%f\n", integer, integer, integer);

  float floating;
  floating = 'c';
  printf("Floating  = %c\t%d\t%f\n", floating, floating, floating);
  floating = 450;
  printf("Floating  = %c\t%d\t%f\n", floating, floating, floating);
  floating = 40.75;
  printf("Floating  = %c\t%d\t%f\n", floating, floating, floating);

  return 0;
}
