cmake_minimum_required(VERSION 3.10)
project(complexlib)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories(include)

add_library(complex src/Complex.cpp)

add_executable(complextest test/test.cpp)
target_link_libraries(complextest complex)
