import tkinter as tk
from tkinter import ttk, messagebox
from utils import mostrar_histograma_en_ventana, mostrar_grafico_en_ventana
from historial import cargar_historial

class VentanaVariables(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Variables e Historial")
        self.geometry("900x600")

        # Treeview para mostrar el historial de cálculos
        self.tree = ttk.Treeview(self, columns=("Algoritmo", "Iteraciones"), show="headings")
        self.tree.heading("Algoritmo", text="Algoritmo")
        self.tree.heading("Iteraciones", text="Iteraciones")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Frame para los botones de acción
        frame_botones = ttk.Frame(self)
        frame_botones.pack(pady=10)

        # Botones para visualizar gráficos
        ttk.Button(frame_botones, text="Ver Histograma", command=self.mostrar_histograma).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Ver Gráfico de ri", command=self.mostrar_grafico_ri).pack(side=tk.LEFT, padx=5)

        # Botón para volver al menú principal
        ttk.Button(self, text="Volver atrás", width=15, command=self.destroy).pack(pady=10)

        # Cargar el historial de cálculos
        self.cargar_historial()

    def cargar_historial(self):
        """Carga el historial de cálculos en el Treeview."""
        historial = cargar_historial()
        for item in historial:
            self.tree.insert("", tk.END, values=(item["algoritmo"], len(item["data"])))

    def mostrar_histograma(self):
        """Muestra el histograma de los valores 'ri' seleccionados."""
        self._mostrar_grafico("histograma")

    def mostrar_grafico_ri(self):
        """Muestra el gráfico de línea de los valores 'ri' seleccionados."""
        self._mostrar_grafico("linea")

    def _mostrar_grafico(self, tipo):
        """
        Muestra un gráfico (histograma o línea) en una nueva ventana.
        Args:
            tipo (str): Tipo de gráfico ("histograma" o "linea").
        """
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un registro del historial")
            return

        item = self.tree.item(seleccion)
        algoritmo = item["values"][0]
        historial = cargar_historial()

        for item in historial:
            if item["algoritmo"] == algoritmo:
                data = {"ri": [fila[4] for fila in item["data"]]}
                ventana_grafico = tk.Toplevel(self)
                ventana_grafico.title(f"{tipo.capitalize()} - {algoritmo}")

                if tipo == "histograma":
                    mostrar_histograma_en_ventana(ventana_grafico, data, f"Histograma - {algoritmo}")
                else:
                    data["Iteración"] = list(range(len(data["ri"])))
                    mostrar_grafico_en_ventana(ventana_grafico, data, f"Gráfico de ri - {algoritmo}", "Iteración", "ri")
                break
