import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

def exportar_a_excel(data, filename):
    """
    Exporta los datos a un archivo Excel.
    Args:
        data (list): Lista de diccionarios con los datos.
        filename (str): Nombre del archivo Excel.
    Returns:
        bool: True si la exportación fue exitosa, False en caso contrario.
    """
    try:
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo exportar a Excel: {e}")
        return False

def mostrar_grafico_en_ventana(ventana, data, titulo, xlabel, ylabel):
    """
    Muestra un gráfico de línea en una ventana de Tkinter.
    Args:
        ventana (tk.Toplevel): Ventana donde se mostrará el gráfico.
        data (dict): Diccionario con los datos para el gráfico.
        titulo (str): Título del gráfico.
        xlabel (str): Etiqueta del eje X.
        ylabel (str): Etiqueta del eje Y.
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(data["Iteración"], data["ri"], 'b-', marker='o')
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def mostrar_histograma_en_ventana(ventana, data, titulo):
    """
    Muestra un histograma en una ventana de Tkinter.
    Args:
        ventana (tk.Toplevel): Ventana donde se mostrará el histograma.
        data (dict): Diccionario con los datos para el histograma.
        titulo (str): Título del histograma.
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(data["ri"], bins=10, edgecolor='black', alpha=0.7)
    ax.set_title(titulo)
    ax.set_xlabel("Valor de ri")
    ax.set_ylabel("Frecuencia")
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
