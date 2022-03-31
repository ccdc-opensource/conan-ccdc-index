cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(ApprovalTests REQUIRED)
find_package(ccdcboost REQUIRED)
find_package(cppad REQUIRED)
find_package(cryptopp REQUIRED)
find_package(CURL REQUIRED)
find_package(EXPAT REQUIRED)
find_package(fasta REQUIRED)
find_package(gsoap REQUIRED)
find_package(GTest REQUIRED)
find_package(httplib REQUIRED)
find_package(Inchi REQUIRED)
find_package(LexActivator REQUIRED)
find_package(LexFloatClient REQUIRED)
find_package(LibArchive REQUIRED)
find_package(libxl REQUIRED)
find_package(LibXml2 REQUIRED)
find_package(mariadb-connector-c REQUIRED)
find_package(OpenSceneGraph REQUIRED)
find_package(OpenSSL REQUIRED)
find_package(Protobuf REQUIRED)
find_package(Qt5 COMPONENTS Core Concurrent Widgets Network Xml OpenGL PrintSupport Test Sql Svg WebEngine WebEngineCore WebEngineWidgets XmlPatterns REQUIRED)
find_package(qwt REQUIRED)
find_package(range-v3 REQUIRED)
find_package(RapidJSON REQUIRED)
find_package(rstatistics REQUIRED)
find_package(SQLite3 REQUIRED)
find_package(ZLIB REQUIRED)
find_package(zstd REQUIRED)

add_executable(example WIN32 example.cpp)

target_link_libraries(example
    ccdcboost::ccdcboost
    cppad::cppad
    cryptopp::cryptopp
#    csdprotobufs::csdprotobufs
    gsoap::gsoap
    Inchi::Inchi
    LexActivator::LexActivator
    LexFloatClient::LexFloatClient
    libxl::libxl
    mariadb-connector-c::mariadb-connector-c
    OPENSCENEGRAPH::OPENSCENEGRAPH
    protobuf::libprotobuf
    range-v3::range-v3
    RapidJSON::RapidJSON
    SQLite::SQLite3
    Qt5::Core Qt5::Concurrent Qt5::Widgets Qt5::Network Qt5::Xml Qt5::OpenGL Qt5::PrintSupport Qt5::Test Qt5::Sql Qt5::Svg Qt5::WebEngine Qt5::WebEngineCore Qt5::WebEngineWidgets
    # deprecated in Qt6
    Qt5::XmlPatterns
)
set_target_properties(example PROPERTIES CXX_STANDARD 17)
