"""
Construye la ventana principal de la Calculadora de Álgebra Lineal.
Organiza seis módulos numerados y una sección general de Propiedades.
Tema de clase: integración de los Programas 1 al 7 por módulos.
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
from interfaz.modulo_propiedades_interfaz import ModuloPropiedadesInterfaz
from interfaz.modulo_numerico_interfaz import ModuloNumericoInterfaz

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

from modulos.modulo_propiedades import (
    obtener_logo_modulo as obtener_logo_propiedades,
)
from modulos.modulo_numerico import (
    obtener_logo_modulo as obtener_logo_numerico,
)
from utilidades.tema_interfaz import COLORES, aplicar_tema, crear_marca, crear_acento
from utilidades.buscador_temas import BuscadorTemas


class CalculadoraAlgebraLineal:
    """Organiza la interfaz principal de la calculadora por secciones."""

    def __init__(self, ventana):
        """Inicializa la ventana principal y construye sus secciones."""
        self.ventana = ventana
        self.ultimo_modulo = None

        aplicar_tema(self.ventana)
        self._configurar_ventana()
        self._crear_interfaz()

    def _configurar_ventana(self):
        """Configura título, tamaño inicial y tamaño mínimo."""
        self.ventana.title(
            "Batería AAA"
        )

        self.ventana.minsize(
            1000,
            700,
        )
        self.ventana.geometry("1200x800")
        try:
            self.ventana.state("zoomed")
        except tk.TclError:
            try:
                self.ventana.attributes("-zoomed", True)
            except tk.TclError:
                pass

    def _crear_interfaz(self):
        """Construye la barra lateral y el área de cálculo."""
        crear_acento(self.ventana).pack(fill="x")

        disposicion = ttk.Frame(
            self.ventana,
            style="Cabecera.TFrame",
        )
        disposicion.pack(
            fill="both",
            expand=True,
        )

        self.barra_lateral = ttk.Frame(
            disposicion,
            style="Lateral.TFrame",
            width=248,
        )
        self.barra_lateral.pack(side="left", fill="y")
        self.barra_lateral.pack_propagate(False)
        self.barra_visible = True

        marca_lateral = ttk.Frame(
            self.barra_lateral,
            style="Lateral.TFrame",
        )
        marca_lateral.pack(fill="x", padx=14, pady=(18, 15))
        crear_marca(
            marca_lateral,
            fondo=COLORES["lateral"],
        ).pack(side="left", padx=(0, 10))

        textos_marca = ttk.Frame(marca_lateral, style="Lateral.TFrame")
        textos_marca.pack(side="left", fill="x", expand=True)
        ttk.Label(
            textos_marca,
            text="BATERÍA AAA",
            style="MarcaLateral.TLabel",
        ).pack(anchor="w")
        ttk.Label(
            textos_marca,
            text="Calculadora",
            style="Lateral.TLabel",
        ).pack(anchor="w", pady=(2, 0))

        marco_busqueda = ttk.Frame(
            self.barra_lateral,
            style="Lateral.TFrame",
        )
        marco_busqueda.pack(fill="x", padx=14, pady=(0, 15))

        ttk.Label(
            self.barra_lateral,
            text="MÓDULOS",
            style="SeccionLateral.TLabel",
        ).pack(anchor="w", padx=22, pady=(2, 8))
        self.marco_navegacion = ttk.Frame(
            self.barra_lateral,
            style="Lateral.TFrame",
        )
        self.marco_navegacion.pack(fill="x", padx=9)
        tk.Frame(
            self.barra_lateral,
            height=1,
            background=COLORES["borde"],
        ).pack(fill="x", padx=18, pady=(15, 0))

        self.area_principal = ttk.Frame(
            disposicion,
            style="Cabecera.TFrame",
        )
        self.area_principal.pack(
            side="left",
            fill="both",
            expand=True,
        )

        cabecera = ttk.Frame(
            self.area_principal,
            style="Cabecera.TFrame",
        )
        cabecera.pack(fill="x", padx=16, pady=(11, 9))
        self.boton_panel = ttk.Button(
            cabecera,
            text="☰  Ocultar panel",
            style="Panel.TButton",
            command=self._alternar_barra,
        )
        self.boton_panel.pack(side="left")
        self.ruta_modulo = tk.StringVar(value="Calculadora / Módulo 1 · Sistemas")
        ttk.Label(
            cabecera,
            textvariable=self.ruta_modulo,
            style="Ruta.TLabel",
        ).pack(side="left", padx=14)
        tk.Frame(
            self.area_principal,
            height=1,
            background=COLORES["borde"],
        ).pack(fill="x")

        self.cuaderno_modulos = ttk.Notebook(
            self.area_principal,
            style="Explorador.TNotebook",
        )
        self.cuaderno_modulos.pack(
            fill="both",
            expand=True,
            padx=(8, 10),
            pady=(7, 8),
        )

        self._crear_modulo_sistemas()
        self._crear_modulo_vectores()
        self._crear_modulo_matrices()
        self._crear_modulo_determinantes()
        self._crear_modulo_lu()
        self._crear_modulo_numerico()
        self._crear_propiedades()
        self._crear_navegacion_lateral()
        self.buscador_temas = BuscadorTemas(self, marco_busqueda)

        self.cuaderno_modulos.bind(
            "<<NotebookTabChanged>>",
            self._cambiar_modulo,
        )
        self.ventana.bind("<Control-f>", self._enfocar_busqueda)
        self._actualizar_navegacion(0)
        self._mostrar_logo_consola(1)

    def _crear_navegacion_lateral(self):
        """Presenta los seis módulos y la sección general."""
        nombres = (
            "01   ∑  Sistemas",
            "02   ↗  Vectores",
            "03   ▦  Matrices",
            "04   Δ  Determinantes",
            "05   ▧  Factorización LU",
            "06   ƒ  Métodos numéricos",
            "✓  Propiedades",
        )
        self.botones_modulos = []
        self.indicadores_modulos = []
        for indice, nombre in enumerate(nombres):
            fila = tk.Frame(
                self.marco_navegacion,
                background=COLORES["lateral"],
            )
            fila.pack(fill="x", pady=2)
            indicador = tk.Frame(
                fila,
                width=3,
                background=COLORES["lateral"],
            )
            indicador.pack(side="left", fill="y")
            boton = ttk.Button(
                fila,
                text=nombre,
                style="Navegacion.TButton",
                command=lambda numero=indice: self.cuaderno_modulos.select(numero),
            )
            boton.pack(side="left", fill="x", expand=True)
            self.indicadores_modulos.append(indicador)
            self.botones_modulos.append(boton)

    def _actualizar_navegacion(self, indice):
        """Sincroniza la barra lateral con el módulo seleccionado."""
        nombres = (
            "Sistemas", "Vectores", "Matrices", "Determinantes",
            "Factorización LU", "Métodos numéricos", "Propiedades",
        )
        ruta = (f"Calculadora / Módulo {indice + 1} · {nombres[indice]}"
                if indice < 6 else "Calculadora / Propiedades")
        self.ruta_modulo.set(ruta)
        for numero, (boton, indicador) in enumerate(
            zip(self.botones_modulos, self.indicadores_modulos)
        ):
            activo = numero == indice
            boton.configure(
                style="NavegacionActiva.TButton" if activo
                else "Navegacion.TButton"
            )
            indicador.configure(
                background=COLORES["magenta"] if activo
                else COLORES["lateral"]
            )

    def _alternar_barra(self):
        """Oculta o muestra el panel sin recrear las páginas de cálculo."""
        if self.barra_visible:
            self.buscador_temas.limpiar()
            self.barra_lateral.pack_forget()
            self.boton_panel.configure(text="☰  Mostrar panel")
        else:
            self.barra_lateral.pack(
                side="left",
                fill="y",
                before=self.area_principal,
            )
            self.boton_panel.configure(text="☰  Ocultar panel")
        self.barra_visible = not self.barra_visible

    def _enfocar_busqueda(self, _evento=None):
        """Abre el panel y enfoca el buscador con Ctrl+F."""
        if not self.barra_visible:
            self._alternar_barra()
        self.buscador_temas.entrada.focus_set()
        return "break"

    def _crear_modulo_sistemas(self):
        """Construye el Módulo I con teoremas y Programas 1 y 2."""
        self.modulo_sistemas = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.modulo_sistemas,
            text="∑  Sistemas",
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
            text="↗  Vectores",
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
        """Construye el Módulo III con operaciones y propiedades de matrices."""
        self.modulo_matrices = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.modulo_matrices,
            text="▦  Matrices",
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
            text="Δ  Determinantes",
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
        """Construye el Módulo V de Factorización LU y solución Ax=b."""
        self.modulo_lu = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.modulo_lu,
            text="▧  LU",
        )

        self.modulo_lu_interfaz = ModuloLUInterfaz(
            self.modulo_lu
        )

        self.modulo_lu_interfaz.pack(
            fill="both",
            expand=True,
        )

    def _crear_propiedades(self):
        """Construye la sección general de Propiedades."""
        self.propiedades = ttk.Frame(
            self.cuaderno_modulos
        )

        self.cuaderno_modulos.add(
            self.propiedades,
            text="✓  Propiedades",
        )

        self.propiedades_interfaz = ModuloPropiedadesInterfaz(
            self.propiedades
        )

        self.propiedades_interfaz.pack(
            fill="both",
            expand=True,
        )

    def _crear_modulo_numerico(self):
        """Integra las cuatro opciones del Programa 7 en el Módulo 6."""
        self.modulo_numerico = ttk.Frame(self.cuaderno_modulos)
        self.cuaderno_modulos.add(
            self.modulo_numerico,
            text="ƒ  Métodos Numéricos",
        )
        self.modulo_numerico_interfaz = ModuloNumericoInterfaz(self.modulo_numerico)
        self.modulo_numerico_interfaz.pack(fill="both", expand=True)

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
            font=(
                "Arial",
                13,
                "bold",
            ),
        ).pack()

        ttk.Label(
            marco,
            text=descripcion,
            font=(
                "Arial",
                9,
            ),
            wraplength=1000,
            justify="center",
        ).pack(
            pady=(2, 3)
        )

    def _crear_pestana_texto(
        self,
        contenedor,
        contenido,
    ):
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
            font=(
                "Consolas",
                10,
            ),
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

    def _cambiar_modulo(
        self,
        evento=None,
    ):
        """Muestra el logotipo correspondiente al cambiar de sección."""
        indice = self.cuaderno_modulos.index(
            self.cuaderno_modulos.select()
        )

        self._actualizar_navegacion(indice)
        self._mostrar_logo_consola(
            indice + 1
        )

    def _mostrar_logo_consola(
        self,
        numero_modulo,
    ):
        """Imprime una sola vez el logotipo de la sección seleccionada."""
        if self.ultimo_modulo == numero_modulo:
            return

        self.ultimo_modulo = numero_modulo

        logos = {
            1: obtener_logo_sistemas,
            2: obtener_logo_vectores,
            3: obtener_logo_matrices,
            4: obtener_logo_determinantes,
            5: obtener_logo_lu,
            6: obtener_logo_numerico,
            7: obtener_logo_propiedades,
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
