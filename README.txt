Build using the Makefiles Package
---------------------------------
The Makefiles package provides a convenient mechanism for downloading
and building some of the external libraries required by some modules
included with Python. In particular, the makefiles package will
download and build:

    * bzip2
    * gdbm
    * openssl
    * sqlite
    * zlib 

Modules that are not supported include:

    * bsddb
    * Tkinter 

Additional modules that can be easily downloaded and compiled using
the makefiles module include:

    * apsw
    * cherrypy
    * genshi
    * kid
    * pil
    * pycurl
    * pylucene
    * sqlalchemy
    * wxpython

Getting the Makefiles 
--------------------- 
Go to:http://sourceforge.net/project/showfiles.php?group_id=182839 and
download the latest makefiles package.

Then, unpack the makefiles:

  # Create a top-level directory for our project;
  mkdir python-mingw             
  cd python-mingw
  tar xvzf makefiles-XXX.tar.gz
  mv makefiles-XXX makefiles

# cd into the makefiles directory where we will do the rest or our work;
cd makefiles

Install the Compilers
---------------------
If you do not already have the mingw compiler suite installed, you can
get it via:

  make mingw-download
  make mingw-unpack

Do the Build
------------
  make python25

Run the Tests
-------------
To verify which modules are working and installed:

  make python25-test

Reorganize the Layout
---------------------
The makefiles used to build Python-MinGW create a layout that is much
as it would be for any other unix platform. To reorganize the layout
so it more closely resembles the windows release from python.org, do
the following:

  make python25-win32-release

Build Additional Modules
------------------------
You can download and build additional modules for installation into
the python build tree. To see a list of available modules and install
them, do:

  make modulelist
  <displays a list of available modules and their versions>

  # Now, download and build a module
  make <module-name>

  # To build most modules; 
  make most

  # To build all modules:
  make all  # most + pil, pylucene, & wxpython;

Additional Make Targets
-----------------------
  make help:       prints a help message
  make download:   download all packages
  make modulelist: display list of modules and their versions 

