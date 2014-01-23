#!/usr/bin/env python

from distutils.core import setup

setup(name='tftpudGui',
      version='0.1',
      description='A TFTP server utility application.',
      author='Huw Lewis',
      author_email='huw.lewis2409@gmail.com',
      packages=['tftpudgui', 'tftpudgui.qt4'],
      #package_dir={'tftpudgui':'src/tftpudgui'},
      package_data={'tftpudgui.qt4' : ['resources/*'] },
      scripts=['tftpudServerGui'],
      license='MIT License',
      requires=['tftpud', 'pyside', 'qt4'])
