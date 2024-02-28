/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:29
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 22:33:49
 */
#include <conio.h>
#include <stdio.h>
#include <time.h>

void printTime(struct tm *);

int main(int argc, const char *argv[]) {
  time_t     now    = time(NULL);
  struct tm *nowPtr = localtime(&now);
  printTime(nowPtr);

  printf("%s", ctime(&now));
  // or
  printf("%s", asctime(nowPtr));

  /*
  double seconds = difftime(time(NULL), start);
  printf("Difftime(time(NULL), start) = %.fs\n", seconds);
  */

  getch();
  return 0;
}

void printTime(struct tm *Time) {
  printf("  Seconds = %d\n", Time->tm_sec);         // range 0 to 59
  printf("  Minutes = %d\n", Time->tm_min);         // range 0 to 59
  printf("    Hours = %d\n", Time->tm_hour);        // range 0 to 23
  printf("Month Day = %d\n", Time->tm_mday);        // range 1 to 31
  printf("    Month = %d\n", Time->tm_mon + 1);     // range 0 to 11
  printf("     Year = %d\n", Time->tm_year + 1900); // since 1900
  printf(" Week Day = %d\n", Time->tm_wday);        // range 0 to 6
  printf(" Year Day = %d\n", Time->tm_yday + 1);    // range 0 to 365
  printf(" Daylight = %d\n", Time->tm_isdst);       // Daylight saving time
}
