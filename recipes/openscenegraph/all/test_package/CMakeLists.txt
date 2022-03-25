cmake_minimum_required(VERSION 3.1.2)
project(test_package)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${PROJECT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(OpenSceneGraph REQUIRED)

get_property(cache_variables DIRECTORY PROPERTY CACHE_VARIABLES)
foreach(cache_variable ${cache_variables})
	if("${cache_variable}" MATCHES "^OSG_HAS_(WITH_.+)$")
		add_compile_definitions("${CMAKE_MATCH_1}=${${cache_variable}}")
	endif()
endforeach()

add_executable(${PROJECT_NAME}
    test_package.cpp
    ${CONAN_USER_OPENSCENEGRAPH_openscenegraph_freetype_plugin_source}/FreeTypeFont.cpp
    ${CONAN_USER_OPENSCENEGRAPH_openscenegraph_freetype_plugin_source}/FreeTypeFont.h
    ${CONAN_USER_OPENSCENEGRAPH_openscenegraph_freetype_plugin_source}/FreeTypeLibrary.cpp
    ${CONAN_USER_OPENSCENEGRAPH_openscenegraph_freetype_plugin_source}/FreeTypeLibrary.h
)

target_include_directories(${PROJECT_NAME}
    PRIVATE ${CONAN_USER_OPENSCENEGRAPH_openscenegraph_freetype_plugin_source})
target_link_libraries(${PROJECT_NAME} OPENSCENEGRAPH::OPENSCENEGRAPH)
