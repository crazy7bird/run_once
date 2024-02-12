# run_once
Python script for limiting to one running of the same script instance.  
Inspired by [Socket-Singleton](https://pypi.org/project/Socket-Singleton/)

The main idea is to provide a way to detect if program is already running (and close it if so),  
by using socket port binding (if port is used, it’s means another instance is already running).

The main purpose of this version is to auto chose a port.

# Algorithm for chose a dedicated port
I chose to implement a checksum based on the program name given by :
```python
    import sys
    name = sys.argv[0]
```
I chose the Alder checksum over basic checksum cause in basic checksum letters order do not change the result.
Futher more Alder give a 32bits checksum, i use it to bind 2 ports and reduce colisions chances.

To launch the program at least one port should be biding.

# Improvement 

The script could be improved by using a sha256 for generating more ports.
This will reduce colision between progs and could also remove port binding for most used ports.


@tobecontinued


