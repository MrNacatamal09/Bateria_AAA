"""
Construye la ventana principal de la Calculadora de Álgebra Lineal.
Integra los módulos, sus programas y el acceso a los teoremas correspondientes.
Tema de clase: integración de herramientas de Álgebra Lineal.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk

from interfaz.programa_1_interfaz import (
    Programa1Interfaz
)

from interfaz.programa_2_interfaz import (
    Programa2Interfaz
)

from interfaz.programa_3_interfaz import (
    Programa3Interfaz
)

from interfaz.programa_4_interfaz import (
    Programa4Interfaz
)

from interfaz.modulo_matrices_interfaz import (
    ModuloMatricesInterfaz
)

from interfaz.modulo_determinantes_interfaz import (
    ModuloDeterminantesInterfaz
)

from modulos.modulo_sistemas import (
    obtener_logo_modulo as obtener_logo_sistemas,
    obtener_descripcion_modulo as obtener_descripcion_sistemas,
    obtener_teoremas_clave as obtener_teoremas_sistemas
)

from modulos.modulo_vectores import (
    obtener_logo_modulo as obtener_logo_vectores,
    obtener_descripcion_modulo as obtener_descripcion_vectores,
    obtener_teoremas_clave as obtener_teoremas_vectores
)

from modulos.modulo_matrices import (
    obtener_logo_modulo as obtener_logo_matrices,
    obtener_descripcion_modulo as obtener_descripcion_matrices,
    obtener_teoremas_clave as obtener_teoremas_matrices
)

from modulos.modulo_determinantes import (
    obtener_logo_modulo as obtener_logo_determinantes,
    obtener_descripcion_modulo as obtener_descripcion_determinantes,
    obtener_teoremas_clave as obtener_teoremas_determinantes
)


class CalculadoraAlgebraLineal:
    """Administra la ventana principal y organiza los módulos de la calculadora."""

    def __init__(self, ventana):
        """Inicializa la ventana y construye la interfaz principal."""
        self.ventana = ventana
        self.ultimo_modulo = None

        self.configurar_ventana()
        self.crear_interfaz()

    def configurar_ventana(self):
        """Configura título, tamaño inicial y tamaño mínimo de la ventana."""
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

    def crear_interfaz(self):
        """Construye el encabezado y los cuatro módulos de la aplicación."""
        encabezado = ttk.Frame(
            self.ventana
        )

        encabezado.pack(
            fill="x",
            padx=15,
            pady=(8, 2)
        )

        titulo = ttk.Label(
            encabezado,
            text="Calculadora de Álgebra Lineal",
            font=(
                "Arial",
                18,
                "bold"
            )
        )

        titulo.pack()

        subtitulo = ttk.Label(
            encabezado,
            text=(
                "Proyecto Integrador - "
                "Herramientas de Álgebra Lineal"
            ),
            font=(
                "Arial",
                10
            )
        )

        subtitulo.pack(
            pady=(2, 4)
        )

        self.cuaderno_modulos = ttk.Notebook(
            self.ventana
        )

        self.cuaderno_modulos.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(2, 8)
        )

        self.crear_modulo_sistemas()
        self.crear_modulo_vectores()
        self.crear_modulo_matrices()
        self.crear_modulo_determinantes()

        self.cuaderno_modulos.bind(
            "<<NotebookTabChanged>>",
            self.cambiar_modulo
        )

        self.mostrar_logo_consola(
            1
        )

    def crear_modulo_sistemas(self):
        """Construye el Módulo 1 con teoremas y los Programas 1 y 2."""
        self.modulo_sistemas = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.modulo_sistemas,
            text="Módulo 1 - Sistemas"
        )

        self.crear_encabezado_modulo(
            self.modulo_sistemas,
            "Módulo 1 - Sistemas de Ecuaciones Lineales",
            obtener_descripcion_sistemas()
        )

        self.cuaderno_sistemas = ttk.Notebook(
            self.modulo_sistemas
        )

        self.cuaderno_sistemas.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5
        )

        pestana_teoremas = ttk.Frame(
            self.cuaderno_sistemas
        )

        self.cuaderno_sistemas.add(
            pestana_teoremas,
            text="0. Teoremas clave"
        )

        self.crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_sistemas()
        )

        self.programa_1 = Programa1Interfaz(
            self.cuaderno_sistemas
        )

        self.cuaderno_sistemas.add(
            self.programa_1,
            text="1. Programa 1"
        )

        self.programa_2 = Programa2Interfaz(
            self.cuaderno_sistemas
        )

        self.cuaderno_sistemas.add(
            self.programa_2,
            text="2. Programa 2"
        )

    def crear_modulo_vectores(self):
        """Construye el Módulo 2 con teoremas y los Programas 3 y 4."""
        self.modulo_vectores = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.modulo_vectores,
            text="Módulo 2 - Vectores"
        )

        self.crear_encabezado_modulo(
            self.modulo_vectores,
            (
                "Módulo 2 - "
                "Vectores e Independencia Lineal"
            ),
            obtener_descripcion_vectores()
        )

        self.cuaderno_vectores = ttk.Notebook(
            self.modulo_vectores
        )

        self.cuaderno_vectores.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5
        )

        pestana_teoremas = ttk.Frame(
            self.cuaderno_vectores
        )

        self.cuaderno_vectores.add(
            pestana_teoremas,
            text="0. Teoremas clave"
        )

        self.crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_vectores()
        )

        self.programa_3 = Programa3Interfaz(
            self.cuaderno_vectores
        )

        self.cuaderno_vectores.add(
            self.programa_3,
            text="3. Programa 3"
        )

        self.programa_4 = Programa4Interfaz(
            self.cuaderno_vectores
        )

        self.cuaderno_vectores.add(
            self.programa_4,
            text="4. Programa 4"
        )

    def crear_modulo_matrices(self):
        """Construye el Módulo 3 con las opciones 0 a 9 del Programa 5."""
        self.modulo_matrices = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.modulo_matrices,
            text="Módulo 3 - Matrices"
        )

        self.crear_encabezado_modulo(
            self.modulo_matrices,
            "Módulo 3 - Álgebra de Matrices",
            obtener_descripcion_matrices()
        )

        self.programa_5 = ModuloMatricesInterfaz(
            self.modulo_matrices
        )

        self.programa_5.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5
        )

        pestana_teoremas = ttk.Frame(
            self.programa_5.cuaderno
        )

        self.programa_5.cuaderno.insert(
            0,
            pestana_teoremas,
            text="0. Teoremas clave"
        )

        self.crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_matrices()
        )

    def crear_modulo_determinantes(self):
        """Construye el Módulo 4 con sus teoremas y herramientas existentes."""
        self.modulo_determinantes = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.modulo_determinantes,
            text="Módulo 4 - Determinantes"
        )

        self.crear_encabezado_modulo(
            self.modulo_determinantes,
            "Módulo 4 - Determinantes",
            obtener_descripcion_determinantes()
        )

        self.cuaderno_determinantes = ttk.Notebook(
            self.modulo_determinantes
        )

        self.cuaderno_determinantes.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5
        )

        pestana_teoremas = ttk.Frame(
            self.cuaderno_determinantes
        )

        self.cuaderno_determinantes.add(
            pestana_teoremas,
            text="0. Teoremas clave"
        )

        self.crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_determinantes()
        )

        self.herramientas_determinantes = (
            ModuloDeterminantesInterfaz(
                self.cuaderno_determinantes
            )
        )

        self.cuaderno_determinantes.add(
            self.herramientas_determinantes,
            text="1. Herramientas"
        )

    def crear_encabezado_modulo(
        self,
        contenedor,
        titulo,
        descripcion
    ):
        """Crea el título y la descripción mostrados al inicio de un módulo."""
        marco = ttk.Frame(
            contenedor
        )

        marco.pack(
            fill="x",
            padx=12,
            pady=(7, 2)
        )

        etiqueta_titulo = ttk.Label(
            marco,
            text=titulo,
            font=(
                "Arial",
                13,
                "bold"
            )
        )

        etiqueta_titulo.pack()

        etiqueta_descripcion = ttk.Label(
            marco,
            text=descripcion,
            font=(
                "Arial",
                9
            ),
            wraplength=1000,
            justify="center"
        )

        etiqueta_descripcion.pack(
            pady=(2, 3)
        )

    def crear_pestana_texto(
        self,
        contenedor,
        contenido
    ):
        """Crea un área de texto desplazable y de solo lectura."""
        contenedor.rowconfigure(
            0,
            weight=1
        )

        contenedor.columnconfigure(
            0,
            weight=1
        )

        texto = tk.Text(
            contenedor,
            wrap="word",
            font=(
                "Consolas",
                10
            ),
            padx=15,
            pady=10
        )

        texto.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scroll_vertical = ttk.Scrollbar(
            contenedor,
            orient="vertical",
            command=texto.yview
        )

        scroll_vertical.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scroll_horizontal = ttk.Scrollbar(
            contenedor,
            orient="horizontal",
            command=texto.xview
        )

        scroll_horizontal.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        texto.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set
        )

        texto.insert(
            tk.END,
            contenido
        )

        texto.configure(
            state="disabled"
        )

    def cambiar_modulo(self, evento=None):
        """Muestra en consola el logo del módulo seleccionado."""
        indice = self.cuaderno_modulos.index(
            self.cuaderno_modulos.select()
        )

        numero_modulo = (
            indice + 1
        )

        self.mostrar_logo_consola(
            numero_modulo
        )

    def mostrar_logo_consola(self, numero_modulo):
        """Imprime una sola vez el logo ASCII del módulo seleccionado."""
        if self.ultimo_modulo == numero_modulo:
            return

        self.ultimo_modulo = numero_modulo

        if numero_modulo == 1:
            logo = obtener_logo_sistemas()

        elif numero_modulo == 2:
            logo = obtener_logo_vectores()

        elif numero_modulo == 3:
            logo = obtener_logo_matrices()

        elif numero_modulo == 4:
            logo = obtener_logo_determinantes()

        else:
            return

        print(
            logo
        )


def main():
    """Inicia la ventana principal de la calculadora."""
    ventana = tk.Tk()

    CalculadoraAlgebraLineal(
        ventana
    )

    ventana.mainloop()


if __name__ == "__main__":
    main()