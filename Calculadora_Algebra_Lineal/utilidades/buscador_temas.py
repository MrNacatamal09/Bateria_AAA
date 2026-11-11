"""Búsqueda y navegación entre los temas de la calculadora."""

import re
import tkinter as tk
import tkinter.font as tkfont
import unicodedata
from dataclasses import dataclass
from tkinter import ttk

from utilidades.tema_interfaz import COLORES


@dataclass(frozen=True)
class _Tema:
    titulo: str
    ruta: tuple
    palabras: str


class BuscadorTemas:
    """Filtra temas y selecciona sus pestañas sin alterar el orden."""

    _MODULOS = (
        ("Sistemas", "cuaderno_sistemas"),
        ("Vectores", "cuaderno_vectores"),
        ("Matrices", "modulo_matrices_interfaz"),
        ("Determinantes", "modulo_determinantes_interfaz"),
        ("LU", "modulo_lu_interfaz"),
        ("Métodos numéricos", "modulo_numerico_interfaz"),
        ("Propiedades", "propiedades_interfaz"),
    )

    _ALIAS_MODULOS = (
        "módulo 1 ecuaciones lineales",
        "módulo 2 independencia lineal",
        "módulo 3 operaciones matriciales",
        "módulo 4 regla de cramer inversa",
        "módulo 5 factorización",
        "módulo 6 programa 7",
        "propiedades consolidadas",
    )

    _ALIAS = {
        (0, 1): "gauss gauss jordan eliminación ecuaciones lineales",
        (0, 2): "forma escalonada reducida rango solución sistema",
        (1, 1): "operaciones vectoriales matriciales combinación lineal ax b",
        (1, 2): "independencia dependencia lineal vectores",
        (2, 3): "producto por escalar multiplicación escalar rA",
        (2, 4): "multiplicación producto matrices AB regla fila columna",
        (2, 5): "transpuesta transposición AT",
        (3, 1): "cofactores sarrus triangular método determinante",
        (3, 2): "regla de cramer sistemas determinantes",
        (3, 3): "gauss jordan matriz inversa",
        (3, 4): "matriz inversa adjunta cofactores",
        (3, 5): "propiedades del determinante",
        (3, 6): "análisis integrado determinante inversa",
        (4, 1): "factorización descomposición LU matriz",
        (4, 2): "sistema ecuaciones resolver Ax b LU",
        (5, 0): "raíz raíces ceros función intervalo bisección",
        (5, 1): "gráfica graficar funciones curva plano cartesiano",
        (5, 2): "notación base 10 base 2 decimal binario posicional",
        (5, 3): "error absoluto relativo porcentual redondeo truncamiento precisión",
        (6, 1): "verificar propiedades consolidadas matrices",
    }

    def __init__(self, aplicacion, contenedor):
        self.aplicacion = aplicacion
        self.consulta = tk.StringVar(master=contenedor)
        self._temas = self._crear_catalogo()
        self._coincidencias = []
        self._fuente_lista = tkfont.Font(root=contenedor, family="Segoe UI", size=10)
        self._ayuda_lista = None
        self._indice_ayuda = None

        self.caja = ttk.Frame(contenedor, style="Lateral.TFrame")
        self.caja.pack(fill="x")
        ttk.Label(
            self.caja,
            text="Buscar tema",
            style="Lateral.TLabel",
        ).pack(anchor="w", pady=(0, 6))
        self.entrada = ttk.Entry(
            self.caja,
            textvariable=self.consulta,
        )
        self.entrada.pack(fill="x")

        self.lista = tk.Listbox(
            self.caja,
            height=5,
            activestyle="none",
            exportselection=False,
            background=COLORES["superficie"],
            foreground=COLORES["texto"],
            selectbackground=COLORES["hover"],
            selectforeground=COLORES["texto"],
            highlightbackground=COLORES["borde"],
            highlightcolor=COLORES["violeta"],
            highlightthickness=1,
            borderwidth=0,
            relief="flat",
            font=self._fuente_lista,
        )

        self.consulta.trace_add("write", self._actualizar)
        self.entrada.bind("<Return>", self._abrir_primero)
        self.entrada.bind("<Down>", self._enfocar_lista)
        self.entrada.bind("<Escape>", self._limpiar)
        self.lista.bind("<Return>", self._abrir_seleccion)
        self.lista.bind("<Double-Button-1>", self._abrir_seleccion)
        self.lista.bind("<Escape>", self._limpiar)
        self.lista.bind("<Motion>", self._mostrar_titulo)
        self.lista.bind("<Leave>", self._ocultar_titulo)

    @staticmethod
    def _etiqueta_resultado(tema):
        partes = tema.titulo.split(" · ")
        if len(partes) == 1:
            return tema.titulo
        if len(partes) == 3 and partes[1].startswith("Programa "):
            return f"P{partes[1].split()[-1]} · {partes[2]}"
        abreviaturas = {"Métodos numéricos": "Numéricos"}
        return f"{abreviaturas.get(partes[0], partes[0])} · {partes[-1]}"

    @staticmethod
    def _normalizar(texto):
        texto = unicodedata.normalize("NFKD", texto.casefold())
        texto = "".join(caracter for caracter in texto
                        if not unicodedata.combining(caracter))
        return " ".join(re.findall(r"[a-z0-9]+", texto))

    @staticmethod
    def _titulo_pestana(cuaderno, indice):
        titulo = cuaderno.tab(indice, "text")
        return re.sub(r"^\d+\.\s*", "", titulo).strip()

    def _crear_catalogo(self):
        principal = self.aplicacion.cuaderno_modulos
        temas = []
        for indice_modulo, (nombre, atributo) in enumerate(self._MODULOS):
            if indice_modulo >= principal.index("end"):
                break
            ruta_modulo = ((principal, indice_modulo),)
            temas.append(_Tema(
                nombre,
                ruta_modulo,
                self._normalizar(
                    f"{nombre} {self._ALIAS_MODULOS[indice_modulo]}"
                ),
            ))

            objeto = getattr(self.aplicacion, atributo)
            cuaderno = getattr(objeto, "cuaderno", objeto)
            for indice_tema in range(cuaderno.index("end")):
                titulo = self._titulo_pestana(cuaderno, indice_tema)
                etiqueta = f"{nombre} · {titulo}"
                alias = self._ALIAS.get((indice_modulo, indice_tema), "")
                if titulo == "Teoremas clave":
                    alias += f" teoría teoremas {nombre}"
                temas.append(_Tema(
                    etiqueta,
                    ruta_modulo + ((cuaderno, indice_tema),),
                    self._normalizar(f"{etiqueta} {alias}"),
                ))

        operaciones = self.aplicacion.programa_3.cuaderno_operaciones
        vectores = self.aplicacion.cuaderno_vectores
        for indice in range(operaciones.index("end")):
            titulo = self._titulo_pestana(operaciones, indice)
            etiqueta = f"Vectores · Programa 3 · {titulo}"
            temas.append(_Tema(
                etiqueta,
                ((principal, 1), (vectores, 1), (operaciones, indice)),
                self._normalizar(etiqueta),
            ))

        return temas

    def _buscar(self, consulta):
        consulta = self._normalizar(consulta)
        if not consulta:
            return []
        palabras = consulta.split()
        candidatos = [
            tema for tema in self._temas
            if all(palabra in tema.palabras for palabra in palabras)
        ]

        def prioridad(tema):
            titulo = self._normalizar(tema.titulo)
            if titulo == consulta:
                return 0
            if titulo.endswith(" " + consulta):
                return 1
            if consulta in titulo:
                return 2
            if consulta in tema.palabras:
                return 3
            return 4

        return sorted(candidatos, key=prioridad)[:8]

    def _actualizar(self, *_):
        self._ocultar_titulo()
        self._coincidencias = self._buscar(self.consulta.get())
        self.lista.delete(0, tk.END)
        if not self.consulta.get().strip():
            self.lista.pack_forget()
            return

        if self._coincidencias:
            for tema in self._coincidencias:
                etiqueta = self._etiqueta_resultado(tema)
                while len(etiqueta) > 1 and self._fuente_lista.measure(etiqueta) > 210:
                    etiqueta = etiqueta[:-2] + "…" if etiqueta.endswith("…") else etiqueta[:-1] + "…"
                self.lista.insert(tk.END, etiqueta)
            self.lista.configure(height=min(6, len(self._coincidencias)))
        else:
            self.lista.insert(tk.END, "Sin coincidencias")
            self.lista.configure(height=1)

        if not self.lista.winfo_manager():
            self.lista.pack(fill="x", pady=(4, 0))

    def _mostrar_titulo(self, evento):
        indice = self.lista.nearest(evento.y)
        if indice >= len(self._coincidencias):
            self._ocultar_titulo()
            return
        tema = self._coincidencias[indice]
        if self.lista.get(indice) == self._etiqueta_resultado(tema):
            self._ocultar_titulo()
            return
        if indice == self._indice_ayuda:
            return
        self._ocultar_titulo()
        self._indice_ayuda = indice
        self._ayuda_lista = tk.Toplevel(self.lista)
        self._ayuda_lista.overrideredirect(True)
        self._ayuda_lista.configure(background=COLORES["borde"])
        ttk.Label(
            self._ayuda_lista, text=tema.titulo,
            background=COLORES["superficie"],
            foreground=COLORES["texto"], wraplength=320,
            padding=(8, 5),
        ).pack(padx=1, pady=1)
        self._ayuda_lista.geometry(f"+{evento.x_root + 12}+{evento.y_root + 12}")

    def _ocultar_titulo(self, _evento=None):
        if self._ayuda_lista is not None:
            self._ayuda_lista.destroy()
            self._ayuda_lista = None
        self._indice_ayuda = None

    def _navegar(self, tema):
        for cuaderno, indice in tema.ruta:
            cuaderno.select(indice)
        self.consulta.set("")
        self.entrada.focus_set()

    def _abrir_primero(self, _evento=None):
        if self._coincidencias:
            self._navegar(self._coincidencias[0])
        return "break"

    def _abrir_seleccion(self, _evento=None):
        seleccion = self.lista.curselection()
        if seleccion and seleccion[0] < len(self._coincidencias):
            self._navegar(self._coincidencias[seleccion[0]])
        return "break"

    def _enfocar_lista(self, _evento=None):
        if self._coincidencias:
            self.lista.selection_clear(0, tk.END)
            self.lista.selection_set(0)
            self.lista.focus_set()
        return "break"

    def _limpiar(self, _evento=None):
        self.limpiar()
        self.entrada.focus_set()
        return "break"

    def limpiar(self):
        """Oculta los resultados cuando se cierra el panel lateral."""
        self.consulta.set("")
