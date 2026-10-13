import socket, pickle
import numpy as np
import matplotlib.pyplot as plt
import time

host = 'localhost' # Symbolic name meaning all available interfaces
port = 12345       # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

vocale_array = pickle.dumps(data)


print("Host: ", host, ", Port: ", port)

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        data1 = conn.recv(4096) # we received this
        dimensione = len(vocale_array)
        if not data1:
            break
        print('Connesso?:', data1.decode())
        conn.sendall(str(dimensione).encode())
        
        for i in range(0, len(vocale_array), 4096):
            blocco = vocale_array[i:i + 4096]
            conn.sendall(blocco)
            
    except socket.error:
        print("Error Occured.")
        break

conn.close()