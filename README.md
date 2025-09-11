# CALCULADORA DE ALGORITMOS Y PRUEBAS

*(Calculadora de algoritmos y pruebas - ENTREGA PRIMER PARCIAL)*

---

## **Descripción**
Este programa permite **generar secuencias de números pseudoaleatorios** utilizando diferentes algoritmos, y **realizar pruebas estadísticas** para validar su calidad. 
---

## **Estructura del Proyecto**

- main.py: Aplicación principal con GUI (Tkinter)
- algoritmos.py:            Implementación de los algoritmos de generación
- ventanas_generadores.py:  Interfaz para los generadores de número
- ventanas_pruebas.py:      Interfaz para las pruebas estadísticas
- ventanas_variables.py:    Interfaz para visualizar historial y gráficos
- ventanas.py:              Ventanas específicas de cada algoritmo
- gistoriaj.py:             Manejo del historial de cálculos (JSON)
- utils.py:                 Funciones utilitarias (gráficos, exportación a Excel)
- requirements.txt:         Dependencias del proyecto


---

## **Requisitos**
- **Python 3.13** (o superior).
- **Librerías requeridas**
- pandas>=2.0.0
- openpyxl>=3.1.0
- matplotlib>=3.7.0
- scipy>=1.10.0
- tkinter>=0.0.1  # Incluido en Python estándar

## **Funcionalidades del programa**
**1. Generación de secuencias pseudoaleatorias**

**Algoritmos implementados:**

- Cuadrados Medios.
- Productos Medios.
- Multiplicador Constante.

**Interfaz:**

-Campos para ingresar semillas e iteraciones.
-Tabla de resultados con formato profesional (ttk.Treeview).
-Gráfico de la secuencia generada (matplotlib).

**2. Pruebas estadísticas**

**Pruebas implementadas:**

- Prueba de Medias: Evalúa si la media de la secuencia es cercana a 0.5.
- Prueba de Varianza: Evalúa si la varianza es cercana a 1/12.
- Prueba de Uniformidad (K-S): Evalúa la uniformidad de la distribución.

**Interfaz:**

-Selección de un registro del historial.
-Resultado detallado de la prueba (estadístico calculado vs. crítico).

**3. Visualización de datos**

**Gráficos disponibles:**

-Histograma de frecuencias.
-Gráfico de línea de la secuencia generada (ri vs. iteración).

**Exportación:**
Botón para exportar tablas a Excel (pandas + openpyxl).



**4. Historial de cálculos**

**Almacenamiento:**

-Los resultados se guardan en un archivo JSON (historial.json).


**Interfaz:**

-Treeview para seleccionar cálculos anteriores.
-Opción para visualizar gráficos de registros históricos.

