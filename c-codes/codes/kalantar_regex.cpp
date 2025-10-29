/*
 * https://quera.org/problemset/275794
 */

#include <iostream>
#include <regex>
#include <string>
#include <utility>
#include <vector>

std::regex kalan_pattern("kalantar");
std::regex kalan_space_pattern("kalan\\s+tar");
std::regex kalan_space_all("(kalantar|kalan\\s+tar)");

std::pair<int, int> count_words(const std::string &line) {
  std::sregex_iterator begin(line.begin(), line.end(), kalan_pattern);
  std::sregex_iterator end;
  int count = std::distance(begin, end);

  std::sregex_iterator begin_space(line.begin(), line.end(), kalan_space_pattern);
  std::sregex_iterator end_space;
  int count_space = std::distance(begin_space, end_space);

  return std::make_pair(count, count_space);
}

int main(int argc, const char *argv[]) {
  std::string line;
  std::getline(std::cin, line);

  std::vector<std::pair<int, int>> level_count;
  while (true) {
    auto count = count_words(line);
    if (count.first <= 0 && count.second <= 0)
      break;
    level_count.push_back(count);
    line = std::regex_replace(line, kalan_space_all, "");
  }

  std::cout << level_count.size() << '\n';
  for (auto &count : level_count) {
    std::cout << count.first << ' ' << count.second << '\n';
  }

  return 0;
}
