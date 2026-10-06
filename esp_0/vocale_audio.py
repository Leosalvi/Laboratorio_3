import soundcard as sc
import numpy as np

speakers = sc.all_speakers()
print('Speakers disponibili: ', speakers, '\n')
default_speakers = sc.default_speaker()
print('speaker selezionato: ', default_speakers, '\n')


mics = sc.all_microphones()
print('Microfoni disponibili: ', mics, '\n')
default_mics = sc.default_microphone()
print('Microfono scelto: ', default_mics, '\n'
      )