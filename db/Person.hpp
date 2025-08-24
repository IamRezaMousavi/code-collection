#ifndef __PERSON_H__
#define __PERSON_H__

#include <string>

class Person {

private:
public:
  Person(std::string name);

  int         id;
  std::string name;
};

#endif /* __PERSON_H__ */
