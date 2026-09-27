import tkinter as tk
from tkinter import ttk, messagebox

from controladores.modulo_matrices_controller import (
    procesar_operacion_basica,
    procesar_multiplicacion_matrices,
    procesar_transpuesta,
    procesar_inversa,
    procesar_propiedad_matrices
)

from utilidades.formato_inversa import (
    formatear_procedimiento_inversa
)


# ==========================================================
# COMPONENTE REUTILIZABLE PARA INGRESAR MATRICES
# ==========================================================

class EntradaMatriz(ttk.LabelFrame):

    def __init__(
        self,
        contenedor,
        titulo,
        filas=2,
        columnas=2
    ):

        super().__init__(
            contenedor,
            text=titulo,
            padding=5
        )

        self.titulo = titulo

        self.filas = tk.StringVar(
            value=str(filas)
        )

        self.columnas = tk.StringVar(
            value=str(columnas)
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
            text="Filas:"
        ).pack(
            side="left",
            padx=3
        )

        ttk.Entry(
            configuracion,
            textvariable=self.filas,
            width=5,
            justify="center"
        ).pack(
            side="left",
            padx=3
        )

        ttk.Label(
            configuracion,
            text="Columnas:"
        ).pack(
            side="left",
            padx=3
        )

        ttk.Entry(
            configuracion,
            textvariable=self.columnas,
            width=5,
            justify="center"
        ).pack(
            side="left",
            padx=3
        )

        ttk.Button(
            configuracion,
            text="Crear",
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
            height=135,
            width=280,
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
    # ACTUALIZAR SCROLL
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
    # CREAR ENTRADAS
    # ======================================================

    def crear_matriz(
        self
    ):

        try:

            filas = int(
                self.filas.get()
            )

            columnas = int(
                self.columnas.get()
            )

            if (
                filas <= 0
                or columnas <= 0
            ):

                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Dimensiones inválidas",
                (
                    "Las filas y columnas deben ser "
                    "números enteros mayores que cero."
                )
            )

            return

        for elemento in (
            self.contenido.winfo_children()
        ):

            elemento.destroy()

        self.entradas = []

        for i in range(
            filas
        ):

            fila_entradas = []

            for j in range(
                columnas
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
                "Debe crear la matriz "
                + self.titulo
                + "."
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

    # ======================================================
    # LIMPIAR
    # ======================================================

    def limpiar(
        self
    ):

        for fila in self.entradas:

            for entrada in fila:

                entrada.delete(
                    0,
                    tk.END
                )


# ==========================================================
# INTERFAZ DEL MÓDULO 3
# ==========================================================

class ModuloMatricesInterfaz(ttk.Frame):

    def __init__(
        self,
        contenedor
    ):

        super().__init__(
            contenedor
        )

        self.crear_interfaz()

    # ======================================================
    # INTERFAZ GENERAL
    # ======================================================

    def crear_interfaz(
        self
    ):

        titulo = ttk.Label(
            self,
            text="Módulo 3 - Álgebra de Matrices",
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
                "Operaciones, multiplicación, "
                "transpuesta, inversa y propiedades"
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

        self.crear_pestana_operaciones()
        self.crear_pestana_multiplicacion()
        self.crear_pestana_transpuesta()
        self.crear_pestana_inversa()
        self.crear_pestana_propiedades()

    # ======================================================
    # UTILIDADES VISUALES
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
    # FORMATO DE MATRICES
    # ======================================================

    def formatear_matriz(
        self,
        matriz
    ):

        if matriz is None:

            return "No existe."

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
    # SUBÍNDICES
    # ======================================================

    def subindice(
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

    # ======================================================
    # PESTAÑA 1
    # OPERACIONES BÁSICAS
    # ======================================================

    def crear_pestana_operaciones(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Operaciones básicas"
        )

        controles = ttk.Frame(
            pestana
        )

        controles.pack(
            pady=5
        )

        ttk.Label(
            controles,
            text="Operación:"
        ).pack(
            side="left",
            padx=4
        )

        self.operacion_basica = tk.StringVar(
            value="A + B"
        )

        combo = ttk.Combobox(
            controles,
            textvariable=self.operacion_basica,
            values=[
                "A + B",
                "A - B",
                "cA"
            ],
            state="readonly",
            width=18
        )

        combo.pack(
            side="left",
            padx=4
        )

        ttk.Label(
            controles,
            text="Escalar c:"
        ).pack(
            side="left",
            padx=4
        )

        self.escalar_basico = ttk.Entry(
            controles,
            width=8,
            justify="center"
        )

        self.escalar_basico.insert(
            0,
            "2"
        )

        self.escalar_basico.pack(
            side="left",
            padx=4
        )

        matrices = ttk.Frame(
            pestana
        )

        matrices.pack(
            fill="x",
            padx=8,
            pady=5
        )

        matrices.columnconfigure(
            0,
            weight=1
        )

        matrices.columnconfigure(
            1,
            weight=1
        )

        self.basica_a = EntradaMatriz(
            matrices,
            "Matriz A"
        )

        self.basica_a.grid(
            row=0,
            column=0,
            padx=5,
            sticky="nsew"
        )

        self.basica_b = EntradaMatriz(
            matrices,
            "Matriz B"
        )

        self.basica_b.grid(
            row=0,
            column=1,
            padx=5,
            sticky="nsew"
        )

        ttk.Button(
            pestana,
            text="Resolver",
            command=self.resolver_operacion_basica
        ).pack(
            pady=4
        )

        self.txt_basica = self.crear_area_texto(
            pestana
        )

    def resolver_operacion_basica(
        self
    ):

        try:

            seleccion = (
                self.operacion_basica.get()
            )

            matriz_a = self.basica_a.leer()

            if seleccion == "A + B":

                resultado = procesar_operacion_basica(
                    "suma",
                    matriz_a,
                    self.basica_b.leer()
                )

                simbolo = "+"

            elif seleccion == "A - B":

                resultado = procesar_operacion_basica(
                    "resta",
                    matriz_a,
                    self.basica_b.leer()
                )

                simbolo = "-"

            else:

                resultado = procesar_operacion_basica(
                    "escalar",
                    matriz_a,
                    escalar=self.escalar_basico.get()
                )

                simbolo = None

            texto = (
                "OPERACIÓN BÁSICA\n"
                + "=" * 55
                + "\n\n"
            )

            texto += (
                "Matriz A:\n\n"
                + self.formatear_matriz(
                    resultado["matriz_a"]
                )
                + "\n\n"
            )

            if seleccion in (
                "A + B",
                "A - B"
            ):

                texto += (
                    "Matriz B:\n\n"
                    + self.formatear_matriz(
                        resultado["matriz_b"]
                    )
                    + "\n\n"
                )

                texto += (
                    "A "
                    + simbolo
                    + " B =\n\n"
                )

            else:

                texto += (
                    "Escalar c = "
                    + str(
                        resultado["escalar"]
                    )
                    + "\n\n"
                    "cA =\n\n"
                )

            texto += self.formatear_matriz(
                resultado["resultado"]
            )

            self.colocar_texto(
                self.txt_basica,
                texto
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ======================================================
    # PESTAÑA 2
    # MULTIPLICACIÓN
    # ======================================================

    def crear_pestana_multiplicacion(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Multiplicación"
        )

        matrices = ttk.Frame(
            pestana
        )

        matrices.pack(
            fill="x",
            padx=8,
            pady=5
        )

        matrices.columnconfigure(
            0,
            weight=1
        )

        matrices.columnconfigure(
            1,
            weight=1
        )

        self.multi_a = EntradaMatriz(
            matrices,
            "Matriz A",
            2,
            2
        )

        self.multi_a.grid(
            row=0,
            column=0,
            padx=5,
            sticky="nsew"
        )

        self.multi_b = EntradaMatriz(
            matrices,
            "Matriz B",
            2,
            2
        )

        self.multi_b.grid(
            row=0,
            column=1,
            padx=5,
            sticky="nsew"
        )

        ttk.Button(
            pestana,
            text="Calcular AB",
            command=self.resolver_multiplicacion
        ).pack(
            pady=4
        )

        resultados = ttk.Notebook(
            pestana
        )

        resultados.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        pesta_resultado = ttk.Frame(
            resultados
        )

        pesta_procedimiento = ttk.Frame(
            resultados
        )

        resultados.add(
            pesta_resultado,
            text="Resultado"
        )

        resultados.add(
            pesta_procedimiento,
            text="Procedimiento"
        )

        self.txt_multi_resultado = (
            self.crear_area_texto(
                pesta_resultado
            )
        )

        self.txt_multi_procedimiento = (
            self.crear_area_texto(
                pesta_procedimiento
            )
        )

    def resolver_multiplicacion(
        self
    ):

        try:

            resultado = procesar_multiplicacion_matrices(
                self.multi_a.leer(),
                self.multi_b.leer()
            )

            texto = (
                "MULTIPLICACIÓN DE MATRICES\n"
                + "=" * 55
                + "\n\n"
                "A =\n\n"
                + self.formatear_matriz(
                    resultado["matriz_a"]
                )
                + "\n\nB =\n\n"
                + self.formatear_matriz(
                    resultado["matriz_b"]
                )
                + "\n\nAB =\n\n"
                + self.formatear_matriz(
                    resultado["resultado"]
                )
            )

            self.colocar_texto(
                self.txt_multi_resultado,
                texto
            )

            procedimiento = (
                "REGLA FILA-COLUMNA\n"
                + "=" * 55
                + "\n\n"
            )

            for paso in resultado[
                "procedimiento"
            ]:

                i = (
                    paso["fila_resultado"]
                    + 1
                )

                j = (
                    paso["columna_resultado"]
                    + 1
                )

                procedimiento += (
                    "(AB)"
                    + self.subindice(i)
                    + self.subindice(j)
                    + "\n\n"
                )

                procedimiento += (
                    "Fila "
                    + str(i)
                    + " de A: "
                    + str(
                        paso["fila_a"]
                    )
                    + "\n"
                )

                procedimiento += (
                    "Columna "
                    + str(j)
                    + " de B: "
                    + str(
                        paso["columna_b"]
                    )
                    + "\n\n"
                )

                productos_texto = []

                resultados_productos = []

                for producto in paso[
                    "productos"
                ]:

                    productos_texto.append(
                        "("
                        + str(
                            producto["valor_a"]
                        )
                        + ")("
                        + str(
                            producto["valor_b"]
                        )
                        + ")"
                    )

                    resultados_productos.append(
                        str(
                            producto["producto"]
                        )
                    )

                procedimiento += (
                    "(AB)"
                    + self.subindice(i)
                    + self.subindice(j)
                    + " = "
                    + " + ".join(
                        productos_texto
                    )
                    + "\n"
                )

                procedimiento += (
                    "= "
                    + " + ".join(
                        resultados_productos
                    )
                    + "\n"
                )

                procedimiento += (
                    "= "
                    + str(
                        paso["resultado"]
                    )
                    + "\n\n"
                    + "-" * 55
                    + "\n\n"
                )

            self.colocar_texto(
                self.txt_multi_procedimiento,
                procedimiento
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ======================================================
    # PESTAÑA 3
    # TRANSPUESTA
    # ======================================================

    def crear_pestana_transpuesta(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Transpuesta"
        )

        self.transpuesta_a = EntradaMatriz(
            pestana,
            "Matriz A",
            2,
            3
        )

        self.transpuesta_a.pack(
            padx=10,
            pady=5,
            fill="x"
        )

        ttk.Button(
            pestana,
            text="Calcular Aᵀ",
            command=self.resolver_transpuesta
        ).pack(
            pady=5
        )

        self.txt_transpuesta = (
            self.crear_area_texto(
                pestana
            )
        )

    def resolver_transpuesta(
        self
    ):

        try:

            resultado = procesar_transpuesta(
                self.transpuesta_a.leer()
            )

            texto = (
                "TRANSPUESTA DE UNA MATRIZ\n"
                + "=" * 55
                + "\n\n"
                "Matriz A:\n\n"
                + self.formatear_matriz(
                    resultado["matriz_a"]
                )
                + "\n\n"
                "Las filas de A pasan a ser "
                "las columnas de Aᵀ.\n\n"
                "Aᵀ =\n\n"
                + self.formatear_matriz(
                    resultado["resultado"]
                )
            )

            self.colocar_texto(
                self.txt_transpuesta,
                texto
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ======================================================
    # PESTAÑA 4
    # INVERSA
    # ======================================================

    def crear_pestana_inversa(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Inversa"
        )

        self.inversa_a = EntradaMatriz(
            pestana,
            "Matriz A",
            2,
            2
        )

        self.inversa_a.pack(
            padx=10,
            pady=5,
            fill="x"
        )

        ttk.Button(
            pestana,
            text="Calcular A⁻¹",
            command=self.resolver_inversa
        ).pack(
            pady=5
        )

        resultado_notebook = ttk.Notebook(
            pestana
        )

        resultado_notebook.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        pesta_resultado = ttk.Frame(
            resultado_notebook
        )

        pesta_procedimiento = ttk.Frame(
            resultado_notebook
        )

        resultado_notebook.add(
            pesta_resultado,
            text="Resultado"
        )

        resultado_notebook.add(
            pesta_procedimiento,
            text="Procedimiento completo"
        )

        self.txt_inversa_resultado = (
            self.crear_area_texto(
                pesta_resultado
            )
        )

        self.txt_inversa_procedimiento = (
            self.crear_area_texto(
                pesta_procedimiento
            )
        )

    def resolver_inversa(
        self
    ):

        try:

            respuesta = procesar_inversa(
                self.inversa_a.leer()
            )

            resultado = respuesta[
                "resultado"
            ]

            texto = (
                "MATRIZ INVERSA\n"
                + "=" * 55
                + "\n\n"
                "A =\n\n"
                + self.formatear_matriz(
                    resultado[
                        "matriz_original"
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
                    "La matriz es invertible.\n\n"
                    "A⁻¹ =\n\n"
                    + self.formatear_matriz(
                        resultado[
                            "inversa"
                        ]
                    )
                    + "\n\n"
                    "Verificación: "
                )

                if resultado[
                    "verificacion"
                ][
                    "verificada"
                ]:

                    texto += (
                        "Correcta.\n"
                        "AA⁻¹ = I y A⁻¹A = I."
                    )

                else:

                    texto += (
                        "No satisfactoria."
                    )

            else:

                texto += (
                    "La matriz no es invertible.\n\n"
                    + resultado["mensaje"]
                )

            self.colocar_texto(
                self.txt_inversa_resultado,
                texto
            )

            procedimiento = (
                formatear_procedimiento_inversa(
                    resultado
                )
            )

            self.colocar_texto(
                self.txt_inversa_procedimiento,
                procedimiento
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ======================================================
    # PESTAÑA 5
    # PROPIEDADES
    # ======================================================

    def crear_pestana_propiedades(
        self
    ):

        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="Propiedades"
        )

        controles = ttk.Frame(
            pestana
        )

        controles.pack(
            pady=5
        )

        ttk.Label(
            controles,
            text="Propiedad:"
        ).pack(
            side="left",
            padx=4
        )

        self.propiedad_seleccionada = tk.StringVar(
            value="A(BC) = (AB)C"
        )

        combo = ttk.Combobox(
            controles,
            textvariable=self.propiedad_seleccionada,
            values=[
                "A(BC) = (AB)C",
                "A(B + C) = AB + AC",
                "(B + C)A = BA + CA",
                "r(AB) = (rA)B = A(rB)",
                "IA = A = AI",
                "(Aᵀ)ᵀ = A",
                "(A + B)ᵀ = Aᵀ + Bᵀ",
                "(rA)ᵀ = rAᵀ",
                "(AB)ᵀ = BᵀAᵀ"
            ],
            state="readonly",
            width=30
        )

        combo.pack(
            side="left",
            padx=4
        )

        ttk.Label(
            controles,
            text="Escalar r:"
        ).pack(
            side="left",
            padx=4
        )

        self.escalar_propiedad = ttk.Entry(
            controles,
            width=8,
            justify="center"
        )

        self.escalar_propiedad.insert(
            0,
            "2"
        )

        self.escalar_propiedad.pack(
            side="left",
            padx=4
        )

        matrices = ttk.Frame(
            pestana
        )

        matrices.pack(
            fill="x",
            padx=5,
            pady=5
        )

        for columna in range(
            3
        ):

            matrices.columnconfigure(
                columna,
                weight=1
            )

        self.prop_a = EntradaMatriz(
            matrices,
            "Matriz A"
        )

        self.prop_a.grid(
            row=0,
            column=0,
            padx=3,
            sticky="nsew"
        )

        self.prop_b = EntradaMatriz(
            matrices,
            "Matriz B"
        )

        self.prop_b.grid(
            row=0,
            column=1,
            padx=3,
            sticky="nsew"
        )

        self.prop_c = EntradaMatriz(
            matrices,
            "Matriz C"
        )

        self.prop_c.grid(
            row=0,
            column=2,
            padx=3,
            sticky="nsew"
        )

        ttk.Button(
            pestana,
            text="Verificar propiedad",
            command=self.resolver_propiedad
        ).pack(
            pady=4
        )

        self.txt_propiedad = (
            self.crear_area_texto(
                pestana
            )
        )

    # ======================================================
    # MAPEO DE PROPIEDADES
    # ======================================================

    def obtener_codigo_propiedad(
        self
    ):

        seleccion = (
            self.propiedad_seleccionada.get()
        )

        equivalencias = {
            "A(BC) = (AB)C":
                "asociativa",

            "A(B + C) = AB + AC":
                "distributiva_izquierda",

            "(B + C)A = BA + CA":
                "distributiva_derecha",

            "r(AB) = (rA)B = A(rB)":
                "escalar_producto",

            "IA = A = AI":
                "identidad",

            "(Aᵀ)ᵀ = A":
                "transpuesta_doble",

            "(A + B)ᵀ = Aᵀ + Bᵀ":
                "transpuesta_suma",

            "(rA)ᵀ = rAᵀ":
                "transpuesta_escalar",

            "(AB)ᵀ = BᵀAᵀ":
                "transpuesta_producto"
        }

        return equivalencias[
            seleccion
        ]

    # ======================================================
    # FORMATEAR VALORES DE PROPIEDADES
    # ======================================================

    def formatear_valor(
        self,
        valor
    ):

        if (
            isinstance(
                valor,
                list
            )
            and valor
            and isinstance(
                valor[0],
                list
            )
        ):

            return (
                "\n"
                + self.formatear_matriz(
                    valor
                )
            )

        return str(
            valor
        )

    # ======================================================
    # RESOLVER PROPIEDAD
    # ======================================================

    def resolver_propiedad(
        self
    ):

        try:

            codigo = (
                self.obtener_codigo_propiedad()
            )

            necesita_b = codigo in (
                "asociativa",
                "distributiva_izquierda",
                "distributiva_derecha",
                "escalar_producto",
                "transpuesta_suma",
                "transpuesta_producto"
            )

            necesita_c = codigo in (
                "asociativa",
                "distributiva_izquierda",
                "distributiva_derecha"
            )

            necesita_escalar = codigo in (
                "escalar_producto",
                "transpuesta_escalar"
            )

            matriz_a = self.prop_a.leer()

            matriz_b = None
            matriz_c = None
            escalar = None

            if necesita_b:

                matriz_b = (
                    self.prop_b.leer()
                )

            if necesita_c:

                matriz_c = (
                    self.prop_c.leer()
                )

            if necesita_escalar:

                escalar = (
                    self.escalar_propiedad.get()
                )

            resultado = procesar_propiedad_matrices(
                codigo,
                matriz_a,
                matriz_b,
                matriz_c,
                escalar
            )

            texto = (
                "VERIFICACIÓN DE PROPIEDAD\n"
                + "=" * 55
                + "\n\n"
                "Propiedad:\n"
                + str(
                    resultado["propiedad"]
                )
                + "\n\n"
            )

            for clave, valor in (
                resultado.items()
            ):

                if clave in (
                    "propiedad",
                    "cumple"
                ):

                    continue

                nombre = (
                    clave
                    .replace(
                        "_",
                        " "
                    )
                    .capitalize()
                )

                texto += (
                    nombre
                    + ": "
                    + self.formatear_valor(
                        valor
                    )
                    + "\n\n"
                )

            texto += (
                "=" * 55
                + "\n"
            )

            if resultado[
                "cumple"
            ]:

                texto += (
                    "La propiedad se verifica correctamente."
                )

            else:

                texto += (
                    "La propiedad no se verificó "
                    "con los datos ingresados."
                )

            self.colocar_texto(
                self.txt_propiedad,
                texto
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )