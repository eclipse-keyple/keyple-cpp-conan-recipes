#include <iostream>

#include "keyple/plugin/pcsc/PcscPluginFactory.hpp"
#include "keyple/plugin/pcsc/PcscPluginFactoryBuilder.hpp"

int
main()
{
    /* Calls into the actual compiled library (not just a header), proving
     * the binary resolved and linked correctly through Conan/CMake -- this
     * only builds the factory config, it does not open a PC/SC session. */
    const std::shared_ptr<keyple::plugin::pcsc::PcscPluginFactory> factory
        = keyple::plugin::pcsc::PcscPluginFactoryBuilder::builder()->build();

    std::cout << "Keyple::Plugin::Pcsc package resolved and linked correctly ("
              << (factory != nullptr ? "factory built" : "factory build failed") << ")" << std::endl;
    return factory != nullptr ? 0 : 1;
}
