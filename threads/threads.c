#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

// The function to be executed by all threads
void *print_numbers(void *vargp) {
  // Store the value argument passed to this thread
  pthread_t myid = pthread_self();

  for (int i = 0; i < 100; i++)
	printf("[%ld]: %d\n", myid, i);

  return NULL;
}

int main() {
  pthread_t thread_ids[4];

  // Let us create three threads
  for (int i = 0; i < 4; i++)
	pthread_create(&thread_ids[i], NULL, print_numbers, NULL);

  for (int i = 0; i < 4; i++)
	pthread_join(thread_ids[i], NULL);

  return 0;
}
