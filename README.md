# OTMql4Fix
## Open Trading Metaquotes4 FIX Bridge

### OTMql4Fix - Open Trading Metaquotes4 FIX Bridge
https://github.com/OpenTrading/OTMql4Fix/

This package allows the OpenTrading Metatrader-Python bridge
(https://github.com/OpenTrading/OTMql4Py/)
to communicate with outside applications that speak the FIX protocol.
FIX is emerging standard for formatting messages for asynchronous
communications between financial and trading applications:
http://fixprotocol.org

This project builds on the FIX parser:
http://github.com/dmitryme/fix_parser
and builds on OTMql4Py, and requires that as a pre-requisite.
There are no pre-requisites in your Python other than `ctypes`,
which is now a part of the Python standard library. The `fix_parser`
works under Windows and Linux, so you can use it from Mt4 under Windows,
and use the `fix_parser` again in the client programs that communicate to Mt4,
under Windows or Linux.

The current code offers only the ability to format and parse FIX messages:
you will still need a communications mechanism to asynchronously
send and receive these formatted messages, such as OTMql4Fix:
https://github.com/OpenTrading/OTMql4Fix/

**This is a work in progress - a developers' pre-release version.**

It works on Mt4 builds > 6xx, but the documentation still needs to be done,
as well as more tests and testing on different versions.
Only Python 2.7.x is supported.

### History

The original idea for this project was to make a Mt4<->FIX
bi-directional bridge based on an existing C-coded gateway:
Http/sourceforge.net/projects/fixmt4gateway/files/fixGateway-mt4.zip
But that code has many problems, and is an incomplete, hard-coded,
partial implementation of FIX.

A better, more complete, Fix parser that is multi-FIX-version is:
http://github.com/dmitryme/fix_parser
which allows FIX to be cleanly integrated into Python. The code is very
efficient, and uses Python's `ctypes import` mechanism to expose
C/C++ code directly into Python. We expect this code to be faster
than code based on QuickFix (http://www.quickfix.org) which uses SWIG,
but we have not yet benchmarked the code.

We have simply compiled the `fix_parser` code according to its instructions
and have included the necessary glue to make it work under OTMql4Py,
and it install it the way Mt4 requires.
There are no changes to the `fix_parser` code itself.

To recompile the binaries we used MSVS2010Express from Microsoft,
and `cmake` from http://www.cmake.org:
http://www.cmake.org/files/v3.2/cmake-3.2.2-win32-x86.zip
The `fix_parser.dll` uses the `libxml2` libraries from http://www.xmlsoft.org,
and we used the compiled DLL supplied with the `fix_parser` distribution.

The project wiki should be open for editing by anyone logged into GitHub:
**Please report any system it works or doesn't work on in the wiki:
include the Metatrader build number, the origin of the metatrader exe,
the Windows version, and the Python version and origin of the Python.**
This code in known to run under Linux Wine (1.7.x), so this project
bridges Metatrader to Python under Linux.

### Installation

For the moment there is no installer: just "git clone" or download the
zip from github.com and unzip into an empty directory. Then recursively copy
the folder MQL4 over the MQL4 folder of your Metatrader installation. It will
not overwrite any Mt4 system files.

You will then need to copy the required DLLs from `lib/windows-x86`
into your Windows system folder (e.g. `c:\windows\system32`).
You may get away with copying them to any directory that is in your
Windows `PATH` environment variable, but your mileage may vary.

### Testing

Tests are yet to be written, but look at the example.py file in the
`MQL4/Python/OTMql427` directory.


### Project

Please file any bugs in the issue tracker:
https://github.com/OpenTrading/OTMql4Fix/issues

Use the Wiki to start topics for discussion:
https://github.com/OpenTrading/OTMql4Fix/wiki
It's better to use the wiki for knowledge capture, and then we can pull
the important pages back into the documentation in the share/doc directory.
You will need to be signed into github.com to see or edit in the wiki.

