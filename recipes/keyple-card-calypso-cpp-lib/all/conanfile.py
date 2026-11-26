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
from conan.tools.build import can_run
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.env import VirtualRunEnv
from conan.tools.files import apply_conandata_patches, copy, export_conandata_patches, get


class KeypleCardCalypsoCppLibConan(ConanFile):
    name = "keyple-card-calypso-cpp-lib"
    license = "EPL-2.0"
    author = "Calypso Networks Association <https://calypsonet.org/>"
    url = "https://github.com/eclipse-keyple/keyple-card-calypso-cpp-lib"
    homepage = "https://keyple.org/apis/card-layer/calypso-lib/"
    description = "C++ implementation of the Eclipse Keyple Calypso card extension"
    topics = ("keyple", "calypso")

    package_type = "library"
    settings = "os", "arch", "compiler", "build_type"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_tests": [True, False]
    }

    default_options = {
        "shared": True,
        "fPIC": True,
        "with_tests": False
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
        self.requires("keyple-card-calypso-crypto-legacysam-cpp-lib/1.0.1", transitive_headers=True)
        self.requires("keyple-common-cpp-api/2.0.2", transitive_headers=True)
        self.requires("keypop-card-cpp-api/2.0.1", transitive_headers=True)
        self.requires("keypop-reader-cpp-api/2.1.0", transitive_headers=True)
        self.requires("keypop-calypso-card-cpp-api/2.2.0", transitive_headers=True)
        self.requires("keypop-calypso-crypto-asymmetric-cpp-api/0.2.0", transitive_headers=True)
        self.requires("keypop-calypso-crypto-legacysam-cpp-api/1.0.0", transitive_headers=True)
        self.requires("keypop-calypso-crypto-symmetric-cpp-api/0.1.1", transitive_headers=True)
        # keyple-card-calypso-crypto-legacysam-cpp-lib is a shared library, so
        # Conan does not propagate its own dependencies' libs transitively by
        # default. This package's own sources call directly into keyple-util
        # symbols, so it needs its own direct requirement on it.
        self.requires("keyple-util-cpp-lib/2.4.1", transitive_headers=True)

    def build_requirements(self):
        if self.options.with_tests:
            # 1.12.1 is the last GoogleTest release still compiling as C++11,
            # matching this project's CMAKE_CXX_STANDARD.
            self.test_requires("gtest/1.12.1")
            # Only the unit test suite constructs keyple-service-cpp-lib
            # types (e.g. ApduResponseAdapter) directly; the shipped library
            # itself doesn't need it.
            self.test_requires("keyple-service-cpp-lib/3.4.1")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["LIBRARY_TYPE"] = "SHARED" if self.options.shared else "STATIC"
        tc.variables["BUILD_TESTING"] = bool(self.options.with_tests)
        tc.generate()
        CMakeDeps(self).generate()
        if self.options.with_tests:
            VirtualRunEnv(self).generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if self.options.with_tests and can_run(self):
            bin_dir = os.path.join(self.build_folder, "bin")
            if self.settings.os == "Windows":
                bin_dir = os.path.join(bin_dir, str(self.settings.build_type))
            bin_name = "keyplecardcalypso_ut.exe" if self.settings.os == "Windows" else "keyplecardcalypso_ut"
            self.run(os.path.join(bin_dir, bin_name), env="conanrun")

    def package(self):
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["keyplecardcalypsocpplib"]
        self.cpp_info.set_property("cmake_file_name", "keyple-card-calypso-cpp-lib")
        self.cpp_info.set_property("cmake_target_name", "Keyple::Card::Calypso")

    def package_id(self):
        self.info.options.rm_safe("with_tests")
