import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0,10,1000)
y1 = np.sin(x1)

x2 = np.linspace(0,15,1500)
y2 = np.sin(x2)

plt.figure(figsize = (16,9))
plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.xlabel('Ascisse')
plt.ylabel('Ordinate')
plt.title('Plot funzione', fontsize = 25, pad = 20)
plt.grid()


plt.subplot(1,2,2)
plt.plot(x2,y2, color = 'red')
plt.xlabel('Ascisse')
plt.ylabel('Ordinate')
plt.grid()
plt.title('Plot funzione n.2', fontsize = 25, pad = 20)

plt.show()