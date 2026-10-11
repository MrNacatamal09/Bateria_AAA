"""
Construye la ventana principal de la Calculadora de Álgebra Lineal.
Organiza los cuatro módulos y coloca los teoremas dentro de cada uno.
Tema de clase: integración de los Programas 1 al 5 por módulos.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk

from interfaz.programa_1_interfaz import Programa1Interfaz
from interfaz.programa_2_interfaz import Programa2Interfaz
from interfaz.programa_3_interfaz import Programa3Interfaz
from interfaz.programa_4_interfaz import Programa4Interfaz

from interfaz.modulo_matrices_interfaz import ModuloMatricesInterfaz
from interfaz.modulo_determinantes_interfaz import ModuloDeterminantesInterfaz

from interfaz.modulo_lu_interfaz import ModuloLUInterfaz

from modulos.modulo_sistemas import (
    obtener_logo_modulo as obtener_logo_sistemas,
    obtener_descripcion_modulo as obtener_descripcion_sistemas,
    obtener_teoremas_clave as obtener_teoremas_sistemas,
)

from modulos.modulo_vectores import (
    obtener_logo_modulo as obtener_logo_vectores,
    obtener_descripcion_modulo as obtener_descripcion_vectores,
    obtener_teoremas_clave as obtener_teoremas_vectores,
)

from modulos.modulo_matrices import (
    obtener_logo_modulo as obtener_logo_matrices,
    obtener_descripcion_modulo as obtener_descripcion_matrices,
    obtener_teoremas_clave as obtener_teoremas_matrices,
)

from modulos.modulo_determinantes import (
    obtener_logo_modulo as obtener_logo_determinantes,
    obtener_descripcion_modulo as obtener_descripcion_determinantes,
    obtener_teoremas_clave as obtener_teoremas_determinantes,
)


from modulos.modulo_lu import (
    obtener_logo_modulo as obtener_logo_lu,
)

class CalculadoraAlgebraLineal:
    """Organiza la interfaz principal de la calculadora por módulos."""

    def __init__(self, ventana):
        """Inicializa la ventana principal y construye sus módulos."""
        self.ventana = ventana
        self.ultimo_modulo = None

        self._configurar_ventana()
        self._crear_interfaz()

    def _configurar_ventana(self):
        """Configura título, tamaño inicial y tamaño mínimo."""
        self.ventana.title(
            "Calculadora de Álgebra Lineal"
        )
        self.ventana.geometry(
            "1200x800"
        )
        self.ventana.minsize(
            1000,
            700,
        )

    def _crear_interfaz(self):
        """Construye el encabezado y los cuatro módulos principales."""
        encabezado = ttk.Frame(
            self.ventana
        )
        encabezado.pack(
            fill="x",
            padx=15,
            pady=(8, 2),
        )

        ttk.Label(
            encabezado,
            text="Calculadora de Álgebra Lineal",
            font=("Arial", 18, "bold"),
        ).pack()

        ttk.Label(
            encabezado,
            text="Proyecto Integrador - Herramientas de Álgebra Lineal",
            font=("Arial", 10),
        ).pack(
            pady=(2, 4)
        )

        self.cuaderno_modulos = ttk.Notebook(
            self.ventana
        )
        self.cuaderno_modulos.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(2, 8),
        )

        self._crear_modulo_sistemas()
        self._crear_modulo_vectores()
        self._crear_modulo_matrices()
        self._crear_modulo_determinantes()
        self._crear_modulo_lu()

        self.cuaderno_modulos.bind(
            "<<NotebookTabChanged>>",
            self._cambiar_modulo,
        )

        self._mostrar_logo_consola(
            1
        )

    def _crear_modulo_sistemas(self):
        """Construye el Módulo I con teoremas y Programas 1 y 2."""
        self.modulo_sistemas = ttk.Frame(
            self.cuaderno_modulos
        )
        self.cuaderno_modulos.add(
            self.modulo_sistemas,
            text="Módulo 1 - Sistemas",
        )

        self._crear_encabezado_modulo(
            self.modulo_sistemas,
            "Módulo 1 - Sistemas de Ecuaciones Lineales",
            obtener_descripcion_sistemas(),
        )

        self.cuaderno_sistemas = ttk.Notebook(
            self.modulo_sistemas
        )
        self.cuaderno_sistemas.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5,
        )

        pestana_teoremas = ttk.Frame(
            self.cuaderno_sistemas
        )
        self.cuaderno_sistemas.add(
            pestana_teoremas,
            text="0. Teoremas clave",
        )
        self._crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_sistemas(),
        )

        self.programa_1 = Programa1Interfaz(
            self.cuaderno_sistemas
        )
        self.cuaderno_sistemas.add(
            self.programa_1,
            text="1. Programa 1",
        )

        self.programa_2 = Programa2Interfaz(
            self.cuaderno_sistemas
        )
        self.cuaderno_sistemas.add(
            self.programa_2,
            text="2. Programa 2",
        )

    def _crear_modulo_vectores(self):
        """Construye el Módulo II con teoremas y Programas 3 y 4."""
        self.modulo_vectores = ttk.Frame(
            self.cuaderno_modulos
        )
        self.cuaderno_modulos.add(
            self.modulo_vectores,
            text="Módulo 2 - Vectores",
        )

        self._crear_encabezado_modulo(
            self.modulo_vectores,
            "Módulo 2 - Vectores e Independencia Lineal",
            obtener_descripcion_vectores(),
        )

        self.cuaderno_vectores = ttk.Notebook(
            self.modulo_vectores
        )
        self.cuaderno_vectores.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5,
        )

        pestana_teoremas = ttk.Frame(
            self.cuaderno_vectores
        )
        self.cuaderno_vectores.add(
            pestana_teoremas,
            text="0. Teoremas clave",
        )
        self._crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_vectores(),
        )

        self.programa_3 = Programa3Interfaz(
            self.cuaderno_vectores
        )
        self.cuaderno_vectores.add(
            self.programa_3,
            text="3. Programa 3",
        )

        self.programa_4 = Programa4Interfaz(
            self.cuaderno_vectores
        )
        self.cuaderno_vectores.add(
            self.programa_4,
            text="4. Programa 4",
        )

    def _crear_modulo_matrices(self):
        """Construye el Módulo III con teoremas, opciones 1 a 5 y propiedades."""
        self.modulo_matrices = ttk.Frame(
            self.cuaderno_modulos
        )
        self.cuaderno_modulos.add(
            self.modulo_matrices,
            text="Módulo 3 - Matrices",
        )

        self.modulo_matrices_interfaz = ModuloMatricesInterfaz(
            self.modulo_matrices
        )
        self.modulo_matrices_interfaz.pack(
            fill="both",
            expand=True,
        )

        pestana_teoremas = ttk.Frame(
            self.modulo_matrices_interfaz.cuaderno
        )
        self.modulo_matrices_interfaz.cuaderno.insert(
            0,
            pestana_teoremas,
            text="0. Teoremas clave",
        )
        self._crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_matrices(),
        )

    def _crear_modulo_determinantes(self):
        """Construye el Módulo IV con teoremas y las opciones 6 a 9."""
        self.modulo_determinantes = ttk.Frame(
            self.cuaderno_modulos
        )
        self.cuaderno_modulos.add(
            self.modulo_determinantes,
            text="Módulo 4 - Determinantes",
        )

        self.modulo_determinantes_interfaz = ModuloDeterminantesInterfaz(
            self.modulo_determinantes
        )
        self.modulo_determinantes_interfaz.pack(
            fill="both",
            expand=True,
        )

        pestana_teoremas = ttk.Frame(
            self.modulo_determinantes_interfaz.cuaderno
        )
        self.modulo_determinantes_interfaz.cuaderno.insert(
            0,
            pestana_teoremas,
            text="0. Teoremas clave",
        )
        self._crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_determinantes(),
        )

    def _crear_modulo_lu(self):
        """Construye el Módulo V de Factorización LU."""
        self.modulo_lu = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.modulo_lu,
            text="Módulo 5 - Factorización LU",
        )

        self.modulo_lu_interfaz = ModuloLUInterfaz(
            self.modulo_lu
        )

        self.modulo_lu_interfaz.pack(
            fill="both",
            expand=True,
        )

    def _crear_encabezado_modulo(
        self,
        contenedor,
        titulo,
        descripcion,
    ):
        """Crea el título y la descripción de un módulo tradicional."""
        marco = ttk.Frame(
            contenedor
        )
        marco.pack(
            fill="x",
            padx=12,
            pady=(7, 2),
        )

        ttk.Label(
            marco,
            text=titulo,
            font=("Arial", 13, "bold"),
        ).pack()

        ttk.Label(
            marco,
            text=descripcion,
            font=("Arial", 9),
            wraplength=1000,
            justify="center",
        ).pack(
            pady=(2, 3)
        )

    def _crear_pestana_texto(self, contenedor, contenido):
        """Muestra texto teórico dentro de una pestaña desplazable."""
        contenedor.rowconfigure(
            0,
            weight=1,
        )
        contenedor.columnconfigure(
            0,
            weight=1,
        )

        texto = tk.Text(
            contenedor,
            wrap="word",
            font=("Consolas", 10),
            padx=15,
            pady=10,
        )
        texto.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        scroll_vertical = ttk.Scrollbar(
            contenedor,
            orient="vertical",
            command=texto.yview,
        )
        scroll_vertical.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        texto.configure(
            yscrollcommand=scroll_vertical.set
        )
        texto.insert(
            tk.END,
            contenido,
        )
        texto.configure(
            state="disabled"
        )

    def _cambiar_modulo(self, evento=None):
        """Muestra el logotipo del módulo cuando cambia la pestaña principal."""
        indice = self.cuaderno_modulos.index(
            self.cuaderno_modulos.select()
        )
        self._mostrar_logo_consola(
            indice + 1
        )

    def _mostrar_logo_consola(self, numero_modulo):
        """Imprime una sola vez el logotipo del módulo seleccionado."""
        if self.ultimo_modulo == numero_modulo:
            return

        self.ultimo_modulo = numero_modulo

        logos = {
            1: obtener_logo_sistemas,
            2: obtener_logo_vectores,
            3: obtener_logo_matrices,
            4: obtener_logo_determinantes,
            5: obtener_logo_lu,
        }

        obtener_logo = logos.get(
            numero_modulo
        )

        if obtener_logo is not None:
            print(
                obtener_logo()
            )


def main():
    """Inicia la Calculadora de Álgebra Lineal."""
    ventana = tk.Tk()

    CalculadoraAlgebraLineal(
        ventana
    )

    ventana.mainloop()


if __name__ == "__main__":
    main()
