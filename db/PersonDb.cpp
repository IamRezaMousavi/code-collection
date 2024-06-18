#include "PersonDb.hpp"

#include <string.h>

PersonDb::PersonDb(std::string filename) {
  ret = sqlite3_open(filename.c_str(), &DB);
  if (ret != SQLITE_OK) {
	std::cerr << "Error open DB" << sqlite3_errmsg(DB) << std::endl;
	throw -1;
  }

  std::string sql = "CREATE TABLE IF NOT EXISTS person("
					"id INTEGER PRIMARY KEY AUTOINCREMENT,"
					"name TEXT NOT NULL);";
  ret = sqlite3_exec(DB, sql.c_str(), NULL, 0, &errorMessage);
  if (ret != SQLITE_OK) {
	std::cerr << "Error open DB" << sqlite3_errmsg(DB) << std::endl;
	std::cout << errorMessage << std::endl;
	sqlite3_free(errorMessage);
	throw -1;
  }
}

PersonDb::~PersonDb() {
  sqlite3_close(DB);
}

static int callback(void *data, int argc, char **argv, char **azColName) {
  std::vector<Person> *persons = (std::vector<Person> *)data;
  Person person("");
  for (int i = 0; i < argc; i++)
	if (strcmp(azColName[i], "id") == 0)
	  person.id = atoi(argv[i]);
	else if (strcmp(azColName[i], "name") == 0)
	  person.name = argv[i];
  persons->push_back(person);
  return 0;
}

std::vector<Person> PersonDb::getPersons() {
  std::vector<Person> persons;
  std::string sql = "SELECT * FROM person;";
  ret = sqlite3_exec(DB, sql.c_str(), callback, &persons, &errorMessage);
  if (ret != SQLITE_OK) {
	std::cerr << "Error select from DB" << sqlite3_errmsg(DB) << std::endl;
	std::cout << errorMessage << std::endl;
	sqlite3_free(errorMessage);
	throw -1;
  }
  return persons;
}

int PersonDb::insert(Person person) {
  std::string sql
	  = "INSERT INTO person VALUES (NULL, \"" + person.name + "\");";
  ret = sqlite3_exec(DB, sql.c_str(), NULL, 0, &errorMessage);
  if (ret != SQLITE_OK) {
	std::cerr << "Error insert to DB" << sqlite3_errmsg(DB) << std::endl;
	std::cout << errorMessage << std::endl;
	sqlite3_free(errorMessage);
	throw -1;
  }
  return (int)sqlite3_last_insert_rowid(DB);
}

void PersonDb::update(Person person) {
  std::string sql = "UPDATE person SET name = \"" + person.name
                    + "\" WHERE id = " + std::to_string(person.id) + ";";
  ret = sqlite3_exec(DB, sql.c_str(), NULL, 0, &errorMessage);
  if (ret != SQLITE_OK) {
	std::cerr << "Error Update DB" << std::endl;
	std::cout << errorMessage << std::endl;
	sqlite3_free(errorMessage);
  }
}

void PersonDb::del(int personId) {
  std::string sql
	  = "DELETE FROM person WHERE id = " + std::to_string(personId) + ";";
  ret = sqlite3_exec(DB, sql.c_str(), NULL, 0, &errorMessage);
  if (ret != SQLITE_OK) {
	std::cerr << "Error Delete from DB" << std::endl;
	std::cout << errorMessage << std::endl;
	sqlite3_free(errorMessage);
  }
}
