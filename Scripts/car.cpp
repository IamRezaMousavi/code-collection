/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-23 18:32:28
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-09-25 17:41:32
 */
#include <iostream>
using namespace std;

class Car {
public:
  int    year;
  string name;

  Car();
  Car(const int year, const string name);

  void display();
};

Car::Car() {
  this->year = 0;
  this->name = "";
}

Car::Car(const int year, const string name) {
  this->year = year;
  this->name = name;
}

void Car::display() {
  cout << "Name is " << name << endl;
  cout << "Year is " << year << endl;
}

int main(int argc, const char *argv[]) {
  cout << "Ya Allah" << endl;
  cout << "Hello C++" << endl;

  struct car {
    string name;
    int    year;
  } dodge;

  cout << "Please enter a NAME for your CAR:";
  cin >> dodge.name;

  cout << "Please enter YEAR for this car:";
  cin >> dodge.year;
  cout << endl;

  Car Dodge = Car(2021, "Dodge Challenger");
  cout << "My Car:" << endl;
  Dodge.display();

  cout << endl;
  if (dodge.year >= Dodge.year)
    cout << "Your Car is Better" << endl;
  else
    cout << "My car is BEST" << endl;

  return 0;
}
