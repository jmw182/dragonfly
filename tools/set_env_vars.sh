# Determine where Dragonfly is installed
THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DRAGONFLY_DIR=$( dirname "${THIS_DIR}")

export DRAGONFLY=${DRAGONFLY_DIR}

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${DRAGONFLY}/lib

export PYTHONPATH=${PYTHONPATH}:${DRAGONFLY}/lang/python

export PATH=${PATH}:${DRAGONFLY}/tools
