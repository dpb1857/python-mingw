#! env python

# Create a distutils.cfg file telling easy_install the location of
# our site-packages directory.  This is really only necessary on windows
# where the mingw build system is creating a non-standard
# directory layout.

import os.path
import distutils.sysconfig

cfg = """
[easy_install]
install_dir = %(site_packages)s
"""

libdir = distutils.sysconfig.get_python_lib(0, 1)
cfg_file = os.path.join(libdir, "distutils", "distutils.cfg")
site_packages = os.path.join(libdir, "site-packages")

f = file(cfg_file, "w")
f.write(cfg % locals())
f.close()
