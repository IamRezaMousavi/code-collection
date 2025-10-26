#include <mysql/mysql.h>

#include <iostream>
#include <string>
#include <vector>

struct User {
  int id;
  std::string name;
  std::string birthday;
  double salary;
};

class Database {
 private:
  MYSQL *conn;

  bool createTable() {
    const char *query =
        "CREATE TABLE IF NOT EXISTS users ("
        "   id INT AUTO_INCREMENT PRIMARY KEY,"
        "   name VARCHAR(50),"
        "   birthday DATE,"
        "   salary DOUBLE"
        ")";
    if (mysql_query(conn, query)) {
      std::cerr << "Error creating table: " << mysql_error(conn) << std::endl;
      return false;
    }
    return true;
  }

 public:
  Database(const std::string &host, const std::string &user,
           const std::string &password, const std::string &dbname,
           unsigned int port = 3306) {
    conn = mysql_init(nullptr);
    if (!conn) {
      std::cerr << "Unable to initialize connection struct\n";
      exit(EXIT_FAILURE);
    }

    if (!mysql_real_connect(conn, host.c_str(), user.c_str(), password.c_str(),
                            dbname.c_str(), port, nullptr, 0)) {
      std::cerr << "Database connection failed: " << mysql_error(conn)
                << std::endl;
      mysql_close(conn);
      exit(EXIT_FAILURE);
    }

    this->createTable();
  }

  ~Database() { mysql_close(conn); }

  std::vector<User> selectUsers() {
    std::vector<User> users;

    const char *query = "SELECT id, name, birthday, salary FROM users";
    if (mysql_query(conn, query)) {
      std::cerr << "Error while selecting data: " << mysql_error(conn)
                << std::endl;
      return users;
    }

    MYSQL_RES *res = mysql_store_result(conn);
    if (!res) {
      std::cerr << "Error getting users result: " << mysql_error(conn)
                << std::endl;
      return users;
    }

    MYSQL_ROW row;
    while ((row = mysql_fetch_row(res))) {
      User user = {.id = row[0] ? std::stoi(row[0]) : 0,
                   .name = row[1] ? row[1] : "",
                   .birthday = row[2] ? row[2] : "",
                   .salary = row[3] ? std::stod(row[3]) : 0.0};
      users.push_back(user);
    }

    mysql_free_result(res);
    return users;
  }

  bool insertUser(const std::string &name) {
    std::string query = "INSERT INTO users (name) VALUES ('" + name + "')";
    if (mysql_query(conn, query.c_str())) {
      std::cerr << "Insert failed: " << mysql_error(conn) << std::endl;
      return false;
    }
    std::cout << "New row inserted successfully\n";
    return true;
  }

  bool deleteUsers() {
    if (mysql_query(conn, "DELETE FROM users")) {
      std::cerr << "Delete failed: " << mysql_error(conn) << std::endl;
      return false;
    }
    if (mysql_query(conn, "ALTER TABLE users AUTO_INCREMENT = 1")) {
      std::cerr << "Reset id after deleteing users failed: " << mysql_error(conn) << std::endl;
      return false;
    }
    std::cout << "users data deleted successfully\n";
    return true;
  }
};

int main() {
  Database db("localhost", "reza", "r", "reza");
  auto users = db.selectUsers();
  db.insertUser("Reza");
  return 0;
}
