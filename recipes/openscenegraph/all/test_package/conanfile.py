from conans import ConanFile, tools
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def generate(self):
        tc = CMakeToolchain(self)
        for key, value in self.options["openscenegraph"].items():
            if key.startswith("with_"):
                tc.variables["OSG_HAS_" + key.upper()] = 1 if value else 0
        if self.settings.os == "Macos":
            tc.variables["OSG_HAS_WITH_GIF"] = 0
            tc.variables["OSG_HAS_WITH_JPEG"] = 0
            tc.variables["OSG_HAS_WITH_PNG"] = 0

        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            bin_path = os.path.join(self.build_folder, "test_package")
            self.run(bin_path, run_environment=True)
