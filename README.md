# dmtx-wrappers

Visual Studio solution for 32-bit and 64-bit builds of the `pydmtx` Python
package. Tested with [Anaconda](http://www.continuum.io/) distribution of
Python 2.7.x and Visual Studio Community 2013.

Forked from [http://sourceforge.net/p/libdmtx/libdmtx/ci/master/tree/](http://sourceforge.net/p/libdmtx/libdmtx/ci/master/tree/)
on 2015-04-03.

## Installing on Windows
Install a release from this repo. For 32-bit:
```
https://github.com/NaturalHistoryMuseum/dmtx-wrappers/releases/download/v0.7.4b1/pydmtx-0.7.4b1-cp27-none-win32.whl
```

64-bit:
```
https://github.com/NaturalHistoryMuseum/dmtx-wrappers/releases/download/v0.7.4b1/pydmtx-0.7.4b1-cp27-none-win_amd64.whl
```

The wheel was built using Visual C++ 2013. If Python reports an `ImportError`
when `import pydmtx` is run then you will need to install the
[Visual C++ Redistributable Packages for Visual Studio 2013](https://www.microsoft.com/en-US/download/details.aspx?id=40784).


## Building

You should only need to build if you want to release a new version.

`pydmtx` can be built using [MinGW](http://www.mingw.org/) but I had limited
success with that solution - the 32-bit build was able to find barcodes in some
images but not all and the 64-bit build caused the Python process to segfault
as soon as a `_pydmtx` function was called. 64-bit builds of `MinGW` are
[known to be buggy](https://github.com/ContinuumIO/anaconda-issues/issues/271).

This Visual Studio project was created by following Python's instructions for
[Building C and C++ Extensions on Windows](https://docs.python.org/2/extending/windows.html)
and [instructions on libdmtx wiki](http://libdmtx.wikidot.com/libdmtx-python-wrapper).

* Install Visual C++ 2013 Community Edition

* Build the 32-bit and/or 64-bit Release target of [libdmtx-windows](https://github.com/NaturalHistoryMuseum/libdmtx-windows/)

* Install the current Python 2.7 release of [Anaconda](https://store.continuum.io/cshop/anaconda/)

* Build the pydmtx Python extension module and a wheel:

    ```
    cd dmtx-wrappers\pydmtx
    pip install --upgrade pip
    pip install --upgrade setuptools
    pip install wheel
    build.bat
    ```
