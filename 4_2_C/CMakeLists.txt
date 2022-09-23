cmake_minimum_required(VERSION 3.1)

project(4_2_C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c11 -Wall -Wextra")

add_executable(4_2_C main.c)
