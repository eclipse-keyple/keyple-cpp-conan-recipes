CMAKE_MINIMUM_REQUIRED(VERSION 3.15)
PROJECT(test_package CXX)

FIND_PACKAGE(keyple-card-calypso-crypto-legacysam-cpp-lib REQUIRED CONFIG)

ADD_EXECUTABLE(test_package src/test_package.cpp)
TARGET_LINK_LIBRARIES(test_package PRIVATE Keyple::Card::Calypso::Crypto::LegacySam)
TARGET_COMPILE_FEATURES(test_package PRIVATE cxx_std_11)
