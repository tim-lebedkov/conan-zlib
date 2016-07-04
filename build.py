from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="zlib:shared", pure_c=True)

    # the following code enables the GCC builds on Windows and
    # should be moved later into conan-io/conan-package-tools
    if platform.system() == "Windows":
        builder._add_linux_gcc_builds(shared_option_name="zlib:shared", 
            pure_c=True)
        
    builder.run()
