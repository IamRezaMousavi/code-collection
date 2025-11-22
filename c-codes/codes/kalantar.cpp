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

  std::string newline;
  newline.reserve(line.size());

  while (true) {
    newline.clear();

    int kalan_count = 0;
    int kalan_space_count = 0;

    size_t i = 0;
    while (i < line.size()) {
      if (line[i] == 'k' && line.compare(i, 5, "kalan") == 0) {
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

      size_t next_k = line.find('k', i + 1);
      if (next_k == std::string::npos) {
        next_k = line.size();
      }
      newline.append(line, i, next_k - i);
      i = next_k;
    }

    if (kalan_count == 0 && kalan_space_count == 0)
      break;

    level_count.push_back({kalan_count, kalan_space_count});
    line.swap(newline);
  }

  std::cout << level_count.size() << '\n';
  for (auto &count : level_count) {
    std::cout << count.first << ' ' << count.second << '\n';
  }

  return 0;
}
