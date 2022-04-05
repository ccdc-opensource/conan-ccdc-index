cmake_minimum_required(VERSION 3.1.2)
project(test_package)

find_package(OpenSceneGraph CONFIG REQUIRED)

if (CONAN_USER_OPENSCENEGRAPH_openscenegraph_freetype_plugin_source)
	set(freetype_plugin_source "${CONAN_USER_OPENSCENEGRAPH_openscenegraph_freetype_plugin_source}")
	message(INFO "A ${freetype_plugin_source}")
elseif(openscenegraph_PACKAGE_FOLDER_RELEASE)
	set(freetype_plugin_source "${openscenegraph_PACKAGE_FOLDER_RELEASE}/freetype-plugin-source")
	message(INFO "B ${freetype_plugin_source}")
elseif(openscenegraph_PACKAGE_FOLDER_DEBUG)
	set(freetype_plugin_source "${openscenegraph_PACKAGE_FOLDER_DEBUG}/freetype-plugin-source")
	message(INFO "C ${freetype_plugin_source}")
endif()

get_property(cache_variables DIRECTORY PROPERTY CACHE_VARIABLES)
foreach(cache_variable ${cache_variables})
	if("${cache_variable}" MATCHES "^OSG_HAS_(WITH_.+)$")
		add_compile_definitions("${CMAKE_MATCH_1}=${${cache_variable}}")
	endif()
endforeach()

add_executable(${PROJECT_NAME}
    test_package.cpp
    ${freetype_plugin_source}/FreeTypeFont.cpp
    ${freetype_plugin_source}/FreeTypeFont.h
    ${freetype_plugin_source}/FreeTypeLibrary.cpp
    ${freetype_plugin_source}/FreeTypeLibrary.h
)

target_include_directories(${PROJECT_NAME} PRIVATE ${freetype_plugin_source})
target_link_libraries(${PROJECT_NAME} OPENSCENEGRAPH::OPENSCENEGRAPH)
