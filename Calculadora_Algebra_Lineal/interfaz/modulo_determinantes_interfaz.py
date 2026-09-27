import tkinter as tk
from tkinter import ttk, messagebox

from controladores.modulo_determinantes_controller import (
    procesar_determinante,
    procesar_menor_cofactor,
    procesar_desarrollo_cofactores,
    procesar_invertibilidad
)

from utilidades.formato_determinantes import (
    formatear_procedimiento_determinante
)

from utilidades.formato_interfaz import (
    convertir_numero_subindice
)


# ==========================================================
# COMPONENTE PARA MATRICES CUADRADAS
# ==========================================================

class EntradaMatrizCuadrada(ttk.LabelFrame):

    def __init__(
        self,
        contenedor,
        titulo,
        orden=3
    ):

        super().__init__(
            contenedor,
            text=titulo,
            padding=5
        )

        self.titulo = titulo

        self.orden = tk.StringVar(
            value=str(orden)
        )

        self.entradas = []

        self.crear_interfaz()

    # ======================================================
    # INTERFAZ
    # ======================================================

    def crear_interfaz(
        self
    ):

        configuracion = ttk.Frame(
            self
        )

        configuracion.pack(
            fill="x",
            pady=(
                0,
                5
            )
        )

        ttk.Label(
            configuracion,
            text="Orden n:"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Entry(
            configuracion,
            textvariable=self.orden,
            width=6,
            justify="center"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            configuracion,
            text="Crear matriz",
            command=self.crear_matriz
        ).pack(
            side="left",
            padx=5
        )

        # ==================================================
        # ÁREA DESPLAZABLE
        # ==================================================

        marco_canvas = ttk.Frame(
            self
        )

        marco_canvas.pack(
            fill="both",
            expand=True
        )

        marco_canvas.rowconfigure(
            0,
            weight=1
        )

        marco_canvas.columnconfigure(
            0,
            weight=1
        )

        self.canvas = tk.Canvas(
            marco_canvas,
            height=160,
            highlightthickness=0
        )

        self.canvas.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scroll_vertical = ttk.Scrollbar(
            marco_canvas,
            orient="vertical",
            command=self.canvas.yview
        )

        scroll_vertical.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scroll_horizontal = ttk.Scrollbar(
            marco_canvas,
            orient="horizontal",
            command=self.canvas.xview
        )

        scroll_horizontal.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.canvas.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set
        )

        self.contenido = ttk.Frame(
            self.canvas
        )

        self.canvas.create_window(
            (0, 0),
            window=self.contenido,
            anchor="nw"
        )

        self.contenido.bind(
            "<Configure>",
            self.actualizar_scroll
        )

        self.crear_matriz()

    # ======================================================
    # SCROLL
    # ======================================================

    def actualizar_scroll(
        self,
        evento=None
    ):

        self.canvas.configure(
            scrollregion=self.canvas.bbox(
                "all"
            )
        )

    # ======================================================
    # CREAR MATRIZ n x n
    # ======================================================

    def crear_matriz(
        self
    ):

        try:

            orden = int(
                self.orden.get()
            )

            if orden <= 0:

                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Orden inválido",
                (
                    "El orden de la matriz debe ser "
                    "un número entero mayor que cero."
                )
            )

            return

        for elemento in (
            self.contenido.winfo_children()
        ):

            elemento.destroy()

        self.entradas = []

        for i in range(
            orden
        ):

            fila_entradas = []

            for j in range(
                orden
            ):

                entrada = ttk.Entry(
                    self.contenido,
                    width=8,
                    justify="center"
                )

                entrada.grid(
                    row=i,
                    column=j,
                    padx=3,
                    pady=3
                )

                fila_entradas.append(
                    entrada
                )

            self.entradas.append(
                fila_entradas
            )

        self.update_idletasks()

        self.actualizar_scroll()

        self.canvas.xview_moveto(
            0
        )

        self.canvas.yview_moveto(
            0
        )

    # ======================================================
    # LEER MATRIZ
    # ======================================================

    def leer(
        self
    ):

        if not self.entradas:

            raise ValueError(
                "Debe crear la matriz."
            )

        matriz = []

        for fila_entradas in (
            self.entradas
        ):

            fila = []

            for entrada in fila_entradas:

                fila.append(
                    entrada.get()
                )

            matriz.append(
                fila
            )

        return matriz


# ==========================================================
# INTERFAZ DEL MÓDULO 4
# ==========================================================

class ModuloDeterminantesInterfaz(ttk.Frame):

    def __init__(
        self,
        contenedor
    ):

        super().__init__(
            contenedor
        )

        self.crear_interfaz()

    # ======================================================
    # INTERFAZ PRINCIPAL
    # ======================================================

    def crear_interfaz(
        self
    ):

        titulo = ttk.Label(
            self,
            text="Módulo 4 - Determinantes",
            font=(
                "Arial",
                15,
                "bold"
            )
        )

        titulo.pack(
            pady=(
                6,
                2
            )
        )

        subtitulo = ttk.Label(
            self,
            text=(
                "Determinantes, menores, cofactores "
                "y análisis de invertibilidad"
            )
        )

        subtitulo.pack(
            pady=(
                0,
                5
            )
        )

        self.cuaderno = ttk.Notebook(
            self
        )

        self.cuaderno.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5
        )

        self.crear_pestana_determinante()
        self.crear_pestana_menor_cofactor()
        self.crear_pestana_desarrollo()
        self.crear_pestana_invertibilidad()

    # ======================================================
    # ÁREA DE TEXTO
    # ======================================================

    def crear_area_texto(
        self,
        contenedor,
        altura=12
    ):

        marco = ttk.Frame(
            contenedor
        )

        marco.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        marco.rowconfigure(
            0,
            weight=1
        )

        marco.columnconfigure(
            0,
            weight=1
        )

        texto = tk.Text(
            marco,
            height=altura,
            wrap="none",
            state="disabled"
        )

        texto.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scroll_vertical = ttk.Scrollbar(
            marco,
            orient="vertical",
            command=texto.yview
        )

        scroll_vertical.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scroll_horizontal = ttk.Scrollbar(
            marco,
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

        return texto

    # ======================================================
    # COLOCAR TEXTO
    # ======================================================

    def colocar_texto(
        self,
        widget,
        texto
    ):

        widget.configure(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END
        )

        widget.insert(
            tk.END,
            texto
        )

        widget.configure(
            state="disabled"
        )

        widget.see(
            "1.0"
        )

    # ======================================================
    # FORMATO DE MATRIZ
    # ======================================================

    def formatear_matriz(
        self,
        matriz
    ):

        if matriz is None:

            return "No existe."

        if not matriz:

            return "[]"

        lineas = []

        for fila in matriz:

            contenido = "   ".join(
                str(valor)
                for valor in fila
            )

            lineas.append(
                "[ "
                + contenido
                + " ]"
            )

        return "\n".join(
            lineas
        )

    # ======================================================
    # PESTAÑA 1
    # DETERMINANTE
    # ======================================================

    def crear_pestana_determinante(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Determinante"
        )

        self.det_matriz = EntradaMatrizCuadrada(
            pestana,
            "Matriz A",
            3
        )

        self.det_matriz.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Button(
            pestana,
            text="Calcular det(A)",
            command=self.resolver_determinante
        ).pack(
            pady=5
        )

        self.txt_determinante = (
            self.crear_area_texto(
                pestana
            )
        )

    # ======================================================
    # RESOLVER DETERMINANTE
    # ======================================================

    def resolver_determinante(
        self
    ):

        try:

            resultado = procesar_determinante(
                self.det_matriz.leer()
            )

            texto = (
                "DETERMINANTE DE UNA MATRIZ\n"
                + "=" * 55
                + "\n\n"
                "Matriz A:\n\n"
                + self.formatear_matriz(
                    resultado[
                        "matriz"
                    ]
                )
                + "\n\n"
                "Orden: "
                + str(
                    resultado[
                        "orden"
                    ]
                )
                + "\n\n"
                "det(A) = "
                + str(
                    resultado[
                        "determinante"
                    ]
                )
            )

            self.colocar_texto(
                self.txt_determinante,
                texto
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ======================================================
    # PESTAÑA 2
    # MENOR Y COFACTOR
    # ======================================================

    def crear_pestana_menor_cofactor(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Menores y cofactores"
        )

        self.mc_matriz = EntradaMatrizCuadrada(
            pestana,
            "Matriz A",
            3
        )

        self.mc_matriz.pack(
            fill="x",
            padx=10,
            pady=5
        )

        controles = ttk.Frame(
            pestana
        )

        controles.pack(
            pady=5
        )

        ttk.Label(
            controles,
            text="Fila i:"
        ).pack(
            side="left",
            padx=4
        )

        self.mc_fila = ttk.Entry(
            controles,
            width=6,
            justify="center"
        )

        self.mc_fila.insert(
            0,
            "1"
        )

        self.mc_fila.pack(
            side="left",
            padx=4
        )

        ttk.Label(
            controles,
            text="Columna j:"
        ).pack(
            side="left",
            padx=4
        )

        self.mc_columna = ttk.Entry(
            controles,
            width=6,
            justify="center"
        )

        self.mc_columna.insert(
            0,
            "1"
        )

        self.mc_columna.pack(
            side="left",
            padx=4
        )

        ttk.Button(
            controles,
            text="Calcular menor y cofactor",
            command=self.resolver_menor_cofactor
        ).pack(
            side="left",
            padx=8
        )

        self.txt_menor_cofactor = (
            self.crear_area_texto(
                pestana
            )
        )

    # ======================================================
    # RESOLVER MENOR Y COFACTOR
    # ======================================================

    def resolver_menor_cofactor(
        self
    ):

        try:

            resultado = procesar_menor_cofactor(
                self.mc_matriz.leer(),
                self.mc_fila.get(),
                self.mc_columna.get()
            )

            fila = resultado[
                "fila"
            ]

            columna = resultado[
                "columna"
            ]

            sub_fila = convertir_numero_subindice(
                fila
            )

            sub_columna = convertir_numero_subindice(
                columna
            )

            posicion = (
                sub_fila
                + sub_columna
            )

            texto = (
                "MENOR Y COFACTOR\n"
                + "=" * 55
                + "\n\n"
                "Matriz A:\n\n"
                + self.formatear_matriz(
                    resultado[
                        "matriz"
                    ]
                )
                + "\n\n"
            )

            texto += (
                "Posición seleccionada: ("
                + str(fila)
                + ", "
                + str(columna)
                + ")\n\n"
            )

            # ==================================================
            # CASO 1 x 1
            # ==================================================

            if resultado[
                "orden"
            ] == 1:

                texto += (
                    "La matriz es de orden 1.\n\n"
                    "C"
                    + posicion
                    + " = "
                    + str(
                        resultado[
                            "cofactor"
                        ]
                    )
                )

            # ==================================================
            # CASO GENERAL
            # ==================================================

            else:

                texto += (
                    "Para obtener M"
                    + posicion
                    + " eliminamos la fila "
                    + str(fila)
                    + " y la columna "
                    + str(columna)
                    + ".\n\n"
                )

                texto += (
                    "M"
                    + posicion
                    + " =\n\n"
                    + self.formatear_matriz(
                        resultado[
                            "menor"
                        ]
                    )
                    + "\n\n"
                )

                texto += (
                    "det(M"
                    + posicion
                    + ") = "
                    + str(
                        resultado[
                            "determinante_menor"
                        ]
                    )
                    + "\n\n"
                )

                texto += (
                    "C"
                    + posicion
                    + " = "
                    + "(-1)^("
                    + str(fila)
                    + "+"
                    + str(columna)
                    + ")"
                    + " det(M"
                    + posicion
                    + ")\n\n"
                )

                texto += (
                    "C"
                    + posicion
                    + " = "
                    + str(
                        resultado[
                            "cofactor"
                        ]
                    )
                )

            self.colocar_texto(
                self.txt_menor_cofactor,
                texto
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ======================================================
    # PESTAÑA 3
    # DESARROLLO POR COFACTORES
    # ======================================================

    def crear_pestana_desarrollo(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Desarrollo por cofactores"
        )

        self.desarrollo_matriz = (
            EntradaMatrizCuadrada(
                pestana,
                "Matriz A",
                3
            )
        )

        self.desarrollo_matriz.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Button(
            pestana,
            text="Resolver paso a paso",
            command=self.resolver_desarrollo
        ).pack(
            pady=5
        )

        self.txt_desarrollo = (
            self.crear_area_texto(
                pestana
            )
        )

    # ======================================================
    # RESOLVER DESARROLLO
    # ======================================================

    def resolver_desarrollo(
        self
    ):

        try:

            respuesta = (
                procesar_desarrollo_cofactores(
                    self.desarrollo_matriz.leer()
                )
            )

            resultado = respuesta[
                "resultado"
            ]

            texto = (
                formatear_procedimiento_determinante(
                    resultado
                )
            )

            self.colocar_texto(
                self.txt_desarrollo,
                texto
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ======================================================
    # PESTAÑA 4
    # INVERTIBILIDAD
    # ======================================================

    def crear_pestana_invertibilidad(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Invertibilidad"
        )

        self.invertibilidad_matriz = (
            EntradaMatrizCuadrada(
                pestana,
                "Matriz A",
                2
            )
        )

        self.invertibilidad_matriz.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Button(
            pestana,
            text="Analizar invertibilidad",
            command=self.resolver_invertibilidad
        ).pack(
            pady=5
        )

        self.txt_invertibilidad = (
            self.crear_area_texto(
                pestana
            )
        )

    # ======================================================
    # RESOLVER INVERTIBILIDAD
    # ======================================================

    def resolver_invertibilidad(
        self
    ):

        try:

            resultado = procesar_invertibilidad(
                self.invertibilidad_matriz.leer()
            )

            texto = (
                "ANÁLISIS DE INVERTIBILIDAD\n"
                + "=" * 55
                + "\n\n"
                "Matriz A:\n\n"
                + self.formatear_matriz(
                    resultado[
                        "matriz"
                    ]
                )
                + "\n\n"
                "det(A) = "
                + str(
                    resultado[
                        "determinante"
                    ]
                )
                + "\n\n"
            )

            if resultado[
                "es_invertible"
            ]:

                texto += (
                    "det(A) ≠ 0\n\n"
                    "La matriz es INVERTIBLE.\n\n"
                )

            else:

                texto += (
                    "det(A) = 0\n\n"
                    "La matriz NO ES INVERTIBLE.\n\n"
                )

            texto += resultado[
                "mensaje"
            ]

            self.colocar_texto(
                self.txt_invertibilidad,
                texto
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )