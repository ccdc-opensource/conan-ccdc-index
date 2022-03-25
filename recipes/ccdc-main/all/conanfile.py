#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration

class CCDCMainConan(ConanFile):
    name = "ccdc-main"
    description = "Dependencies of main repository in CCDC"
    homepage = "https://ccdc.cam.ac.uk/"
    url = "https://github.com/conan-io/conan-center-index"
    topics = ("conan", "chemistry", "crystallography")
    license = "Proprietary"
    author = "Claudio Bantaloukas <cbantaloukas@ccdc.cam.ac.uk>"

    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True

    def build_requirements(self):
        if self.settings.os == 'Windows':
            self.build_requires("7zip/19.00")

        self.build_requires("cmake/3.22.3")
        self.build_requires("gtest/1.11.1")
        self.build_requires("installbuilder/21.12.0")
        self.build_requires("ninja/1.10.2")
        self.build_requires("swig/4.0.2")

    def requirements(self):
        if self.settings.os != 'Windows':
            self.requires("fontconfig/2.13.93")

        self.requires("ccdcboost/1.78.0")
        self.requires("ccdcsqlite3/3.38.1")
        self.requires("cpp-httplib/0.10.4")
        self.requires("cppad/20150000.9")
        self.requires("cryptopp/8.6.0")
        self.requires("fasta/36.3.8f")
        self.requires("gsoap/2.8.117")
        self.requires("inchi/1.04")
        self.requires("lexactivator/3.18.0")
        self.requires("lexfloatclient/4.6.0")
        self.requires("lexfloatserver/4.7.1")
        self.requires("libarchive/3.6.0")
        self.requires("libxl/3.8.2.0")
        self.requires("mariadb-connector-c/3.1.12")
        self.requires("openscenegraph/3.6.3")
        self.requires("openssl/1.1.1n")
        self.requires("povray/3.7.0.8")
        self.requires("range-v3/0.11.0")
        self.requires("rapidjson/1.1.0")
        self.requires("rstatistics/2.11.1")
        self.requires("zlib/1.2.11")
        self.requires("zstd/1.5.2")
