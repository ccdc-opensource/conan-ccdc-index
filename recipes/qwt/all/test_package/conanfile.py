from conans import ConanFile, CMake, tools
import os


class QwtTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            bin_path = os.path.join(self.build_folder, "example")
            self.run(bin_path, run_environment=True)
