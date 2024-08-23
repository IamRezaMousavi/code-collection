/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-03-06 23:10:19
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-03-06 23:17:38
 */

#ifndef __MEMORY_H__
#define __MEMORY_H__

class MyString {
  char *ptrString;
  int length;

public:
  MyString(const char *string = "");
  MyString(MyString &other);
  ~MyString();

  MyString &operator=(const MyString &other);

  char *getString();
  int getLength();
};

#endif /* __MEMORY_H__ */
