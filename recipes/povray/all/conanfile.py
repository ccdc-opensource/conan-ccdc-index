import glob
import os
import stat

from conans import ConanFile, AutoToolsBuildEnvironment, MSBuild, tools, RunEnvironment

class PovrayConan(ConanFile):
    name = "povray"
    description = "The Persistence of Vision Raytracer."
    license = ["AGPL-3.0-only"]
    topics = ("conan", "freexl", "excel", "xls")
    homepage = "https://www.povray.org"
    url = "https://github.com/POV-Ray/povray"
    settings = "os_build", "arch_build", "compiler"

    _autotools= None

    @property
    def _source_subfolder(self):
        return "source_subfolder"


    def build_requirements(self):
        self.build_requires("automake/1.16.4")
        if self.settings.os_build == 'Windows':
            self.build_requires('7zip/19.00')

    def requirements(self):
        self.requires("boost/1.78.0")
        self.requires("zlib/1.2.12")
        self.requires("libpng/1.6.37")
        self.requires("libjpeg/9d")
        self.requires("libtiff/4.3.0")

    def source(self):
        if self.settings.os_build == "Windows":
            archive_name='povray-3.7.0.0.7z'
            # Building on windows Is a royal pain... I'll just grab a build
            tools.download(
                url=f'https://artifactory.ccdc.cam.ac.uk:443/artifactory/ccdc-3rdparty-windows-runtime-exes/{archive_name}',
                filename=archive_name,
                sha256='9fe7dead0e07e2425ff8c6784e6a6991c9a0feee2582563c6fa1450b37da8702',
                headers={
                'X-JFrog-Art-Api': os.environ.get("ARTIFACTORY_API_KEY", None)
            })
            self.run('7z x %s' % archive_name)
            os.unlink(archive_name)
            os.rename('povray-3.7.0.0', self._source_subfolder)
        else:
            tools.get(**self.conan_data["sources"][self.version])
            os.rename(f"povunix-v{self.version}-src", self._source_subfolder)

    def build(self):
        if self.settings.compiler == "Visual Studio":
            pass
            # self._build_msvc()
        else:
            self._build_autotools()

    def _build_autotools(self):
        with tools.environment_append(RunEnvironment(self).vars):
            autotools = self._configure_autotools()
            autotools.make()

    def _build_msvc(self):
        msbuild = MSBuild(self)
        msbuild.build(
            project_file=os.path.join(self._source_subfolder, "windows", "vs10", "povray.sln"),
            build_type='Release',
            arch='x86_64',
        )

    def _configure_autotools(self):
        if self._autotools:
            return self._autotools
        self._autotools = AutoToolsBuildEnvironment(self, win_bash=tools.os_info.is_windows)
        args = [
            'COMPILED_BY=CCDC',
            f'--with-boost-libdir={tools.unix_path(self.deps_cpp_info["boost"].lib_paths[0])}'
        ]
        with tools.environment_append(self._autotools.vars):
            self._autotools.configure(args=args, configure_dir=self._source_subfolder)
        return self._autotools

    def package(self):
        self.copy("COPYING", dst="licenses", src=self._source_subfolder)
        if self.settings.os_build == "Windows":
            self.copy("*", src=self._source_subfolder)
        else:
            autotools = self._configure_autotools()
            autotools.install()

    def package_id(self):
        del self.info.settings.compiler

    def package_info(self):
        bin_path = os.path.join(self.package_folder, 'bin')
        self.output.info('Appending PATH environment variable: %s' % bin_path)
        self.env_info.PATH.append(bin_path)
