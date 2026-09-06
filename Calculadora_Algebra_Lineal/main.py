import tkinter as tk
from tkinter import ttk

from interfaz.programa_1_interfaz import Programa1Interfaz
from interfaz.programa_2_interfaz import Programa2Interfaz


class CalculadoraAlgebraLineal:

    def __init__(self, ventana):
        self.ventana = ventana

        self.configurar_ventana()
        self.crear_interfaz()

    # Configuramos la ventana principal de la calculadora
    def configurar_ventana(self):

        self.ventana.title(
            "Calculadora de Álgebra Lineal"
        )

        self.ventana.geometry(
            "1200x800"
        )

        self.ventana.minsize(
            1000,
            700
        )

    # Construimos la calculadora principal
    def crear_interfaz(self):

        # Encabezado general
        encabezado = ttk.Frame(
            self.ventana
        )

        encabezado.pack(
            fill="x",
            padx=20,
            pady=(15, 5)
        )

        titulo = ttk.Label(
            encabezado,
            text="Calculadora de Álgebra Lineal",
            font=("Arial", 20, "bold")
        )

        titulo.pack()

        subtitulo = ttk.Label(
            encabezado,
            text=(
                "Herramientas matriciales "
                "y sistemas de ecuaciones lineales"
            ),
            font=("Arial", 11)
        )

        subtitulo.pack(
            pady=(5, 10)
        )

        # Contenedor de los diferentes programas
        self.cuaderno_programas = ttk.Notebook(
            self.ventana
        )

        self.cuaderno_programas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # Programa 1
        self.programa_1 = Programa1Interfaz(
            self.cuaderno_programas
        )

        self.cuaderno_programas.add(
            self.programa_1,
            text="Programa 1"
        )

        # Programa 2
        self.programa_2 = Programa2Interfaz(
            self.cuaderno_programas
        )

        self.cuaderno_programas.add(
            self.programa_2,
            text="Programa 2"
        )


# Punto de entrada de toda la calculadora
def main():

    ventana = tk.Tk()

    CalculadoraAlgebraLineal(
        ventana
    )

    ventana.mainloop()


if __name__ == "__main__":
    main()