cmake_minimum_required(VERSION 3.5)
project(PackageTest CXX)

find_package(qwt REQUIRED)

add_executable(example example.cpp)
# Must compile with "-fPIC" since Qt was built with -reduce-relocations.
target_compile_options(example PRIVATE -fPIC)
target_link_libraries(example qwt::qwt)
set_property(TARGET example PROPERTY CXX_STANDARD 11)

