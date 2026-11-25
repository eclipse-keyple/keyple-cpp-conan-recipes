#include <iostream>

#include "keyple/core/service/resource/CardResourceServiceProvider.hpp"

int
main()
{
    /* Calls into the actual compiled library (not just a header), proving
     * the binary resolved and linked correctly through Conan/CMake. */
    const auto service = keyple::core::service::resource::CardResourceServiceProvider::getService();

    std::cout << "Keyple::Service::Resource package resolved and linked correctly ("
              << (service != nullptr ? "service obtained" : "service unavailable") << ")" << std::endl;
    return service != nullptr ? 0 : 1;
}
