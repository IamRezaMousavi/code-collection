/*
 * https://quera.org/problemset/275794
 */

#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main(int argc, const char *argv[]) {
  std::string line;
  std::getline(std::cin, line);

  std::vector<std::pair<int, int>> level_count;
  level_count.reserve(line.size() / 5);
  while (true) {
    int kalan_count = 0;
    int kalan_space_count = 0;

    size_t i = 0;
    size_t write = 0;
    while (i < line.size()) {
      if (line[i] == 'k') {
        if (line.compare(i, 5, "kalan") == 0) {
          size_t j = i + 5;
          if (line[j] == ' ') {
            while (j < line.size() && line[j] == ' ')
              j++;

            if (line.compare(j, 3, "tar") == 0) {
              kalan_space_count++;
              i = j + 3;
              continue;
            }

          } else if (line.compare(j, 3, "tar") == 0) {
            kalan_count++;
            i += 8;
            continue;
          }
        }
      }

      line[write++] = line[i++];
    }
    if (kalan_count == 0 && kalan_space_count == 0)
      break;
    line.resize(write);
    level_count.emplace_back(kalan_count, kalan_space_count);
  }

  std::cout << level_count.size() << '\n';
  for (auto &count : level_count) {
    std::cout << count.first << ' ' << count.second << '\n';
  }

  return 0;
}
