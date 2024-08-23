#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

void handler_signal(int signo) {
  printf("signal no: %d\n", signo);
  printf("EXITING...\n");
  exit(EXIT_SUCCESS);
}

int main() {
  // ctrl + c
  if (signal(SIGINT, handler_signal)) {
	printf("Error while settings a signal handler\n");
	return EXIT_FAILURE;
  }
  // kill -15 [pid]
  signal(SIGTERM, handler_signal);

  while (1) {
	/* code */
  }

  return 0;
}
