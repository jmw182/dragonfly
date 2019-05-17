BASE_DIR   = ../..
SWIG       = swig # swig executable (add to path or include full path here)
SYMBOLS    = -DUSE_LINUX
GCC        = g++
CPPFLAGS   = -shared -Wall -Wno-deprecated -pthread -fPIC
PYTHON     = python3 # path (or name if on path) to preferred python interpreter for use with clang2py (python 2 or python 3)
PY3_CONFIG = python3-config # path or command to python3-config utility
PY3_INC     := $(shell ${PY3_CONFIG} --includes) # generate command to include python header files
PY3_LD_FLAGS := $(shell ${PY3_CONFIG} --ldflags) # generate commands to link to python library files
PY2_CONFIG = python-config # path or command to python-config utility (may need to replace with python2-config)
PY2_INC     := $(shell ${PY2_CONFIG} --includes) # generate command to include python header files
PY2_LD_FLAGS := $(shell ${PY2_CONFIG} --ldflags) # generate commands to link to python library files
LIBS       = -L${BASE_DIR}/lib -lDragonfly # link dragonfly library
LDFLAGS_PY3   += ${LIBS} ${PY3_LD_FLAGS}
LDFLAGS_PY2   += ${LIBS} ${PY2_LD_FLAGS}
INCLUDES   = -I${BASE_DIR}/include -I${BASE_DIR}/include/internal
CLANG2PY   = /usr/local/lib/python3.7/site-packages/ctypeslib/clang2py.py # path to clang2py to convert message defs

all:  _PyDragonfly3.so _PyDragonfly2.so Dragonfly_types.py

PyDragonfly3.py: PyDragonfly3.i
	${SWIG} ${SYMBOLS} ${INCLUDES} -c++ -python PyDragonfly3.i

_PyDragonfly3.so:  PyDragonfly3.py
	${GCC} ${CPPFLAGS} ${INCLUDES} ${SYMBOLS} ${PY3_INC} ${LDFLAGS_PY3} PyDragonfly3_wrap.cxx -o _PyDragonfly3.so -lDragonfly

PyDragonfly2.py: PyDragonfly2.i
	${SWIG} ${SYMBOLS} ${INCLUDES} -c++ -python PyDragonfly2.i

_PyDragonfly2.so:  PyDragonfly2.py
	${GCC} ${CPPFLAGS} ${INCLUDES} ${SYMBOLS} ${PY2_INC} ${LDFLAGS_PY2} PyDragonfly2_wrap.cxx -o _PyDragonfly2.so -lDragonfly

Dragonfly_types.py: ${BASE_DIR}/include/Dragonfly_types.h
	${PYTHON} ${CLANG2PY} -c -k cdefmstu -o Dragonfly_types.py `pwd`/../../include/Dragonfly_types.h

clean:
	rm -f *.so
	rm -f *.cxx
	rm -f PyDragonfly{2,3}.py
	rm -f *.pyc
	rm -f Dragonfly_types.py

