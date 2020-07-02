from conans import ConanFile, CMake, tools


class CXXProjectConan(ConanFile):
    name = "CXXProjectConan"
    version = "1.0.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "git@github.com:Portfence/transparent_cmake_conan_project_template.git"
    description = "Example of a CXX Project using cmake_find_package_multi generator"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    requires = "boost/1.73.0", \
               "websocketpp/0.8.2"
    generators = "cmake_find_package_multi"
    scm = {
        "type": "git",
        "url": url,
        "revision": "auto"
    }


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()


    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()


    def package_info(self):
        if not self.in_local_cache:
            self.cpp_info.includedirs = ["include"]
            self.cpp_info.libdirs = ["build/src"]

        self.cpp_info.libs = [self.name]
