import tkinter as tk
from tkinter import ttk, messagebox

from controladores.programa_4_controller import (
    procesar_independencia_lineal
)

from utilidades.formato_interfaz import (
    formatear_texto_matematico
)


class Programa4Interfaz(ttk.Frame):

    def __init__(
        self,
        contenedor
    ):

        super().__init__(
            contenedor
        )

        # ==================================================
        # CONFIGURACIÓN
        # ==================================================

        self.cantidad_vectores = tk.StringVar(
            value="3"
        )

        self.dimension_vectores = tk.StringVar(
            value="3"
        )

        # Entradas creadas dinámicamente
        self.entradas_vectores = []

        self.crear_interfaz()

    # ==================================================
    # INTERFAZ GENERAL
    # ==================================================

    def crear_interfaz(
        self
    ):

        titulo = ttk.Label(
            self,
            text=(
                "Programa 4 - Independencia Lineal"
            ),
            font=(
                "Arial",
                16,
                "bold"
            )
        )

        titulo.pack(
            pady=(
                7,
                2
            )
        )

        subtitulo = ttk.Label(
            self,
            text=(
                "Determine si un conjunto de vectores "
                "es linealmente independiente o dependiente"
            ),
            font=(
                "Arial",
                10
            )
        )

        subtitulo.pack(
            pady=(
                0,
                5
            )
        )

        # ==================================================
        # CONFIGURACIÓN
        # ==================================================

        marco_configuracion = ttk.LabelFrame(
            self,
            text="Configuración del conjunto de vectores",
            padding=7
        )

        marco_configuracion.pack(
            padx=12,
            pady=5
        )

        ttk.Label(
            marco_configuracion,
            text="Cantidad de vectores k:"
        ).grid(
            row=0,
            column=0,
            padx=6,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.cantidad_vectores,
            width=8,
            justify="center"
        ).grid(
            row=0,
            column=1,
            padx=6,
            pady=3
        )

        ttk.Label(
            marco_configuracion,
            text="Dimensión n:"
        ).grid(
            row=0,
            column=2,
            padx=6,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.dimension_vectores,
            width=8,
            justify="center"
        ).grid(
            row=0,
            column=3,
            padx=6,
            pady=3
        )

        ttk.Button(
            marco_configuracion,
            text="Crear vectores",
            command=self.crear_vectores
        ).grid(
            row=0,
            column=4,
            padx=8,
            pady=3
        )

        # ==================================================
        # ÁREA DESPLAZABLE PARA LOS VECTORES
        # ==================================================

        (
            self.marco_entrada,
            self.canvas_entrada,
            self.contenido_entrada
        ) = self.crear_area_desplazable(
            self,
            "Entrada de vectores",
            145
        )

        # ==================================================
        # BOTONES
        # ==================================================

        self.marco_acciones = ttk.Frame(
            self
        )

        ttk.Button(
            self.marco_acciones,
            text="Analizar independencia",
            command=self.resolver_independencia
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=3
        )

        ttk.Button(
            self.marco_acciones,
            text="Limpiar",
            command=self.limpiar
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=3
        )

        # ==================================================
        # RESULTADOS
        # ==================================================

        self.marco_resultado = ttk.LabelFrame(
            self,
            text="Análisis de Independencia Lineal",
            padding=5
        )

        self.cuaderno_resultado = ttk.Notebook(
            self.marco_resultado
        )

        self.cuaderno_resultado.pack(
            fill="both",
            expand=True
        )

        self.pestana_resultado = ttk.Frame(
            self.cuaderno_resultado
        )

        self.pestana_procedimiento = ttk.Frame(
            self.cuaderno_resultado
        )

        self.cuaderno_resultado.add(
            self.pestana_resultado,
            text="Resultado"
        )

        self.cuaderno_resultado.add(
            self.pestana_procedimiento,
            text="Procedimiento"
        )

        self.txt_resultado = (
            self.crear_area_texto(
                self.pestana_resultado,
                13
            )
        )

        self.txt_procedimiento = (
            self.crear_area_texto(
                self.pestana_procedimiento,
                13
            )
        )

    # ==================================================
    # ÁREA DESPLAZABLE
    # ==================================================

    def crear_area_desplazable(
        self,
        padre,
        titulo,
        altura=120
    ):

        marco = ttk.LabelFrame(
            padre,
            text=titulo,
            padding=4
        )

        marco.rowconfigure(
            0,
            weight=1
        )

        marco.columnconfigure(
            0,
            weight=1
        )

        canvas = tk.Canvas(
            marco,
            height=altura,
            highlightthickness=0
        )

        canvas.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scroll_vertical = ttk.Scrollbar(
            marco,
            orient="vertical",
            command=canvas.yview
        )

        scroll_vertical.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scroll_horizontal = ttk.Scrollbar(
            marco,
            orient="horizontal",
            command=canvas.xview
        )

        scroll_horizontal.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        canvas.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set
        )

        contenido = ttk.Frame(
            canvas
        )

        canvas.create_window(
            (
                0,
                0
            ),
            window=contenido,
            anchor="nw"
        )

        contenido.bind(
            "<Configure>",
            lambda evento, c=canvas:
                self.actualizar_scroll(
                    c
                )
        )

        return (
            marco,
            canvas,
            contenido
        )

    def actualizar_scroll(
        self,
        canvas
    ):

        canvas.configure(
            scrollregion=canvas.bbox(
                "all"
            )
        )

    # ==================================================
    # ÁREA DE TEXTO
    # ==================================================

    def crear_area_texto(
        self,
        contenedor,
        altura=10
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

        # Los pivotes se muestran en rojo.
        texto.tag_configure(
            "pivote",
            foreground="red"
        )

        texto.tag_configure(
            "titulo",
            font=(
                "Arial",
                10,
                "bold"
            )
        )

        return texto

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

    # ==================================================
    # SUBÍNDICES
    # ==================================================

    def numero_subindice(
        self,
        numero
    ):

        equivalencias = str.maketrans(
            "0123456789",
            "₀₁₂₃₄₅₆₇₈₉"
        )

        return str(
            numero
        ).translate(
            equivalencias
        )

    # ==================================================
    # CREAR LOS VECTORES
    # ==================================================

    def crear_vectores(
        self
    ):

        try:

            cantidad = int(
                self.cantidad_vectores.get()
            )

            dimension = int(
                self.dimension_vectores.get()
            )

            if (
                cantidad <= 0
                or dimension <= 0
            ):

                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Datos inválidos",
                (
                    "La cantidad de vectores y su dimensión "
                    "deben ser números enteros mayores que cero."
                )
            )

            return

        # Limpiamos entradas anteriores.
        for elemento in (
            self.contenido_entrada.winfo_children()
        ):

            elemento.destroy()

        self.entradas_vectores = []

        self.marco_resultado.pack_forget()

        # ==================================================
        # ENCABEZADOS DE COMPONENTES
        # ==================================================

        ttk.Label(
            self.contenido_entrada,
            text="Vector",
            font=(
                "Arial",
                9,
                "bold"
            )
        ).grid(
            row=0,
            column=0,
            padx=6,
            pady=4
        )

        for j in range(
            dimension
        ):

            ttk.Label(
                self.contenido_entrada,
                text=(
                    "Componente "
                    + str(
                        j + 1
                    )
                )
            ).grid(
                row=0,
                column=j + 1,
                padx=4,
                pady=4
            )

        # ==================================================
        # VECTORES v₁, v₂, ..., vₖ
        # ==================================================

        for i in range(
            cantidad
        ):

            ttk.Label(
                self.contenido_entrada,
                text=(
                    "v"
                    + self.numero_subindice(
                        i + 1
                    )
                    + " ="
                ),
                font=(
                    "Arial",
                    10,
                    "bold"
                )
            ).grid(
                row=i + 1,
                column=0,
                padx=6,
                pady=4
            )

            entradas_vector = []

            for j in range(
                dimension
            ):

                entrada = ttk.Entry(
                    self.contenido_entrada,
                    width=9,
                    justify="center"
                )

                entrada.grid(
                    row=i + 1,
                    column=j + 1,
                    padx=3,
                    pady=4
                )

                entradas_vector.append(
                    entrada
                )

            self.entradas_vectores.append(
                entradas_vector
            )

        # ==================================================
        # AJUSTE VISUAL
        # ==================================================

        altura = (
            55
            + cantidad * 31
        )

        if altura < 100:

            altura = 100

        if altura > 190:

            altura = 190

        self.canvas_entrada.configure(
            height=altura
        )

        self.marco_entrada.pack(
            padx=12,
            pady=5,
            fill="x"
        )

        self.marco_acciones.pack(
            pady=3
        )

        self.update_idletasks()

        self.actualizar_scroll(
            self.canvas_entrada
        )

        self.canvas_entrada.xview_moveto(
            0
        )

        self.canvas_entrada.yview_moveto(
            0
        )

    # ==================================================
    # LEER LOS VECTORES
    # ==================================================

    def leer_vectores(
        self
    ):

        vectores = []

        for entradas_vector in (
            self.entradas_vectores
        ):

            vector = []

            for entrada in entradas_vector:

                vector.append(
                    entrada.get()
                )

            vectores.append(
                vector
            )

        return vectores

    # ==================================================
    # RESOLVER
    # ==================================================

    def resolver_independencia(
        self
    ):

        try:

            if not self.entradas_vectores:

                raise ValueError(
                    "Primero debe crear los vectores."
                )

            vectores = (
                self.leer_vectores()
            )

            resultado = (
                procesar_independencia_lineal(
                    vectores
                )
            )

            self.mostrar_resultado(
                resultado
            )

        except ValueError as error:

            messagebox.showerror(
                "Error en los datos",
                str(
                    error
                )
            )

    # ==================================================
    # FORMATO DE VECTOR
    # ==================================================

    def formatear_vector(
        self,
        vector
    ):

        return (
            "[ "
            + ", ".join(
                str(
                    valor
                )
                for valor in vector
            )
            + " ]ᵀ"
        )

    # ==================================================
    # FORMATO DE MATRIZ
    # ==================================================

    def formatear_matriz(
        self,
        matriz
    ):

        lineas = []

        for fila in matriz:

            contenido = "   ".join(
                str(
                    valor
                )
                for valor in fila
            )

            lineas.append(
                f"[ {contenido} ]"
            )

        return "\n".join(
            lineas
        )

    # ==================================================
    # FORMATO DE MATRIZ AUMENTADA
    # ==================================================

    def formatear_matriz_aumentada(
        self,
        matriz
    ):

        lineas = []

        for fila in matriz:

            izquierda = "   ".join(
                str(
                    valor
                )
                for valor in fila[:-1]
            )

            termino_independiente = (
                fila[-1]
            )

            lineas.append(
                (
                    "[ "
                    + izquierda
                    + "  |  "
                    + str(
                        termino_independiente
                    )
                    + " ]"
                )
            )

        return "\n".join(
            lineas
        )

    # ==================================================
    # INSERTAR MATRIZ REDUCIDA CON PIVOTES
    # ==================================================

    def insertar_matriz_con_pivotes(
        self,
        widget,
        matriz,
        posiciones_pivote
    ):

        posiciones = set(
            posiciones_pivote
        )

        for i, fila in enumerate(
            matriz
        ):

            widget.insert(
                tk.END,
                "[ "
            )

            for j in range(
                len(
                    fila
                ) - 1
            ):

                valor = str(
                    fila[j]
                )

                if (
                    i,
                    j
                ) in posiciones:

                    widget.insert(
                        tk.END,
                        valor,
                        "pivote"
                    )

                else:

                    widget.insert(
                        tk.END,
                        valor
                    )

                if j < (
                    len(
                        fila
                    ) - 2
                ):

                    widget.insert(
                        tk.END,
                        "   "
                    )

            widget.insert(
                tk.END,
                "  |  "
            )

            columna_aumentada = (
                len(
                    fila
                ) - 1
            )

            valor_aumentado = str(
                fila[-1]
            )

            if (
                i,
                columna_aumentada
            ) in posiciones:

                widget.insert(
                    tk.END,
                    valor_aumentado,
                    "pivote"
                )

            else:

                widget.insert(
                    tk.END,
                    valor_aumentado
                )

            widget.insert(
                tk.END,
                " ]\n"
            )

    # ==================================================
    # FORMATEAR RELACIÓN LINEAL
    # ==================================================

    def formatear_relacion_lineal(
        self,
        coeficientes
    ):

        if not coeficientes:

            return ""

        partes = []

        for i, coeficiente in enumerate(
            coeficientes
        ):

            if coeficiente == 0:

                continue

            nombre_vector = (
                "v"
                + self.numero_subindice(
                    i + 1
                )
            )

            valor_absoluto = abs(
                coeficiente
            )

            # Primer término
            if not partes:

                if coeficiente < 0:

                    signo = "-"

                else:

                    signo = ""

            else:

                if coeficiente < 0:

                    signo = " - "

                else:

                    signo = " + "

            if valor_absoluto == 1:

                termino = (
                    signo
                    + nombre_vector
                )

            else:

                termino = (
                    signo
                    + str(
                        valor_absoluto
                    )
                    + nombre_vector
                )

            partes.append(
                termino
            )

        if not partes:

            return "0 = 0"

        return (
            "".join(
                partes
            )
            + " = 0"
        )

    # ==================================================
    # MOSTRAR RESULTADO
    # ==================================================

    def mostrar_resultado(
        self,
        resultado
    ):

        datos = resultado[
            "resultado"
        ]

        vectores = datos[
            "vectores"
        ]

        cantidad_vectores = datos[
            "cantidad_vectores"
        ]

        dimension = datos[
            "dimension"
        ]

        matriz_a = datos[
            "matriz_a"
        ]

        matriz_homogenea = datos[
            "matriz_homogenea"
        ]

        matriz_reducida = datos[
            "matriz_reducida"
        ]

        numero_pivotes = datos[
            "numero_pivotes"
        ]

        columnas_pivote = datos[
            "columnas_pivote"
        ]

        posiciones_pivote = datos[
            "posiciones_pivote"
        ]

        variables_basicas = datos[
            "variables_basicas"
        ]

        variables_libres = datos[
            "variables_libres"
        ]

        solucion_formateada = datos[
            "solucion_formateada"
        ]

        solucion_no_trivial = datos[
            "solucion_no_trivial"
        ]

        es_independiente = datos[
            "es_independiente"
        ]

        veredicto = datos[
            "veredicto"
        ]

        razon = datos[
            "razon"
        ]

        historial = datos[
            "historial"
        ]

        # ==================================================
        # TEXTOS AUXILIARES
        # ==================================================

        columnas_pivote_texto = []

        for columna in columnas_pivote:

            columnas_pivote_texto.append(
                str(
                    columna + 1
                )
            )

        variables_basicas_texto = []

        for variable in variables_basicas:

            variables_basicas_texto.append(
                (
                    "x"
                    + self.numero_subindice(
                        variable + 1
                    )
                )
            )

        variables_libres_texto = []

        for variable in variables_libres:

            variables_libres_texto.append(
                (
                    "x"
                    + self.numero_subindice(
                        variable + 1
                    )
                )
            )

        posiciones_texto = []

        for fila, columna in posiciones_pivote:

            posiciones_texto.append(
                (
                    "("
                    + str(
                        fila + 1
                    )
                    + ", "
                    + str(
                        columna + 1
                    )
                    + ")"
                )
            )

        # ==================================================
        # MOSTRAR MARCO
        # ==================================================

        self.marco_resultado.pack(
            padx=12,
            pady=(
                4,
                7
            ),
            fill="both",
            expand=True
        )

        widget = (
            self.txt_resultado
        )

        widget.configure(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END
        )

        # ==================================================
        # ENCABEZADO
        # ==================================================

        widget.insert(
            tk.END,
            (
                "ANÁLISIS DE INDEPENDENCIA LINEAL\n"
                + "=" * 60
                + "\n\n"
            ),
            "titulo"
        )

        # ==================================================
        # DATOS DEL CONJUNTO
        # ==================================================

        widget.insert(
            tk.END,
            (
                "Cantidad de vectores: "
                + str(
                    cantidad_vectores
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Dimensión de los vectores: "
                + str(
                    dimension
                )
                + "\n\n"
            )
        )

        widget.insert(
            tk.END,
            "Vectores ingresados:\n"
        )

        for i, vector in enumerate(
            vectores
        ):

            widget.insert(
                tk.END,
                (
                    "v"
                    + self.numero_subindice(
                        i + 1
                    )
                    + " = "
                    + self.formatear_vector(
                        vector
                    )
                    + "\n"
                )
            )

        # ==================================================
        # MATRIZ A
        # ==================================================

        widget.insert(
            tk.END,
            (
                "\n"
                + "-" * 60
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Matriz A formada colocando "
                "los vectores como columnas:\n\n"
            )
        )

        widget.insert(
            tk.END,
            (
                self.formatear_matriz(
                    matriz_a
                )
                + "\n"
            )
        )

        # ==================================================
        # SISTEMA HOMOGÉNEO
        # ==================================================

        widget.insert(
            tk.END,
            (
                "\nSe construye el sistema homogéneo:\n\n"
                "Ax = 0\n\n"
            )
        )

        widget.insert(
            tk.END,
            "Matriz aumentada [A | 0]:\n"
        )

        widget.insert(
            tk.END,
            (
                self.formatear_matriz_aumentada(
                    matriz_homogenea
                )
                + "\n"
            )
        )

        # ==================================================
        # MATRIZ REDUCIDA
        # ==================================================

        widget.insert(
            tk.END,
            (
                "\n"
                + "-" * 60
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Forma escalonada reducida "
                "por filas:\n\n"
            )
        )

        self.insertar_matriz_con_pivotes(
            widget,
            matriz_reducida,
            posiciones_pivote
        )

        widget.insert(
            tk.END,
            (
                "\nLos valores mostrados en rojo "
                "corresponden a las posiciones pivote.\n"
            )
        )

        # ==================================================
        # PIVOTES Y VARIABLES
        # ==================================================

        widget.insert(
            tk.END,
            (
                "\n"
                + "-" * 60
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            "Análisis de pivotes y variables:\n\n"
        )

        widget.insert(
            tk.END,
            (
                "Número de pivotes: "
                + str(
                    numero_pivotes
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Número de vectores: "
                + str(
                    cantidad_vectores
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Columnas pivote: "
                + (
                    ", ".join(
                        columnas_pivote_texto
                    )
                    if columnas_pivote_texto
                    else "Ninguna"
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Posiciones pivote: "
                + (
                    ", ".join(
                        posiciones_texto
                    )
                    if posiciones_texto
                    else "Ninguna"
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Variables básicas: "
                + (
                    ", ".join(
                        variables_basicas_texto
                    )
                    if variables_basicas_texto
                    else "Ninguna"
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Variables libres: "
                + (
                    ", ".join(
                        variables_libres_texto
                    )
                    if variables_libres_texto
                    else "Ninguna"
                )
                + "\n"
            )
        )

        # ==================================================
        # SOLUCIÓN DE Ax = 0
        # ==================================================

        widget.insert(
            tk.END,
            (
                "\n"
                + "-" * 60
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            "Solución del sistema homogéneo:\n\n"
        )

        for linea in solucion_formateada:

            widget.insert(
                tk.END,
                (
                    formatear_texto_matematico(
                        linea
                    )
                    + "\n"
                )
            )

        # ==================================================
        # EXPLICACIÓN TEÓRICA
        # ==================================================

        widget.insert(
            tk.END,
            (
                "\n"
                + "-" * 60
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            "Interpretación teórica:\n\n"
        )

        if es_independiente:

            widget.insert(
                tk.END,
                (
                    "No existen variables libres.\n"
                    "Por tanto, Ax = 0 solamente posee "
                    "la solución trivial:\n\n"
                )
            )

            vector_cero = []

            for _ in range(
                cantidad_vectores
            ):

                vector_cero.append(
                    0
                )

            widget.insert(
                tk.END,
                (
                    "x = "
                    + self.formatear_vector(
                        vector_cero
                    )
                    + "\n\n"
                )
            )

            widget.insert(
                tk.END,
                (
                    "Esto significa que la única forma de "
                    "obtener el vector cero mediante una "
                    "combinación lineal de los vectores es "
                    "utilizando todos los coeficientes "
                    "iguales a cero.\n"
                )
            )

        else:

            widget.insert(
                tk.END,
                (
                    "Existe al menos una variable libre.\n"
                    "Por tanto, Ax = 0 posee soluciones "
                    "no triviales.\n"
                )
            )

            if solucion_no_trivial is not None:

                widget.insert(
                    tk.END,
                    (
                        "\nUna solución no trivial es:\n\n"
                        "x = "
                        + self.formatear_vector(
                            solucion_no_trivial
                        )
                        + "\n"
                    )
                )

                widget.insert(
                    tk.END,
                    (
                        "\nEsta solución produce "
                        "la relación lineal:\n\n"
                    )
                )

                widget.insert(
                    tk.END,
                    (
                        self.formatear_relacion_lineal(
                            solucion_no_trivial
                        )
                        + "\n"
                    )
                )

                widget.insert(
                    tk.END,
                    (
                        "\nLos coeficientes de esta relación "
                        "no son todos cero."
                    )
                )

        # ==================================================
        # VEREDICTO
        # ==================================================

        widget.insert(
            tk.END,
            (
                "\n\n"
                + "=" * 60
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            "VEREDICTO FINAL\n",
            "titulo"
        )

        widget.insert(
            tk.END,
            (
                "=" * 60
                + "\n\n"
            )
        )

        widget.insert(
            tk.END,
            veredicto
            + "\n\n"
        )

        widget.insert(
            tk.END,
            "Razón:\n"
        )

        widget.insert(
            tk.END,
            razon
            + "\n"
        )

        widget.configure(
            state="disabled"
        )

        widget.see(
            "1.0"
        )

        # ==================================================
        # PROCEDIMIENTO
        # ==================================================

        self.mostrar_procedimiento(
            historial
        )

        self.cuaderno_resultado.select(
            self.pestana_resultado
        )

    # ==================================================
    # PROCEDIMIENTO GAUSS-JORDAN
    # ==================================================

    def mostrar_procedimiento(
        self,
        historial
    ):

        widget = (
            self.txt_procedimiento
        )

        widget.configure(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END
        )

        widget.insert(
            tk.END,
            (
                "PROCEDIMIENTO DE REDUCCIÓN POR FILAS\n"
                + "=" * 60
                + "\n\n"
            ),
            "titulo"
        )

        for indice, paso in enumerate(
            historial
        ):

            if indice == 0:

                titulo_paso = (
                    "Paso 0 - Matriz inicial"
                )

            else:

                titulo_paso = (
                    "Paso "
                    + str(
                        indice
                    )
                )

            widget.insert(
                tk.END,
                titulo_paso
                + "\n"
            )

            operacion = paso.get(
                "operacion",
                "Operación no especificada"
            )

            widget.insert(
                tk.END,
                (
                    "Operación: "
                    + str(
                        operacion
                    )
                    + "\n\n"
                )
            )

            matriz = paso.get(
                "matriz",
                []
            )

            if matriz:

                widget.insert(
                    tk.END,
                    (
                        self.formatear_matriz_aumentada(
                            matriz
                        )
                        + "\n"
                    )
                )

            verificada = paso.get(
                "verificada"
            )

            if verificada is True:

                widget.insert(
                    tk.END,
                    "\nVerificación del paso: Correcta\n"
                )

            elif verificada is False:

                widget.insert(
                    tk.END,
                    "\nVerificación del paso: Incorrecta\n"
                )

            widget.insert(
                tk.END,
                (
                    "\n"
                    + "-" * 60
                    + "\n\n"
                )
            )

        widget.insert(
            tk.END,
            "Fin del procedimiento."
        )

        widget.configure(
            state="disabled"
        )

        widget.see(
            "1.0"
        )

    # ==================================================
    # LIMPIAR
    # ==================================================

    def limpiar(
        self
    ):

        self.cantidad_vectores.set(
            "3"
        )

        self.dimension_vectores.set(
            "3"
        )

        self.entradas_vectores = []

        for elemento in (
            self.contenido_entrada.winfo_children()
        ):

            elemento.destroy()

        self.marco_entrada.pack_forget()
        self.marco_acciones.pack_forget()
        self.marco_resultado.pack_forget()

        self.colocar_texto(
            self.txt_resultado,
            ""
        )

        self.colocar_texto(
            self.txt_procedimiento,
            ""
        )

        self.cuaderno_resultado.select(
            self.pestana_resultado
        )