#!/bin/bash
# Thank you to Robert Lujo for the answer he gave to https://stackoverflow.com/questions/6141581/detect-python-version-in-shell-script.
cd ~/Latin_app/Contents

ver=$(python -c"import sys; print(sys.version_info.major)")
if [ $ver -eq 2 ]; then
    echo "python version 2"
    echo "Configuring using python3 to install keyboard. Make sure to use python 3 in your shell."
    python3 -m pip install keyboard
elif [ $ver -eq 3 ]; then
    echo "python version 3"
    pip install keyboard
else 
    echo "Unknown python version: $ver"
    echo "terminating pre setup."
    exit
fi  