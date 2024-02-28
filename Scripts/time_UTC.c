/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-30 22:34:08
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 22:38:15
 */
#include <stdio.h>
#include <time.h>

int main(int argc, const char *argv[]) {
  time_t     nowUTC = time(NULL);
  struct tm *nowPtr = gmtime(&nowUTC); // UTC = Coordinated Universal Time

  printf("%s", asctime(nowPtr));

  return 0;
}
