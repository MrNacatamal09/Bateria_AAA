import tkinter as tk
from tkinter import ttk, messagebox

from controladores.programa_1_controller import procesar_sistema


class Programa1Interfaz:

    def __init__(self, ventana):
        self.ventana = ventana

        self.numero_ecuaciones = tk.StringVar()
        self.numero_variables = tk.StringVar()

        self.metodo = tk.StringVar(
            value="gauss"
        )

        self.ecuaciones = 0
        self.variables = 0

        self.entradas_matriz = []

        self.ultimo_resultado = None

        self.configurar_ventana()
        self.crear_interfaz()

    # Configuración principal de la ventana
    def configurar_ventana(self):

        self.ventana.title(
            "Calculadora de Álgebra Lineal - Programa 1"
        )

        self.ventana.geometry(
            "1000x700"
        )

        self.ventana.minsize(
            900,
            600
        )

    # Construcción inicial de la interfaz
    def crear_interfaz(self):

        titulo = ttk.Label(
            self.ventana,
            text="Programa 1 - Sistemas de Ecuaciones Lineales",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=(20, 5)
        )

        subtitulo = ttk.Label(
            self.ventana,
            text="Eliminación por filas",
            font=("Arial", 12)
        )

        subtitulo.pack(
            pady=(0, 20)
        )

        # Contenedor para las dimensiones del sistema
        marco_dimensiones = ttk.LabelFrame(
            self.ventana,
            text="Dimensiones del sistema",
            padding=15
        )

        marco_dimensiones.pack(
            padx=20,
            pady=10
        )

        # Número de ecuaciones
        lbl_ecuaciones = ttk.Label(
            marco_dimensiones,
            text="Número de ecuaciones:"
        )

        lbl_ecuaciones.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        txt_ecuaciones = ttk.Entry(
            marco_dimensiones,
            textvariable=self.numero_ecuaciones,
            width=10
        )

        txt_ecuaciones.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # Número de variables
        lbl_variables = ttk.Label(
            marco_dimensiones,
            text="Número de variables:"
        )

        lbl_variables.grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        txt_variables = ttk.Entry(
            marco_dimensiones,
            textvariable=self.numero_variables,
            width=10
        )

        txt_variables.grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        # Botón para crear la matriz
        btn_crear = ttk.Button(
            marco_dimensiones,
            text="Crear matriz",
            command=self.validar_dimensiones
        )

        btn_crear.grid(
            row=0,
            column=4,
            padx=15,
            pady=10
        )

        # Mensaje de estado
        self.lbl_estado = ttk.Label(
            self.ventana,
            text=""
        )

        self.lbl_estado.pack(
            pady=10
        )

        # Contenedor donde se generará la matriz
        self.marco_matriz = ttk.LabelFrame(
            self.ventana,
            text="Matriz aumentada",
            padding=15
        )

        # Contenedor de las opciones de resolución
        self.marco_acciones = ttk.LabelFrame(
            self.ventana,
            text="Método de resolución",
            padding=10
        )

        # Método Gauss
        rb_gauss = ttk.Radiobutton(
            self.marco_acciones,
            text="Gauss",
            variable=self.metodo,
            value="gauss"
        )

        rb_gauss.grid(
            row=0,
            column=0,
            padx=10,
            pady=5
        )

        # Método Gauss-Jordan
        rb_gauss_jordan = ttk.Radiobutton(
            self.marco_acciones,
            text="Gauss-Jordan",
            variable=self.metodo,
            value="gauss_jordan"
        )

        rb_gauss_jordan.grid(
            row=0,
            column=1,
            padx=10,
            pady=5
        )

        # Botón resolver
        btn_resolver = ttk.Button(
            self.marco_acciones,
            text="Resolver sistema",
            command=self.resolver_desde_interfaz
        )

        btn_resolver.grid(
            row=0,
            column=2,
            padx=20,
            pady=5
        )

        # Contenedor general de resultados
        self.marco_resultado = ttk.LabelFrame(
            self.ventana,
            text="Resolución del sistema",
            padding=10
        )

        # Pestañas de resultado y procedimiento
        self.cuaderno_resultados = ttk.Notebook(
            self.marco_resultado
        )

        self.cuaderno_resultados.pack(
            fill="both",
            expand=True
        )

        # Pestaña del resultado final
        self.pestana_resultado = ttk.Frame(
            self.cuaderno_resultados
        )

        # Pestaña del procedimiento
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

        # Configuramos la pestaña de resultado
        self.pestana_resultado.rowconfigure(
            0,
            weight=1
        )

        self.pestana_resultado.columnconfigure(
            0,
            weight=1
        )

        # Área de texto del resultado
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

        # Barra vertical del resultado
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

        # Barra horizontal del resultado
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
            yscrollcommand=scroll_resultado_vertical.set,
            xscrollcommand=scroll_resultado_horizontal.set
        )

        # Configuramos la pestaña del procedimiento
        self.pestana_procedimiento.rowconfigure(
            0,
            weight=1
        )

        self.pestana_procedimiento.columnconfigure(
            0,
            weight=1
        )

        # Área de texto del historial
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

        # Barra vertical del historial
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

        # Barra horizontal del historial
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
            yscrollcommand=scroll_historial_vertical.set,
            xscrollcommand=scroll_historial_horizontal.set
        )

    # Validamos el número de ecuaciones y variables
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

    # Generamos las casillas de la matriz aumentada
    def crear_matriz(self):

        # Limpiamos una matriz anterior
        for elemento in self.marco_matriz.winfo_children():
            elemento.destroy()

        self.entradas_matriz = []

        # Ocultamos resultados anteriores
        self.marco_resultado.pack_forget()

        self.ultimo_resultado = None

        # Mostramos el contenedor
        self.marco_matriz.pack(
            padx=20,
            pady=15
        )

        # Encabezados de las variables
        for columna in range(self.variables):

            encabezado = ttk.Label(
                self.marco_matriz,
                text=f"x{columna + 1}"
            )

            encabezado.grid(
                row=0,
                column=columna + 1,
                padx=5,
                pady=5
            )

        # Separador de la matriz aumentada
        separador = ttk.Label(
            self.marco_matriz,
            text="|"
        )

        separador.grid(
            row=0,
            column=self.variables + 1,
            padx=5
        )

        # Encabezado del término independiente
        termino = ttk.Label(
            self.marco_matriz,
            text="b"
        )

        termino.grid(
            row=0,
            column=self.variables + 2,
            padx=5,
            pady=5
        )

        # Creamos las filas
        for fila in range(self.ecuaciones):

            fila_entradas = []

            lbl_fila = ttk.Label(
                self.marco_matriz,
                text=f"E{fila + 1}"
            )

            lbl_fila.grid(
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
            barra = ttk.Label(
                self.marco_matriz,
                text="|"
            )

            barra.grid(
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

        # Mostramos las opciones para resolver
        self.marco_acciones.pack(
            padx=20,
            pady=10
        )

    # Leemos los valores escritos en la matriz
    def leer_datos_matriz(self):

        datos = []

        for fila in self.entradas_matriz:

            valores_fila = []

            for entrada in fila:

                valores_fila.append(
                    entrada.get()
                )

            datos.append(
                valores_fila
            )

        return datos

    # Enviamos los datos al controlador
    def resolver_desde_interfaz(self):

        try:

            datos = self.leer_datos_matriz()

            resultado = procesar_sistema(
                datos,
                self.ecuaciones,
                self.variables,
                self.metodo.get()
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

            linea = (
                f"[ {izquierda}  |  "
                f"{termino_independiente} ]"
            )

            lineas.append(
                linea
            )

        return "\n".join(
            lineas
        )

    # Formateamos la verificación automática
    def formatear_verificacion(self, verificacion):

        if not verificacion["aplica"]:

            return (
                "La verificación numérica no aplica "
                "para este tipo de sistema."
            )

        lineas = []

        for ecuacion in verificacion["ecuaciones"]:

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
    def mostrar_resultado(self, resultado):

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

        metodo = resultado[
            "metodo"
        ]

        clasificacion = resultado[
            "clasificacion"
        ]

        solucion = resultado[
            "solucion_formateada"
        ]

        matriz_original = resultado[
            "matriz_original"
        ]

        matriz_resultado = resultado[
            "matriz_resultado"
        ]

        verificacion = resultado[
            "verificacion"
        ]

        # Nombre visible del método
        if metodo == "gauss":

            nombre_metodo = "Gauss"

            nombre_matriz_final = (
                "Matriz escalonada"
            )

        else:

            nombre_metodo = "Gauss-Jordan"

            nombre_matriz_final = (
                "Matriz escalonada reducida"
            )

        nombre_clasificacion = clasificacion[
            "nombre"
        ]

        descripcion = clasificacion[
            "descripcion"
        ]

        variables_basicas = clasificacion.get(
            "variables_basicas",
            []
        )

        variables_libres = clasificacion.get(
            "variables_libres",
            []
        )

        # Convertimos índices a nombres de variables
        basicas_texto = []

        for variable in variables_basicas:

            basicas_texto.append(
                f"x{variable + 1}"
            )

        libres_texto = []

        for variable in variables_libres:

            libres_texto.append(
                f"x{variable + 1}"
            )

        # Construimos el resumen
        texto = (
            f"Método utilizado: {nombre_metodo}\n\n"
            f"Clasificación del sistema:\n"
            f"{nombre_clasificacion}\n"
            f"{descripcion}\n\n"
        )

        # Variables básicas
        if basicas_texto:

            texto += (
                "Variables básicas: "
                + ", ".join(basicas_texto)
                + "\n"
            )

        else:

            texto += (
                "Variables básicas: Ninguna\n"
            )

        # Variables libres
        if libres_texto:

            texto += (
                "Variables libres: "
                + ", ".join(libres_texto)
                + "\n"
            )

        else:

            texto += (
                "Variables libres: Ninguna\n"
            )

        # Solución
        texto += (
            "\nSolución:\n"
        )

        if isinstance(
            solucion,
            (list, tuple)
        ):

            for linea in solucion:

                texto += (
                    str(linea)
                    + "\n"
                )

        else:

            texto += (
                str(solucion)
                + "\n"
            )

        # Matriz inicial
        texto += (
            "\nMatriz aumentada inicial:\n"
        )

        texto += self.formatear_matriz(
            matriz_original
        )

        # Matriz final
        texto += (
            f"\n\n{nombre_matriz_final}:\n"
        )

        texto += self.formatear_matriz(
            matriz_resultado
        )

        # Verificación
        texto += (
            "\n\nVerificación de la solución:\n"
        )

        texto += self.formatear_verificacion(
            verificacion
        )

        self.txt_resultado.insert(
            tk.END,
            texto
        )

        self.txt_resultado.config(
            state="disabled"
        )

        # Regresamos el desplazamiento al inicio
        self.txt_resultado.see(
            "1.0"
        )

    # Mostramos las operaciones por filas paso a paso
    def mostrar_historial(self, resultado):

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

        # En caso de que no existan pasos registrados
        if not historial:

            self.txt_historial.insert(
                tk.END,
                "No existen operaciones registradas."
            )

            self.txt_historial.config(
                state="disabled"
            )

            return

        lineas = []

        lineas.append(
            "PROCEDIMIENTO DE ELIMINACIÓN POR FILAS"
        )

        lineas.append(
            "=" * 45
        )

        lineas.append(
            ""
        )

        # Recorremos cada paso guardado
        for indice in range(
            len(historial)
        ):

            paso = historial[
                indice
            ]

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

            # Matriz obtenida en ese paso
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

            # Resultado de la verificación interna del paso
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

        texto_historial = "\n".join(
            lineas
        )

        self.txt_historial.insert(
            tk.END,
            texto_historial
        )

        self.txt_historial.config(
            state="disabled"
        )

        # Mostramos el historial desde el inicio
        self.txt_historial.see(
            "1.0"
        )


# Permite probar esta interfaz como módulo
if __name__ == "__main__":

    ventana = tk.Tk()

    app = Programa1Interfaz(
        ventana
    )

    ventana.mainloop()