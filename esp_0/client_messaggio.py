import socket , pickle
import soundcard as sc
import time 
import matplotlib.pyplot as plt
import numpy as np

#host = socket.gethostname()
host = "localhost"
#host = "192.168.1.131"

port = 12345  # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('si'.encode())  # we send this string

vocale = s.recv(10_000_000)
array_vocale_fin = pickle.loads(vocale)
s.close()

plt.figure(figsize = (14,9))
x = np.arange(1, 480001)
y = array_vocale_fin/np.max(array_vocale_fin)

plt.xlabel('Tempo(s)')
plt.ylabel('Intensità')
plt.title('Plot line')
plt.grid()
plt.plot(x/48000,y)
plt.show()

