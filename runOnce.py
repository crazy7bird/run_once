import socket
import sys

DEFAULT_PORT = 1337
LOCAL_HOST = "127.0.0.1"

ALDER_PRIME_MODULO = 65521

class runOnce() :
    """ runOnce, bind a port to the program.
        if the port is already binded, will close it.
        this program is designed to detected and prevent,
        multiple program instances.
        To use it just use a variable never deleted during all the programme run :
         var_to_not_del = runOnce()
    """
    def __init__(self, port : int = None, verbose = False) -> None:
        self.portB = None
        self.portA = None
        self.callerName = sys.argv[0]
        self.socket_list = []
        self.port_list = []

        if port is None :
            for generatedPort in  self.alderChecksum() :
                self.port_list.append(generatedPort)
                print(f" - port : {generatedPort}")
        else :
            self.port_list.append(port)

        for p in self.port_list :
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0)
            try : 
                s.bind((LOCAL_HOST,p))
            except socket.error:
                print(f" Warning port : {p} already in use")
                continue
            self.socket_list.append(s)

        if not self.socket_list :
            print(" Program is already running")
            exit(1)


    def __del__(self) -> None :
        for s in self.socket_list :
            s.close()

    
    def alderChecksum(self) :
        A = 1
        B = 0
        for c in self.callerName :
            A = A + ord(c)
            B = B + A
        A = A % ALDER_PRIME_MODULO
        B = B % ALDER_PRIME_MODULO
        #checksum = B<<16 + A
        return [B,A]