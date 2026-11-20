#include <iostream>

#include "keyple/card/generic/GenericExtensionService.hpp"

int
main()
{
    /* Calls into the actual compiled library (not just a header), proving
     * the binary resolved and linked correctly through Conan/CMake. */
    const auto service = keyple::card::generic::GenericExtensionService::getInstance();

    std::cout << "Keyple::Card::Generic package resolved and linked correctly ("
              << (service != nullptr ? "service obtained" : "service unavailable") << ")" << std::endl;
    return service != nullptr ? 0 : 1;
}
