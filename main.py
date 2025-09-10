import tkinter as tk
from tkinter import ttk
from ventanas_generadores import VentanaGeneradores
from ventanas_pruebas import VentanaPruebas
from ventanas_variables import VentanaVariables

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú Principal - Números Pseudoaleatorios")
        self.geometry("500x300")
        self.resizable(False, False)

        # Etiqueta principal
        ttk.Label(self, text="Seleccione una opción", font=("Arial", 16)).pack(pady=20)

        # Botones para acceder a las ventanas secundarias
        ttk.Button(self, text="Generadores de Números Pseudoaleatorios", width=35, command=self.abrir_generadores).pack(pady=10)
        ttk.Button(self, text="Pruebas Estadísticas", width=35, command=self.abrir_pruebas).pack(pady=10)
        ttk.Button(self, text="Variables e Historial", width=35, command=self.abrir_variables).pack(pady=10)

    def abrir_generadores(self):
        """Abre la ventana de generadores de números pseudoaleatorios."""
        VentanaGeneradores(self)

    def abrir_pruebas(self):
        """Abre la ventana de pruebas estadísticas."""
        VentanaPruebas(self)

    def abrir_variables(self):
        """Abre la ventana de variables e historial."""
        VentanaVariables(self)

if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()
