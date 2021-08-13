# Description
A script/executable to aid running your program from the command line. This is like `make` but it's `run`.
# Usage
Create a file called `runfile` containing the command to run you program, whether it's a script or an executable, including command line parameters and whatnot. Then call 
```
run
```
and it will kick off your program according to your makefile.
# Setup
Make sure you have `pyinstaller` installed, then run 
```
make
```
and add the binary to your path.
