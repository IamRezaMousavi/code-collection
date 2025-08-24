/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:29
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 21:54:37
 */
#include <stdio.h>
#include <unistd.h>

int main(int argc, const char *argv[]) {
  int n = 5;

  for (int i = n; i > 0; i--) {
	printf("%d\n", i);
	sleep(1);
  }
  printf("It's done\n");

  return 0;
}
