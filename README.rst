PyCdll
======

This is a very quick, simple demonstration of C code being compiled on seperate
platforms (using MSVC on Windows and GCC on *nix) in such a way that the Python
module 'ctypes' can be used to invoke those functions from the resulting library
format (.DLL on Windows and .SO on *nix) in a fairly transparent way. Ideas
derived from `Wolf Projects
<http://wolfprojects.altervista.org/articles/dll-in-c-for-python/>`_.

On Windows
----------

On Windows, you must first ensure that the Microsoft Visual C++ Compiler (also
known as MSVC, used through the executable cl.exe, and typically exposed by the
vsvarsall.bat script in your Visual Studio installatino folder) is within the
current path scope. Then, you can run the 'built.bat' file to produce 'test.dll'
and, finally, run the 'test.py' script to ensure that 'test.dll' can be invoked.

On *nix
-------

On *nix platforoms (including MacOS), the compiler ('gcc') is already exposed in
the vast majority of cases (see your platform's specific package manager for
instructions on how to install GCC if it is not already available). In this case
you can simply run 'build.sh' (the shebang assumes /bin/bash, but any shell will
do) and, finally, run the 'test.py' script to ensure that 'test.so' can be
invoked.
