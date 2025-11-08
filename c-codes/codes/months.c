/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-07-23 00:33:53
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-08 10:28:59
 */
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
  // clang-format off
  char *Month_name[] = {"",
    "Farvardin", "Ordibehesht", "Khordad",
    "Tir",       "Mordad",      "Shahrivar",
    "Mehr",      "Aban",        "Azar",
    "Day",       "Bahman",      "Esfand"
  };
  // clang-format on

  for (Month m = FAR; m <= ESF; m++)
    printf("%3d %s\n", m, Month_name[m]);

  getc(stdin);
  return 0;
}
