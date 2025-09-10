import json
import os

HISTORIAL_FILE = "historial.json"

def guardar_en_historial(data, algoritmo):
    """
    Guarda los resultados en el historial.
    Args:
        data (list): Lista de filas con los resultados.
        algoritmo (str): Nombre del algoritmo utilizado.
    """
    historial = cargar_historial()
    historial.append({"algoritmo": algoritmo, "data": data})
    with open(HISTORIAL_FILE, "w") as f:
        json.dump(historial, f)

def cargar_historial():
    """
    Carga el historial desde el archivo.
    Returns:
        list: Lista con los registros del historial.
    """
    if not os.path.exists(HISTORIAL_FILE):
        return []
    with open(HISTORIAL_FILE, "r") as f:
        return json.load(f)
