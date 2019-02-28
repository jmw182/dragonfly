BASE_DIR   = ../..
SWIG       = swig # swig executable (add to path or include full path here)
SYMBOLS    = -DUSE_LINUX
GCC        = g++
CPPFLAGS   = -shared -Wall -Wno-deprecated -pthread -fPIC
PY_INC     = $(shell python-config --includes) # generate command to include python header files
PYTHON     = python # path to python executable (might be unecessary? Some systems may need to reference this var to run H2XML and XML2PY)
PY_LD_FLAGS := $(shell python-config --ldflags) # generate commands to link to python library files
LIBS       = -L${BASE_DIR}/lib -lDragonfly # link dragonfly library
LDFLAGS   += ${LIBS} ${PY_LD_FLAGS}
INCLUDES   = -I${BASE_DIR}/include -I${BASE_DIR}/include/internal
H2XML      = h2xml
XML2PY     = xml2py

all:  _PyDragonfly.so Dragonfly_types.py

PyDragonfly.py: PyDragonfly.i
	${SWIG} ${SYMBOLS} ${INCLUDES} -c++ -python PyDragonfly.i

_PyDragonfly.so:  PyDragonfly.py
	${GCC} ${CPPFLAGS} ${INCLUDES} ${SYMBOLS} ${PY_INC} ${LDFLAGS} PyDragonfly_wrap.cxx -o _PyDragonfly.so -lDragonfly

Dragonfly_types.xml: ${BASE_DIR}/include/Dragonfly_types.h
	${H2XML} -c -o Dragonfly_types.xml `pwd`/../../include/Dragonfly_types.h

Dragonfly_types.py: Dragonfly_types.xml
	${XML2PY} -o Dragonfly_types.py Dragonfly_types.xml

clean:
	rm -f *.so
	rm -f *.cxx
	rm -f PyDragonfly.py
	rm -f *.pyc
	rm -f Dragonfly_types.xml
	rm -f Dragonfly_types.py

