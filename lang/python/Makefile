BASE_DIR   		= ../..
SWIG       		= swig # swig executable (add to path or include full path here)
SYMBOLS    		= -DUSE_LINUX
GCC        		= g++
CPPFLAGS   		= -shared -Wall -Wno-deprecated -pthread -fPIC
PY2_CONFIG  	= python2-config # path or command to python-config utility
PYTHON2     	= python2 # path to python executable (unecessary if on path)
PY2_INC     	:= $(shell ${PY2_CONFIG} --includes) # path to python header files
PY2_LD_FLAGS 	:= $(shell ${PY2_CONFIG} --ldflags) # generate commands to link to python library files
PY3_CONFIG  	= python3-config # path or command to python-config utility
PYTHON3     	= python3 # path to python executable (unecessary if on path)
PY3_INC     	:= $(shell ${PY3_CONFIG} --includes) # path to python header files
PY3_LD_FLAGS 	:= $(shell ${PY3_CONFIG} --ldflags) # generate commands to link to python library files
LIBS       		= -L${BASE_DIR}/lib -lDragonfly # link Dragonfly library
LDFLAGS_PY2   	+= ${LIBS} ${PY2_LD_FLAGS}
LDFLAGS_PY3   	+= ${LIBS} ${PY3_LD_FLAGS}
INCLUDES   		= -I${BASE_DIR}/include -I${BASE_DIR}/include/internal # Dragonfly includes
CLANG2PY   		= /usr/local/lib/python3.7/site-packages/ctypeslib/clang2py.py

all:  _PyDragonfly2.so _PyDragonfly3.so

PyDragonfly2.py: PyDragonfly2.i
	${SWIG} ${SYMBOLS} ${INCLUDES} -c++ -python PyDragonfly2.i

PyDragonfly3.py: PyDragonfly3.i
	${SWIG} ${SYMBOLS} ${INCLUDES} -c++ -python PyDragonfly3.i

_PyDragonfly2.so:  PyDragonfly2.py
	${GCC} ${CPPFLAGS} ${INCLUDES} ${SYMBOLS} -I${PY2_INC} ${LDFLAGS_PY2} PyDragonfly2_wrap.cxx -o _PyDragonfly2.so

_PyDragonfly3.so:  PyDragonfly3.py
	${GCC} ${CPPFLAGS} ${INCLUDES} ${SYMBOLS} -I${PY3_INC} ${LDFLAGS_PY3} PyDragonfly3_wrap.cxx -o _PyDragonfly3.so

clean:
	rm -f *.so
	rm -f *.cxx
	rm -f PyDragonfly{2,3}.py
	rm -f *.pyc