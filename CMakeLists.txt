cmake_minimum_required(VERSION 3.18)

project(Hello LANGUAGES CXX)

add_executable(helloworld)

target_sources(helloworld
   PRIVATE
      src/hello.cpp
)
