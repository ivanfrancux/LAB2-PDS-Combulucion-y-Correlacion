import numpy as np
import matplotlib.pyplot as plt
import wfdb
from scipy.fftpack import fft
from scipy.signal import welch
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Cargar la señal desde los archivos
record_name = r"C:\Users\alejo\Desktop\señales\Lab 2\s01_ex01_s02"
record = wfdb.rdrecord(record_name)
signal = record.p_signal[:, 0]  # Primera señal (asumiendo una sola)
fs = record.fs  # Frecuencia de muestreo

def estadisticos_descriptivos(signal):
    return {
        "Media": np.mean(signal),
        "Mediana": np.median(signal),
        "Desviación estándar": np.std(signal),
        "Mínimo": np.min(signal),
        "Máximo": np.max(signal)
    }

# Calcular estadísticos
descriptive_stats = estadisticos_descriptivos(signal)

# Transformada de Fourier
N = len(signal)
frequencies = np.fft.fftfreq(N, 1/fs)
fft_values = fft(signal)

# Densidad espectral de potencia (PSD)
freqs, psd = welch(signal, fs, nperseg=1024)

# Cálculo de estadísticas en frecuencia
frecuencia_media = np.sum(freqs * psd) / np.sum(psd)
frecuencia_mediana = freqs[np.searchsorted(np.cumsum(psd), np.sum(psd) / 2)]
desviacion_estandar = np.sqrt(np.sum(psd * (freqs - frecuencia_media) ** 2) / np.sum(psd))

# Crear ventana gráfica
root = tk.Tk()
root.title("Análisis de Señal")

fig, axs = plt.subplots(4, 1, figsize=(8, 12))

# Señal en función del tiempo
time = np.arange(len(signal)) / fs
axs[0].plot(time, signal, label='Señal en el tiempo')
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Amplitud (mV)')
axs[0].set_title('Señal en función del tiempo')
axs[0].legend()

# Transformada de Fourier
axs[1].plot(frequencies[:N//2], np.abs(fft_values[:N//2]), label='FFT')
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Amplitud (mV)')
axs[1].set_title('Transformada de Fourier de la señal')
axs[1].legend()

# Densidad espectral de potencia
axs[2].semilogy(freqs, psd, label='Densidad espectral de potencia')
axs[2].set_xlabel('Frecuencia (Hz)')
axs[2].set_ylabel('Densidad espectral (mV²/Hz)')
axs[2].set_title('Densidad espectral de la señal')
axs[2].legend()

# Histograma de frecuencias
axs[3].hist(freqs, bins=30, weights=psd, alpha=0.7, label='Histograma de frecuencias')
axs[3].set_xlabel('Frecuencia (Hz)')
axs[3].set_ylabel('Densidad de potencia (mV²/Hz)')
axs[3].set_title('Histograma de la distribución de frecuencias')
axs[3].legend()

fig.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()

# Mostrar estadísticas
stats_text = f"""
Estadísticos descriptivos:
Media: {descriptive_stats['Media']}
Mediana: {descriptive_stats['Mediana']}
Desviación estándar: {descriptive_stats['Desviación estándar']}
Mínimo: {descriptive_stats['Mínimo']}
Máximo: {descriptive_stats['Máximo']}

Frecuencia media: {frecuencia_media}
Frecuencia mediana: {frecuencia_mediana}
Desviación estándar en frecuencia: {desviacion_estandar}
"""
label = tk.Label(root, text=stats_text, justify='left', font=('Arial', 10))
label.pack()

root.mainloop()
