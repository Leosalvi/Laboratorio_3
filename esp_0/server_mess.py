import socket, pickle
import numpy as np
import matplotlib.pyplot as plt
import time

host = 'localhost' # Symbolic name meaning all available interfaces
port = 12345       # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

vil = [(1,2,3,4,5)]
array = pickle.dumps(vil)

print("Host: ", host, ", Port: ", port)

s.listen(1)
conn, addr = s.accept()

while True:
    try:
        data1 = conn.recv(4096) # we received this
        if not data1:
            break
        print('Connesso?', 'client:[',data1.decode(),']')
        conn.sendall(str('Adesso ti manderò un array va bene?').encode())
        risp = conn.recv(4096)
        print('Posso mandare?','client:[',risp.decode(),']')
        
        conn.sendall(array)
    except socket.error:
        print("Error Occured.")
        break

conn.close()