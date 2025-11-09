#include <sys/types.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#ifdef _WIN32
#include <winsock2.h>
#else
#include <arpa/inet.h>
#include <sys/socket.h>
#endif

#define PORT 8080

int main(void) {
#ifdef _WIN32
  WSADATA wsaData;
  if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
    fprintf(stderr, "WSAStartup failed\n");
    exit(EXIT_FAILURE);
  }
#endif

  int server_socket = socket(AF_INET, SOCK_STREAM, 0);

  char opt = 1;
  setsockopt(server_socket, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

  struct sockaddr_in address;
  address.sin_family = AF_INET;
  address.sin_port = htons(PORT);
  address.sin_addr.s_addr = INADDR_ANY;

  if (bind(server_socket, (struct sockaddr *)&address, sizeof(address)) < 0) {
    perror("Bind failed");
    exit(EXIT_FAILURE);
  }

  listen(server_socket, 4);
  printf("Listening on %d...\n", PORT);

  int client_socket = accept(server_socket, NULL, NULL);

  char message[] = "Hello, World!\n";
  send(client_socket, message, strlen(message), 0);

  char buffer[2048];
  recv(client_socket, buffer, 2048, 0);

  printf("%s", buffer);

  close(client_socket);
  close(server_socket);

#ifdef _WIN32
  WSACleanup();
#endif

  return EXIT_SUCCESS;
}
