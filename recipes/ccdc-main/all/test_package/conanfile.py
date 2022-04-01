import os
from conans import ConanFile, CMake, tools
from conan.tools.cmake import CMakeToolchain


class FontconfigTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self, skip_x64_x86=True):
            self.run("example", run_environment=True)
