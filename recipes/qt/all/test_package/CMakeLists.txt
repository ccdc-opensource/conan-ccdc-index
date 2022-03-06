cmake_minimum_required(VERSION 3.3.0)

set(CMAKE_CXX_STANDARD 11)

project(test_package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_set_vs_runtime()
conan_set_libcxx()
conan_output_dirs_setup()

find_package(Qt5 COMPONENTS Core Concurrent Widgets Network Xml OpenGL PrintSupport Test Sql Svg WebEngine WebEngineCore WebEngineWidgets XmlPatterns REQUIRED CONFIG)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(SOURCES test_package.cpp greeter.h example.qrc all-qt-includes-used-in-main.cpp)

add_executable(${PROJECT_NAME} WIN32 ${SOURCES})
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 17)


target_link_libraries(${PROJECT_NAME} Qt5::Core Qt5::Concurrent Qt5::Widgets Qt5::Network Qt5::Xml Qt5::OpenGL Qt5::PrintSupport Qt5::Test Qt5::Sql Qt5::Svg Qt5::WebEngine Qt5::WebEngineCore Qt5::WebEngineWidgets)

# deprecated in Qt6
target_link_libraries(${PROJECT_NAME} Qt5::XmlPatterns)
