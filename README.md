tftpudGui
=========

A simple GUI for the tftpud server. Written using Qt4, python and PySide.
The code is entirely platform independent. Tested on:
- Linux Mint (Ubuntu 12.04 LTS)
- Crunchbang Linux 11 (Debian 6)

The tftpud project: https://github.com/javert/tftpud

Dependencies:
- python
- Qt4 (libraries Core, Gui)
- PySide
- tftpud (https://github.com/javert/ttpud/tftpud)


Installation:
Obtain the source distribution (python setup.py sdist).

Use python distutils to build and install:
$ python setup.py build
$ sudo python setup.py install

The GUI can be run using the script tftpudServerGui:
$ tftpudServerGui


