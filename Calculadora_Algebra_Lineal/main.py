import tkinter as tk
from tkinter import ttk


# ==========================================================
# INTERFACES DE LOS PROGRAMAS
# ==========================================================

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


# ==========================================================
# INTERFACES DE LOS NUEVOS MÓDULOS
# ==========================================================

from interfaz.modulo_matrices_interfaz import (
    ModuloMatricesInterfaz
)

from interfaz.modulo_determinantes_interfaz import (
    ModuloDeterminantesInterfaz
)


# ==========================================================
# INFORMACIÓN DE LOS MÓDULOS
# ==========================================================

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


# ==========================================================
# CALCULADORA PRINCIPAL
# ==========================================================

class CalculadoraAlgebraLineal:

    def __init__(
        self,
        ventana
    ):

        self.ventana = ventana

        self.ultimo_modulo = None

        self.configurar_ventana()
        self.crear_interfaz()

    # ======================================================
    # CONFIGURACIÓN DE VENTANA
    # ======================================================

    def configurar_ventana(
        self
    ):

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

    # ======================================================
    # INTERFAZ GENERAL
    # ======================================================

    def crear_interfaz(
        self
    ):

        # ==================================================
        # ENCABEZADO
        # ==================================================

        encabezado = ttk.Frame(
            self.ventana
        )

        encabezado.pack(
            fill="x",
            padx=15,
            pady=(
                8,
                2
            )
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
            pady=(
                2,
                4
            )
        )

        # ==================================================
        # NOTEBOOK PRINCIPAL
        # ==================================================

        self.cuaderno_modulos = ttk.Notebook(
            self.ventana
        )

        self.cuaderno_modulos.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(
                2,
                8
            )
        )

        # ==================================================
        # CREAMOS LOS CUATRO MÓDULOS
        # ==================================================

        self.crear_modulo_sistemas()
        self.crear_modulo_vectores()
        self.crear_modulo_matrices()
        self.crear_modulo_determinantes()

        # Detectamos cambio de módulo.
        self.cuaderno_modulos.bind(
            "<<NotebookTabChanged>>",
            self.cambiar_modulo
        )

        # Logo inicial.
        self.mostrar_logo_consola(
            1
        )

    # ======================================================
    # MÓDULO 1
    # SISTEMAS DE ECUACIONES
    # ======================================================

    def crear_modulo_sistemas(
        self
    ):

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

        # ==================================================
        # 0. TEOREMAS
        # ==================================================

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

        # ==================================================
        # PROGRAMA 1
        # ==================================================

        self.programa_1 = Programa1Interfaz(
            self.cuaderno_sistemas
        )

        self.cuaderno_sistemas.add(
            self.programa_1,
            text="1. Programa 1"
        )

        # ==================================================
        # PROGRAMA 2
        # ==================================================

        self.programa_2 = Programa2Interfaz(
            self.cuaderno_sistemas
        )

        self.cuaderno_sistemas.add(
            self.programa_2,
            text="2. Programa 2"
        )

    # ======================================================
    # MÓDULO 2
    # VECTORES E INDEPENDENCIA LINEAL
    # ======================================================

    def crear_modulo_vectores(
        self
    ):

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

        # ==================================================
        # 0. TEOREMAS
        # ==================================================

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

        # ==================================================
        # PROGRAMA 3
        # ==================================================

        self.programa_3 = Programa3Interfaz(
            self.cuaderno_vectores
        )

        self.cuaderno_vectores.add(
            self.programa_3,
            text="3. Programa 3"
        )

        # ==================================================
        # PROGRAMA 4
        # ==================================================

        self.programa_4 = Programa4Interfaz(
            self.cuaderno_vectores
        )

        self.cuaderno_vectores.add(
            self.programa_4,
            text="4. Programa 4"
        )

    # ======================================================
    # MÓDULO 3
    # ÁLGEBRA DE MATRICES
    # ======================================================

    def crear_modulo_matrices(
        self
    ):

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

        self.cuaderno_matrices = ttk.Notebook(
            self.modulo_matrices
        )

        self.cuaderno_matrices.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5
        )

        # ==================================================
        # 0. TEOREMAS
        # ==================================================

        pestana_teoremas = ttk.Frame(
            self.cuaderno_matrices
        )

        self.cuaderno_matrices.add(
            pestana_teoremas,
            text="0. Teoremas clave"
        )

        self.crear_pestana_texto(
            pestana_teoremas,
            obtener_teoremas_matrices()
        )

        # ==================================================
        # HERRAMIENTAS DEL MÓDULO 3
        # ==================================================

        self.herramientas_matrices = (
            ModuloMatricesInterfaz(
                self.cuaderno_matrices
            )
        )

        self.cuaderno_matrices.add(
            self.herramientas_matrices,
            text="1. Herramientas"
        )

    # ======================================================
    # MÓDULO 4
    # DETERMINANTES
    # ======================================================

    def crear_modulo_determinantes(
        self
    ):

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

        # ==================================================
        # 0. TEOREMAS
        # ==================================================

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

        # ==================================================
        # HERRAMIENTAS DEL MÓDULO 4
        # ==================================================

        self.herramientas_determinantes = (
            ModuloDeterminantesInterfaz(
                self.cuaderno_determinantes
            )
        )

        self.cuaderno_determinantes.add(
            self.herramientas_determinantes,
            text="1. Herramientas"
        )

    # ======================================================
    # ENCABEZADO DE MÓDULO
    # ======================================================

    def crear_encabezado_modulo(
        self,
        contenedor,
        titulo,
        descripcion
    ):

        marco = ttk.Frame(
            contenedor
        )

        marco.pack(
            fill="x",
            padx=12,
            pady=(
                7,
                2
            )
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
            pady=(
                2,
                3
            )
        )

    # ======================================================
    # PESTAÑA DE TEXTO
    # ======================================================

    def crear_pestana_texto(
        self,
        contenedor,
        contenido
    ):

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

    # ======================================================
    # CAMBIO DE MÓDULO
    # ======================================================

    def cambiar_modulo(
        self,
        evento=None
    ):

        indice = self.cuaderno_modulos.index(
            self.cuaderno_modulos.select()
        )

        numero_modulo = (
            indice + 1
        )

        self.mostrar_logo_consola(
            numero_modulo
        )

    # ======================================================
    # LOGO ASCII EN CONSOLA
    # ======================================================

    def mostrar_logo_consola(
        self,
        numero_modulo
    ):

        if (
            self.ultimo_modulo
            == numero_modulo
        ):

            return

        self.ultimo_modulo = (
            numero_modulo
        )

        if numero_modulo == 1:

            logo = (
                obtener_logo_sistemas()
            )

        elif numero_modulo == 2:

            logo = (
                obtener_logo_vectores()
            )

        elif numero_modulo == 3:

            logo = (
                obtener_logo_matrices()
            )

        elif numero_modulo == 4:

            logo = (
                obtener_logo_determinantes()
            )

        else:

            return

        print(
            logo
        )


# ==========================================================
# PUNTO DE ENTRADA
# ==========================================================

def main():

    ventana = tk.Tk()

    CalculadoraAlgebraLineal(
        ventana
    )

    ventana.mainloop()


if __name__ == "__main__":

    main()