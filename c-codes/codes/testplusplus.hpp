#ifndef __TESTPLUSPLUS_HPP__
#define __TESTPLUSPLUS_HPP__

#include <exception>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

namespace testplusplus {

static constexpr const char *RESET = "\033[0m";

static constexpr const char *BOLD = "\033[1m";
static constexpr const char *UNDERLINE = "\033[4m";

static constexpr const char *BLACK = "\033[30m";
static constexpr const char *RED = "\033[31m";
static constexpr const char *GREEN = "\033[32m";
static constexpr const char *YELLOW = "\033[33m";
static constexpr const char *BLUE = "\033[34m";
static constexpr const char *MAGENTA = "\033[35m";
static constexpr const char *CYAN = "\033[36m";
static constexpr const char *WHITE = "\033[37m";

static constexpr const char *BRED = "\033[1;31m";
static constexpr const char *BGREEN = "\033[1;32m";
static constexpr const char *BYELLOW = "\033[1;33m";
static constexpr const char *BBLUE = "\033[1;34m";
static constexpr const char *BMAGENTA = "\033[1;35m";
static constexpr const char *BCYAN = "\033[1;36m";
static constexpr const char *BWHITE = "\033[1;37m";

struct Test {
  std::string name;
  std::function<void()> func;
};

// Safe static registry constructor using "Meyers Singleton"
inline std::vector<Test> &registry() {
  static std::vector<Test> tests;
  return tests;
}

inline void registerTest(const std::string &name, std::function<void()> func) {
  registry().push_back({name, func});
}

struct TestFailure : public std::exception {
  const char *what() const noexcept override { return "Test failed"; }
};

#define TEST(name)                                                                                                     \
  void name();                                                                                                         \
  struct name##_registrar {                                                                                            \
    name##_registrar() { ::testplusplus::registerTest(#name, name); }                                                  \
  } name##_registrar_instance;                                                                                         \
  void name()

#define ASSERT(expr)                                                                                                   \
  do {                                                                                                                 \
    if (!(expr)) {                                                                                                     \
      std::cerr << ::testplusplus::BRED << "[FAILED] " << ::testplusplus::RESET << ::testplusplus::BOLD                \
                << __FUNCTION__ << ::testplusplus::RESET << " at " << ::testplusplus::CYAN << __FILE__ << ":"          \
                << __LINE__ << ::testplusplus::RESET << "   (" << ::testplusplus::YELLOW << #expr                      \
                << ::testplusplus::RESET << ")\n";                                                                     \
      throw ::testplusplus::TestFailure();                                                                             \
    }                                                                                                                  \
  } while (0)

#define ASSERT_EQ(actual, expected)                                                                                    \
  do {                                                                                                                 \
    auto _act = (actual);                                                                                              \
    auto _exp = (expected);                                                                                            \
    if (!(_act == _exp)) {                                                                                             \
      std::cerr << ::testplusplus::BRED << "[FAILED] " << ::testplusplus::RESET << ::testplusplus::BOLD                \
                << __FUNCTION__ << ::testplusplus::RESET << " at " << ::testplusplus::CYAN << __FILE__ << ":"          \
                << __LINE__ << ::testplusplus::RESET << "\n"                                                           \
                << "  expected: " << ::testplusplus::YELLOW << _exp << ::testplusplus::RESET << "\n"                   \
                << "  actual:   " << ::testplusplus::YELLOW << _act << ::testplusplus::RESET << "\n";                  \
      throw ::testplusplus::TestFailure();                                                                             \
    }                                                                                                                  \
  } while (0)

inline int runAllTests() {
  std::cout << BCYAN << BOLD << "\n===== Running testplusplus tests =====\n\n" << RESET;

  int failedCount = 0;

  for (auto &test : registry()) {
    try {
      test.func();
      std::cout << BGREEN << "[PASS] " << RESET << BBLUE << test.name << RESET << "\n";
    } catch (const TestFailure &) {
      failedCount++;
    } catch (...) {
      std::cerr << BRED << "[EXCEPTION] " << RESET << BBLUE << test.name << RESET << "\n";
      failedCount++;
    }
  }

  std::cout << "\n" << BOLD << "===== Summary =====" << RESET << "\n";
  std::cout << BRED << "Failed: " << failedCount << RESET << "\n";
  std::cout << BGREEN << "Passed: " << (registry().size() - failedCount) << RESET << "\n";

  return failedCount;
}

} // namespace testplusplus

#endif // __TESTPLUSPLUS_HPP__
