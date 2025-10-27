/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-03-15 03:11:49
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-10-28 01:30:32
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void checkFile(const char *fileName);
size_t getFileSize(const char *fileName);

int main(int argc, const char *argv[]) {
  if (argc != 2) {
    printf("\n\nUsage Error: key <FileName>");
    exit(1);
  }

  checkFile(argv[1]);
  size_t size = getFileSize(argv[1]);
  printf("File Size: %.2f kB\n", (float)size / 1024);
  // printf("File Size: %ld B\n", size);

  FILE *file;
  file = fopen(argv[1], "rb");

  char *data = (char *)malloc(size);
  size_t index = 0;
  while (!feof(file))
    data[index++] = fgetc(file);
  fclose(file);

  file = fopen(argv[1], "wb");

  for (size_t i = 0; i < index - 1; i++)
    fputc((data[i] ^ 0x60), file);
  fclose(file);
  free(data);

  printf("\n\t***** DONE SUCCESSFULLY *****\n");
  return 0;
}

void checkFile(const char *fileName) {
  FILE *filePtr = fopen(fileName, "r");

  // checking if the file exist or not
  if (filePtr == NULL) {
    printf("\nFile Error: File Not Found!\n");
    exit(1);
  }

  fclose(filePtr);
}

size_t getFileSize(const char *fileName) {
  // opening the file in read mode
  FILE *fp = fopen(fileName, "rb");

  fseek(fp, 0L, SEEK_END);

  // calculating the size of the file
  long size = ftell(fp);

  // closing the file
  fclose(fp);

  return (size < 0) ? 0 : (size_t)size;
}
