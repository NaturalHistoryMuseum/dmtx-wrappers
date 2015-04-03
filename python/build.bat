rem Builds wheels of pydmtx
echo Clean
del /S *pyc
del /S libdmtx.dll
rmdir /Q /S dist build

echo Build
rem Default installation directory of Visual Studio Community 2013 tools
set "VS90COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\Tools\"
python setup.py build --compiler msvc bdist bdist_wheel
