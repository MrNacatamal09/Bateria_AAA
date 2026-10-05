"""
Construye la interfaz gráfica del Programa 5 para el Módulo III.
Permite ejecutar operaciones, determinantes, inversas y propiedades.
Tema de clase: Álgebra de Matrices, Determinantes y Matriz Inversa.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from controladores.modulo_matrices_controller import (
    procesar_operacion_basica,
    procesar_multiplicacion_matrices,
    procesar_transpuesta,
    procesar_determinante_programa_5,
    procesar_inversa_gauss_jordan_programa_5,
    procesar_inversa_adjunta_programa_5,
    procesar_propiedad_programa_5
)

from utilidades.formato_determinantes import (
    formatear_matriz,
    formatear_procedimiento_determinante,
    formatear_sarrus,
    formatear_triangular,
    formatear_comparacion_determinantes
)

from utilidades.formato_inversa import (
    formatear_procedimiento_inversa
)

from utilidades.formato_inversa_adjunta import (
    formatear_inversa_adjunta,
    formatear_comparacion_inversas
)

from utilidades.formato_propiedades_programa_5 import (
    formatear_propiedad
)


class EntradaMatriz(ttk.LabelFrame):
    """Gestiona una matriz editable con dimensiones configurables."""

    def __init__(
        self,
        contenedor,
        titulo,
        filas=2,
        columnas=2,
        cuadrada=False
    ):
        """Inicializa una entrada matricial con dimensiones configurables."""
        super().__init__(
            contenedor,
            text=titulo,
            padding=5
        )

        self.titulo = titulo
        self.cuadrada = cuadrada

        self.filas = tk.StringVar(
            value=str(filas)
        )

        self.columnas = tk.StringVar(
            value=str(columnas)
        )

        self.entradas = []

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye los controles de dimensión y el área desplazable."""
        controles = ttk.Frame(
            self
        )

        controles.pack(
            fill="x",
            pady=(0, 5)
        )

        if self.cuadrada:
            ttk.Label(
                controles,
                text="Orden n:"
            ).pack(
                side="left",
                padx=3
            )

            ttk.Entry(
                controles,
                textvariable=self.filas,
                width=6,
                justify="center"
            ).pack(
                side="left",
                padx=3
            )

        else:
            ttk.Label(
                controles,
                text="Filas:"
            ).pack(
                side="left",
                padx=3
            )

            ttk.Entry(
                controles,
                textvariable=self.filas,
                width=6,
                justify="center"
            ).pack(
                side="left",
                padx=3
            )

            ttk.Label(
                controles,
                text="Columnas:"
            ).pack(
                side="left",
                padx=3
            )

            ttk.Entry(
                controles,
                textvariable=self.columnas,
                width=6,
                justify="center"
            ).pack(
                side="left",
                padx=3
            )

        ttk.Button(
            controles,
            text="Crear matriz",
            command=self.crear_matriz
        ).pack(
            side="left",
            padx=6
        )

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
            height=140,
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
            self._actualizar_scroll
        )

        self.crear_matriz()

    def _actualizar_scroll(self, evento=None):
        """Actualiza el área desplazable cuando cambia el tamaño de la matriz."""
        self.canvas.configure(
            scrollregion=self.canvas.bbox(
                "all"
            )
        )

    def _obtener_dimensiones(self):
        """Valida y devuelve las dimensiones solicitadas por el usuario."""
        try:
            filas = int(
                self.filas.get()
            )

            columnas = (
                filas
                if self.cuadrada
                else int(
                    self.columnas.get()
                )
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
        """Crea las entradas de la matriz según las dimensiones indicadas."""
        try:
            filas, columnas = self._obtener_dimensiones()

        except ValueError as error:
            messagebox.showerror(
                "Dimensiones inválidas",
                str(error)
            )
            return

        for elemento in self.contenido.winfo_children():
            elemento.destroy()

        self.entradas = []

        for fila in range(filas):
            fila_entradas = []

            for columna in range(columnas):
                entrada = ttk.Entry(
                    self.contenido,
                    width=8,
                    justify="center"
                )

                entrada.grid(
                    row=fila,
                    column=columna,
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

        self._actualizar_scroll()

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

    def leer(self):
        """Devuelve el contenido escrito en las entradas de la matriz."""
        if not self.entradas:
            raise ValueError(
                f"Debe crear {self.titulo}."
            )

        matriz = []

        for fila_entradas in self.entradas:
            fila = []

            for entrada in fila_entradas:
                fila.append(
                    entrada.get()
                )

            matriz.append(
                fila
            )

        return matriz


class ModuloMatricesInterfaz(ttk.Frame):
    """Presenta las opciones 1 a 9 del Programa 5 mediante pestañas."""

    def __init__(self, contenedor):
        """Inicializa la interfaz gráfica con las opciones del Programa 5."""
        super().__init__(
            contenedor
        )

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye el encabezado y las nueve opciones del Programa 5."""
        ttk.Label(
            self,
            text="Programa 5 - Módulo III: Álgebra de Matrices",
            font=(
                "Arial",
                15,
                "bold"
            )
        ).pack(
            pady=(6, 2)
        )

        ttk.Label(
            self,
            text=(
                "Operaciones, determinantes, inversas "
                "y verificación de propiedades"
            )
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
            pady=5
        )

        self._crear_pestana_suma()
        self._crear_pestana_resta()
        self._crear_pestana_escalar()
        self._crear_pestana_producto()
        self._crear_pestana_transpuesta()
        self._crear_pestana_determinante()
        self._crear_pestana_gauss_jordan()
        self._crear_pestana_adjunta()
        self._crear_pestana_propiedades()

    def _crear_area_texto(self, contenedor):
        """Crea un área de resultados con desplazamiento vertical y horizontal."""
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
            wrap="none",
            state="disabled",
            font=(
                "Consolas",
                10
            )
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

    def _colocar_texto(self, widget, contenido):
        """Reemplaza el contenido de un área de texto de solo lectura."""
        widget.configure(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END
        )

        widget.insert(
            tk.END,
            contenido
        )

        widget.configure(
            state="disabled"
        )

        widget.see(
            "1.0"
        )

    def _crear_dos_matrices(
        self,
        contenedor,
        filas_a=2,
        columnas_a=2,
        filas_b=2,
        columnas_b=2
    ):
        """Crea dos entradas de matrices colocadas lado a lado."""
        marco = ttk.Frame(
            contenedor
        )

        marco.pack(
            fill="x",
            padx=8,
            pady=5
        )

        marco.columnconfigure(
            0,
            weight=1
        )

        marco.columnconfigure(
            1,
            weight=1
        )

        matriz_a = EntradaMatriz(
            marco,
            "Matriz A",
            filas_a,
            columnas_a
        )

        matriz_a.grid(
            row=0,
            column=0,
            padx=5,
            sticky="nsew"
        )

        matriz_b = EntradaMatriz(
            marco,
            "Matriz B",
            filas_b,
            columnas_b
        )

        matriz_b.grid(
            row=0,
            column=1,
            padx=5,
            sticky="nsew"
        )

        return matriz_a, matriz_b

    def _crear_pestana_suma(self):
        """Construye la opción 1 para sumar matrices."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="1. Suma"
        )

        self.suma_a, self.suma_b = self._crear_dos_matrices(
            pestana
        )

        ttk.Button(
            pestana,
            text="Calcular A + B",
            command=self._resolver_suma
        ).pack(
            pady=4
        )

        self.txt_suma = self._crear_area_texto(
            pestana
        )

    def _resolver_suma(self):
        """Ejecuta la suma de las matrices ingresadas."""
        try:
            resultado = procesar_operacion_basica(
                "suma",
                self.suma_a.leer(),
                self.suma_b.leer()
            )

            texto = (
                "A + B =\n\n"
                + formatear_matriz(
                    resultado["resultado"]
                )
            )

            self._colocar_texto(
                self.txt_suma,
                texto
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def _crear_pestana_resta(self):
        """Construye la opción 2 para restar matrices."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="2. Resta"
        )

        self.resta_a, self.resta_b = self._crear_dos_matrices(
            pestana
        )

        ttk.Button(
            pestana,
            text="Calcular A - B",
            command=self._resolver_resta
        ).pack(
            pady=4
        )

        self.txt_resta = self._crear_area_texto(
            pestana
        )

    def _resolver_resta(self):
        """Ejecuta la resta de las matrices ingresadas."""
        try:
            resultado = procesar_operacion_basica(
                "resta",
                self.resta_a.leer(),
                self.resta_b.leer()
            )

            texto = (
                "A - B =\n\n"
                + formatear_matriz(
                    resultado["resultado"]
                )
            )

            self._colocar_texto(
                self.txt_resta,
                texto
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def _crear_pestana_escalar(self):
        """Construye la opción 3 para multiplicar una matriz por un escalar."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="3. Multiplicación por Escalar"
        )

        self.escalar_a = EntradaMatriz(
            pestana,
            "Matriz A"
        )

        self.escalar_a.pack(
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
            text="Escalar:"
        ).pack(
            side="left",
            padx=4
        )

        self.valor_escalar = ttk.Entry(
            controles,
            width=10,
            justify="center"
        )

        self.valor_escalar.insert(
            0,
            "2"
        )

        self.valor_escalar.pack(
            side="left",
            padx=4
        )

        ttk.Button(
            controles,
            text="Calcular cA",
            command=self._resolver_escalar
        ).pack(
            side="left",
            padx=6
        )

        self.txt_escalar = self._crear_area_texto(
            pestana
        )

    def _resolver_escalar(self):
        """Ejecuta la multiplicación de una matriz por un escalar."""
        try:
            resultado = procesar_operacion_basica(
                "escalar",
                self.escalar_a.leer(),
                escalar=self.valor_escalar.get()
            )

            texto = (
                "c = "
                + str(
                    resultado["escalar"]
                )
                + "\n\n"
                + "cA =\n\n"
                + formatear_matriz(
                    resultado["resultado"]
                )
            )

            self._colocar_texto(
                self.txt_escalar,
                texto
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def _crear_pestana_producto(self):
        """Construye la opción 4 para calcular el producto matricial."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="4. Producto Matricial"
        )

        self.producto_a, self.producto_b = self._crear_dos_matrices(
            pestana,
            2,
            3,
            3,
            2
        )

        ttk.Button(
            pestana,
            text="Calcular A · B",
            command=self._resolver_producto
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

        pestana_resultado = ttk.Frame(
            resultados
        )

        pestana_procedimiento = ttk.Frame(
            resultados
        )

        resultados.add(
            pestana_resultado,
            text="Resultado"
        )

        resultados.add(
            pestana_procedimiento,
            text="Regla fila-columna"
        )

        self.txt_producto = self._crear_area_texto(
            pestana_resultado
        )

        self.txt_producto_procedimiento = self._crear_area_texto(
            pestana_procedimiento
        )

    def _resolver_producto(self):
        """Calcula AB y muestra el procedimiento fila-columna."""
        try:
            resultado = procesar_multiplicacion_matrices(
                self.producto_a.leer(),
                self.producto_b.leer()
            )

            texto = (
                "A · B =\n\n"
                + formatear_matriz(
                    resultado["resultado"]
                )
                + "\n\n"
                + "Dimensiones del resultado: "
                + str(
                    len(
                        resultado["resultado"]
                    )
                )
                + " × "
                + str(
                    len(
                        resultado["resultado"][0]
                    )
                )
            )

            self._colocar_texto(
                self.txt_producto,
                texto
            )

            procedimiento = self._formatear_producto(
                resultado["procedimiento"]
            )

            self._colocar_texto(
                self.txt_producto_procedimiento,
                procedimiento
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def _formatear_producto(self, pasos):
        """Convierte el procedimiento fila-columna en texto legible."""
        lineas = [
            "REGLA FILA-COLUMNA",
            "=" * 60,
            ""
        ]

        for paso in pasos:
            fila = (
                paso["fila_resultado"]
                + 1
            )

            columna = (
                paso["columna_resultado"]
                + 1
            )

            productos = []

            for producto in paso["productos"]:
                productos.append(
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

            lineas.append(
                f"Entrada ({fila}, {columna}):"
            )

            lineas.append(
                " + ".join(
                    productos
                )
                + " = "
                + str(
                    paso["resultado"]
                )
            )

            lineas.append("")

        return "\n".join(
            lineas
        )

    def _crear_pestana_transpuesta(self):
        """Construye la opción 5 para obtener la transpuesta."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="5. Transposición"
        )

        self.transpuesta_a = EntradaMatriz(
            pestana,
            "Matriz A",
            2,
            3
        )

        self.transpuesta_a.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Button(
            pestana,
            text="Calcular Aᵀ",
            command=self._resolver_transpuesta
        ).pack(
            pady=5
        )

        self.txt_transpuesta = self._crear_area_texto(
            pestana
        )

    def _resolver_transpuesta(self):
        """Obtiene y muestra la transpuesta de A."""
        try:
            resultado = procesar_transpuesta(
                self.transpuesta_a.leer()
            )

            texto = (
                "A =\n\n"
                + formatear_matriz(
                    resultado["matriz_a"]
                )
                + "\n\n"
                + "Aᵀ =\n\n"
                + formatear_matriz(
                    resultado["resultado"]
                )
            )

            self._colocar_texto(
                self.txt_transpuesta,
                texto
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def _crear_pestana_determinante(self):
        """Construye la opción 6 con los métodos de determinante."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="6. Determinante"
        )

        self.determinante_a = EntradaMatriz(
            pestana,
            "Matriz A",
            3,
            3,
            cuadrada=True
        )

        self.determinante_a.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Button(
            pestana,
            text="Calcular determinante",
            command=self._resolver_determinante
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
            pady=5
        )

        cof = ttk.Frame(
            resultados
        )

        sarrus = ttk.Frame(
            resultados
        )

        triangular = ttk.Frame(
            resultados
        )

        comparacion = ttk.Frame(
            resultados
        )

        resultados.add(
            cof,
            text="Cofactores"
        )

        resultados.add(
            sarrus,
            text="Sarrus 3×3"
        )

        resultados.add(
            triangular,
            text="Triangular"
        )

        resultados.add(
            comparacion,
            text="Comparación"
        )

        self.txt_cofactores = self._crear_area_texto(
            cof
        )

        self.txt_sarrus = self._crear_area_texto(
            sarrus
        )

        self.txt_triangular = self._crear_area_texto(
            triangular
        )

        self.txt_comparacion_det = self._crear_area_texto(
            comparacion
        )

    def _resolver_determinante(self):
        """Calcula el determinante por todos los métodos aplicables."""
        try:
            respuesta = procesar_determinante_programa_5(
                self.determinante_a.leer()
            )

            metodos = respuesta[
                "metodos"
            ]

            self._colocar_texto(
                self.txt_cofactores,
                formatear_procedimiento_determinante(
                    metodos["cofactores"]
                )
            )

            if metodos["sarrus"] is None:
                texto_sarrus = (
                    "La regla de Sarrus solamente "
                    "se aplica a matrices de orden 3."
                )

            else:
                texto_sarrus = formatear_sarrus(
                    metodos["sarrus"]
                )

            self._colocar_texto(
                self.txt_sarrus,
                texto_sarrus
            )

            self._colocar_texto(
                self.txt_triangular,
                formatear_triangular(
                    metodos["triangular"]
                )
            )

            comparacion = (
                formatear_comparacion_determinantes(
                    metodos
                )
                + "\n\n"
                + "Número de posiciones pivote: "
                + str(
                    respuesta[
                        "diagnostico"
                    ][
                        "num_pivotes"
                    ]
                )
                + "\n\n"
                + respuesta[
                    "diagnostico"
                ][
                    "diagnostico"
                ]
            )

            self._colocar_texto(
                self.txt_comparacion_det,
                comparacion
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def _crear_pestana_gauss_jordan(self):
        """Construye la opción 7 para calcular la inversa por Gauss-Jordan."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="7. Inversa por Gauss-Jordan"
        )

        self.gauss_a = EntradaMatriz(
            pestana,
            "Matriz A",
            3,
            3,
            cuadrada=True
        )

        self.gauss_a.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Button(
            pestana,
            text="Calcular A⁻¹",
            command=self._resolver_gauss
        ).pack(
            pady=5
        )

        self.txt_gauss = self._crear_area_texto(
            pestana
        )

    def _resolver_gauss(self):
        """Calcula y presenta la inversa de A mediante Gauss-Jordan."""
        try:
            respuesta = (
                procesar_inversa_gauss_jordan_programa_5(
                    self.gauss_a.leer()
                )
            )

            texto = formatear_procedimiento_inversa(
                respuesta["resultado"]
            )

            texto += (
                "\n\n"
                + "=" * 60
                + "\nDIAGNÓSTICO\n"
                + "=" * 60
                + "\n\n"
                + "Número de posiciones pivote: "
                + str(
                    respuesta[
                        "diagnostico"
                    ][
                        "num_pivotes"
                    ]
                )
                + "\n\n"
                + respuesta[
                    "diagnostico"
                ][
                    "diagnostico"
                ]
            )

            self._colocar_texto(
                self.txt_gauss,
                texto
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def _crear_pestana_adjunta(self):
        """Construye la opción 8 para calcular la inversa mediante adj(A)."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="8. Inversa por Matriz Adjunta"
        )

        self.adjunta_a = EntradaMatriz(
            pestana,
            "Matriz A",
            3,
            3,
            cuadrada=True
        )

        self.adjunta_a.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Button(
            pestana,
            text="Calcular A⁻¹ por adjunta",
            command=self._resolver_adjunta
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
            pady=5
        )

        procedimiento = ttk.Frame(
            resultados
        )

        comparacion = ttk.Frame(
            resultados
        )

        resultados.add(
            procedimiento,
            text="Procedimiento"
        )

        resultados.add(
            comparacion,
            text="Comparación"
        )

        self.txt_adjunta = self._crear_area_texto(
            procedimiento
        )

        self.txt_comparacion_inversa = self._crear_area_texto(
            comparacion
        )

    def _resolver_adjunta(self):
        """Calcula la inversa por adjunta y la compara con Gauss-Jordan."""
        try:
            respuesta = procesar_inversa_adjunta_programa_5(
                self.adjunta_a.leer()
            )

            texto = formatear_inversa_adjunta(
                respuesta["resultado"]
            )

            texto += (
                "\n\n"
                + "=" * 60
                + "\nDIAGNÓSTICO\n"
                + "=" * 60
                + "\n\n"
                + "Número de posiciones pivote: "
                + str(
                    respuesta[
                        "diagnostico"
                    ][
                        "num_pivotes"
                    ]
                )
                + "\n\n"
                + respuesta[
                    "diagnostico"
                ][
                    "diagnostico"
                ]
            )

            self._colocar_texto(
                self.txt_adjunta,
                texto
            )

            self._colocar_texto(
                self.txt_comparacion_inversa,
                formatear_comparacion_inversas(
                    respuesta["comparacion"]
                )
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def _crear_pestana_propiedades(self):
        """Construye la opción 9 para verificar las seis propiedades."""
        pestana = ttk.Frame(
            self.cuaderno
        )

        self.cuaderno.add(
            pestana,
            text="9. Verificador de propiedades"
        )

        controles = ttk.Frame(
            pestana
        )

        controles.pack(
            fill="x",
            padx=8,
            pady=5
        )

        ttk.Label(
            controles,
            text="Propiedad:"
        ).pack(
            side="left",
            padx=4
        )

        self.numero_propiedad = tk.StringVar(
            value="1"
        )

        propiedades = ttk.Combobox(
            controles,
            textvariable=self.numero_propiedad,
            state="readonly",
            width=48,
            values=[
                "1",
                "2",
                "3",
                "4",
                "5",
                "6"
            ]
        )

        propiedades.pack(
            side="left",
            padx=4
        )

        ttk.Label(
            controles,
            text=(
                "1:(A⁻¹)⁻¹=A   "
                "2:(AB)⁻¹=B⁻¹A⁻¹   "
                "3:(Aᵀ)⁻¹=(A⁻¹)ᵀ   "
                "4:det(A⁻¹)   "
                "5:Filas   "
                "6:Triangular"
            )
        ).pack(
            side="left",
            padx=8
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

        self.propiedad_a = EntradaMatriz(
            matrices,
            "Matriz A",
            2,
            2,
            cuadrada=True
        )

        self.propiedad_a.grid(
            row=0,
            column=0,
            padx=5,
            sticky="nsew"
        )

        self.propiedad_b = EntradaMatriz(
            matrices,
            "Matriz B",
            2,
            2,
            cuadrada=True
        )

        self.propiedad_b.grid(
            row=0,
            column=1,
            padx=5,
            sticky="nsew"
        )

        self._crear_controles_propiedad_5(
            pestana
        )

        ttk.Button(
            pestana,
            text="Verificar propiedad",
            command=self._resolver_propiedad
        ).pack(
            pady=5
        )

        self.txt_propiedades = self._crear_area_texto(
            pestana
        )

    def _crear_controles_propiedad_5(self, contenedor):
        """Crea los valores que el usuario selecciona para la propiedad 5."""
        marco = ttk.LabelFrame(
            contenedor,
            text="Datos para la propiedad 5",
            padding=5
        )

        marco.pack(
            fill="x",
            padx=10,
            pady=4
        )

        ttk.Label(
            marco,
            text="Fila 1:"
        ).pack(
            side="left",
            padx=3
        )

        self.fila_1 = ttk.Entry(
            marco,
            width=5,
            justify="center"
        )

        self.fila_1.insert(
            0,
            "1"
        )

        self.fila_1.pack(
            side="left",
            padx=3
        )

        ttk.Label(
            marco,
            text="Fila 2:"
        ).pack(
            side="left",
            padx=3
        )

        self.fila_2 = ttk.Entry(
            marco,
            width=5,
            justify="center"
        )

        self.fila_2.insert(
            0,
            "2"
        )

        self.fila_2.pack(
            side="left",
            padx=3
        )

        ttk.Label(
            marco,
            text="k reemplazo:"
        ).pack(
            side="left",
            padx=3
        )

        self.k_reemplazo = ttk.Entry(
            marco,
            width=7,
            justify="center"
        )

        self.k_reemplazo.insert(
            0,
            "-3"
        )

        self.k_reemplazo.pack(
            side="left",
            padx=3
        )

        ttk.Label(
            marco,
            text="Fila a escalar:"
        ).pack(
            side="left",
            padx=3
        )

        self.fila_escalar = ttk.Entry(
            marco,
            width=5,
            justify="center"
        )

        self.fila_escalar.insert(
            0,
            "1"
        )

        self.fila_escalar.pack(
            side="left",
            padx=3
        )

        ttk.Label(
            marco,
            text="k:"
        ).pack(
            side="left",
            padx=3
        )

        self.k_escalar = ttk.Entry(
            marco,
            width=7,
            justify="center"
        )

        self.k_escalar.insert(
            0,
            "3"
        )

        self.k_escalar.pack(
            side="left",
            padx=3
        )

    def _resolver_propiedad(self):
        """Ejecuta y presenta una de las seis propiedades del Programa 5."""
        try:
            numero = int(
                self.numero_propiedad.get()
            )

            matriz_b = None

            if numero == 2:
                matriz_b = self.propiedad_b.leer()

            resultado = procesar_propiedad_programa_5(
                numero,
                self.propiedad_a.leer(),
                matriz_b=matriz_b,
                fila_1=self.fila_1.get(),
                fila_2=self.fila_2.get(),
                escalar_reemplazo=self.k_reemplazo.get(),
                fila_escalar=self.fila_escalar.get(),
                escalar_fila=self.k_escalar.get()
            )

            self._colocar_texto(
                self.txt_propiedades,
                formatear_propiedad(
                    numero,
                    resultado
                )
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )