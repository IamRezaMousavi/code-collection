/**
 * @Author: Reza Mousavi
 * @Date:   2025-08-25 01:52:52
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 21:18:13
 */
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

// The function to be executed by all threads
void *print_numbers(void *vargp) {
  pthread_t myid = pthread_self();

  for (int i = 0; i < 100; i++)
    printf("[%ld]: %d\n", myid, i);

  return NULL;
}

int main() {
  pthread_t thread_ids[4];

  for (int i = 0; i < 4; i++)
    pthread_create(&thread_ids[i], NULL, print_numbers, NULL);

  for (int i = 0; i < 4; i++)
    pthread_join(thread_ids[i], NULL);

  return 0;
}
