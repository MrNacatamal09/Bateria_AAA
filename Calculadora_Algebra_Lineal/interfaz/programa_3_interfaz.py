import tkinter as tk
from tkinter import ttk, messagebox

from controladores.programa_3_controller import (
    procesar_vectores,
    procesar_matrices,
    procesar_combinacion_lineal,
    procesar_ecuacion_matricial
)

from utilidades.formato_interfaz import (
    formatear_texto_matematico
)


class Programa3Interfaz(ttk.Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)

        # ==================================================
        # VECTORES
        # ==================================================

        self.dimension_vector = tk.StringVar(
            value="3"
        )

        self.operacion_vector = tk.StringVar(
            value="suma"
        )

        self.cantidad_vectores_suma = tk.StringVar(
            value="2"
        )

        self.escalar_vector = tk.StringVar()

        self.entradas_vector_1 = []
        self.entradas_vector_2 = []

        # Para v₁, v₂, ..., vₙ en la suma
        self.entradas_vectores_suma = []

        # ==================================================
        # MATRICES
        # ==================================================

        self.filas_matriz_1 = tk.StringVar(
            value="2"
        )

        self.columnas_matriz_1 = tk.StringVar(
            value="2"
        )

        self.columnas_matriz_2 = tk.StringVar(
            value="2"
        )

        self.operacion_matriz = tk.StringVar(
            value="suma"
        )

        self.escalar_matriz = tk.StringVar()

        self.entradas_matriz_1 = []
        self.entradas_matriz_2 = []

        # ==================================================
        # COMBINACIÓN LINEAL
        # ==================================================

        self.numero_vectores_combinacion = tk.StringVar(
            value="2"
        )

        self.dimension_combinacion = tk.StringVar(
            value="2"
        )

        self.entradas_vectores_combinacion = []
        self.entradas_vector_b_combinacion = []

        # ==================================================
        # ECUACIÓN MATRICIAL Ax = b
        # ==================================================

        self.filas_axb = tk.StringVar(
            value="2"
        )

        self.columnas_axb = tk.StringVar(
            value="2"
        )

        self.entradas_matriz_axb = []
        self.entradas_vector_b_axb = []

        self.crear_interfaz()

    # ==================================================
    # INTERFAZ GENERAL
    # ==================================================

    def crear_interfaz(self):

        titulo = ttk.Label(
            self,
            text="Programa 3 - Vectores y Matrices",
            font=("Arial", 16, "bold")
        )

        titulo.pack(
            pady=(5, 1)
        )

        subtitulo = ttk.Label(
            self,
            text=(
                "Operaciones vectoriales, matriciales, "
                "combinación lineal y ecuación Ax = b"
            ),
            font=("Arial", 10)
        )

        subtitulo.pack(
            pady=(0, 4)
        )

        self.cuaderno_operaciones = ttk.Notebook(
            self
        )

        self.cuaderno_operaciones.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(2, 5)
        )

        self.pestana_vectores = ttk.Frame(
            self.cuaderno_operaciones
        )

        self.pestana_matrices = ttk.Frame(
            self.cuaderno_operaciones
        )

        self.pestana_combinacion = ttk.Frame(
            self.cuaderno_operaciones
        )

        self.pestana_axb = ttk.Frame(
            self.cuaderno_operaciones
        )

        self.cuaderno_operaciones.add(
            self.pestana_vectores,
            text="Vectores"
        )

        self.cuaderno_operaciones.add(
            self.pestana_matrices,
            text="Matrices"
        )

        self.cuaderno_operaciones.add(
            self.pestana_combinacion,
            text="Combinación lineal"
        )

        self.cuaderno_operaciones.add(
            self.pestana_axb,
            text="Ax = b"
        )

        self.crear_interfaz_vectores()
        self.crear_interfaz_matrices()
        self.crear_interfaz_combinacion()
        self.crear_interfaz_axb()

    # ==================================================
    # UTILIDADES VISUALES
    # ==================================================

    def crear_area_desplazable(
        self,
        padre,
        titulo,
        altura=110
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
            (0, 0),
            window=contenido,
            anchor="nw"
        )

        contenido.bind(
            "<Configure>",
            lambda evento, c=canvas:
                self.actualizar_scroll(c)
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
            scrollregion=
                canvas.bbox("all")
        )

    def calcular_altura(
        self,
        filas,
        minimo=85,
        maximo=175
    ):

        altura = (
            45
            + filas * 28
        )

        if altura < minimo:
            altura = minimo

        if altura > maximo:
            altura = maximo

        return altura

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

        # Los pivotes de las RREF se mostrarán en rojo
        texto.tag_configure(
            "pivote",
            foreground="red"
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
    # FORMATO MATEMÁTICO
    # ==================================================

    def numero_subindice(
        self,
        numero
    ):

        equivalencias = str.maketrans(
            "0123456789",
            "₀₁₂₃₄₅₆₇₈₉"
        )

        return str(numero).translate(
            equivalencias
        )

    def formatear_vector(
        self,
        vector
    ):

        return (
            "[ "
            + ", ".join(
                str(valor)
                for valor in vector
            )
            + " ]"
        )

    def formatear_matriz(
        self,
        matriz
    ):

        lineas = []

        for fila in matriz:

            contenido = "   ".join(
                str(valor)
                for valor in fila
            )

            lineas.append(
                f"[ {contenido} ]"
            )

        return "\n".join(
            lineas
        )

    def formatear_matriz_aumentada(
        self,
        matriz
    ):

        lineas = []

        for fila in matriz:

            izquierda = "   ".join(
                str(valor)
                for valor in fila[:-1]
            )

            lineas.append(
                f"[ {izquierda}  |  {fila[-1]} ]"
            )

        return "\n".join(
            lineas
        )

    def nombre_tipo_sistema(
        self,
        tipo
    ):

        if tipo == "determinado":

            return (
                "Sistema Consistente Determinado\n"
                "Presenta Solución Única"
            )

        if tipo == "indeterminado":

            return (
                "Sistema Consistente Indeterminado\n"
                "Presenta Infinitas Soluciones"
            )

        return (
            "Sistema Inconsistente\n"
            "Sin Solución"
        )

    def obtener_posiciones_pivote_visuales(
        self,
        matriz
    ):

        posiciones = []

        for i, fila in enumerate(matriz):

            for j, valor in enumerate(fila):

                if valor != 0:

                    posiciones.append(
                        (i, j)
                    )

                    break

        return posiciones

    def insertar_matriz_aumentada_con_pivotes(
        self,
        widget,
        matriz,
        posiciones_pivote
    ):

        posiciones = set(
            posiciones_pivote
        )

        for i, fila in enumerate(matriz):

            widget.insert(
                tk.END,
                "[ "
            )

            for j in range(
                len(fila) - 1
            ):

                valor = str(
                    fila[j]
                )

                if (i, j) in posiciones:

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

                if j < len(fila) - 2:

                    widget.insert(
                        tk.END,
                        "   "
                    )

            widget.insert(
                tk.END,
                "  |  "
            )

            columna_aumentada = (
                len(fila) - 1
            )

            termino = str(
                fila[-1]
            )

            if (
                i,
                columna_aumentada
            ) in posiciones:

                widget.insert(
                    tk.END,
                    termino,
                    "pivote"
                )

            else:

                widget.insert(
                    tk.END,
                    termino
                )

            widget.insert(
                tk.END,
                " ]\n"
            )

    def formatear_verificacion(
        self,
        verificacion
    ):

        if not verificacion["aplica"]:

            return (
                "La verificación numérica no aplica "
                "para este tipo de sistema."
            )

        lineas = []

        for ecuacion in verificacion[
            "ecuaciones"
        ]:

            estado = (
                "Correcta"
                if ecuacion["correcta"]
                else "Incorrecta"
            )

            lineas.append(
                f"Ecuación {ecuacion['ecuacion']}: "
                f"{ecuacion['lado_izquierdo']} = "
                f"{ecuacion['lado_derecho']} "
                f"({estado})"
            )

        if verificacion["correcta"]:

            lineas.append(
                "\nLa solución satisface "
                "todas las ecuaciones."
            )

        else:

            lineas.append(
                "\nLa solución no satisface "
                "todas las ecuaciones."
            )

        return "\n".join(
            lineas
        )

    # ==================================================
    # PROCEDIMIENTO REUTILIZABLE
    # ==================================================

    def mostrar_procedimiento(
        self,
        historial,
        widget
    ):

        lineas = [
            "PROCEDIMIENTO DE GAUSS-JORDAN",
            "=" * 45,
            ""
        ]

        for indice, paso in enumerate(
            historial
        ):

            if indice == 0:

                lineas.append(
                    "Paso 0 - Matriz inicial"
                )

            else:

                lineas.append(
                    f"Paso {indice}"
                )

            lineas.append(
                "Operación: "
                + paso.get(
                    "operacion",
                    "Operación no especificada"
                )
            )

            lineas.append(
                ""
            )

            matriz = paso.get(
                "matriz",
                []
            )

            if matriz:

                lineas.append(
                    self.formatear_matriz_aumentada(
                        matriz
                    )
                )

            verificada = paso.get(
                "verificada"
            )

            if verificada is True:

                lineas.append(
                    "\nVerificación del paso: Correcta"
                )

            elif verificada is False:

                lineas.append(
                    "\nVerificación del paso: Incorrecta"
                )

            lineas.append(
                ""
            )

            lineas.append(
                "-" * 45
            )

            lineas.append(
                ""
            )

        lineas.append(
            "Fin del procedimiento."
        )

        self.colocar_texto(
            widget,
            "\n".join(lineas)
        )

    # ==================================================
    # VECTORES
    # ==================================================

    def crear_interfaz_vectores(self):

        marco_configuracion = ttk.LabelFrame(
            self.pestana_vectores,
            text="Configuración",
            padding=6
        )

        marco_configuracion.pack(
            padx=12,
            pady=5
        )

        # Dimensión
        ttk.Label(
            marco_configuracion,
            text="Dimensión:"
        ).grid(
            row=0,
            column=0,
            padx=6,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.dimension_vector,
            width=7
        ).grid(
            row=0,
            column=1,
            padx=6,
            pady=3
        )

        # Operación
        ttk.Label(
            marco_configuracion,
            text="Operación:"
        ).grid(
            row=0,
            column=2,
            padx=6,
            pady=3
        )

        cb_operacion = ttk.Combobox(
            marco_configuracion,
            textvariable=self.operacion_vector,
            values=[
                "suma",
                "resta",
                "escalar"
            ],
            state="readonly",
            width=14
        )

        cb_operacion.grid(
            row=0,
            column=3,
            padx=6,
            pady=3
        )

        cb_operacion.bind(
            "<<ComboboxSelected>>",
            self.actualizar_operacion_vector
        )

        # Cantidad de vectores
        self.lbl_cantidad_vectores = ttk.Label(
            marco_configuracion,
            text="Cantidad de vectores:"
        )

        self.lbl_cantidad_vectores.grid(
            row=0,
            column=4,
            padx=6,
            pady=3
        )

        self.txt_cantidad_vectores = ttk.Entry(
            marco_configuracion,
            textvariable=self.cantidad_vectores_suma,
            width=7
        )

        self.txt_cantidad_vectores.grid(
            row=0,
            column=5,
            padx=6,
            pady=3
        )

        # Crear
        ttk.Button(
            marco_configuracion,
            text="Crear vectores",
            command=self.crear_vectores
        ).grid(
            row=0,
            column=6,
            padx=8,
            pady=3
        )

        (
            self.marco_vectores,
            self.canvas_vectores,
            self.contenido_vectores
        ) = self.crear_area_desplazable(
            self.pestana_vectores,
            "Entrada de vectores",
            100
        )

        # Acciones
        self.marco_acciones_vector = ttk.Frame(
            self.pestana_vectores
        )

        ttk.Button(
            self.marco_acciones_vector,
            text="Calcular",
            command=self.resolver_vector
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=3
        )

        ttk.Button(
            self.marco_acciones_vector,
            text="Limpiar",
            command=self.limpiar_vectores
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=3
        )

        # Resultado
        self.marco_resultado_vector = ttk.LabelFrame(
            self.pestana_vectores,
            text="Resultado",
            padding=5
        )

        self.txt_resultado_vector = (
            self.crear_area_texto(
                self.marco_resultado_vector,
                10
            )
        )

    def crear_vectores(self):

        try:

            dimension = int(
                self.dimension_vector.get()
            )

            if dimension <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Dimensión inválida",
                "La dimensión debe ser un entero mayor que cero."
            )

            return

        operacion = (
            self.operacion_vector.get()
        )

        # La suma admite una cantidad variable
        if operacion == "suma":

            try:

                cantidad = int(
                    self.cantidad_vectores_suma.get()
                )

                if cantidad < 2:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Cantidad inválida",
                    "La suma debe contener "
                    "al menos dos vectores."
                )

                return

        else:

            cantidad = 0

        # Limpiamos entradas anteriores
        for elemento in (
            self.contenido_vectores.winfo_children()
        ):

            elemento.destroy()

        self.entradas_vector_1 = []
        self.entradas_vector_2 = []
        self.entradas_vectores_suma = []

        self.marco_resultado_vector.pack_forget()

        # ==================================================
        # SUMA DE VARIOS VECTORES
        # ==================================================

        if operacion == "suma":

            for numero_vector in range(
                cantidad
            ):

                entradas_vector = []

                ttk.Label(
                    self.contenido_vectores,
                    text=(
                        "v"
                        + self.numero_subindice(
                            numero_vector + 1
                        )
                        + ":"
                    )
                ).grid(
                    row=numero_vector,
                    column=0,
                    padx=6,
                    pady=4
                )

                for componente in range(
                    dimension
                ):

                    entrada = ttk.Entry(
                        self.contenido_vectores,
                        width=7,
                        justify="center"
                    )

                    entrada.grid(
                        row=numero_vector,
                        column=componente + 1,
                        padx=3,
                        pady=4
                    )

                    entradas_vector.append(
                        entrada
                    )

                self.entradas_vectores_suma.append(
                    entradas_vector
                )

            filas_visuales = cantidad

        # ==================================================
        # RESTA
        # ==================================================

        elif operacion == "resta":

            ttk.Label(
                self.contenido_vectores,
                text="v₁:"
            ).grid(
                row=0,
                column=0,
                padx=6,
                pady=5
            )

            for i in range(dimension):

                entrada = ttk.Entry(
                    self.contenido_vectores,
                    width=7,
                    justify="center"
                )

                entrada.grid(
                    row=0,
                    column=i + 1,
                    padx=3,
                    pady=5
                )

                self.entradas_vector_1.append(
                    entrada
                )

            ttk.Label(
                self.contenido_vectores,
                text="v₂:"
            ).grid(
                row=1,
                column=0,
                padx=6,
                pady=5
            )

            for i in range(dimension):

                entrada = ttk.Entry(
                    self.contenido_vectores,
                    width=7,
                    justify="center"
                )

                entrada.grid(
                    row=1,
                    column=i + 1,
                    padx=3,
                    pady=5
                )

                self.entradas_vector_2.append(
                    entrada
                )

            filas_visuales = 2

        # ==================================================
        # PRODUCTO POR ESCALAR
        # ==================================================

        else:

            ttk.Label(
                self.contenido_vectores,
                text="v₁:"
            ).grid(
                row=0,
                column=0,
                padx=6,
                pady=5
            )

            for i in range(dimension):

                entrada = ttk.Entry(
                    self.contenido_vectores,
                    width=7,
                    justify="center"
                )

                entrada.grid(
                    row=0,
                    column=i + 1,
                    padx=3,
                    pady=5
                )

                self.entradas_vector_1.append(
                    entrada
                )

            ttk.Label(
                self.contenido_vectores,
                text="Escalar:"
            ).grid(
                row=1,
                column=0,
                padx=6,
                pady=5
            )

            ttk.Entry(
                self.contenido_vectores,
                textvariable=self.escalar_vector,
                width=10
            ).grid(
                row=1,
                column=1,
                padx=3,
                pady=5
            )

            filas_visuales = 2

        # Altura dinámica
        self.canvas_vectores.configure(
            height=self.calcular_altura(
                filas_visuales,
                minimo=90,
                maximo=170
            )
        )

        self.marco_vectores.pack(
            padx=12,
            pady=5,
            fill="x"
        )

        self.marco_acciones_vector.pack(
            pady=3
        )

        self.update_idletasks()

        self.actualizar_scroll(
            self.canvas_vectores
        )

        self.canvas_vectores.xview_moveto(
            0
        )

        self.canvas_vectores.yview_moveto(
            0
        )

    def actualizar_operacion_vector(
        self,
        evento=None
    ):

        operacion = (
            self.operacion_vector.get()
        )

        # Cantidad de vectores únicamente para suma
        if operacion == "suma":

            self.lbl_cantidad_vectores.grid()
            self.txt_cantidad_vectores.grid()

        else:

            self.lbl_cantidad_vectores.grid_remove()
            self.txt_cantidad_vectores.grid_remove()

        # Si ya existen entradas,
        # reconstruimos según la nueva operación
        if (
            self.entradas_vector_1
            or self.entradas_vector_2
            or self.entradas_vectores_suma
        ):

            self.crear_vectores()

    def leer_vector(
        self,
        entradas
    ):

        return [
            entrada.get()
            for entrada in entradas
        ]

    def resolver_vector(self):

        try:

            operacion = (
                self.operacion_vector.get()
            )

            # ==================================================
            # SUMA DE VARIOS VECTORES
            # ==================================================

            if operacion == "suma":

                if not self.entradas_vectores_suma:

                    raise ValueError(
                        "Primero debe crear los vectores."
                    )

                vectores = []

                for entradas in (
                    self.entradas_vectores_suma
                ):

                    vectores.append(
                        self.leer_vector(
                            entradas
                        )
                    )

                resultado = procesar_vectores(
                    operacion,
                    vectores=vectores
                )

            # ==================================================
            # RESTA
            # ==================================================

            elif operacion == "resta":

                if not self.entradas_vector_1:

                    raise ValueError(
                        "Primero debe crear los vectores."
                    )

                vector_1 = self.leer_vector(
                    self.entradas_vector_1
                )

                vector_2 = self.leer_vector(
                    self.entradas_vector_2
                )

                resultado = procesar_vectores(
                    operacion,
                    vector_1,
                    vector_2
                )

            # ==================================================
            # PRODUCTO POR ESCALAR
            # ==================================================

            else:

                if not self.entradas_vector_1:

                    raise ValueError(
                        "Primero debe crear el vector."
                    )

                vector_1 = self.leer_vector(
                    self.entradas_vector_1
                )

                escalar = (
                    self.escalar_vector.get()
                )

                resultado = procesar_vectores(
                    operacion,
                    vector_1,
                    escalar=escalar
                )

            self.mostrar_resultado_vector(
                resultado
            )

        except ValueError as error:

            messagebox.showerror(
                "Error en los datos",
                str(error)
            )

    def mostrar_resultado_vector(
        self,
        resultado
    ):

        operacion = resultado[
            "operacion"
        ]

        vector_resultado = resultado[
            "resultado"
        ]

        if operacion == "suma_vectores":

            cantidad = resultado.get(
                "cantidad_vectores",
                2
            )

            expresion = " + ".join(
                "v"
                + self.numero_subindice(
                    i + 1
                )
                for i in range(cantidad)
            )

            texto = (
                "Operación: Suma de vectores\n\n"
                f"{expresion}\n\n"
                "Resultado:\n"
                f"{self.formatear_vector(vector_resultado)}"
            )

        elif operacion == "resta_vectores":

            texto = (
                "Operación: Resta de vectores\n\n"
                "v₁ - v₂\n\n"
                "Resultado:\n"
                f"{self.formatear_vector(vector_resultado)}"
            )

        else:

            texto = (
                "Operación: Multiplicación de vector "
                "por escalar\n\n"
                "Resultado:\n"
                f"{self.formatear_vector(vector_resultado)}"
            )

        self.marco_resultado_vector.pack(
            padx=12,
            pady=(4, 7),
            fill="both",
            expand=True
        )

        self.colocar_texto(
            self.txt_resultado_vector,
            texto
        )

    def limpiar_vectores(self):

        self.dimension_vector.set(
            "3"
        )

        self.operacion_vector.set(
            "suma"
        )

        self.cantidad_vectores_suma.set(
            "2"
        )

        self.escalar_vector.set(
            ""
        )

        self.entradas_vector_1 = []
        self.entradas_vector_2 = []
        self.entradas_vectores_suma = []

        for elemento in (
            self.contenido_vectores.winfo_children()
        ):

            elemento.destroy()

        self.marco_vectores.pack_forget()
        self.marco_acciones_vector.pack_forget()
        self.marco_resultado_vector.pack_forget()

        self.colocar_texto(
            self.txt_resultado_vector,
            ""
        )

        # Al volver a suma mostramos otra vez
        # la cantidad de vectores
        self.lbl_cantidad_vectores.grid()
        self.txt_cantidad_vectores.grid()

    # ==================================================
    # MATRICES
    # ==================================================

    def crear_interfaz_matrices(self):

        marco_configuracion = ttk.LabelFrame(
            self.pestana_matrices,
            text="Configuración",
            padding=6
        )

        marco_configuracion.pack(
            padx=12,
            pady=5
        )

        ttk.Label(
            marco_configuracion,
            text="Filas A:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.filas_matriz_1,
            width=6
        ).grid(
            row=0,
            column=1,
            padx=5,
            pady=3
        )

        ttk.Label(
            marco_configuracion,
            text="Columnas A:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.columnas_matriz_1,
            width=6
        ).grid(
            row=0,
            column=3,
            padx=5,
            pady=3
        )

        ttk.Label(
            marco_configuracion,
            text="Operación:"
        ).grid(
            row=0,
            column=4,
            padx=5,
            pady=3
        )

        cb_operacion = ttk.Combobox(
            marco_configuracion,
            textvariable=self.operacion_matriz,
            values=[
                "suma",
                "resta",
                "escalar",
                "multiplicacion"
            ],
            state="readonly",
            width=15
        )

        cb_operacion.grid(
            row=0,
            column=5,
            padx=5,
            pady=3
        )

        cb_operacion.bind(
            "<<ComboboxSelected>>",
            self.actualizar_operacion_matriz
        )

        self.lbl_columnas_b = ttk.Label(
            marco_configuracion,
            text="Columnas B:"
        )

        self.txt_columnas_b = ttk.Entry(
            marco_configuracion,
            textvariable=self.columnas_matriz_2,
            width=6
        )

        ttk.Button(
            marco_configuracion,
            text="Crear matrices",
            command=self.crear_matrices
        ).grid(
            row=0,
            column=8,
            padx=7,
            pady=3
        )

        (
            self.marco_matrices_scroll,
            self.canvas_matrices,
            self.contenido_matrices
        ) = self.crear_area_desplazable(
            self.pestana_matrices,
            "Entrada de matrices",
            120
        )

        self.marco_matriz_1 = ttk.LabelFrame(
            self.contenido_matrices,
            text="Matriz A",
            padding=6
        )

        self.marco_matriz_1.grid(
            row=0,
            column=0,
            padx=8,
            pady=4,
            sticky="n"
        )

        self.marco_matriz_2 = ttk.LabelFrame(
            self.contenido_matrices,
            text="Matriz B",
            padding=6
        )

        self.marco_matriz_2.grid(
            row=0,
            column=1,
            padx=8,
            pady=4,
            sticky="n"
        )

        self.marco_escalar_matriz = ttk.LabelFrame(
            self.contenido_matrices,
            text="Escalar",
            padding=6
        )

        self.marco_acciones_matriz = ttk.Frame(
            self.pestana_matrices
        )

        ttk.Button(
            self.marco_acciones_matriz,
            text="Calcular",
            command=self.resolver_matriz
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=3
        )

        ttk.Button(
            self.marco_acciones_matriz,
            text="Limpiar",
            command=self.limpiar_matrices
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=3
        )

        self.marco_resultado_matriz = ttk.LabelFrame(
            self.pestana_matrices,
            text="Resultado",
            padding=5
        )

        self.txt_resultado_matriz = (
            self.crear_area_texto(
                self.marco_resultado_matriz,
                10
            )
        )

        self.actualizar_operacion_matriz()

    def actualizar_operacion_matriz(
        self,
        evento=None
    ):

        operacion = (
            self.operacion_matriz.get()
        )

        if operacion == "multiplicacion":

            self.lbl_columnas_b.grid(
                row=0,
                column=6,
                padx=5,
                pady=3
            )

            self.txt_columnas_b.grid(
                row=0,
                column=7,
                padx=5,
                pady=3
            )

        else:

            self.lbl_columnas_b.grid_remove()
            self.txt_columnas_b.grid_remove()

        if self.entradas_matriz_1:
            self.crear_matrices()

    def crear_matrices(self):

        try:

            filas_a = int(
                self.filas_matriz_1.get()
            )

            columnas_a = int(
                self.columnas_matriz_1.get()
            )

            if (
                filas_a <= 0
                or columnas_a <= 0
            ):
                raise ValueError

            operacion = (
                self.operacion_matriz.get()
            )

            if operacion == "multiplicacion":

                columnas_b = int(
                    self.columnas_matriz_2.get()
                )

                if columnas_b <= 0:
                    raise ValueError

            else:

                columnas_b = columnas_a

        except ValueError:

            messagebox.showerror(
                "Dimensiones inválidas",
                "Las dimensiones deben ser "
                "enteros mayores que cero."
            )

            return

        self.entradas_matriz_1 = []
        self.entradas_matriz_2 = []

        for elemento in (
            self.marco_matriz_1.winfo_children()
        ):
            elemento.destroy()

        for elemento in (
            self.marco_matriz_2.winfo_children()
        ):
            elemento.destroy()

        for elemento in (
            self.marco_escalar_matriz.winfo_children()
        ):
            elemento.destroy()

        self.marco_resultado_matriz.pack_forget()

        operacion = (
            self.operacion_matriz.get()
        )

        self.entradas_matriz_1 = (
            self.generar_casillas_matriz(
                self.marco_matriz_1,
                filas_a,
                columnas_a
            )
        )

        filas_visuales = filas_a

        if operacion in (
            "suma",
            "resta"
        ):

            self.marco_matriz_2.grid()
            self.marco_escalar_matriz.grid_remove()

            self.entradas_matriz_2 = (
                self.generar_casillas_matriz(
                    self.marco_matriz_2,
                    filas_a,
                    columnas_a
                )
            )

        elif operacion == "multiplicacion":

            self.marco_matriz_2.grid()
            self.marco_escalar_matriz.grid_remove()

            self.entradas_matriz_2 = (
                self.generar_casillas_matriz(
                    self.marco_matriz_2,
                    columnas_a,
                    columnas_b
                )
            )

            filas_visuales = max(
                filas_a,
                columnas_a
            )

        else:

            self.marco_matriz_2.grid_remove()

            self.marco_escalar_matriz.grid(
                row=0,
                column=1,
                padx=8,
                pady=4,
                sticky="n"
            )

            ttk.Label(
                self.marco_escalar_matriz,
                text="Valor:"
            ).grid(
                row=0,
                column=0,
                padx=5,
                pady=5
            )

            ttk.Entry(
                self.marco_escalar_matriz,
                textvariable=self.escalar_matriz,
                width=10
            ).grid(
                row=0,
                column=1,
                padx=5,
                pady=5
            )

        self.canvas_matrices.configure(
            height=self.calcular_altura(
                filas_visuales
            )
        )

        self.marco_matrices_scroll.pack(
            padx=12,
            pady=5,
            fill="x"
        )

        self.marco_acciones_matriz.pack(
            pady=3
        )

        self.update_idletasks()

        self.actualizar_scroll(
            self.canvas_matrices
        )

        self.canvas_matrices.xview_moveto(
            0
        )

        self.canvas_matrices.yview_moveto(
            0
        )

    def generar_casillas_matriz(
        self,
        contenedor,
        filas,
        columnas
    ):

        entradas = []

        for i in range(filas):

            fila_entradas = []

            for j in range(columnas):

                entrada = ttk.Entry(
                    contenedor,
                    width=7,
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

            entradas.append(
                fila_entradas
            )

        return entradas

    def leer_matriz(
        self,
        entradas
    ):

        return [
            [
                entrada.get()
                for entrada in fila
            ]
            for fila in entradas
        ]

    def resolver_matriz(self):

        try:

            if not self.entradas_matriz_1:

                raise ValueError(
                    "Primero debe crear las matrices."
                )

            operacion = (
                self.operacion_matriz.get()
            )

            matriz_1 = self.leer_matriz(
                self.entradas_matriz_1
            )

            matriz_2 = None
            escalar = None

            if operacion in (
                "suma",
                "resta",
                "multiplicacion"
            ):

                matriz_2 = self.leer_matriz(
                    self.entradas_matriz_2
                )

            elif operacion == "escalar":

                escalar = (
                    self.escalar_matriz.get()
                )

            resultado = procesar_matrices(
                operacion,
                matriz_1,
                matriz_2,
                escalar
            )

            self.mostrar_resultado_matriz(
                resultado
            )

        except ValueError as error:

            messagebox.showerror(
                "Error en los datos",
                str(error)
            )

    def mostrar_resultado_matriz(
        self,
        resultado
    ):

        nombres = {
            "suma_matrices":
                "Suma de matrices",

            "resta_matrices":
                "Resta de matrices",

            "matriz_por_escalar":
                "Multiplicación de matriz por escalar",

            "multiplicacion_matrices":
                "Multiplicación matricial"
        }

        operacion = resultado[
            "operacion"
        ]

        matriz_resultado = resultado[
            "resultado"
        ]

        texto = (
            f"Operación: "
            f"{nombres.get(operacion, operacion)}\n\n"
            "Resultado:\n"
            f"{self.formatear_matriz(matriz_resultado)}"
        )

        self.marco_resultado_matriz.pack(
            padx=12,
            pady=(4, 7),
            fill="both",
            expand=True
        )

        self.colocar_texto(
            self.txt_resultado_matriz,
            texto
        )

    def limpiar_matrices(self):

        self.filas_matriz_1.set(
            "2"
        )

        self.columnas_matriz_1.set(
            "2"
        )

        self.columnas_matriz_2.set(
            "2"
        )

        self.operacion_matriz.set(
            "suma"
        )

        self.escalar_matriz.set(
            ""
        )

        self.entradas_matriz_1 = []
        self.entradas_matriz_2 = []

        for contenedor in (
            self.marco_matriz_1,
            self.marco_matriz_2,
            self.marco_escalar_matriz
        ):

            for elemento in (
                contenedor.winfo_children()
            ):
                elemento.destroy()

        self.marco_matrices_scroll.pack_forget()
        self.marco_acciones_matriz.pack_forget()
        self.marco_resultado_matriz.pack_forget()

        self.colocar_texto(
            self.txt_resultado_matriz,
            ""
        )

        self.actualizar_operacion_matriz()

    # ==================================================
    # COMBINACIÓN LINEAL
    # ==================================================

    def crear_interfaz_combinacion(self):

        marco_configuracion = ttk.LabelFrame(
            self.pestana_combinacion,
            text="Configuración",
            padding=6
        )

        marco_configuracion.pack(
            padx=12,
            pady=5
        )

        ttk.Label(
            marco_configuracion,
            text="Cantidad de vectores:"
        ).grid(
            row=0,
            column=0,
            padx=6,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.numero_vectores_combinacion,
            width=7
        ).grid(
            row=0,
            column=1,
            padx=6,
            pady=3
        )

        ttk.Label(
            marco_configuracion,
            text="Dimensión:"
        ).grid(
            row=0,
            column=2,
            padx=6,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.dimension_combinacion,
            width=7
        ).grid(
            row=0,
            column=3,
            padx=6,
            pady=3
        )

        ttk.Button(
            marco_configuracion,
            text="Crear vectores",
            command=self.crear_vectores_combinacion
        ).grid(
            row=0,
            column=4,
            padx=8,
            pady=3
        )

        (
            self.marco_combinacion_entrada,
            self.canvas_combinacion,
            self.contenido_combinacion
        ) = self.crear_area_desplazable(
            self.pestana_combinacion,
            "Vectores de la combinación",
            120
        )

        self.marco_acciones_combinacion = ttk.Frame(
            self.pestana_combinacion
        )

        ttk.Button(
            self.marco_acciones_combinacion,
            text="Evaluar combinación",
            command=self.resolver_combinacion
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=3
        )

        ttk.Button(
            self.marco_acciones_combinacion,
            text="Limpiar",
            command=self.limpiar_combinacion
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=3
        )

        self.marco_resultado_combinacion = ttk.LabelFrame(
            self.pestana_combinacion,
            text="Resultado",
            padding=5
        )

        self.cuaderno_combinacion = ttk.Notebook(
            self.marco_resultado_combinacion
        )

        self.cuaderno_combinacion.pack(
            fill="both",
            expand=True
        )

        self.pestana_resultado_combinacion = ttk.Frame(
            self.cuaderno_combinacion
        )

        self.pestana_procedimiento_combinacion = ttk.Frame(
            self.cuaderno_combinacion
        )

        self.cuaderno_combinacion.add(
            self.pestana_resultado_combinacion,
            text="Resultado"
        )

        self.cuaderno_combinacion.add(
            self.pestana_procedimiento_combinacion,
            text="Procedimiento"
        )

        self.txt_resultado_combinacion = (
            self.crear_area_texto(
                self.pestana_resultado_combinacion,
                10
            )
        )

        self.txt_procedimiento_combinacion = (
            self.crear_area_texto(
                self.pestana_procedimiento_combinacion,
                10
            )
        )

    def crear_vectores_combinacion(self):

        try:

            cantidad = int(
                self.numero_vectores_combinacion.get()
            )

            dimension = int(
                self.dimension_combinacion.get()
            )

            if (
                cantidad <= 0
                or dimension <= 0
            ):
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Datos inválidos",
                "La cantidad de vectores y la dimensión "
                "deben ser enteros mayores que cero."
            )

            return

        for elemento in (
            self.contenido_combinacion.winfo_children()
        ):
            elemento.destroy()

        self.entradas_vectores_combinacion = []
        self.entradas_vector_b_combinacion = []

        self.marco_resultado_combinacion.pack_forget()

        for i in range(cantidad):

            fila_vector = []

            ttk.Label(
                self.contenido_combinacion,
                text=(
                    "v"
                    + self.numero_subindice(
                        i + 1
                    )
                    + " ="
                )
            ).grid(
                row=i,
                column=0,
                padx=6,
                pady=3
            )

            for j in range(dimension):

                entrada = ttk.Entry(
                    self.contenido_combinacion,
                    width=7,
                    justify="center"
                )

                entrada.grid(
                    row=i,
                    column=j + 1,
                    padx=3,
                    pady=3
                )

                fila_vector.append(
                    entrada
                )

            self.entradas_vectores_combinacion.append(
                fila_vector
            )

        fila_b = cantidad

        ttk.Label(
            self.contenido_combinacion,
            text="b =",
            font=("Arial", 10, "bold")
        ).grid(
            row=fila_b,
            column=0,
            padx=6,
            pady=(7, 3)
        )

        for j in range(dimension):

            entrada = ttk.Entry(
                self.contenido_combinacion,
                width=7,
                justify="center"
            )

            entrada.grid(
                row=fila_b,
                column=j + 1,
                padx=3,
                pady=(7, 3)
            )

            self.entradas_vector_b_combinacion.append(
                entrada
            )

        self.canvas_combinacion.configure(
            height=self.calcular_altura(
                cantidad + 1,
                minimo=90,
                maximo=160
            )
        )

        self.marco_combinacion_entrada.pack(
            padx=12,
            pady=5,
            fill="x"
        )

        self.marco_acciones_combinacion.pack(
            pady=3
        )

        self.update_idletasks()

        self.actualizar_scroll(
            self.canvas_combinacion
        )

        self.canvas_combinacion.xview_moveto(
            0
        )

        self.canvas_combinacion.yview_moveto(
            0
        )

    def resolver_combinacion(self):

        try:

            if not self.entradas_vectores_combinacion:

                raise ValueError(
                    "Primero debe crear los vectores."
                )

            vectores = []

            for entradas in (
                self.entradas_vectores_combinacion
            ):

                vectores.append(
                    self.leer_vector(
                        entradas
                    )
                )

            vector_b = self.leer_vector(
                self.entradas_vector_b_combinacion
            )

            resultado = procesar_combinacion_lineal(
                vectores,
                vector_b
            )

            self.mostrar_resultado_combinacion(
                resultado
            )

        except ValueError as error:

            messagebox.showerror(
                "Error en los datos",
                str(error)
            )

    def mostrar_resultado_combinacion(
        self,
        resultado
    ):

        datos = resultado[
            "resultado"
        ]

        es_combinacion = datos[
            "es_combinacion"
        ]

        resultado_sistema = datos[
            "resultado_sistema"
        ]

        tipo = datos[
            "tipo"
        ]

        coeficientes = datos[
            "coeficientes"
        ]

        matriz_aumentada = datos[
            "matriz_aumentada"
        ]

        matriz_reducida = resultado_sistema[
            "matriz_reducida"
        ]

        variables_basicas = resultado_sistema[
            "variables_basicas"
        ]

        variables_libres = resultado_sistema[
            "variables_libres"
        ]

        posiciones_pivote = resultado_sistema[
            "posiciones_pivote"
        ]

        if es_combinacion:

            respuesta = (
                "Sí. El vector b pertenece al espacio "
                "generado por los vectores dados."
            )

        else:

            respuesta = (
                "No. El vector b no puede expresarse "
                "como combinación lineal de los vectores dados."
            )

        posiciones_texto = [
            f"({fila + 1}, {columna + 1})"
            for fila, columna
            in posiciones_pivote
        ]

        basicas_texto = [
            "x"
            + self.numero_subindice(
                variable + 1
            )
            for variable in variables_basicas
        ]

        libres_texto = [
            "x"
            + self.numero_subindice(
                variable + 1
            )
            for variable in variables_libres
        ]

        self.marco_resultado_combinacion.pack(
            padx=12,
            pady=(4, 7),
            fill="both",
            expand=True
        )

        widget = self.txt_resultado_combinacion

        widget.configure(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END
        )

        widget.insert(
            tk.END,
            respuesta + "\n\n"
        )

        widget.insert(
            tk.END,
            "Clasificación del sistema:\n"
        )

        widget.insert(
            tk.END,
            self.nombre_tipo_sistema(
                tipo
            )
            + "\n\n"
        )

        widget.insert(
            tk.END,
            (
                "Posiciones pivote: "
                + (
                    ", ".join(posiciones_texto)
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
                    ", ".join(basicas_texto)
                    if basicas_texto
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
                    ", ".join(libres_texto)
                    if libres_texto
                    else "Ninguna"
                )
                + "\n"
            )
        )

        if es_combinacion:

            widget.insert(
                tk.END,
                "\nCoeficientes de la combinación:\n"
            )

            for linea in coeficientes:

                widget.insert(
                    tk.END,
                    formatear_texto_matematico(
                        linea
                    )
                    + "\n"
                )

        widget.insert(
            tk.END,
            "\nMatriz aumentada [A|b]:\n"
        )

        widget.insert(
            tk.END,
            self.formatear_matriz_aumentada(
                matriz_aumentada
            )
            + "\n"
        )

        widget.insert(
            tk.END,
            (
                "\nForma escalonada reducida "
                "por filas (RREF):\n"
            )
        )

        self.insertar_matriz_aumentada_con_pivotes(
            widget,
            matriz_reducida,
            posiciones_pivote
        )

        widget.insert(
            tk.END,
            (
                "\nLos valores mostrados en rojo "
                "corresponden a posiciones pivote."
            )
        )

        widget.configure(
            state="disabled"
        )

        widget.see(
            "1.0"
        )

        self.mostrar_procedimiento(
            resultado_sistema["historial"],
            self.txt_procedimiento_combinacion
        )

        self.cuaderno_combinacion.select(
            self.pestana_resultado_combinacion
        )

    def limpiar_combinacion(self):

        self.numero_vectores_combinacion.set(
            "2"
        )

        self.dimension_combinacion.set(
            "2"
        )

        self.entradas_vectores_combinacion = []
        self.entradas_vector_b_combinacion = []

        for elemento in (
            self.contenido_combinacion.winfo_children()
        ):
            elemento.destroy()

        self.marco_combinacion_entrada.pack_forget()
        self.marco_acciones_combinacion.pack_forget()
        self.marco_resultado_combinacion.pack_forget()

        self.colocar_texto(
            self.txt_resultado_combinacion,
            ""
        )

        self.colocar_texto(
            self.txt_procedimiento_combinacion,
            ""
        )

        self.cuaderno_combinacion.select(
            self.pestana_resultado_combinacion
        )

    # ==================================================
    # ECUACIÓN MATRICIAL Ax = b
    # ==================================================

    def crear_interfaz_axb(self):

        marco_configuracion = ttk.LabelFrame(
            self.pestana_axb,
            text="Dimensiones de A",
            padding=6
        )

        marco_configuracion.pack(
            padx=12,
            pady=5
        )

        ttk.Label(
            marco_configuracion,
            text="Filas:"
        ).grid(
            row=0,
            column=0,
            padx=6,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.filas_axb,
            width=7
        ).grid(
            row=0,
            column=1,
            padx=6,
            pady=3
        )

        ttk.Label(
            marco_configuracion,
            text="Columnas:"
        ).grid(
            row=0,
            column=2,
            padx=6,
            pady=3
        )

        ttk.Entry(
            marco_configuracion,
            textvariable=self.columnas_axb,
            width=7
        ).grid(
            row=0,
            column=3,
            padx=6,
            pady=3
        )

        ttk.Button(
            marco_configuracion,
            text="Crear sistema",
            command=self.crear_sistema_axb
        ).grid(
            row=0,
            column=4,
            padx=8,
            pady=3
        )

        (
            self.marco_entrada_axb,
            self.canvas_axb,
            self.contenido_axb
        ) = self.crear_area_desplazable(
            self.pestana_axb,
            "Ecuación matricial Ax = b",
            120
        )

        self.marco_matriz_axb = ttk.LabelFrame(
            self.contenido_axb,
            text="Matriz A",
            padding=6
        )

        self.marco_matriz_axb.grid(
            row=0,
            column=0,
            padx=8,
            pady=4,
            sticky="n"
        )

        self.marco_vector_b_axb = ttk.LabelFrame(
            self.contenido_axb,
            text="Vector b",
            padding=6
        )

        self.marco_vector_b_axb.grid(
            row=0,
            column=1,
            padx=8,
            pady=4,
            sticky="n"
        )

        self.marco_acciones_axb = ttk.Frame(
            self.pestana_axb
        )

        ttk.Button(
            self.marco_acciones_axb,
            text="Resolver Ax = b",
            command=self.resolver_axb
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=3
        )

        ttk.Button(
            self.marco_acciones_axb,
            text="Limpiar",
            command=self.limpiar_axb
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=3
        )

        self.marco_resultado_axb = ttk.LabelFrame(
            self.pestana_axb,
            text="Resolución de Ax = b",
            padding=5
        )

        self.cuaderno_axb = ttk.Notebook(
            self.marco_resultado_axb
        )

        self.cuaderno_axb.pack(
            fill="both",
            expand=True
        )

        self.pestana_resultado_axb = ttk.Frame(
            self.cuaderno_axb
        )

        self.pestana_procedimiento_axb = ttk.Frame(
            self.cuaderno_axb
        )

        self.cuaderno_axb.add(
            self.pestana_resultado_axb,
            text="Resultado"
        )

        self.cuaderno_axb.add(
            self.pestana_procedimiento_axb,
            text="Procedimiento"
        )

        self.txt_resultado_axb = (
            self.crear_area_texto(
                self.pestana_resultado_axb,
                10
            )
        )

        self.txt_procedimiento_axb = (
            self.crear_area_texto(
                self.pestana_procedimiento_axb,
                10
            )
        )

    def crear_sistema_axb(self):

        try:

            filas = int(
                self.filas_axb.get()
            )

            columnas = int(
                self.columnas_axb.get()
            )

            if (
                filas <= 0
                or columnas <= 0
            ):
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Dimensiones inválidas",
                "Las filas y columnas deben ser "
                "enteros mayores que cero."
            )

            return

        for elemento in (
            self.marco_matriz_axb.winfo_children()
        ):
            elemento.destroy()

        for elemento in (
            self.marco_vector_b_axb.winfo_children()
        ):
            elemento.destroy()

        self.entradas_matriz_axb = (
            self.generar_casillas_matriz(
                self.marco_matriz_axb,
                filas,
                columnas
            )
        )

        self.entradas_vector_b_axb = []

        for i in range(filas):

            entrada = ttk.Entry(
                self.marco_vector_b_axb,
                width=7,
                justify="center"
            )

            entrada.grid(
                row=i,
                column=0,
                padx=3,
                pady=3
            )

            self.entradas_vector_b_axb.append(
                entrada
            )

        self.marco_resultado_axb.pack_forget()

        self.canvas_axb.configure(
            height=self.calcular_altura(
                filas
            )
        )

        self.marco_entrada_axb.pack(
            padx=12,
            pady=5,
            fill="x"
        )

        self.marco_acciones_axb.pack(
            pady=3
        )

        self.update_idletasks()

        self.actualizar_scroll(
            self.canvas_axb
        )

        self.canvas_axb.xview_moveto(
            0
        )

        self.canvas_axb.yview_moveto(
            0
        )

    def resolver_axb(self):

        try:

            if not self.entradas_matriz_axb:

                raise ValueError(
                    "Primero debe crear la matriz A "
                    "y el vector b."
                )

            matriz_a = self.leer_matriz(
                self.entradas_matriz_axb
            )

            vector_b = self.leer_vector(
                self.entradas_vector_b_axb
            )

            resultado = procesar_ecuacion_matricial(
                matriz_a,
                vector_b
            )

            self.mostrar_resultado_axb(
                resultado
            )

        except ValueError as error:

            messagebox.showerror(
                "Error en los datos",
                str(error)
            )

    def mostrar_resultado_axb(
        self,
        resultado
    ):

        datos = resultado[
            "resultado"
        ]

        matriz_a = datos[
            "matriz_a"
        ]

        vector_b = datos[
            "vector_b"
        ]

        matriz_aumentada = datos[
            "matriz_aumentada"
        ]

        matriz_reducida = datos[
            "matriz_reducida"
        ]

        tipo = datos[
            "tipo"
        ]

        solucion = datos[
            "solucion_formateada"
        ]

        columnas_pivote = datos[
            "columnas_pivote"
        ]

        variables_basicas = datos[
            "variables_basicas"
        ]

        variables_libres = datos[
            "variables_libres"
        ]

        historial = datos[
            "historial"
        ]

        verificacion = datos[
            "verificacion"
        ]

        posiciones_pivote = (
            self.obtener_posiciones_pivote_visuales(
                matriz_reducida
            )
        )

        numero_variables = len(
            matriz_a[0]
        )

        pivote_columna_aumentada = any(
            columna == numero_variables
            for fila, columna
            in posiciones_pivote
        )

        columnas_texto = [
            str(i + 1)
            for i in columnas_pivote
        ]

        posiciones_texto = [
            f"({fila + 1}, {columna + 1})"
            for fila, columna
            in posiciones_pivote
        ]

        basicas_texto = [
            "x"
            + self.numero_subindice(
                i + 1
            )
            for i in variables_basicas
        ]

        libres_texto = [
            "x"
            + self.numero_subindice(
                i + 1
            )
            for i in variables_libres
        ]

        self.marco_resultado_axb.pack(
            padx=12,
            pady=(4, 7),
            fill="both",
            expand=True
        )

        widget = self.txt_resultado_axb

        widget.configure(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END
        )

        widget.insert(
            tk.END,
            "Ecuación matricial Ax = b\n\n"
        )

        widget.insert(
            tk.END,
            "Clasificación del sistema:\n"
        )

        widget.insert(
            tk.END,
            self.nombre_tipo_sistema(
                tipo
            )
            + "\n\n"
        )

        widget.insert(
            tk.END,
            (
                "Columnas pivote de las variables: "
                + (
                    ", ".join(columnas_texto)
                    if columnas_texto
                    else "Ninguna"
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Pivote en la columna aumentada: "
                + (
                    "Sí"
                    if pivote_columna_aumentada
                    else "No"
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            (
                "Posiciones pivote: "
                + (
                    ", ".join(posiciones_texto)
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
                    ", ".join(basicas_texto)
                    if basicas_texto
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
                    ", ".join(libres_texto)
                    if libres_texto
                    else "Ninguna"
                )
                + "\n"
            )
        )

        widget.insert(
            tk.END,
            "\nSolución:\n"
        )

        for linea in solucion:

            widget.insert(
                tk.END,
                formatear_texto_matematico(
                    linea
                )
                + "\n"
            )

        widget.insert(
            tk.END,
            "\nMatriz A:\n"
        )

        widget.insert(
            tk.END,
            self.formatear_matriz(
                matriz_a
            )
            + "\n"
        )

        widget.insert(
            tk.END,
            "\nVector b:\n"
        )

        widget.insert(
            tk.END,
            self.formatear_vector(
                vector_b
            )
            + "\n"
        )

        widget.insert(
            tk.END,
            "\nMatriz aumentada [A|b]:\n"
        )

        widget.insert(
            tk.END,
            self.formatear_matriz_aumentada(
                matriz_aumentada
            )
            + "\n"
        )

        widget.insert(
            tk.END,
            (
                "\nForma escalonada reducida "
                "por filas (RREF):\n"
            )
        )

        self.insertar_matriz_aumentada_con_pivotes(
            widget,
            matriz_reducida,
            posiciones_pivote
        )

        widget.insert(
            tk.END,
            (
                "\nLos valores mostrados en rojo "
                "corresponden a posiciones pivote.\n"
            )
        )

        widget.insert(
            tk.END,
            "\nVerificación de la solución:\n"
        )

        widget.insert(
            tk.END,
            self.formatear_verificacion(
                verificacion
            )
        )

        widget.configure(
            state="disabled"
        )

        widget.see(
            "1.0"
        )

        self.mostrar_procedimiento(
            historial,
            self.txt_procedimiento_axb
        )

        self.cuaderno_axb.select(
            self.pestana_resultado_axb
        )

    def limpiar_axb(self):

        self.filas_axb.set(
            "2"
        )

        self.columnas_axb.set(
            "2"
        )

        self.entradas_matriz_axb = []
        self.entradas_vector_b_axb = []

        for elemento in (
            self.marco_matriz_axb.winfo_children()
        ):
            elemento.destroy()

        for elemento in (
            self.marco_vector_b_axb.winfo_children()
        ):
            elemento.destroy()

        self.marco_entrada_axb.pack_forget()
        self.marco_acciones_axb.pack_forget()
        self.marco_resultado_axb.pack_forget()

        self.colocar_texto(
            self.txt_resultado_axb,
            ""
        )

        self.colocar_texto(
            self.txt_procedimiento_axb,
            ""
        )

        self.cuaderno_axb.select(
            self.pestana_resultado_axb
        )