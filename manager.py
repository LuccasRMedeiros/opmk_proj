import os
import sys
import subprocess
from enum import Enum


__libopmk_dir = "open_maker"
__libopmk_build = __libopmk_dir + "/build"

class ManagerError(Enum):
    CMAKE_FAIL = 1
    MAKE_FAIL = 2

def build():
    print("Building libopen_maker")

    try:
        os.mkdir(__libopmk_build)
    except FileExistsError:
        pass

    os.chdir(__libopmk_build)
    if subprocess.run(["cmake", "-DCMAKE_BUILD_TYPE=Debug", ".."]).return_code() != 0:
        print("Cmake build step failed.")
        sys.exit(ManagerError.CMAKE_FAIL)

    if subprocess.run(["make", "-j8"]).return_code() != 0:
        print("Make build step failed.")
        sys.exit(ManagerError.MAKE_FAIL)

def show_help_message():
    print(
            "Use this script to execute mundane tasks on Open Maker Project.",
            "The following are accepted commands and its functions")
    print("  -b | --build : Build libopen_maker and radiant_vivarium")

def main():
    if len(sys.argv) < 2:
        show_help_message()

    for arg in sys.argv:
        if arg == '-b' or arg == '--build':
            build()
        else:
            print("Unrecognizable argument:", arg + ";", "will be ignored")

if __name__ == "__main__":
    main()
