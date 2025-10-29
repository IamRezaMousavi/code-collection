/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:29
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-10-28 02:32:29
 */
#include <stdio.h>
#include <time.h>

// For Find Clock Ticks
void clock_ticks();
void printTime(struct tm *);
void formatTime(struct tm *);

// For Time Difference
int main(int argc, const char *argv[]) {
  time_t start = time(NULL);
  struct tm *startPtr = localtime(&start);
  formatTime(startPtr);
  printTime(startPtr);

  printf("%s", ctime(&start));
  // or
  printf("%s", asctime(startPtr));

  double seconds = difftime(time(NULL), start);
  printf("Difftime(time(NULL), start) = %.fs\n", seconds);

  return 0;
}

void clock_ticks() {
  clock_t t = clock();

  int count = 100000;
  for (size_t i = 0; i < count; i++)
    printf("%ld\n", i);

  t = clock() - t;
  printf("No. of clicks %ld clicks (%f seconds).\n", t, ((float)t) / CLOCKS_PER_SEC);
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

void formatTime(struct tm *time) {
  char buffer[20];
  strftime(buffer, 20, "%I:%M:%S %p.", time);
  printf("Time is %s\n", buffer);
}

/*
Specifier 	Replaced By 	Example
%a 	Abbreviated weekday name 	Sun
%A 	Full weekday name 	Sunday
%b 	Abbreviated month name 	Mar
%B 	Full month name 	March
%c 	Date and time representation 	Sun Aug 19 02:56:02 2012
%d 	Day of the month (01-31) 	19
%H 	Hour in 24h format (00-23) 	14
%I 	Hour in 12h format (01-12) 	05
%j 	Day of the year (001-366) 	231
%m 	Month as a decimal number (01-12) 	08
%M 	Minute (00-59) 	55
%p 	AM or PM designation 	PM
%S 	Second (00-61) 	02
%U 	Week number with the first Sunday as the first day of week one (00-53) 33
%w 	Weekday as a decimal number with Sunday as 0 (0-6) 	4
%W 	Week number with the first Monday as the first day of week one (00-53) 	34
%x 	Date representation 	08/19/12
%X 	Time representation 	02:50:06
%y 	Year, last two digits (00-99) 	01
%Y 	Year 	2012
%Z 	Timezone name or abbreviation 	CDT
%% 	A % sign 	%
*/
