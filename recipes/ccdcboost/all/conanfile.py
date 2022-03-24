from conans import ConanFile, tools
import os
import glob


class CcdcBoostConan(ConanFile):
    name = "ccdcboost"
    description = "A copy of boost with a patched shared_ptr"
    topics = ("conan", "kludge", "boost", "libraries", "cpp")
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://www.boost.org"
    license = "BSL-1.0"
    settings = "os", "compiler", "arch", "build_type"
    no_copy_source = True
    exports_sources = ['patches/*']

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = 'boost_'+self.version.replace('.','_')
        os.rename(extracted_dir, self._source_subfolder)
        for patch in self.conan_data["patches"].get(self.version, []):
            tools.patch(**patch)

    def package(self):
        self.copy("LICENSE_1_0.txt", dst="licenses", src=os.path.join(self.source_folder,
                                                                      self._source_subfolder))
        tools.rmdir(os.path.join(self.package_folder, "lib", "cmake"))
        self.copy(pattern="*", dst="include/boost", src="%s/boost" % self._source_subfolder)

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.env_info.BOOST_ROOT = self.package_folder
        self.cpp_info.names["cmake_find_package"] = "ccdcboost"
        self.cpp_info.names["cmake_find_package_multi"] = "ccdcboost"
