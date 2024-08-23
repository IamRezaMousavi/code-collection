/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-03-06 23:15:51
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-03-07 00:18:29
 */

#include "memory.h"
#include <string.h>

MyString::MyString(const char *string) {
  length = strlen(string);

  ptrString = new char[length + 1];
  strncpy(ptrString, string, length);
  ptrString[length] = '\0';
}

MyString::MyString(MyString &other) {
  length = other.length;
  if (other.ptrString) {
	ptrString = new char[length];
	strncpy(ptrString, other.ptrString, length);
  } else {
	ptrString = 0;
  }
}

MyString::~MyString() {
  if (ptrString) delete[] ptrString;
  ptrString = 0;
}

MyString &MyString::operator=(const MyString &other) {
  if (this == &other) return *this;
  if (ptrString) delete[] ptrString;

  length = other.length;

  if (other.length) {
	ptrString = new char[length + 1];
	strcpy(ptrString, other.ptrString);
  } else {
	ptrString = 0;
  }

  return *this;
}

char *MyString::getString() {
  return ptrString;
}

int MyString::getLength() {
  return length;
}
