#include "boost/shared_ptr.hpp"
#include <iostream>

int main() {
    try
    {
        boost::shared_ptr<int> empty;
        (void)*empty;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << "\nException thrown correctly\n";
        return 0;
    }
    std::cerr << "No exception when dereferencing null boost::shared_ptr\n";
    return 1;
}
