import soundcard as sc
import numpy as np
import time
import matplotlib.pyplot as plt

speakers = sc.all_speakers()
print('Speakers disponibili: ', speakers, '\n')
default_speakers = sc.default_speaker()
print('speaker selezionato: ', default_speakers, '\n')


mics = sc.all_microphones()
print('Microfoni disponibili: ', mics, '\n')
default_mics = sc.default_microphone()
print('Microfono scelto: ', default_mics, '\n')

inizio = time.perf_counter()

data = default_mics.record(samplerate=48000, numframes=480000)
print('array acquisito: ')
print(data)
print('\n')

fine = time.perf_counter()

time.sleep(2)

inizio_1 = time.perf_counter()

#default_speakers.play(data/np.max(data), samplerate=48000)

fine_1 = time.perf_counter()

print('Tempo: ',fine - inizio)
print('Tempo registrazione: ',fine_1 - inizio_1)
print('Larray è lungo: ' ,len(data))


default_speakers = sc.default_speaker()
default_speakers.play(data/np.max(data), samplerate=48000)

plt.figure(figsize = (14,9))
x = np.arange(1, 480001)
y = data/np.max(data)

plt.xlabel('Tempo(s)')
plt.ylabel('Intensità')
plt.title('Plot line')
plt.grid()
plt.plot(x/48000,y)
plt.show()
