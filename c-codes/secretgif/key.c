/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-03-15 03:11:49
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-03-15 05:10:18
 */
#include <stdio.h>
#include <stdlib.h>

void checkFile(const char *fileName);
long int getFileSize(const char *fileName);

int main(int argc, const char *argv[]) {
  if (argc != 2) {
    printf("\n\nUsage Error: key [FileName.Extension]");
    exit(1);
  }

  checkFile(argv[1]);
  long int size = getFileSize(argv[1]);
  printf("File Size: %.2f kB\n", (float)size / 1024);
  // printf("File Size: %ld B\n", size);

  FILE *file;
  file = fopen(argv[1], "rb");

  char *data = (char *)malloc(size);
  long int index = 0;
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

long int getFileSize(const char *fileName) {
  // opening the file in read mode
  FILE *fp = fopen(fileName, "r");

  fseek(fp, 0L, SEEK_END);

  // calculating the size of the file
  long int res = ftell(fp);

  // closing the file
  fclose(fp);

  return res;
}
