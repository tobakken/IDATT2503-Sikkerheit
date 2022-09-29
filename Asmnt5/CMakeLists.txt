cmake_minimum_required(VERSION 3.1)

project(Asmnt5)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11 -Wall -Wextra")

add_library(utility INTERFACE)
target_include_directories(utility INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(Asmnt5 main.c)
target_link_libraries(Asmnt5 utility)

enable_testing()
add_subdirectory(tests)
