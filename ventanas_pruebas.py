import tkinter as tk
from tkinter import ttk, messagebox
import math
import statistics as stats
from scipy.stats import chi2
from historial import cargar_historial

# Valores críticos para las pruebas estadísticas
Z_CRIT = {0.10: 1.6448536269514722, 0.05: 1.959963984540054, 0.01: 2.5758293035489004}
KS_C = {0.10: 1.22, 0.05: 1.36, 0.01: 1.63}

def prueba_medias(samples, alpha=0.05):
    """
    Realiza la prueba de medias para evaluar si la media de los números generados es cercana a 0.5.
    Args:
        samples (list): Lista de números pseudoaleatorios (ri).
        alpha (float): Nivel de significancia (default: 0.05).
    Returns:
        dict: Resultado de la prueba.
    """
    n = len(samples)
    if n == 0:
        return {'error': 'NO HAY DATOS'}
    mu = sum(samples) / n
    z = (mu - 0.5) / math.sqrt(1 / (12 * n))  # Cálculo del estadístico Z
    zc = Z_CRIT.get(alpha, Z_CRIT[0.05])  # Valor crítico de Z para el nivel de significancia
    ok = abs(z) <= zc  # Comparación para aceptar o rechazar H0
    return {
        "nombre": "Prueba de Medias",
        "resultado": "ACEPTA" if ok else "RECHAZA",
        "z": z,
        "zc": zc,
        "media": mu
    }

def prueba_varianza(samples, alpha=0.05):
    """
    Realiza la prueba de varianza para evaluar si la varianza es cercana a 1/12.
    Args:
        samples (list): Lista de números pseudoaleatorios (ri).
        alpha (float): Nivel de significancia (default: 0.05).
    Returns:
        dict: Resultado de la prueba.
    """
    n = len(samples)
    if n < 2:
        return {'error': 'NO HAY DATOS'}
    s2 = stats.variance(samples)  # Varianza muestral
    sigma2 = 1 / 12  # Varianza teórica esperada
    k = n - 1  # Grados de libertad
    chi = k * s2 / sigma2  # Estadístico chi-cuadrado
    low = chi2.ppf(alpha / 2, k)  # Límite inferior del intervalo crítico
    high = chi2.ppf(1 - alpha / 2, k)  # Límite superior del intervalo crítico
    ok = low <= chi <= high  # Comparación para aceptar o rechazar H0
    return {
        "nombre": "Prueba de Varianza",
        "resultado": "ACEPTA" if ok else "RECHAZA",
        "chi2": chi,
        "rango": [low, high]
    }

def prueba_uniformidad(samples, alpha=0.05):
    """
    Realiza la prueba de Kolmogorov-Smirnov para evaluar la uniformidad de los números generados.
    Args:
        samples (list): Lista de números pseudoaleatorios (ri).
        alpha (float): Nivel de significancia (default: 0.05).
    Returns:
        dict: Resultado de la prueba.
    """
    n = len(samples)
    if n == 0:
        return {'error': 'NO HAY DATOS'}
    xs = sorted(samples)
    d_plus = max((i + 1) / n - x for i, x in enumerate(xs))  # Máxima diferencia positiva
    d_minus = max(x - i / n for i, x in enumerate(xs))  # Máxima diferencia negativa
    d = max(d_plus, d_minus)  # Estadístico D de KS
    c = KS_C.get(alpha, KS_C[0.05])  # Valor crítico para el nivel de significancia
    dcrit = c / math.sqrt(n)  # Valor crítico ajustado
    ok = d <= dcrit  # Comparación para aceptar o rechazar H0
    return {
        "nombre": "Prueba de Uniformidad (K-S)",
        "resultado": "ACEPTA" if ok else "RECHAZA",
        "D": d,
        "Dcrit": dcrit
    }

class VentanaPruebas(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pruebas Estadísticas")
        self.geometry("800x600")

        # Frame para seleccionar el registro del historial
        self.frame_historial = ttk.LabelFrame(self, text="Seleccionar Datos del Historial")
        self.frame_historial.pack(pady=10, padx=10, fill=tk.X)

        # Treeview para mostrar el historial de cálculos
        self.tree_historial = ttk.Treeview(self.frame_historial, columns=("Algoritmo", "Iteraciones"), show="headings")
        self.tree_historial.heading("Algoritmo", text="Algoritmo")
        self.tree_historial.heading("Iteraciones", text="Iteraciones")
        self.tree_historial.pack(fill=tk.BOTH, expand=True)

        # Frame para seleccionar la prueba
        self.frame_pruebas = ttk.LabelFrame(self, text="Seleccionar Prueba")
        self.frame_pruebas.pack(pady=10, padx=10, fill=tk.X)

        # Botones para ejecutar cada prueba
        ttk.Button(self.frame_pruebas, text="Prueba de Medias", command=lambda: self.ejecutar_prueba("medias")).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_pruebas, text="Prueba de Varianza", command=lambda: self.ejecutar_prueba("varianza")).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_pruebas, text="Prueba de Uniformidad", command=lambda: self.ejecutar_prueba("uniformidad")).pack(side=tk.LEFT, padx=5)

        # Frame para mostrar resultados
        self.frame_resultados = ttk.LabelFrame(self, text="Resultados")
        self.frame_resultados.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Área de texto para mostrar los resultados
        self.text_resultados = tk.Text(self.frame_resultados, wrap=tk.WORD, width=80, height=15)
        self.text_resultados.pack(fill=tk.BOTH, expand=True)

        # Botón para volver al menú principal
        ttk.Button(self, text="Volver atrás", width=15, command=self.destroy).pack(pady=10)

        # Cargar el historial de cálculos
        self.cargar_historial()

    def cargar_historial(self):
        """Carga el historial de cálculos en el Treeview."""
        historial = cargar_historial()
        for item in historial:
            self.tree_historial.insert("", tk.END, values=(item["algoritmo"], len(item["data"])))

    def ejecutar_prueba(self, tipo_prueba):
        """
        Ejecuta la prueba estadística seleccionada sobre los datos del historial.
        Args:
            tipo_prueba (str): Tipo de prueba a realizar ("medias", "varianza", "uniformidad").
        """
        seleccion = self.tree_historial.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un registro del historial")
            return

        item = self.tree_historial.item(seleccion)
        algoritmo = item["values"][0]
        historial = cargar_historial()

        for item in historial:
            if item["algoritmo"] == algoritmo:
                samples = [fila[4] for fila in item["data"]]  # Extraer los valores 'ri'
                resultado = self.realizar_prueba(tipo_prueba, samples)
                self.mostrar_resultado(resultado)
                break

    def realizar_prueba(self, tipo_prueba, samples):
        """
        Realiza la prueba estadística seleccionada.
        Args:
            tipo_prueba (str): Tipo de prueba ("medias", "varianza", "uniformidad").
            samples (list): Lista de números pseudoaleatorios (ri).
        Returns:
            dict: Resultado de la prueba.
        """
        if tipo_prueba == "medias":
            return prueba_medias(samples)
        elif tipo_prueba == "varianza":
            return prueba_varianza(samples)
        elif tipo_prueba == "uniformidad":
            return prueba_uniformidad(samples)
        else:
            return {"error": "Prueba no reconocida"}

    def mostrar_resultado(self, resultado):
        """
        Muestra el resultado de la prueba en el área de texto.
        Args:
            resultado (dict): Resultado de la prueba estadística.
        """
        self.text_resultados.delete(1.0, tk.END)
        if "error" in resultado:
            self.text_resultados.insert(tk.END, resultado["error"])
            return

        self.text_resultados.insert(tk.END, f"{resultado['nombre']}\n")
        self.text_resultados.insert(tk.END, f"Resultado: {resultado['resultado']}\n")
        if resultado['nombre'] == "Prueba de Medias":
            self.text_resultados.insert(tk.END, f"Z calculado: {resultado['z']:.4f}\n")
            self.text_resultados.insert(tk.END, f"Z crítico: {resultado['zc']:.4f}\n")
            self.text_resultados.insert(tk.END, f"Media muestral: {resultado['media']:.4f}\n")
        elif resultado['nombre'] == "Prueba de Varianza":
            self.text_resultados.insert(tk.END, f"Chi² calculado: {resultado['chi2']:.4f}\n")
            self.text_resultados.insert(tk.END, f"Rango crítico: [{resultado['rango'][0]:.4f}, {resultado['rango'][1]:.4f}]\n")
        elif resultado['nombre'] == "Prueba de Uniformidad (K-S)":
            self.text_resultados.insert(tk.END, f"D calculado: {resultado['D']:.4f}\n")
            self.text_resultados.insert(tk.END, f"D crítico: {resultado['Dcrit']:.4f}\n")
