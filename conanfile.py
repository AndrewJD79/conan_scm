import os
import shutil
from conans import ConanFile, tools, CMake
from conans.errors import ConanException

class Pkg(ConanFile):

    scm = {
         "type": "git",
         "url": "auto",
         "revision": "auto",
    }