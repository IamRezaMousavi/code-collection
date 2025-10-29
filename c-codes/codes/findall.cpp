#include <iostream>
#include <regex>
#include <string>
#include <vector>

std::vector<std::string> findall(const std::string &pattern, const std::string &text) {
  std::regex re(pattern);
  std::sregex_iterator begin(text.begin(), text.end(), re);
  std::sregex_iterator end;
  std::vector<std::string> results;

  for (auto it = begin; it != end; ++it)
    results.push_back(it->str());

  return results;
}

template <typename T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &vec) {
  os << "[";
  for (size_t i = 0; i < vec.size(); i++) {
    os << vec[i];
    if (i + 1 < vec.size())
      os << ", ";
  }
  os << "]";
  return os;
}

int main(int argc, const char *argv[]) {
  std::string words = "The rain in Spain 123456 Kilo";
  auto matches = findall("[a-m]", words);
  std::cout << matches << std::endl;

  matches = findall("in", words);
  std::cout << matches << std::endl;

  matches = findall("\\d", words);
  std::cout << matches << std::endl;

  return 0;
}
