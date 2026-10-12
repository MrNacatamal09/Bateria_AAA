"""
Construye la interfaz gráfica del módulo de Factorización LU.
Permite resolver LU, Ax=b y consultar propiedades mediante filtros reutilizables.
Tema de clase: factorización LU, propiedades y encadenamiento de resultados.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from controladores.modulo_lu_controller import (
    procesar_factorizacion_lu,
    procesar_sistema_lu,
    procesar_propiedades_consolidadas,
    procesar_categorias_propiedades,
    procesar_filtro_propiedades,
)

from utilidades.formato_lu import (
    formatear_factorizacion_lu,
    formatear_sustitucion_adelante,
    formatear_sustitucion_atras,
    formatear_verificaciones_lu,
)

from utilidades.formato_propiedades_lu import (
    formatear_propiedades_consolidadas,
)

from modulos.modulo_lu import (
    obtener_teoremas_clave,
)


class EntradaMatrizLU(ttk.LabelFrame):
    """Gestiona una matriz editable de dimensiones configurables."""

    def __init__(
        self,
        contenedor,
        titulo,
        filas=3,
        columnas=3,
        cuadrada=False,
    ):
        """Inicializa la entrada de matriz y crea sus controles."""
        super().__init__(
            contenedor,
            text=titulo,
            padding=5,
        )

        self.titulo = titulo
        self.cuadrada = cuadrada

        self.variable_filas = tk.StringVar(
            value=str(filas)
        )

        self.variable_columnas = tk.StringVar(
            value=str(columnas)
        )

        self.entradas = []

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye controles de dimensiones y el área desplazable."""
        controles = ttk.Frame(
            self
        )

        controles.pack(
            fill="x",
            pady=(0, 5),
        )

        if self.cuadrada:
            ttk.Label(
                controles,
                text="Orden n:",
            ).pack(
                side="left",
                padx=3,
            )

            ttk.Entry(
                controles,
                textvariable=self.variable_filas,
                width=6,
                justify="center",
            ).pack(
                side="left",
                padx=3,
            )

        else:
            ttk.Label(
                controles,
                text="Filas:",
            ).pack(
                side="left",
                padx=3,
            )

            ttk.Entry(
                controles,
                textvariable=self.variable_filas,
                width=6,
                justify="center",
            ).pack(
                side="left",
                padx=3,
            )

            ttk.Label(
                controles,
                text="Columnas:",
            ).pack(
                side="left",
                padx=3,
            )

            ttk.Entry(
                controles,
                textvariable=self.variable_columnas,
                width=6,
                justify="center",
            ).pack(
                side="left",
                padx=3,
            )

        ttk.Button(
            controles,
            text="Crear matriz",
            command=self.crear_matriz,
        ).pack(
            side="left",
            padx=6,
        )

        marco_canvas = ttk.Frame(
            self
        )

        marco_canvas.pack(
            fill="both",
            expand=True,
        )

        marco_canvas.rowconfigure(
            0,
            weight=1,
        )

        marco_canvas.columnconfigure(
            0,
            weight=1,
        )

        self.canvas = tk.Canvas(
            marco_canvas,
            height=155,
            highlightthickness=0,
        )

        self.canvas.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        scroll_vertical = ttk.Scrollbar(
            marco_canvas,
            orient="vertical",
            command=self.canvas.yview,
        )

        scroll_vertical.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        scroll_horizontal = ttk.Scrollbar(
            marco_canvas,
            orient="horizontal",
            command=self.canvas.xview,
        )

        scroll_horizontal.grid(
            row=1,
            column=0,
            sticky="ew",
        )

        self.canvas.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set,
        )

        self.contenido = ttk.Frame(
            self.canvas
        )

        self.canvas.create_window(
            (0, 0),
            window=self.contenido,
            anchor="nw",
        )

        self.contenido.bind(
            "<Configure>",
            self._actualizar_scroll,
        )

        self.crear_matriz()

    def _actualizar_scroll(self, evento=None):
        """Actualiza el área visible cuando cambia el tamaño de la matriz."""
        self.canvas.configure(
            scrollregion=self.canvas.bbox(
                "all"
            )
        )

    def _obtener_dimensiones(self):
        """Valida y devuelve las dimensiones solicitadas."""
        try:
            filas = int(
                self.variable_filas.get()
            )

            if self.cuadrada:
                columnas = filas

                self.variable_columnas.set(
                    str(filas)
                )

            else:
                columnas = int(
                    self.variable_columnas.get()
                )

        except ValueError:
            raise ValueError(
                "Las dimensiones deben ser números enteros positivos."
            )

        if filas <= 0 or columnas <= 0:
            raise ValueError(
                "Las dimensiones deben ser números enteros positivos."
            )

        return filas, columnas

    def crear_matriz(self):
        """Crea las entradas correspondientes a la dimensión indicada."""
        try:
            filas, columnas = self._obtener_dimensiones()

        except ValueError as error:
            messagebox.showerror(
                "Dimensiones inválidas",
                str(error),
            )
            return

        for elemento in self.contenido.winfo_children():
            elemento.destroy()

        self.entradas = []

        for i in range(filas):
            fila_entradas = []

            for j in range(columnas):
                entrada = ttk.Entry(
                    self.contenido,
                    width=9,
                    justify="center",
                )

                entrada.grid(
                    row=i,
                    column=j,
                    padx=3,
                    pady=3,
                )

                fila_entradas.append(
                    entrada
                )

            self.entradas.append(
                fila_entradas
            )

        self.update_idletasks()
        self._actualizar_scroll()

        self.canvas.xview_moveto(
            0
        )

        self.canvas.yview_moveto(
            0
        )

    def leer(self):
        """Devuelve la matriz escrita por el usuario."""
        if not self.entradas:
            raise ValueError(
                f"Debe crear {self.titulo}."
            )

        return [
            [
                entrada.get()
                for entrada in fila
            ]
            for fila in self.entradas
        ]

    def obtener_filas(self):
        """Devuelve la cantidad actual de filas de la matriz."""
        return len(
            self.entradas
        )

    def establecer_orden(self, orden):
        """Ajusta una matriz cuadrada al orden n indicado."""
        self.variable_filas.set(
            str(orden)
        )

        self.variable_columnas.set(
            str(orden)
        )

        self.crear_matriz()


class EntradaVectorLU(ttk.LabelFrame):
    """Gestiona el vector columna b usado en Ax=b."""

    def __init__(
        self,
        contenedor,
        titulo="Vector b",
        orden=3,
    ):
        """Inicializa el vector y crea sus entradas."""
        super().__init__(
            contenedor,
            text=titulo,
            padding=5,
        )

        self.variable_orden = tk.StringVar(
            value=str(orden)
        )

        self.entradas = []

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye el control del tamaño y el vector editable."""
        controles = ttk.Frame(
            self
        )

        controles.pack(
            fill="x",
            pady=(0, 5),
        )

        ttk.Label(
            controles,
            text="Tamaño n:",
        ).pack(
            side="left",
            padx=3,
        )

        ttk.Entry(
            controles,
            textvariable=self.variable_orden,
            width=6,
            justify="center",
        ).pack(
            side="left",
            padx=3,
        )

        ttk.Button(
            controles,
            text="Crear vector",
            command=self.crear_vector,
        ).pack(
            side="left",
            padx=6,
        )

        self.contenido = ttk.Frame(
            self
        )

        self.contenido.pack(
            fill="both",
            expand=True,
        )

        self.crear_vector()

    def crear_vector(self):
        """Crea un vector columna de tamaño n."""
        try:
            orden = int(
                self.variable_orden.get()
            )

        except ValueError:
            messagebox.showerror(
                "Tamaño inválido",
                "El tamaño del vector debe ser un número entero positivo.",
            )
            return

        if orden <= 0:
            messagebox.showerror(
                "Tamaño inválido",
                "El tamaño del vector debe ser un número entero positivo.",
            )
            return

        for elemento in self.contenido.winfo_children():
            elemento.destroy()

        self.entradas = []

        for i in range(orden):
            entrada = ttk.Entry(
                self.contenido,
                width=10,
                justify="center",
            )

            entrada.grid(
                row=i,
                column=0,
                padx=3,
                pady=3,
            )

            self.entradas.append(
                entrada
            )

    def establecer_orden(self, orden):
        """Sincroniza el tamaño del vector con el orden de A."""
        self.variable_orden.set(
            str(orden)
        )

        self.crear_vector()

    def leer(self):
        """Devuelve los valores escritos en el vector b."""
        if not self.entradas:
            raise ValueError(
                "Debe crear el vector b."
            )

        return [
            entrada.get()
            for entrada in self.entradas
        ]


class ModuloLUInterfaz(ttk.Frame):
    """Presenta factorización LU, sistemas y propiedades consolidadas."""

    def __init__(
        self,
        contenedor,
    ):
        """Inicializa la interfaz del Módulo V."""
        super().__init__(
            contenedor
        )

        self.resultado_propiedades = None

        self.mapa_propiedades = {
            "Todas las propiedades": None,
        }

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye encabezado y pestañas funcionales del módulo."""
        ttk.Label(
            self,
            text="Módulo V - Factorización LU",
            font=(
                "Arial",
                15,
                "bold",
            ),
        ).pack(
            pady=(6, 2)
        )

        ttk.Label(
            self,
            text=(
                "Descomposición A = L·U y resolución de sistemas "
                "mediante Ly = b y Ux = y"
            ),
        ).pack(
            pady=(0, 5)
        )

        self.cuaderno = ttk.Notebook(
            self
        )

        self.cuaderno.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5,
        )

        self._crear_pestana_teoremas()
        self._crear_pestana_factorizacion()
        self._crear_pestana_sistema()
        self._crear_pestana_propiedades()

    def _crear_area_texto(
        self,
        contenedor,
    ):
        """Crea un área de salida con desplazamiento vertical y horizontal."""
        marco = ttk.Frame(
            contenedor
        )

        marco.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5,
        )

        marco.rowconfigure(
            0,
            weight=1,
        )

        marco.columnconfigure(
            0,
            weight=1,
        )

        texto = tk.Text(
            marco,
            wrap="none",
            state="disabled",
            font=(
                "Consolas",
                10,
            ),
        )

        texto.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        scroll_vertical = ttk.Scrollbar(
            marco,
            orient="vertical",
            command=texto.yview,
        )

        scroll_vertical.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        scroll_horizontal = ttk.Scrollbar(
            marco,
            orient="horizontal",
            command=texto.xview,
        )

        scroll_horizontal.grid(
            row=1,
            column=0,
            sticky="ew",
        )

        texto.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set,
        )

        return texto

    def _colocar_texto(
        self,
        widget,
        contenido,
    ):
        """Reemplaza el contenido mostrado en un área de salida."""
        widget.configure(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END,
        )

        widget.insert(
            tk.END,
            contenido,
        )

        widget.configure(
            state="disabled"
        )

        widget.see(
            "1.0"
        )

    def _crear_pestana_teoremas(self):
        """Construye la opción 0 con el resumen teórico del módulo."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="0. Teoremas clave",
        )

        texto = self._crear_area_texto(
            pestana
        )

        self._colocar_texto(
            texto,
            obtener_teoremas_clave(),
        )

    def _crear_pestana_factorizacion(self):
        """Construye la opción para factorizar una matriz A en L·U."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="1. Factorización A = LU",
        )

        ttk.Label(
            pestana,
            text=(
                "La factorización admite matrices m×n y usa únicamente "
                "operaciones de reemplazo de filas, sin intercambios."
            ),
        ).pack(
            pady=(5, 2)
        )

        self.entrada_factorizacion = EntradaMatrizLU(
            pestana,
            "Matriz A",
            filas=3,
            columnas=3,
            cuadrada=False,
        )

        self.entrada_factorizacion.pack(
            fill="x",
            padx=10,
            pady=5,
        )

        ttk.Button(
            pestana,
            text="Factorizar A = L·U",
            command=self._resolver_factorizacion,
        ).pack(
            pady=5
        )

        self.txt_factorizacion = self._crear_area_texto(
            pestana
        )

    def _resolver_factorizacion(self):
        """Ejecuta la factorización y muestra el procedimiento completo."""
        try:
            resultado = procesar_factorizacion_lu(
                self.entrada_factorizacion.leer()
            )

            self._colocar_texto(
                self.txt_factorizacion,
                formatear_factorizacion_lu(
                    resultado
                ),
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )

    def _crear_pestana_sistema(self):
        """Construye la resolución Ax=b mediante la factorización LU."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="2. Resolver Ax = b",
        )

        ttk.Label(
            pestana,
            text=(
                "Para resolver Ax=b, A debe ser cuadrada. "
                "Se factoriza una vez y luego se resuelven Ly=b y Ux=y."
            ),
        ).pack(
            pady=(5, 2)
        )

        controles = ttk.Frame(
            pestana
        )

        controles.pack(
            fill="x",
            padx=10,
            pady=4,
        )

        ttk.Button(
            controles,
            text="Sincronizar b con A",
            command=self._sincronizar_vector_b,
        ).pack(
            side="left",
            padx=4,
        )

        entradas = ttk.Frame(
            pestana
        )

        entradas.pack(
            fill="x",
            padx=8,
            pady=5,
        )

        entradas.columnconfigure(
            0,
            weight=3,
        )

        entradas.columnconfigure(
            1,
            weight=1,
        )

        self.entrada_sistema_a = EntradaMatrizLU(
            entradas,
            "Matriz A",
            filas=3,
            columnas=3,
            cuadrada=True,
        )

        self.entrada_sistema_a.grid(
            row=0,
            column=0,
            padx=5,
            sticky="nsew",
        )

        self.entrada_sistema_b = EntradaVectorLU(
            entradas,
            "Vector b",
            orden=3,
        )

        self.entrada_sistema_b.grid(
            row=0,
            column=1,
            padx=5,
            sticky="nsew",
        )

        ttk.Button(
            pestana,
            text="Resolver Ax = b mediante LU",
            command=self._resolver_sistema,
        ).pack(
            pady=5
        )

        resultados = ttk.Notebook(
            pestana
        )

        resultados.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5,
        )

        tab_factorizacion = ttk.Frame(
            resultados
        )

        tab_adelante = ttk.Frame(
            resultados
        )

        tab_atras = ttk.Frame(
            resultados
        )

        tab_verificacion = ttk.Frame(
            resultados
        )

        resultados.add(
            tab_factorizacion,
            text="A = LU",
        )

        resultados.add(
            tab_adelante,
            text="Ly = b",
        )

        resultados.add(
            tab_atras,
            text="Ux = y",
        )

        resultados.add(
            tab_verificacion,
            text="Verificación",
        )

        self.txt_sistema_factorizacion = self._crear_area_texto(
            tab_factorizacion
        )

        self.txt_sistema_adelante = self._crear_area_texto(
            tab_adelante
        )

        self.txt_sistema_atras = self._crear_area_texto(
            tab_atras
        )

        self.txt_sistema_verificacion = self._crear_area_texto(
            tab_verificacion
        )

    def _sincronizar_vector_b(self):
        """Ajusta el tamaño de b al orden actual de la matriz A."""
        orden = self.entrada_sistema_a.obtener_filas()

        if orden <= 0:
            messagebox.showerror(
                "Error",
                "Debe crear primero la matriz A.",
            )
            return

        self.entrada_sistema_b.establecer_orden(
            orden
        )

    def _resolver_sistema(self):
        """Resuelve Ax=b y distribuye el procedimiento entre subpestañas."""
        try:
            resultado = procesar_sistema_lu(
                self.entrada_sistema_a.leer(),
                self.entrada_sistema_b.leer(),
            )

            self._colocar_texto(
                self.txt_sistema_factorizacion,
                formatear_factorizacion_lu(
                    resultado[
                        "factorizacion"
                    ]
                ),
            )

            self._colocar_texto(
                self.txt_sistema_adelante,
                formatear_sustitucion_adelante(
                    resultado
                ),
            )

            self._colocar_texto(
                self.txt_sistema_atras,
                formatear_sustitucion_atras(
                    resultado
                ),
            )

            self._colocar_texto(
                self.txt_sistema_verificacion,
                formatear_verificaciones_lu(
                    resultado
                ),
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )

    def _crear_pestana_propiedades(self):
        """Construye el verificador consolidado y sus controles de búsqueda."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="3. Propiedades consolidadas",
        )

        ttk.Label(
            pestana,
            text=(
                "Ingrese A, B y C una sola vez. Deben ser cuadradas "
                "y del mismo orden. Los resultados se calculan una vez "
                "y después pueden filtrarse sin recalcularlos."
            ),
        ).pack(
            pady=(5, 2)
        )

        controles = ttk.Frame(
            pestana
        )

        controles.pack(
            fill="x",
            padx=8,
            pady=4,
        )

        ttk.Label(
            controles,
            text="Escalar r:",
        ).pack(
            side="left",
            padx=4,
        )

        self.propiedades_escalar = tk.StringVar(
            value="2"
        )

        ttk.Entry(
            controles,
            textvariable=self.propiedades_escalar,
            width=8,
            justify="center",
        ).pack(
            side="left",
            padx=4,
        )

        ttk.Button(
            controles,
            text="Sincronizar B y C con A",
            command=self._sincronizar_propiedades,
        ).pack(
            side="left",
            padx=6,
        )

        matrices = ttk.Frame(
            pestana
        )

        matrices.pack(
            fill="x",
            padx=8,
            pady=5,
        )

        matrices.columnconfigure(
            0,
            weight=1,
        )

        matrices.columnconfigure(
            1,
            weight=1,
        )

        matrices.columnconfigure(
            2,
            weight=1,
        )

        self.propiedades_a = EntradaMatrizLU(
            matrices,
            "Matriz A",
            filas=2,
            columnas=2,
            cuadrada=True,
        )

        self.propiedades_a.grid(
            row=0,
            column=0,
            padx=4,
            sticky="nsew",
        )

        self.propiedades_b = EntradaMatrizLU(
            matrices,
            "Matriz B",
            filas=2,
            columnas=2,
            cuadrada=True,
        )

        self.propiedades_b.grid(
            row=0,
            column=1,
            padx=4,
            sticky="nsew",
        )

        self.propiedades_c = EntradaMatrizLU(
            matrices,
            "Matriz C",
            filas=2,
            columnas=2,
            cuadrada=True,
        )

        self.propiedades_c.grid(
            row=0,
            column=2,
            padx=4,
            sticky="nsew",
        )

        ttk.Button(
            pestana,
            text="Verificar propiedades consolidadas",
            command=self._resolver_propiedades,
        ).pack(
            pady=5
        )

        self._crear_controles_filtro(
            pestana
        )

        self.txt_propiedades = self._crear_area_texto(
            pestana
        )

    def _crear_controles_filtro(
        self,
        contenedor,
    ):
        """Construye buscador, categorías y selector de propiedades."""
        marco = ttk.LabelFrame(
            contenedor,
            text="Filtrar resultados",
            padding=6,
        )

        marco.pack(
            fill="x",
            padx=8,
            pady=(3, 5),
        )

        fila_busqueda = ttk.Frame(
            marco
        )

        fila_busqueda.pack(
            fill="x",
            pady=2,
        )

        ttk.Label(
            fila_busqueda,
            text="Buscar:",
        ).pack(
            side="left",
            padx=(0, 4),
        )

        self.propiedades_busqueda = tk.StringVar()

        entrada_busqueda = ttk.Entry(
            fila_busqueda,
            textvariable=self.propiedades_busqueda,
            width=35,
        )

        entrada_busqueda.pack(
            side="left",
            padx=4,
        )

        entrada_busqueda.bind(
            "<Return>",
            lambda evento: self._filtrar_propiedades(),
        )

        ttk.Label(
            fila_busqueda,
            text=(
                "Acepta: número, nombre, palabra parcial o fórmula "
                "(13, inversa, A^-1, A⁻¹, A^T, det(AB))"
            ),
        ).pack(
            side="left",
            padx=8,
        )

        fila_selectores = ttk.Frame(
            marco
        )

        fila_selectores.pack(
            fill="x",
            pady=3,
        )

        ttk.Label(
            fila_selectores,
            text="Categoría:",
        ).pack(
            side="left",
            padx=(0, 4),
        )

        categorias = procesar_categorias_propiedades()

        self.propiedades_categoria = tk.StringVar(
            value="Todas"
        )

        self.combo_categoria = ttk.Combobox(
            fila_selectores,
            textvariable=self.propiedades_categoria,
            values=categorias,
            state="readonly",
            width=24,
        )

        self.combo_categoria.pack(
            side="left",
            padx=4,
        )

        self.combo_categoria.bind(
            "<<ComboboxSelected>>",
            self._cambiar_categoria_propiedades,
        )

        ttk.Label(
            fila_selectores,
            text="Propiedad:",
        ).pack(
            side="left",
            padx=(12, 4),
        )

        self.propiedades_seleccion = tk.StringVar(
            value="Todas las propiedades"
        )

        self.combo_propiedad = ttk.Combobox(
            fila_selectores,
            textvariable=self.propiedades_seleccion,
            values=[
                "Todas las propiedades"
            ],
            state="readonly",
            width=58,
        )

        self.combo_propiedad.pack(
            side="left",
            padx=4,
            fill="x",
            expand=True,
        )

        fila_botones = ttk.Frame(
            marco
        )

        fila_botones.pack(
            fill="x",
            pady=(3, 0),
        )

        ttk.Button(
            fila_botones,
            text="Filtrar",
            command=self._filtrar_propiedades,
        ).pack(
            side="left",
            padx=4,
        )

        ttk.Button(
            fila_botones,
            text="Mostrar todas",
            command=self._mostrar_todas_propiedades,
        ).pack(
            side="left",
            padx=4,
        )

    def _sincronizar_propiedades(self):
        """Sincroniza B y C con el orden actual de A."""
        orden = self.propiedades_a.obtener_filas()

        if orden <= 0:
            messagebox.showerror(
                "Error",
                "Debe crear primero la matriz A.",
            )
            return

        self.propiedades_b.establecer_orden(
            orden
        )

        self.propiedades_c.establecer_orden(
            orden
        )

    def _resolver_propiedades(self):
        """Calcula las propiedades una vez y conserva sus resultados."""
        try:
            resultado = procesar_propiedades_consolidadas(
                self.propiedades_a.leer(),
                self.propiedades_b.leer(),
                self.propiedades_c.leer(),
                self.propiedades_escalar.get(),
            )

            self.resultado_propiedades = resultado

            self.propiedades_busqueda.set(
                ""
            )

            self.propiedades_categoria.set(
                "Todas"
            )

            self._actualizar_selector_propiedades()

            self._colocar_texto(
                self.txt_propiedades,
                formatear_propiedades_consolidadas(
                    resultado
                ),
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )

    def _actualizar_selector_propiedades(self):
        """Actualiza el selector según la categoría sin recalcular propiedades."""
        self.mapa_propiedades = {
            "Todas las propiedades": None,
        }

        if self.resultado_propiedades is None:
            self.combo_propiedad.configure(
                values=[
                    "Todas las propiedades"
                ]
            )

            self.propiedades_seleccion.set(
                "Todas las propiedades"
            )

            return

        categoria = self.propiedades_categoria.get()

        try:
            propiedades = procesar_filtro_propiedades(
                self.resultado_propiedades,
                "",
                categoria,
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )
            return

        opciones = [
            "Todas las propiedades"
        ]

        for propiedad in propiedades:
            etiqueta = (
                f"{propiedad['numero']}. "
                f"{propiedad['nombre']} — "
                f"{propiedad['formula']}"
            )

            opciones.append(
                etiqueta
            )

            self.mapa_propiedades[
                etiqueta
            ] = propiedad[
                "numero"
            ]

        self.combo_propiedad.configure(
            values=opciones
        )

        self.propiedades_seleccion.set(
            "Todas las propiedades"
        )

    def _cambiar_categoria_propiedades(
        self,
        evento=None,
    ):
        """Actualiza el listado de propiedades al cambiar de categoría."""
        self._actualizar_selector_propiedades()

    def _filtrar_propiedades(self):
        """Filtra los resultados ya calculados según los controles actuales."""
        if self.resultado_propiedades is None:
            messagebox.showerror(
                "Error",
                "Primero debe verificar las propiedades consolidadas.",
            )
            return

        texto = self.propiedades_busqueda.get().strip()

        categoria = self.propiedades_categoria.get()

        seleccion = self.propiedades_seleccion.get()

        try:
            propiedades = procesar_filtro_propiedades(
                self.resultado_propiedades,
                texto,
                categoria,
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )
            return

        numero_seleccionado = self.mapa_propiedades.get(
            seleccion
        )

        if numero_seleccionado is not None:
            propiedades = [
                propiedad
                for propiedad in propiedades
                if propiedad[
                    "numero"
                ] == numero_seleccionado
            ]

        criterio = self._crear_descripcion_filtro(
            texto,
            categoria,
            seleccion,
        )

        self._colocar_texto(
            self.txt_propiedades,
            formatear_propiedades_consolidadas(
                self.resultado_propiedades,
                propiedades,
                criterio,
            ),
        )

    def _crear_descripcion_filtro(
        self,
        texto,
        categoria,
        seleccion,
    ):
        """Describe los filtros activos para mostrarlos con el resultado."""
        filtros = []

        if texto:
            filtros.append(
                f'Búsqueda = "{texto}"'
            )

        if categoria != "Todas":
            filtros.append(
                f"Categoría = {categoria}"
            )

        numero = self.mapa_propiedades.get(
            seleccion
        )

        if numero is not None:
            filtros.append(
                f"Propiedad = {numero}"
            )

        if not filtros:
            return "Sin filtros"

        return " | ".join(
            filtros
        )

    def _mostrar_todas_propiedades(self):
        """Restablece los filtros y muestra los 22 resultados guardados."""
        if self.resultado_propiedades is None:
            messagebox.showerror(
                "Error",
                "Primero debe verificar las propiedades consolidadas.",
            )
            return

        self.propiedades_busqueda.set(
            ""
        )

        self.propiedades_categoria.set(
            "Todas"
        )

        self._actualizar_selector_propiedades()

        self._colocar_texto(
            self.txt_propiedades,
            formatear_propiedades_consolidadas(
                self.resultado_propiedades
            ),
        )