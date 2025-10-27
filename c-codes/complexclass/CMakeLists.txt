cmake_minimum_required(VERSION 3.10)
project(ComplexLibrary)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories(include)

add_library(ComplexLib src/Complex.cpp)

add_executable(ComplexTest test/test.cpp)
target_link_libraries(ComplexTest ComplexLib)
