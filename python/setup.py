# pydmtx - Python wrapper for libdmtx
#
# Copyright (C) 2006 Dan Watson
# Copyright (C) 2007, 2008, 2009 Mike Laughton
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# $Id$

import os
import platform
import shutil
import sys

from setuptools import setup, Extension

LIBDMTX = '../../libdmtx/'

if '64bit' == platform.architecture()[0]:
    LIBDMTX_DLL_DIR = os.path.join(LIBDMTX, 'x64', 'Release')
else:
    LIBDMTX_DLL_DIR = os.path.join(LIBDMTX, 'Win32', 'Release')

if 'bdist' in sys.argv:
    shutil.copy(os.path.join(LIBDMTX_DLL_DIR, 'libdmtx.dll'), '.')

mod = Extension( '_pydmtx',
                 include_dirs = [LIBDMTX],
                 library_dirs = [LIBDMTX_DLL_DIR],
                 libraries = ['libdmtx'],
                 sources = ['pydmtxmodule.c']
               )

setup(name = 'pydmtx',
      version = '0.7.4b1',
      description = 'A thin wrapper around libdmtx',
      py_modules = ['pydmtx'],
      ext_modules = [mod],
      data_files = [('', ['libdmtx.dll'])],
     )
