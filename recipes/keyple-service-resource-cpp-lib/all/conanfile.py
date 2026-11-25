# *****************************************************************************
# Copyright (c) 2025 Calypso Networks Association https://calypsonet.org/     *
#                                                                             *
# This program and the accompanying materials are made available under the    *
# terms of the Eclipse Public License 2.0 which is available at               *
# http://www.eclipse.org/legal/epl-2.0                                        *
#                                                                             *
# SPDX-License-Identifier: EPL-2.0                                            *
# *****************************************************************************/

import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import apply_conandata_patches, copy, export_conandata_patches, get


class KeypleServiceResourceCppLibConan(ConanFile):
    name = "keyple-service-resource-cpp-lib"
    license = "EPL-2.0"
    author = "Calypso Networks Association <https://calypsonet.org/>"
    url = "https://github.com/eclipse-keyple/keyple-service-resource-cpp-lib"
    homepage = "https://keyple.org/apis/core-layer/service-resource-lib/"
    description = "C++ implementation of the Eclipse Keyple card resource service"
    topics = ("keyple", "calypso")

    package_type = "library"
    settings = "os", "arch", "compiler", "build_type"

    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }

    default_options = {
        "shared": True,
        "fPIC": True
    }

    def export_sources(self):
        export_conandata_patches(self)

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)
        apply_conandata_patches(self)

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("keyple-service-cpp-lib/3.4.1", transitive_headers=True)
        # keyple-service-cpp-lib is a shared library, so Conan does not
        # propagate its own dependencies' libs transitively by default (its
        # consumers are only expected to need the shared lib itself). This
        # package's own sources call directly into keyple-util symbols
        # (Logger, Pattern, Matcher, Assert), so it needs its own direct
        # requirement on it.
        self.requires("keyple-util-cpp-lib/2.4.1", transitive_headers=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["LIBRARY_TYPE"] = "SHARED" if self.options.shared else "STATIC"
        tc.generate()
        CMakeDeps(self).generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["keypleserviceresourcecpplib"]
        self.cpp_info.set_property("cmake_file_name", "keyple-service-resource-cpp-lib")
        self.cpp_info.set_property("cmake_target_name", "Keyple::Service::Resource")
