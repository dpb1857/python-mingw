# -*- Makefile -*-

include .configuration
include make/templates


### Avoid problems when building under cygwin by making sure we're 
### in the directory we need to be in;

ifneq "$(BASE)" ""
ifneq "$(shell pwd)" "$(BASE)/$(MAKEFILES)"
$(error You must run 'make' from the directory $(BASE)/$(MAKEFILES))
endif
endif

##################################################
# GLOBAL DEFINES 
##################################################

ifeq "$(PLATFORM)" "WIN32"
EXE= .exe
endif

ifeq "$(PLATFORM)" "WIN32"
# On WIN32, update the path so that we can (a) automatically find the mingw
# compilers, and (b) locate modules we have compiled as DLLs;
PATH := $(BASE)/work/bin:$(MINGW_BASE)/bin:$(PATH)
else
# On Unix, we need to add $(BASE)/work/bin to the path to find wx-config;
PATH := $(BASE)/work/bin:$(PATH)
endif

export MAKE

default: help

help:: top-level-help

##################################################
# MODULES
##################################################

include config/module-config
include config/VersionList
MODULE_FILES = $(wildcard modules/*[^~\#])
include $(MODULE_FILES)

##################################################
# Top-level targets;
##################################################

top-level-help:
	@echo
	@echo "Type 'make most' to build python with most add-on modules."
	@echo "Type 'make all' to build most + larger packages - pil, pylucene, and wxpython."
	@echo "Type 'make test' to run tests on unpacked modules with a test target."
	@echo
	@echo "'make download' will download the source packages for all modules."
	@echo "'make clean' will do a 'make clean' for all modules."
	@echo "'make distclean' will do a 'make distclean' for all modules."
	@echo "'make work-clean' will remove the work directory and the -install timestamps."
	@echo
	@echo "'make modulelist' for list of buildable/installable modules."
	@echo "'make <module-name>' will build a single module and any prerequisites."
	@echo
ifeq "$(PLATFORM)" "WIN32"
	@echo "'make mingw-download' will download the MinGW compiler suite;"
	@echo "'make mingw-unpack' will unpack the MinGW compilers in ../mingw."
endif
	@echo "'make configuration' will regenerate the .configuration file."

# NOTE: drop pyinstaller for now, support has moved;
most:  python setuptools readline apsw pycurl cherrypy kid genshi sqlalchemy lxml flup
# NOTE: pylucene doesn't want to build, newer versions use a different mechanism;
# all:   most pil pylucene wxpython
all:   most pil wxpython

_clean:
	rm -f *~
	rm -rf timestamps

clean:: _clean

distclean:: _clean work-clean
	rm -f .configuration
	rm -f ../.configuration
	rm -f *.log

timestamps:
	mkdir timestamps

work-clean:
	rm -rf ../work
	rm -f timestamps/*-install

$(BASE)/download:
	mkdir $@

$(BASE)/src:
	mkdir $@

.PHONY: download clean distclean help 
.PHONY: most all _clean work-clean 

###################################################################################
# Build .configuration, a file that will hold various system-dependendent variables;
#
# PLATFORM : the platform we're building for - SUNOS, LINUX, or WIN32
# BASE     : the top level directory which contains the src, makefiles, work, 
#            and download directories;
###################################################################################

# Determine our  build platform;

ifeq "$(PLATFORM)" ""
ifeq "$(OS)" "Windows_NT"
PLATFORM=WIN32
endif
ifeq "$(shell uname -s)" "SunOS"
PLATFORM=SOLARIS
endif
ifeq "$(shell uname -s)" "Linux"
PLATFORM=LINUX
endif
endif

export PLATFORM

# Determine our top level directory;
BASE = $(realpath ..)
ifeq "$(BASE)" ""
BASE = $(shell cd .. && pwd)
endif

CWD = $(realpath .)
ifeq "$(CWD)" ""
CWD = $(shell pwd)
endif

MAKEFILES = $(notdir $(CWD))

configuration: force_configuration
	@echo
	@echo "**"
	@echo "** Current configuration file:"
	@echo "**"
	@echo
	@cat .configuration

force_configuration .configuration:
	@echo "Trying to generate .configuration..."
	@# You can remove this directory name check if you want to take your chances...
	@# See the script for components with known problems.
ifeq "$(PLATFORM)" "WIN32"
	@./scripts/check-nt-directory-name
endif
	@./scripts/check-tools
	@echo "Generating .configuration"
	@echo '# -*-Makefile-*-' 				      	>  .configuration
	@echo '# DO NOT EDIT, THIS FILE IS GENERATED BY THE MAKEFILE'	>> .configuration
	@echo ''                                  			>> .configuration
	@echo "PLATFORM = $(PLATFORM)"                			>> .configuration
	@echo "BASE = $(BASE)"	                			>> .configuration
	@echo "MAKEFILES = $(MAKEFILES)"               			>> .configuration
	@if [ $(PLATFORM) = "WIN32" ]; then \
	    ./scripts/find-mingw;	 \
	fi
	@rm -f ../.configuration
	ln -s $(MAKEFILES)/.configuration ../.configuration

status:
	@echo "*****************************"
	@echo "***** top-level status: *****"
	@echo "*****************************"
	cd .. && git status
	@echo "*****************************"
	@echo "***** makefiles status: *****"
	@echo "*****************************"
	git status
	@echo "*****************************"
	@echo "***** python status:    *****"
	@echo "*****************************"
	cd ../src/python && git status


.PHONY: default all _clean clean distclean update status configuration force_configuration
