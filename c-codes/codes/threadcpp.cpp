/**
 * @Author: Reza Mousavi
 * @Date:   2025-08-25 03:50:05
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-10-28 01:32:26
 */
#include <atomic>
#include <chrono>
#include <iostream>
#include <thread>
#include <vector>

int main(int argc, char const *argv[]) {
  std::vector<std::thread> threads;

  for (int i = 0; i < 3; i++) {
    threads.emplace_back([i]() {
      for (int j = 0; j < 100; j++) {
        std::cout << "[" << std::this_thread::get_id() << "(" << i << ")"
                  << "]: " << j << std::endl;
      }
    });
  }

  std::atomic_bool running = true;
  std::thread t0([&running]() {
    while (running) {
      std::cout << "I'm Runnung..." << std::endl;
      std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
    std::cout << "T0 DONE!" << std::endl;
  });

  for (auto &t : threads) {
    t.join();
  }
  running = false;
  t0.join();

  return 0;
}
