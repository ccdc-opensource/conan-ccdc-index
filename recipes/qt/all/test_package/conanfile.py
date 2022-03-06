import os
import shutil

from conans import ConanFile, tools, Meson, RunEnvironment, CMake
from conans.errors import ConanException


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "qt", "cmake", "cmake_find_package_multi", "qmake"

    @property
    def _settings_build(self):
        return getattr(self, "settings_build", self.settings)

    def build_requirements(self):
        if self._settings_build.os == "Windows" and self.settings.compiler == "Visual Studio":
            self.build_requires("jom/1.1.3")

    def build(self):
        self.output.info("Building with cmake_find_package_multi")
        env_build = RunEnvironment(self)
        with tools.environment_append(env_build.vars):
            cmake = CMake(self, set_cmake_flags=True)
            if self.settings.os == "Macos":
                cmake.definitions['CMAKE_OSX_DEPLOYMENT_TARGET'] = '10.14'

            cmake.configure()
            cmake.build()

    def test(self):
        if not tools.cross_building(self.settings, skip_x64_x86=True):
            self.output.info("Testing CMake_find_package_multi")
            shutil.copy("qt.conf", "bin")
            self.run(os.path.join("bin", "test_package"), run_environment=True)
