import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Definir las señales h[n] y x[n] para Hugo, Geral y Yonatan
hugo_h = np.array([5, 6, 0, 0, 7, 2, 6])
hugo_x = np.array([1, 0, 3, 3, 0, 9, 6, 3, 9, 7])

geral_h = np.array([5, 6, 0, 0, 6, 4, 4])
geral_x = np.array([1, 0, 3, 4, 3, 9, 7, 1, 3, 7])

yonatan_h = np.array([5, 6, 0, 0, 7, 2, 5])
yonatan_x = np.array([1, 0, 5, 3, 3, 2, 2, 4, 1, 5])

# Calcular la convolución
hugo_y = np.convolve(hugo_x, hugo_h)
geral_y = np.convolve(geral_x, geral_h)
yonatan_y = np.convolve(yonatan_x, yonatan_h)
print(yonatan_y)
# Crear interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Resultados de la Convolución")
root.geometry("800x500")

frame = ttk.Frame(root)
frame.pack(pady=10)

def show_vectors():
    vector_text = f"Hugo: {hugo_y.tolist()}\nGeral: {geral_y.tolist()}\nYonatan: {yonatan_y.tolist()}"
    vector_label.config(text=vector_text)

vector_label = ttk.Label(frame, text="", wraplength=700, justify="left")
vector_label.pack()

show_button = ttk.Button(root, text="Mostrar Vectores", command=show_vectors)
show_button.pack(pady=5)

# Graficar las convoluciones con colores distintos
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(range(len(hugo_y)), hugo_y, linefmt='b-', markerfmt='bo', basefmt=' ')  # Azul
plt.title('Convolución de Hugo')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid()
plt.xticks(range(0, len(hugo_y), 2))  # Espaciado mayor en eje x

plt.subplot(3, 1, 2)
plt.stem(range(len(geral_y)), geral_y, linefmt='m-', markerfmt='mo', basefmt=' ')  # Morado
plt.title('Convolución de Geral')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid()
plt.xticks(range(0, len(geral_y), 2))  # Espaciado mayor en eje x

plt.subplot(3, 1, 3)
plt.stem(range(len(yonatan_y)), yonatan_y, linefmt='g-', markerfmt='go', basefmt=' ')  # Verde
plt.title('Convolución de Yonatan')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid()
plt.xticks(range(0, len(yonatan_y), 2))  # Espaciado mayor en eje x

plt.tight_layout()
plt.show()

root.mainloop()
