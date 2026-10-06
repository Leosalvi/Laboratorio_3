import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (16,9))
x = np.array([1,8,6,9,0,4,5,7,3,4])
y = np.array([1,2,3,4,5,6,7,8,9,10])
plt.plot(x,y, color = 'blue')

plt.xlabel('cazzi')
plt.ylabel('cromosomi')
plt.title('Cazzi per cromosomi grafico')

plt.show()