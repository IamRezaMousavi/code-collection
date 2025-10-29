/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-07-23 00:33:53
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2021-12-13 12:43:03
 */
#include <conio.h>
#include <stdio.h>

typedef enum bool {
  FALSE = 0,
  TRUE = 1
} bool;

typedef enum months {
  FAR = 1,
  ORD,
  KHR,
  TIR,
  MOR,
  SHR,
  MHR,
  ABN,
  AZR,
  DAY,
  BAH,
  ESF
} Month;

int main(int argc, const char *argv[]) {
  char *Month_name[] = {"",     "Farvardin", "Ordibehesht", "Khordad", "Tir",    "Mordad", "Shahrivar",
                        "Mehr", "Aban",      "Azar",        "Day",     "Bahman", "Esfand"};

  for (Month m = FAR; m <= ESF; m++)
    printf("%3d %s\n", m, Month_name[m]);

  getch();
  return 0;
}
