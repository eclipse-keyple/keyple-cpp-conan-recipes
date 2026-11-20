#include <iostream>

#include "keyple/card/calypso/CalypsoExtensionService.hpp"

int
main()
{
    /* Calls into the actual compiled library (not just a header), proving
     * the binary resolved and linked correctly through Conan/CMake. */
    const auto service = keyple::card::calypso::CalypsoExtensionService::getInstance();

    std::cout << "Keyple::Card::Calypso package resolved and linked correctly ("
              << (service != nullptr ? "service obtained" : "service unavailable") << ")" << std::endl;
    return service != nullptr ? 0 : 1;
}
