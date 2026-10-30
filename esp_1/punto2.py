
import numpy as np
import matplotlib.pyplot as plt

# Componenti
R1 = 10000
R2 = 100000
C = 4.7e-9

# Le tue misure sperimentali (NON MODIFICATE)
f = np.array([20, 50,100,200,300, 340,400, 500,700,1000,2000, 5000,10000,20000])
Vin = np.array([0.20, 0.20, 0.20, 0.20, 0.20,0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20,0.20])
Vout = np.array([2.00, 2.00, 1.92, 1.67, 1.40, 1.32,1.20, 1.04, 0.8, 0.56, 0.28, 0.12, 0.08, 0.04 ])

# Incertezze PROVVISORIE, da verificare
sVin = 0.005
sVout = 0.005
sR2 = 0.05 * R2
sC = 0.10 * C

# Guadagno sperimentale ed errore propagato
G = Vout / Vin
sG = G * np.sqrt((sVout/Vout)**2 + (sVin/Vin)**2)

# Guadagno in decibel ed errore propagato
GdB = 20 * np.log10(G)
sGdB = (20 / np.log(10)) * sG / G

# Frequenza di taglio e relativo errore
fc = 1 / (2 * np.pi * R2 * C)
sfc = fc * np.sqrt((sR2/R2)**2 + (sC/C)**2)

# Guadagno teorico
f_teo = np.logspace(1, 5, 300)
G_teo = (R2/R1) / np.sqrt(1 + (f_teo/fc)**2)

print("Frequenza di taglio:", fc, "+/-", sfc, "Hz")

# Grafico log-log
plt.figure()
plt.loglog(f_teo, G_teo, label="Teorico")
plt.errorbar(f, G, yerr=sG, fmt="o", capsize=3, label="Sperimentale")
plt.axvline(fc, color="red", linestyle="--", label="fc teorica")
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Guadagno")
plt.title("Integratore reale - scala log-log")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("integratore_loglog_errori.png", dpi=200)

# Grafico di Bode
plt.figure()
plt.semilogx(f_teo, 20*np.log10(G_teo), label="Teorico")
plt.errorbar(f, GdB, yerr=sGdB, fmt="o", capsize=3, label="Sperimentale")
plt.axvline(fc, color="red", linestyle="--", label="fc teorica")
plt.axhline(20*np.log10(R2/R1)-3.01, color="gray",
            linestyle=":", label="-3 dB dal massimo")
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Guadagno (dB)")
plt.title("Integratore reale - diagramma di Bode")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("integratore_bode_errori.png", dpi=200)

plt.show()