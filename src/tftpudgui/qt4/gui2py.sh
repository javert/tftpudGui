#!/bin/bash
pyside-uic -o ui_mainwindow.py mainwindow.ui
pyside-rcc -o TftpServer_rc.py TftpServer.qrc
