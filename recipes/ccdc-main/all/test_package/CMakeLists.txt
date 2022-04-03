cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

find_package(approvaltests.cpp REQUIRED)
find_package(ccdcboost REQUIRED)
find_package(cppad REQUIRED)
find_package(cryptopp REQUIRED)
find_package(EXPAT REQUIRED)
find_package(fasta REQUIRED)
find_package(GTest REQUIRED)
find_package(OpenSSL REQUIRED)
find_package(CURL REQUIRED)
find_package(gsoap REQUIRED)
find_package(httplib REQUIRED)

find_package(mariadb-connector-c REQUIRED)
find_package(LexActivator REQUIRED)
find_package(LexFloatClient REQUIRED)

find_package(ZLIB REQUIRED)
find_package(zstd REQUIRED)
find_package(LibArchive REQUIRED)

find_package(Protobuf REQUIRED)

find_package(Inchi REQUIRED)
find_package(libxl REQUIRED)
find_package(LibXml2 REQUIRED)

find_package(range-v3 REQUIRED)
find_package(RapidJSON REQUIRED)
find_package(rstatistics REQUIRED)
find_package(SQLite3 REQUIRED)

# find_package(OpenSceneGraph REQUIRED)
find_package(OpenSceneGraph CONFIG REQUIRED)
find_package(Qt5 COMPONENTS Core Concurrent Widgets Network Xml OpenGL PrintSupport Test Sql Svg WebEngine WebEngineCore WebEngineWidgets XmlPatterns REQUIRED)
find_package(qwt REQUIRED)

add_executable(example WIN32 example.cpp)

target_link_libraries(example
    approvaltests.cpp::approvaltests.cpp
    BZip2::BZip2
    ccdcboost::ccdcboost
    cppad::cppad
    cryptopp-static
    CURL::libcurl
    EXPAT::EXPAT
    freetype
    gsoap::gsoap
    GTest::gtest
    httplib::httplib
    Inchi::Inchi
    jbig::jbig
    JPEG::JPEG
    LexActivator::LexActivator
    LexFloatClient::LexFloatClient
    LibArchive::LibArchive
    LibLZMA::LibLZMA
    libxl::libxl
    LibXml2::LibXml2
    mariadb-connector-c::mariadb-connector-c
    OPENSCENEGRAPH::OPENSCENEGRAPH
    openssl::openssl
    PNG::PNG
    protobuf::libprotobuf
    Qt5::Concurrent
    Qt5::Core
    Qt5::Network
    Qt5::OpenGL
    Qt5::PrintSupport
    Qt5::QSQLiteDriverPlugin
    Qt5::Sql
    Qt5::Svg
    Qt5::Test
    Qt5::WebEngine
    Qt5::WebEngineCore
    Qt5::WebEngineWidgets
    Qt5::Widgets
    Qt5::Xml
    Qt5::XmlPatterns # deprecated in Qt6
    qwt::qwt
    range-v3::range-v3
    rapidjson::rapidjson
    SQLite::SQLite3
    TIFF::TIFF
    libwebp::libwebp
    ZLIB::ZLIB
    zstd::libzstd_shared
)
if(WIN32)
    target_link_libraries(example Qt5::AXServer)
else()
    target_link_libraries(example Fontconfig::Fontconfig)
    if(APPLE)
    else()
    endif()
endif()
set_target_properties(example PROPERTIES CXX_STANDARD 17)


