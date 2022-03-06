#include <iostream>

#if !defined(_WIN32)
#include <fontconfig/fontconfig.h>
#endif

#include <boost/shared_ptr.hpp>
#include <sqlite3.h>
/*
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
*/
int main() {
#if !defined(_WIN32)
	FcConfig* config = FcInitLoadConfigAndFonts();
#endif

	std::cout << "The death star is complete!" << std::endl;
    return EXIT_SUCCESS;
}
