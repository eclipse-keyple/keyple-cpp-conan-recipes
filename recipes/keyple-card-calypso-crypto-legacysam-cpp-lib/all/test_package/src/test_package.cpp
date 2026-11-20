#include <iostream>

#include "keyple/card/calypso/crypto/legacysam/LegacySamExtensionService.hpp"

int
main()
{
    /* Calls into the actual compiled library (not just a header), proving
     * the binary resolved and linked correctly through Conan/CMake. */
    const auto service = keyple::card::calypso::crypto::legacysam::LegacySamExtensionService::getInstance();

    std::cout << "Keyple::Card::Calypso::Crypto::LegacySam package resolved and linked correctly ("
              << (service != nullptr ? "service obtained" : "service unavailable") << ")" << std::endl;
    return service != nullptr ? 0 : 1;
}
