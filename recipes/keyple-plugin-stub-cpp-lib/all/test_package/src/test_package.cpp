#include <iostream>

#include "keyple/plugin/stub/StubPluginFactory.hpp"
#include "keyple/plugin/stub/StubPluginFactoryBuilder.hpp"

int
main()
{
    /* Calls into the actual compiled library (not just a header), proving
     * the binary resolved and linked correctly through Conan/CMake. */
    const std::shared_ptr<keyple::plugin::stub::StubPluginFactory> factory
        = keyple::plugin::stub::StubPluginFactoryBuilder::builder()->build();

    std::cout << "Keyple::Plugin::Stub package resolved and linked correctly ("
              << (factory != nullptr ? "factory built" : "factory build failed") << ")" << std::endl;
    return factory != nullptr ? 0 : 1;
}
