@echo off
rem Builds the test.c 'library' into a .DLL using the Microsoft Visual C++
rem compiler (cl.exe), which must be within scope of the current path.
cl /LD /nologo test.c > NUL
