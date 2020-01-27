BASE_DIR   = ../..
SWIG       = swig
SYMBOLS    = -DUSE_LINUX
GCC        = g++
CPPFLAGS   = -shared -Wall -Wno-deprecated -pthread -fPIC
LIBS       = -L${BASE_DIR}/lib -lDragonfly
PY_INC     = /usr/include/python3.7
PYTHON     = /usr/bin/python3
INCLUDES   = -I${BASE_DIR}/include -I${BASE_DIR}/include/internal
H2PY	   = ctypesgen

all:  _PyDragonfly.so Dragonfly_types.py

PyDragonfly.py: PyDragonfly.i
	${SWIG} ${SYMBOLS} ${INCLUDES} -c++ -python PyDragonfly.i

_PyDragonfly.so:  PyDragonfly.py
	${GCC} ${CPPFLAGS} ${INCLUDES} ${SYMBOLS} -I${PY_INC} ${LIBS} PyDragonfly_wrap.cxx -o _PyDragonfly.so -lDragonfly -lpython3.7m

Dragonfly_types.py: ${BASE_DIR}/include/Dragonfly_types.h
	${H2PY} `pwd`/../../include/Dragonfly_types.h -a -o Dragonfly_types.py

clean:
	rm -f *.so
	rm -f *.cxx
	rm -f PyDragonfly.py
	rm -f *.pyc
	rm -f Dragonfly_types.xml
	rm -f Dragonfly_types.py

