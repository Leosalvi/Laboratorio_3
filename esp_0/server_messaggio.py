import socket, pickle
import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
import time

speakers = sc.all_speakers()
print('Speakers disponibili: ', speakers, '\n')
default_speakers = sc.default_speaker()
print('speaker selezionato: ', default_speakers, '\n')


mics = sc.all_microphones()
print('Microfoni disponibili: ', mics, '\n')
default_mics = sc.default_microphone()
print('Microfono scelto: ', default_mics, '\n')

data = default_mics.record(samplerate=48000, numframes=48000)
print('array acquisito: ')
print(data)
print('\n')

host = 'localhost' # Symbolic name meaning all available interfaces
port = 12345       # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

vocale_array = pickle.dumps(data)
print(len(vocale_array))

print("Host: ", host, ", Port: ", port)

s.listen(1)
conn, addr = s.accept()

print('Connected by ', addr)

while True:

    try:
        data1 = conn.recv(4096) # we received this
        
        if not data1:
            break
        print('Connesso?:', data1.decode())
        conn.send(vocale_array)
    except socket.error:
        print("Error Occured.")
        break

conn.close()