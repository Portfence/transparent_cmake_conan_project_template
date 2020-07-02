cmake_minimum_required(VERSION 3.16.0 FATAL_ERROR)
project(CXXProjectConan CXX)

if (NOT CMAKE_BUILD_TYPE)
  message(STATUS "Setting build type to Release as none was specified")
  set(CMAKE_BUILD_TYPE "Release")
else ()
  message(STATUS "Build type is ${CMAKE_BUILD_TYPE}")
endif ()

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
  add_compile_options (-fdiagnostics-color=always)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
  add_compile_options (-fcolor-diagnostics)
endif ()

set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR} ${CMAKE_MODULE_PATH})
set(CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR} ${CMAKE_PREFIX_PATH})

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Boost CONFIG REQUIRED)
find_package(websocketpp CONFIG REQUIRED)
find_package(Threads MODULE REQUIRED)

add_subdirectory(src)
