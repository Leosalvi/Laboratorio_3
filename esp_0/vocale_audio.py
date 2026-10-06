import soundcard as sc
import numpy as np

speakers = sc.all_speakers()
print('Speakers disponibili: ', speakers, '\n')
default_speakers = sc.default_speaker()
print('speaker selezionato: ', default_speakers, '\n')


mics = sc.all_microphones()
print('Microfoni disponibili: ', mics, '\n')
default_mics = sc.default_microphone()
print('Microfono scelto: ', default_mics, '\n')

data = default_mics.records(samplerate=48000, numframes=48000)
print('array acquisito: ')
print(data)
print('\n')

default_speakers.play(data/np.max(data), samplerate=48000)

print('Larray è lungo: ' ,len(data))