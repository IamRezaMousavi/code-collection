#include <iostream>
#include <vector>

#include "Person.hpp"
#include "PersonDb.hpp"

int main(int argc, const char *argv[]) {
  PersonDb db("person.db");
  std::vector<Person> personArr = db.getPersons();
  std::cout << "Persons " << std::endl;
  for (auto p : personArr)
    std::cout << p.id << ": " << p.name << std::endl;

  Person persons[] = {
      Person("reza"),
      Person("ali"),
      Person("mehdi"),
      Person("ahmad"),
  };

  int personsSize = sizeof(persons) / sizeof(persons[0]);
  for (int i = 0; i < personsSize; i++) {
    persons[i].id = db.insert(persons[i]);
    std::cout << persons[i].id << ": " << persons[i].name << std::endl;
  }

  persons[2].name = "mohammad";
  db.update(persons[2]);
  std::cout << persons[2].id << ": " << persons[2].name << " updated!"
            << std::endl;

  db.del(persons[0].id);
  std::cout << persons[0].id << " deleted!" << std::endl;

  personArr = db.getPersons();
  std::cout << "Persons: " << std::endl;
  for (auto p : personArr)
    std::cout << p.id << ": " << p.name << std::endl;

  return 0;
}
