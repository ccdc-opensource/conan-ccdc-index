cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(ccdcboost REQUIRED)
find_package(cppad REQUIRED)
find_package(cryptopp REQUIRED)
find_package(csdprotobufs REQUIRED)
find_package(gsoap REQUIRED)
find_package(Inchi REQUIRED)
find_package(LexActivator REQUIRED)
find_package(LexFloatClient REQUIRED)
find_package(libxl REQUIRED)
find_package(mariadb-connector-c REQUIRED)
find_package(openscenegraph REQUIRED)
find_package(range-v3 REQUIRED)
find_package(RapidJSON REQUIRED)
find_package(SQLite3 REQUIRED)

add_executable(example example.cpp)

target_link_libraries(example
    ccdcboost::ccdcboost
    cppad::cppad
    cryptopp::cryptopp
    csdprotobufs::csdprotobufs
    gsoap::gsoap
    Inchi::Inchi
    LexActivator::LexActivator
    LexFloatClient::LexFloatClient
    libxl::libxl
    mariadb-connector-c::mariadb-connector-c
    openscenegraph::openscenegraph
    range-v3::range-v3
    RapidJSON::RapidJSON
    SQLite3::SQLite3
)
set_target_properties(example PROPERTIES CXX_STANDARD 17)
