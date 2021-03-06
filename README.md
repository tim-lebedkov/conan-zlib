[![Build Status](https://travis-ci.org/lasote/conan-zlib.svg)](https://travis-ci.org/lasote/conan-zlib)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/lasote/conan-zlib)](https://ci.appveyor.com/project/lasote/conan-zlib)


# conan-zlib

[Conan.io](https://conan.io) package for ZLIB library

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/zlib/1.2.8/lasote/stable).

## Build packages

    $ pip install conan_package_tools
    $ python build.py
    
## Upload packages to server

    $ conan upload zlib/1.2.8@lasote/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install zlib/1.2.8@lasote/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    zlib/1.2.8@lasote/stable

    [options]
    zlib:shared=true # false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
