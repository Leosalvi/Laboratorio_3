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
print('Larray è lungo: ' ,len(data))


default_speakers = sc.default_speaker()
default_speakers.play(data/np.max(abs(data)), samplerate=48000)

plt.figure(figsize = (16,9))
x = np.arange(len(data))/48000
y = data/np.max(abs(data))
plt.plot(x,y)

plt.xlabel('Tempo[s]', fontsize = 15)
plt.ylabel('Ampiezza digitale[adimens.]', fontsize = 15)
plt.title('Waveform audio registrato', fontsize = 25, pad = 20)
plt.grid()
plt.axhline(y=0, color='black', linewidth=1, linestyle='-')
plt.show()
