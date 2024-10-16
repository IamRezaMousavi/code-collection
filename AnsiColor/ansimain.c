#include "ansi_color.h"
#include <stdio.h>

int main(void) {
  setupConsole();
  puts("Hello my friend");
  puts(RED_TEXT "DANGER TEXT" RESET_COLOR);
  puts("HAHAHAHA");
  restoreConsole();
}
