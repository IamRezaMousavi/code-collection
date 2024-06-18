#ifndef __PERSON_DB_HPP__
#define __PERSON_DB_HPP__

#include <iostream>
#include <sqlite3.h>
#include <vector>

#include "Person.hpp"

class PersonDb {

private:
  sqlite3 *DB;
  int ret;
  char *errorMessage;

public:
  PersonDb(std::string filename);
  ~PersonDb();

  std::vector<Person> getPersons();
  int insert(Person person);
  void update(Person person);
  void del(int personId);
};

#endif /* __PERSON_DB_HPP__ */
