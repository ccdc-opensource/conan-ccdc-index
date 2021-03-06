#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain


required_conan_version = ">=1.43.0"


class CCDCMainConan(ConanFile):
    name = "ccdc-main"
    description = "Dependencies of main repository in CCDC"
    homepage = "https://ccdc.cam.ac.uk/"
    url = "https://github.com/conan-io/conan-center-index"
    topics = ("conan", "chemistry", "crystallography")
    license = "Proprietary"
    author = "Claudio Bantaloukas <cbantaloukas@ccdc.cam.ac.uk>"

    settings = "os", "arch", "compiler", "build_type"
    generators = ["CMakeDeps", "CMakeToolchain", "json"]
    no_copy_source = True

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["USING_CONAN_PACKAGES"] = "TRUE"
        tc.generate()

    def build_requirements(self):
        if self.settings.os == 'Windows':
            self.tool_requires("7zip/19.00")

        self.tool_requires("cmake/3.22.3")
        self.tool_requires("installbuilder/21.12.0")
        self.tool_requires("ninja/1.10.2")

        # When we upgrade swig to 4.1, please remove the no_fatal_warnings line in SwigPyLibrary
        self.tool_requires("swig/4.0.2")

        # Needed to create intermediate files
        self.tool_requires("gsoap/2.8.117")

    def requirements(self):
        if self.settings.os != 'Windows':
            self.requires("fontconfig/2.13.93")

        self.requires("approvaltests.cpp/10.12.1")
        self.requires("ccdcboost/1.78.0")
        self.requires("ccdcsqlite3/3.38.1")
        self.requires("cpp-httplib/0.10.4")
        self.requires("cppad/20150000.9")
        self.requires("cryptopp/8.6.0")
        self.requires("expat/2.4.7")
        self.requires("fasta/36.3.8f")
        self.requires("gsoap/2.8.117")
        self.requires("gtest/1.11.0")
        self.requires("inchi/1.04")
        self.requires("lexactivator/3.18.0")
        self.requires("lexfloatclient/4.6.0")
        self.requires("lexfloatserver/4.7.1")
        self.requires("libarchive/3.6.0")
        self.requires("libxl/3.8.2.0")
        self.requires("mariadb-connector-c/3.1.12")
        self.requires("openscenegraph/3.6.5")
        self.requires("openssl/1.1.1n")
        self.requires("povray/3.8.0-beta.2")
        self.requires("protobuf/3.19.2")
        self.requires("qt/5.15.8")
        self.requires("qwt/6.2.0")
        self.requires("range-v3/0.11.0")
        self.requires("rapidjson/1.1.0")
        self.requires("rstatistics/2.11.1")
        self.requires("zlib/1.2.12")
        self.requires("zstd/1.5.2")
