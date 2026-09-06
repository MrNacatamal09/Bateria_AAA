import tkinter as tk
from tkinter import ttk, messagebox

from controladores.programa_2_controller import (
    procesar_programa_2
)

from utilidades.formato_interfaz import (
    nombre_variable,
    formatear_texto_matematico
)


class Programa2Interfaz(ttk.Frame):

    def __init__(self, contenedor):
        super().__init__(contenedor)

        self.numero_ecuaciones = tk.StringVar()
        self.numero_variables = tk.StringVar()

        self.ecuaciones = 0
        self.variables = 0

        self.entradas_matriz = []

        self.ultimo_resultado = None

        self.crear_interfaz()

    # Construimos la interfaz del Programa 2
    def crear_interfaz(self):

        titulo = ttk.Label(
            self,
            text="Programa 2 - Forma Escalonada Reducida",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=(20, 5)
        )

        subtitulo = ttk.Label(
            self,
            text=(
                "Gauss-Jordan e identificación "
                "de columnas pivote"
            ),
            font=("Arial", 12)
        )

        subtitulo.pack(
            pady=(0, 20)
        )

        # ==================================================
        # DIMENSIONES DEL SISTEMA
        # ==================================================

        marco_dimensiones = ttk.LabelFrame(
            self,
            text="Dimensiones del sistema",
            padding=15
        )

        marco_dimensiones.pack(
            padx=20,
            pady=10
        )

        ttk.Label(
            marco_dimensiones,
            text="Número de ecuaciones:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        ttk.Entry(
            marco_dimensiones,
            textvariable=self.numero_ecuaciones,
            width=10
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            marco_dimensiones,
            text="Número de variables:"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        ttk.Entry(
            marco_dimensiones,
            textvariable=self.numero_variables,
            width=10
        ).grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        ttk.Button(
            marco_dimensiones,
            text="Crear matriz",
            command=self.validar_dimensiones
        ).grid(
            row=0,
            column=4,
            padx=15,
            pady=10
        )

        # Mensaje de estado
        self.lbl_estado = ttk.Label(
            self,
            text=""
        )

        self.lbl_estado.pack(
            pady=10
        )

        # ==================================================
        # MATRIZ AUMENTADA CON SCROLL
        # ==================================================

        self.marco_matriz_contenedor = ttk.LabelFrame(
            self,
            text="Matriz aumentada",
            padding=5
        )

        self.marco_matriz_contenedor.rowconfigure(
            0,
            weight=1
        )

        self.marco_matriz_contenedor.columnconfigure(
            0,
            weight=1
        )

        # Canvas que permite desplazamiento
        self.canvas_matriz = tk.Canvas(
            self.marco_matriz_contenedor,
            height=220,
            highlightthickness=0
        )

        self.canvas_matriz.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # Scroll vertical
        self.scroll_matriz_vertical = ttk.Scrollbar(
            self.marco_matriz_contenedor,
            orient="vertical",
            command=self.canvas_matriz.yview
        )

        self.scroll_matriz_vertical.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        # Scroll horizontal
        self.scroll_matriz_horizontal = ttk.Scrollbar(
            self.marco_matriz_contenedor,
            orient="horizontal",
            command=self.canvas_matriz.xview
        )

        self.scroll_matriz_horizontal.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.canvas_matriz.config(
            yscrollcommand=
                self.scroll_matriz_vertical.set,

            xscrollcommand=
                self.scroll_matriz_horizontal.set
        )

        # Frame donde realmente se crean las casillas
        self.marco_matriz = ttk.Frame(
            self.canvas_matriz
        )

        self.canvas_matriz.create_window(
            (0, 0),
            window=self.marco_matriz,
            anchor="nw"
        )

        self.marco_matriz.bind(
            "<Configure>",
            self.actualizar_scroll_matriz
        )

        # ==================================================
        # ACCIONES
        # ==================================================

        self.marco_acciones = ttk.LabelFrame(
            self,
            text="Procesamiento",
            padding=10
        )

        ttk.Label(
            self.marco_acciones,
            text="Método: Gauss-Jordan"
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=5
        )

        ttk.Button(
            self.marco_acciones,
            text="Reducir matriz",
            command=self.resolver_desde_interfaz
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=5
        )

        ttk.Button(
            self.marco_acciones,
            text="Limpiar",
            command=self.limpiar
        ).grid(
            row=0,
            column=2,
            padx=15,
            pady=5
        )

        # ==================================================
        # RESULTADOS
        # ==================================================

        self.marco_resultado = ttk.LabelFrame(
            self,
            text="Análisis de la matriz",
            padding=10
        )

        self.cuaderno_resultados = ttk.Notebook(
            self.marco_resultado
        )

        self.cuaderno_resultados.pack(
            fill="both",
            expand=True
        )

        # Pestaña Resultado
        self.pestana_resultado = ttk.Frame(
            self.cuaderno_resultados
        )

        # Pestaña Procedimiento
        self.pestana_procedimiento = ttk.Frame(
            self.cuaderno_resultados
        )

        self.cuaderno_resultados.add(
            self.pestana_resultado,
            text="Resultado"
        )

        self.cuaderno_resultados.add(
            self.pestana_procedimiento,
            text="Procedimiento"
        )

        # ==================================================
        # PESTAÑA RESULTADO
        # ==================================================

        self.pestana_resultado.rowconfigure(
            0,
            weight=1
        )

        self.pestana_resultado.columnconfigure(
            0,
            weight=1
        )

        self.txt_resultado = tk.Text(
            self.pestana_resultado,
            width=80,
            height=16,
            wrap="none",
            state="disabled"
        )

        self.txt_resultado.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # Scroll vertical del resultado
        scroll_resultado_vertical = ttk.Scrollbar(
            self.pestana_resultado,
            orient="vertical",
            command=self.txt_resultado.yview
        )

        scroll_resultado_vertical.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        # Scroll horizontal del resultado
        scroll_resultado_horizontal = ttk.Scrollbar(
            self.pestana_resultado,
            orient="horizontal",
            command=self.txt_resultado.xview
        )

        scroll_resultado_horizontal.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.txt_resultado.config(
            yscrollcommand=
                scroll_resultado_vertical.set,

            xscrollcommand=
                scroll_resultado_horizontal.set
        )

        # Estilo visual para los pivotes
        self.txt_resultado.tag_configure(
            "pivote",
            foreground="red"
        )

        # ==================================================
        # PESTAÑA PROCEDIMIENTO
        # ==================================================

        self.pestana_procedimiento.rowconfigure(
            0,
            weight=1
        )

        self.pestana_procedimiento.columnconfigure(
            0,
            weight=1
        )

        self.txt_historial = tk.Text(
            self.pestana_procedimiento,
            width=80,
            height=16,
            wrap="none",
            state="disabled"
        )

        self.txt_historial.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # Scroll vertical del historial
        scroll_historial_vertical = ttk.Scrollbar(
            self.pestana_procedimiento,
            orient="vertical",
            command=self.txt_historial.yview
        )

        scroll_historial_vertical.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        # Scroll horizontal del historial
        scroll_historial_horizontal = ttk.Scrollbar(
            self.pestana_procedimiento,
            orient="horizontal",
            command=self.txt_historial.xview
        )

        scroll_historial_horizontal.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.txt_historial.config(
            yscrollcommand=
                scroll_historial_vertical.set,

            xscrollcommand=
                scroll_historial_horizontal.set
        )

    # Actualizamos el área desplazable de la matriz
    def actualizar_scroll_matriz(
        self,
        evento=None
    ):

        self.canvas_matriz.configure(
            scrollregion=
                self.canvas_matriz.bbox("all")
        )

    # Validamos las dimensiones
    def validar_dimensiones(self):

        try:

            ecuaciones = int(
                self.numero_ecuaciones.get()
            )

            variables = int(
                self.numero_variables.get()
            )

            if ecuaciones <= 0 or variables <= 0:

                messagebox.showerror(
                    "Datos inválidos",
                    "El número de ecuaciones y variables "
                    "debe ser mayor que cero."
                )

                return

            self.ecuaciones = ecuaciones
            self.variables = variables

            self.lbl_estado.config(
                text=(
                    f"Sistema de {self.ecuaciones} ecuaciones "
                    f"y {self.variables} variables."
                )
            )

            self.crear_matriz()

        except ValueError:

            messagebox.showerror(
                "Datos inválidos",
                "Debe ingresar números enteros."
            )

    # Creamos dinámicamente la matriz aumentada
    def crear_matriz(self):

        # Limpiamos una matriz anterior
        for elemento in self.marco_matriz.winfo_children():

            elemento.destroy()

        self.entradas_matriz = []
        self.ultimo_resultado = None

        # Ocultamos resultados anteriores
        self.marco_resultado.pack_forget()

        # Mostramos el contenedor de la matriz
        self.marco_matriz_contenedor.pack(
            padx=20,
            pady=15,
            fill="x"
        )

        # Encabezados x₁, x₂, x₃...
        for columna in range(self.variables):

            ttk.Label(
                self.marco_matriz,
                text=nombre_variable(
                    columna + 1
                )
            ).grid(
                row=0,
                column=columna + 1,
                padx=5,
                pady=5
            )

        # Separador de la matriz aumentada
        ttk.Label(
            self.marco_matriz,
            text="|"
        ).grid(
            row=0,
            column=self.variables + 1,
            padx=5
        )

        # Término independiente
        ttk.Label(
            self.marco_matriz,
            text="b"
        ).grid(
            row=0,
            column=self.variables + 2,
            padx=5,
            pady=5
        )

        # Creamos las filas
        for fila in range(self.ecuaciones):

            fila_entradas = []

            # Nombre de la ecuación
            ttk.Label(
                self.marco_matriz,
                text=f"E{fila + 1}"
            ).grid(
                row=fila + 1,
                column=0,
                padx=5,
                pady=5
            )

            # Coeficientes
            for columna in range(self.variables):

                entrada = ttk.Entry(
                    self.marco_matriz,
                    width=8,
                    justify="center"
                )

                entrada.grid(
                    row=fila + 1,
                    column=columna + 1,
                    padx=5,
                    pady=5
                )

                fila_entradas.append(
                    entrada
                )

            # Separador visual
            ttk.Label(
                self.marco_matriz,
                text="|"
            ).grid(
                row=fila + 1,
                column=self.variables + 1,
                padx=5
            )

            # Término independiente
            entrada_independiente = ttk.Entry(
                self.marco_matriz,
                width=8,
                justify="center"
            )

            entrada_independiente.grid(
                row=fila + 1,
                column=self.variables + 2,
                padx=5,
                pady=5
            )

            fila_entradas.append(
                entrada_independiente
            )

            self.entradas_matriz.append(
                fila_entradas
            )

        # Actualizamos el área desplazable
        self.update_idletasks()

        self.actualizar_scroll_matriz()

        # Regresamos al inicio del scroll
        self.canvas_matriz.xview_moveto(
            0
        )

        self.canvas_matriz.yview_moveto(
            0
        )

        # Mostramos las acciones
        self.marco_acciones.pack(
            padx=20,
            pady=10
        )

    # Leemos los datos de la matriz
    def leer_datos_matriz(self):

        datos = []

        for fila in self.entradas_matriz:

            valores = []

            for entrada in fila:

                valores.append(
                    entrada.get()
                )

            datos.append(
                valores
            )

        return datos

    # Ejecutamos el Programa 2
    def resolver_desde_interfaz(self):

        try:

            if not self.entradas_matriz:

                raise ValueError(
                    "Primero debe crear la matriz."
                )

            datos = self.leer_datos_matriz()

            resultado = procesar_programa_2(
                datos,
                self.ecuaciones,
                self.variables
            )

            self.ultimo_resultado = resultado

            self.mostrar_resultado(
                resultado
            )

            self.mostrar_historial(
                resultado
            )

        except ValueError as error:

            messagebox.showerror(
                "Error en los datos",
                str(error)
            )

    # Convertimos una matriz a texto
    def formatear_matriz(self, matriz):

        lineas = []

        for fila in matriz:

            coeficientes = fila[:-1]

            termino_independiente = fila[-1]

            izquierda = "   ".join(
                str(valor)
                for valor in coeficientes
            )

            lineas.append(
                f"[ {izquierda}  |  "
                f"{termino_independiente} ]"
            )

        return "\n".join(
            lineas
        )

    # Insertamos una matriz y resaltamos sus pivotes
    def insertar_matriz_con_pivotes(
        self,
        widget,
        matriz,
        posiciones_pivote=None
    ):

        if posiciones_pivote is None:

            posiciones_pivote = []

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

            # Coeficientes de las variables
            for j in range(
                len(fila) - 1
            ):

                valor = str(
                    fila[j]
                )

                # Si la posición es pivote,
                # mostramos el valor en rojo
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

            # Separador de la matriz aumentada
            widget.insert(
                tk.END,
                "  |  "
            )

            columna_aumentada = (
                len(fila) - 1
            )

            termino_independiente = str(
                fila[-1]
            )

            # También resaltamos un pivote
            # en la columna aumentada
            if (
                i,
                columna_aumentada
            ) in posiciones:

                widget.insert(
                    tk.END,
                    termino_independiente,
                    "pivote"
                )

            else:

                widget.insert(
                    tk.END,
                    termino_independiente
                )

            widget.insert(
                tk.END,
                " ]\n"
            )

    # Nombre visible del tipo de sistema
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

    # Formateamos la verificación
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

            numero = ecuacion[
                "ecuacion"
            ]

            lado_izquierdo = ecuacion[
                "lado_izquierdo"
            ]

            lado_derecho = ecuacion[
                "lado_derecho"
            ]

            correcta = ecuacion[
                "correcta"
            ]

            if correcta:

                estado = "Correcta"

            else:

                estado = "Incorrecta"

            lineas.append(
                f"Ecuación {numero}: "
                f"{lado_izquierdo} = "
                f"{lado_derecho} "
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

    # Mostramos el resultado final
    def mostrar_resultado(
        self,
        resultado
    ):

        self.marco_resultado.pack(
            padx=20,
            pady=15,
            fill="both",
            expand=True
        )

        self.txt_resultado.config(
            state="normal"
        )

        self.txt_resultado.delete(
            "1.0",
            tk.END
        )

        # Datos recibidos desde la lógica
        matriz_original = resultado[
            "matriz_original"
        ]

        matriz_reducida = resultado[
            "matriz_reducida"
        ]

        columnas_pivote = resultado[
            "columnas_pivote"
        ]

        posiciones_pivote = resultado[
            "posiciones_pivote"
        ]

        pivote_columna_aumentada = resultado[
            "pivote_columna_aumentada"
        ]

        variables_basicas = resultado[
            "variables_basicas"
        ]

        variables_libres = resultado[
            "variables_libres"
        ]

        tipo = resultado[
            "tipo"
        ]

        solucion = resultado[
            "solucion_formateada"
        ]

        verificacion = resultado[
            "verificacion"
        ]

        # Columnas pivote
        columnas_texto = []

        for columna in columnas_pivote:

            columnas_texto.append(
                str(columna + 1)
            )

        # Posiciones pivote
        posiciones_texto = []

        for fila, columna in posiciones_pivote:

            posiciones_texto.append(
                f"({fila + 1}, {columna + 1})"
            )

        # Variables básicas
        basicas_texto = []

        for variable in variables_basicas:

            basicas_texto.append(
                nombre_variable(
                    variable + 1
                )
            )

        # Variables libres
        libres_texto = []

        for variable in variables_libres:

            libres_texto.append(
                nombre_variable(
                    variable + 1
                )
            )

        # Método utilizado
        self.txt_resultado.insert(
            tk.END,
            "Método utilizado: Gauss-Jordan\n\n"
        )

        # Clasificación
        self.txt_resultado.insert(
            tk.END,
            "Clasificación del sistema:\n"
        )

        self.txt_resultado.insert(
            tk.END,
            (
                self.nombre_tipo_sistema(
                    tipo
                )
                + "\n\n"
            )
        )

        # Columnas pivote de variables
        if columnas_texto:

            self.txt_resultado.insert(
                tk.END,
                (
                    "Columnas pivote de las variables: "
                    + ", ".join(columnas_texto)
                    + "\n"
                )
            )

        else:

            self.txt_resultado.insert(
                tk.END,
                (
                    "Columnas pivote de las variables: "
                    "Ninguna\n"
                )
            )

        # Pivote en columna aumentada
        if pivote_columna_aumentada:

            self.txt_resultado.insert(
                tk.END,
                "Pivote en la columna aumentada: Sí\n"
            )

        else:

            self.txt_resultado.insert(
                tk.END,
                "Pivote en la columna aumentada: No\n"
            )

        # Posiciones pivote
        if posiciones_texto:

            self.txt_resultado.insert(
                tk.END,
                (
                    "Posiciones pivote: "
                    + ", ".join(posiciones_texto)
                    + "\n"
                )
            )

        else:

            self.txt_resultado.insert(
                tk.END,
                "Posiciones pivote: Ninguna\n"
            )

        # Variables básicas
        if basicas_texto:

            self.txt_resultado.insert(
                tk.END,
                (
                    "Variables básicas: "
                    + ", ".join(basicas_texto)
                    + "\n"
                )
            )

        else:

            self.txt_resultado.insert(
                tk.END,
                "Variables básicas: Ninguna\n"
            )

        # Variables libres
        if libres_texto:

            self.txt_resultado.insert(
                tk.END,
                (
                    "Variables libres: "
                    + ", ".join(libres_texto)
                    + "\n"
                )
            )

        else:

            self.txt_resultado.insert(
                tk.END,
                "Variables libres: Ninguna\n"
            )

        # Solución
        self.txt_resultado.insert(
            tk.END,
            "\nSolución:\n"
        )

        if isinstance(
            solucion,
            (list, tuple)
        ):

            for linea in solucion:

                self.txt_resultado.insert(
                    tk.END,
                    (
                        formatear_texto_matematico(
                            linea
                        )
                        + "\n"
                    )
                )

        else:

            self.txt_resultado.insert(
                tk.END,
                (
                    formatear_texto_matematico(
                        solucion
                    )
                    + "\n"
                )
            )

        # Matriz aumentada inicial
        self.txt_resultado.insert(
            tk.END,
            "\nMatriz aumentada inicial:\n"
        )

        self.insertar_matriz_con_pivotes(
            self.txt_resultado,
            matriz_original
        )

        # RREF
        self.txt_resultado.insert(
            tk.END,
            (
                "\nForma Escalonada Reducida "
                "por Filas (RREF):\n"
            )
        )

        # Aquí resaltamos los pivotes en rojo
        self.insertar_matriz_con_pivotes(
            self.txt_resultado,
            matriz_reducida,
            posiciones_pivote
        )

        # Leyenda
        self.txt_resultado.insert(
            tk.END,
            (
                "\nLos valores mostrados en rojo "
                "corresponden a posiciones pivote.\n"
            )
        )

        # Verificación final
        self.txt_resultado.insert(
            tk.END,
            "\nVerificación de la solución:\n"
        )

        self.txt_resultado.insert(
            tk.END,
            self.formatear_verificacion(
                verificacion
            )
        )

        # Bloqueamos nuevamente el Text
        self.txt_resultado.config(
            state="disabled"
        )

        # Regresamos al inicio
        self.txt_resultado.see(
            "1.0"
        )

        # Seleccionamos Resultado
        self.cuaderno_resultados.select(
            self.pestana_resultado
        )

    # Mostramos el procedimiento completo
    def mostrar_historial(
        self,
        resultado
    ):

        historial = resultado[
            "historial"
        ]

        self.txt_historial.config(
            state="normal"
        )

        self.txt_historial.delete(
            "1.0",
            tk.END
        )

        # Si no existen operaciones
        if not historial:

            self.txt_historial.insert(
                tk.END,
                "No existen operaciones registradas."
            )

            self.txt_historial.config(
                state="disabled"
            )

            return

        lineas = [
            "PROCEDIMIENTO DE GAUSS-JORDAN",
            "=" * 45,
            ""
        ]

        # Recorremos todos los pasos
        for indice, paso in enumerate(
            historial
        ):

            operacion = paso.get(
                "operacion",
                "Operación no especificada"
            )

            matriz = paso.get(
                "matriz",
                []
            )

            verificada = paso.get(
                "verificada"
            )

            # Número del paso
            if indice == 0:

                lineas.append(
                    "Paso 0 - Matriz inicial"
                )

            else:

                lineas.append(
                    f"Paso {indice}"
                )

            lineas.append(
                f"Operación: {operacion}"
            )

            lineas.append(
                ""
            )

            # Matriz correspondiente al paso
            if matriz:

                lineas.append(
                    self.formatear_matriz(
                        matriz
                    )
                )

            else:

                lineas.append(
                    "No hay matriz registrada."
                )

            # Verificación del paso
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

        self.txt_historial.insert(
            tk.END,
            "\n".join(lineas)
        )

        self.txt_historial.config(
            state="disabled"
        )

        # Regresamos al inicio
        self.txt_historial.see(
            "1.0"
        )

    # Limpiamos completamente Programa 2
    def limpiar(self):

        self.numero_ecuaciones.set("")
        self.numero_variables.set("")

        self.ecuaciones = 0
        self.variables = 0

        self.entradas_matriz = []

        self.ultimo_resultado = None

        # Eliminamos las casillas
        for elemento in self.marco_matriz.winfo_children():

            elemento.destroy()

        # Reiniciamos los scroll
        self.canvas_matriz.xview_moveto(
            0
        )

        self.canvas_matriz.yview_moveto(
            0
        )

        # Ocultamos secciones
        self.marco_matriz_contenedor.pack_forget()

        self.marco_acciones.pack_forget()

        self.marco_resultado.pack_forget()

        # Limpiamos el estado
        self.lbl_estado.config(
            text=""
        )

        # Limpiamos Resultado
        self.txt_resultado.config(
            state="normal"
        )

        self.txt_resultado.delete(
            "1.0",
            tk.END
        )

        self.txt_resultado.config(
            state="disabled"
        )

        # Limpiamos Procedimiento
        self.txt_historial.config(
            state="normal"
        )

        self.txt_historial.delete(
            "1.0",
            tk.END
        )

        self.txt_historial.config(
            state="disabled"
        )

        # Regresamos a la pestaña Resultado
        self.cuaderno_resultados.select(
            self.pestana_resultado
        )