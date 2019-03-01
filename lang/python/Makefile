BASE_DIR   = ../..
SWIG       = swig # swig executable (add to path or include full path here)
SYMBOLS    = -DUSE_LINUX
GCC        = g++
CPPFLAGS   = -shared -Wall -Wno-deprecated -pthread -fPIC
PY_CONFIG = python3-config # path or command to python-config utility
PYTHON     = python3 # path to python executable (might be unecessary? Some systems may need to reference this var to run H2XML and XML2PY)
PY_INC     := $(shell ${PY_CONFIG} --includes) # generate command to include python header files
PY_LD_FLAGS := $(shell ${PY_CONFIG} --ldflags) # generate commands to link to python library files
LIBS       = -L${BASE_DIR}/lib -lDragonfly # link dragonfly library
LDFLAGS   += ${LIBS} ${PY_LD_FLAGS}
INCLUDES   = -I${BASE_DIR}/include -I${BASE_DIR}/include/internal
H2XML      = h2xml
XML2PY     = xml2py
CLANG2PY   = /usr/local/lib/python3.7/site-packages/ctypeslib/clang2py.py # path to clang2py to convert message defs

all:  _PyDragonfly.so Dragonfly_types.py

PyDragonfly.py: PyDragonfly.i
	${SWIG} ${SYMBOLS} ${INCLUDES} -c++ -python PyDragonfly.i

_PyDragonfly.so:  PyDragonfly.py
	${GCC} ${CPPFLAGS} ${INCLUDES} ${SYMBOLS} ${PY_INC} ${LDFLAGS} PyDragonfly_wrap.cxx -o _PyDragonfly.so -lDragonfly

Dragonfly_types.py: ${BASE_DIR}/include/Dragonfly_types.h
	${PYTHON} ${CLANG2PY} -c -k cdefmstu -o Dragonfly_types.py `pwd`/../../include/Dragonfly_types.h

clean:
	rm -f *.so
	rm -f *.cxx
	rm -f PyDragonfly.py
	rm -f *.pyc
	rm -f Dragonfly_types.xml
	rm -f Dragonfly_types.py

