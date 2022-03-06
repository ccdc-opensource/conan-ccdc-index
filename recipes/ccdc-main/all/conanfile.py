#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration

class CCDCMainConan(ConanFile):
    name = "ccdc-main"
    version = '2021.0.0'
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

        self.build_requires("cmake/3.20.1")
        self.build_requires("gtest/1.8.1")
        self.build_requires("installbuilder/21.7.0-bld1")
        self.build_requires("ninja/1.10.2")
        self.build_requires("swig/4.0.2")

    def requirements(self):
        if self.settings.os != 'Windows':
            self.requires("fontconfig/2.13.93")

        self.requires("ccdcboost/1.75.0")
        self.requires("ccdcsqlite3/3.17.0")
        self.requires("cppad/20150000.9")
        self.requires("cryptopp/8.2.0@bincrafters/stable")
        self.requires("csdprotobufs/1.0.128")
        self.requires("fasta/36.3.8f")
        self.requires("gsoap/2.8.113")
        self.requires("inchi/1.04")
        self.requires("lexactivator/3.14.7")
        self.requires("lexfloatclient/4.5.2")
        self.requires("lexfloatserver/4.5.2")
        self.requires("libarchive/3.5.1")
        self.requires("libxl/3.8.2.0")
        self.requires("mariadb-connector-c/3.1.11")
        self.requires("openscenegraph/3.6.3")
        self.requires("openssl/1.1.1k")
        self.requires("povray/3.7.0.8")
        self.requires("range-v3/0.11.0")
        self.requires("rapidjson/1.1.0")
        self.requires("rstatistics/2.11.1")
        self.requires("zlib/1.2.11")
        self.requires("zstd/1.4.9")
