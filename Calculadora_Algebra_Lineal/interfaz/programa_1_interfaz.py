import tkinter as tk
from tkinter import ttk, messagebox


class Programa1Interfaz:

    def __init__(self, ventana):
        self.ventana = ventana

        self.numero_ecuaciones = tk.StringVar()
        self.numero_variables = tk.StringVar()

        self.ecuaciones = 0
        self.variables = 0

        self.entradas_matriz = []

        self.configurar_ventana()
        self.crear_interfaz()

    # Configuración principal de la ventana
    def configurar_ventana(self):

        self.ventana.title(
            "Calculadora de Álgebra Lineal - Programa 1"
        )

        self.ventana.geometry("1000x700")

        self.ventana.minsize(
            900,
            600
        )

    # Construcción inicial de la interfaz
    def crear_interfaz(self):

        titulo = ttk.Label(
            self.ventana,
            text="Programa 1 - Sistemas de Ecuaciones Lineales",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=(20, 5)
        )

        subtitulo = ttk.Label(
            self.ventana,
            text="Eliminación por filas",
            font=("Arial", 12)
        )

        subtitulo.pack(
            pady=(0, 20)
        )

        # Contenedor para las dimensiones del sistema
        marco_dimensiones = ttk.LabelFrame(
            self.ventana,
            text="Dimensiones del sistema",
            padding=15
        )

        marco_dimensiones.pack(
            padx=20,
            pady=10
        )

        # Número de ecuaciones
        lbl_ecuaciones = ttk.Label(
            marco_dimensiones,
            text="Número de ecuaciones:"
        )

        lbl_ecuaciones.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        txt_ecuaciones = ttk.Entry(
            marco_dimensiones,
            textvariable=self.numero_ecuaciones,
            width=10
        )

        txt_ecuaciones.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # Número de variables
        lbl_variables = ttk.Label(
            marco_dimensiones,
            text="Número de variables:"
        )

        lbl_variables.grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        txt_variables = ttk.Entry(
            marco_dimensiones,
            textvariable=self.numero_variables,
            width=10
        )

        txt_variables.grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        # Botón para crear la matriz
        btn_crear = ttk.Button(
            marco_dimensiones,
            text="Crear matriz",
            command=self.validar_dimensiones
        )

        btn_crear.grid(
            row=0,
            column=4,
            padx=15,
            pady=10
        )

        # Mensaje de estado
        self.lbl_estado = ttk.Label(
            self.ventana,
            text=""
        )

        self.lbl_estado.pack(
            pady=10
        )

        # Contenedor donde se generará la matriz aumentada
        self.marco_matriz = ttk.LabelFrame(
            self.ventana,
            text="Matriz aumentada",
            padding=15
        )

    # Validamos el número de ecuaciones y variables
    def validar_dimensiones(self):

        try:

            ecuaciones = int(
                self.numero_ecuaciones.get()
            )

            variables = int(
                self.numero_variables.get()
            )

            if ecuaciones <= 0 or variables <= 0:

                messagebox.showerror(
                    "Datos inválidos",
                    "El número de ecuaciones y variables debe ser mayor que cero."
                )

                return

            self.ecuaciones = ecuaciones
            self.variables = variables

            self.lbl_estado.config(
                text=(
                    f"Sistema de {self.ecuaciones} ecuaciones "
                    f"y {self.variables} variables."
                )
            )

            self.crear_matriz()

        except ValueError:

            messagebox.showerror(
                "Datos inválidos",
                "Debe ingresar números enteros."
            )

    # Generamos las casillas de la matriz aumentada
    def crear_matriz(self):

        # Limpiamos una matriz anterior, si existe
        for elemento in self.marco_matriz.winfo_children():
            elemento.destroy()

        self.entradas_matriz = []

        # Mostramos el contenedor
        self.marco_matriz.pack(
            padx=20,
            pady=15
        )

        # Encabezados de las variables
        for columna in range(self.variables):

            encabezado = ttk.Label(
                self.marco_matriz,
                text=f"x{columna + 1}"
            )

            encabezado.grid(
                row=0,
                column=columna + 1,
                padx=5,
                pady=5
            )

        # Separador de la matriz aumentada
        separador = ttk.Label(
            self.marco_matriz,
            text="|"
        )

        separador.grid(
            row=0,
            column=self.variables + 1,
            padx=5
        )

        # Encabezado del término independiente
        termino = ttk.Label(
            self.marco_matriz,
            text="b"
        )

        termino.grid(
            row=0,
            column=self.variables + 2,
            padx=5,
            pady=5
        )

        # Creamos cada fila de la matriz
        for fila in range(self.ecuaciones):

            fila_entradas = []

            # Número de ecuación
            lbl_fila = ttk.Label(
                self.marco_matriz,
                text=f"E{fila + 1}"
            )

            lbl_fila.grid(
                row=fila + 1,
                column=0,
                padx=5,
                pady=5
            )

            # Coeficientes de las variables
            for columna in range(self.variables):

                entrada = ttk.Entry(
                    self.marco_matriz,
                    width=8,
                    justify="center"
                )

                entrada.grid(
                    row=fila + 1,
                    column=columna + 1,
                    padx=5,
                    pady=5
                )

                fila_entradas.append(
                    entrada
                )

            # Separador visual
            barra = ttk.Label(
                self.marco_matriz,
                text="|"
            )

            barra.grid(
                row=fila + 1,
                column=self.variables + 1,
                padx=5
            )

            # Término independiente
            entrada_independiente = ttk.Entry(
                self.marco_matriz,
                width=8,
                justify="center"
            )

            entrada_independiente.grid(
                row=fila + 1,
                column=self.variables + 2,
                padx=5,
                pady=5
            )

            fila_entradas.append(
                entrada_independiente
            )

            self.entradas_matriz.append(
                fila_entradas
            )


# Permite ejecutar esta interfaz directamente
if __name__ == "__main__":

    ventana = tk.Tk()

    app = Programa1Interfaz(
        ventana
    )

    ventana.mainloop()