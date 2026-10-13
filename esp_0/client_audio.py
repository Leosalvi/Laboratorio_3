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

dimensione = int(s.recv(4096).decode())

vocale = b''

while len(vocale) < dimensione:
    blocco = s.recv(4096)
    
    if not blocco: break
    
    vocale += blocco
    
array_vocale_fin = pickle.loads(vocale)

default_speakers = sc.default_speaker()
#default_speakers.play(array_vocale_fin/np.max(array_vocale_fin), samplerate=48000)

s.close()

plt.figure(figsize = (16,9))
x = np.arange(len(array_vocale_fin))/48000
y = array_vocale_fin/np.max(abs(array_vocale_fin))
plt.plot(x,y)

plt.xlabel('Tempo[s]', fontsize = 15)
plt.ylabel('Ampiezza digitale[adimens.]', fontsize = 15)
plt.title('Waveform audio registrato', fontsize = 25, pad = 20)
plt.grid()
plt.axhline(y=0, color='black', linewidth=1, linestyle='-')

plt.show()
