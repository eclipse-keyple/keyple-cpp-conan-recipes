#include <iostream>

#include "keyple/core/plugin/PluginApiProperties.hpp"
#include "keyple/core/plugin/PluginIOException.hpp"

int
main()
{
    /* PluginIOException.hpp transitively pulls in keyple-util-cpp-lib's
     * Exception.hpp; compiling and throwing/catching it here proves the
     * transitive dependency resolves through Conan/CMake alone. */
    try {
        throw keyple::core::plugin::PluginIOException("test");
    } catch (const keyple::core::plugin::PluginIOException& e) {
        std::cout << "Keyple::Plugin header-only package resolved and linked correctly (API version "
                  << keyple::core::plugin::PluginApiProperties_VERSION << ", caught: " << e.getMessage() << ")"
                  << std::endl;
    }
    return 0;
}
