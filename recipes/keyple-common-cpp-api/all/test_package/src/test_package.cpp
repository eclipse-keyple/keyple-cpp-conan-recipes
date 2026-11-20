#include <iostream>

#include "keyple/core/common/CommonApiProperties.hpp"

int
main()
{
    std::cout << "Keyple::Common header-only package resolved and linked correctly (API version "
              << keyple::core::common::CommonApiProperties_VERSION << ")" << std::endl;
    return 0;
}
