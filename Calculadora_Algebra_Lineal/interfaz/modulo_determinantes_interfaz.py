"""
Construye la interfaz del Módulo IV para las opciones 6 a 9.
Permite trabajar con determinantes, inversas y sus propiedades.
Tema de clase: determinantes, matriz inversa y teorema de invertibilidad.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from controladores.modulo_determinantes_controller import (
    procesar_determinante_programa_5,
    procesar_cramer,
    procesar_inversa_gauss_jordan_programa_5,
    procesar_inversa_adjunta_programa_5,
    procesar_propiedad_programa_5,
)

from utilidades.formato_determinantes import (
    formatear_procedimiento_determinante,
    formatear_sarrus,
    formatear_triangular,
    formatear_comparacion_determinantes,
)

from utilidades.formato_inversa import (
    formatear_procedimiento_inversa,
)

from utilidades.formato_inversa_adjunta import (
    formatear_inversa_adjunta,
    formatear_comparacion_inversas,
)

from utilidades.formato_propiedades_programa_5 import (
    formatear_propiedad,
)


class EntradaMatrizCuadrada(ttk.LabelFrame):
    """Gestiona una matriz cuadrada editable con orden configurable."""

    def __init__(self, contenedor, titulo, orden=3):
        """Inicializa una matriz cuadrada y crea sus entradas."""
        super().__init__(
            contenedor,
            text=titulo,
            padding=5,
        )

        self.titulo = titulo
        self.orden = tk.StringVar(
            value=str(orden)
        )
        self.entradas = []

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye el control del orden y el área desplazable."""
        controles = ttk.Frame(
            self
        )
        controles.pack(
            fill="x",
            pady=(0, 5),
        )

        ttk.Label(
            controles,
            text="Orden n:",
        ).pack(
            side="left",
            padx=3,
        )

        ttk.Entry(
            controles,
            textvariable=self.orden,
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
            height=145,
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
        """Actualiza el área desplazable cuando cambia la matriz."""
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

    def _obtener_orden(self):
        """Valida y devuelve el orden indicado por el usuario."""
        try:
            orden = int(
                self.orden.get()
            )
        except ValueError:
            raise ValueError(
                "El orden de la matriz debe ser un número entero positivo."
            )

        if orden <= 0:
            raise ValueError(
                "El orden de la matriz debe ser un número entero positivo."
            )

        return orden

    def crear_matriz(self):
        """Crea una matriz cuadrada de orden n."""
        try:
            orden = self._obtener_orden()
        except ValueError as error:
            messagebox.showerror(
                "Orden inválido",
                str(error),
            )
            return

        for elemento in self.contenido.winfo_children():
            elemento.destroy()

        self.entradas = []

        for fila in range(orden):
            fila_entradas = []

            for columna in range(orden):
                entrada = ttk.Entry(
                    self.contenido,
                    width=8,
                    justify="center",
                )
                entrada.grid(
                    row=fila,
                    column=columna,
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
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

    def leer(self):
        """Devuelve los valores escritos en la matriz."""
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


class ModuloDeterminantesInterfaz(ttk.Frame):
    """Presenta las opciones 6 a 9 del Módulo IV."""

    def __init__(self, contenedor):
        """Inicializa la interfaz gráfica de determinantes e inversas."""
        super().__init__(
            contenedor
        )
        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye el encabezado y las opciones 6 a 9."""
        ttk.Label(
            self,
            text="Módulo IV - Determinantes e Inversa",
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
                "Determinantes, matriz inversa "
                "y verificación de propiedades"
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

        self._crear_pestana_determinante()
        self._crear_pestana_cramer()
        self._crear_pestana_gauss_jordan()
        self._crear_pestana_adjunta()
        self._crear_pestana_propiedades()

    def _crear_area_texto(self, contenedor):
        """Crea un área de resultados con barras de desplazamiento."""
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

    def _colocar_texto(self, widget, contenido):
        """Reemplaza el contenido de un área de texto."""
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

    def _crear_pestana_determinante(self):
        """Construye la opción 6 con los métodos de determinante."""
        pestana = ttk.Frame(
            self.cuaderno
        )
        self.cuaderno.add(
            pestana,
            text="6. Determinante",
        )

        self.determinante_a = EntradaMatrizCuadrada(
            pestana,
            "Matriz A",
            3,
        )
        self.determinante_a.pack(
            fill="x",
            padx=10,
            pady=5,
        )

        ttk.Button(
            pestana,
            text="Calcular det(A)",
            command=self._resolver_determinante,
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
            text="Cofactores",
        )
        resultados.add(
            sarrus,
            text="Sarrus 3×3",
        )
        resultados.add(
            triangular,
            text="Triangular",
        )
        resultados.add(
            comparacion,
            text="Comparación",
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
        """Calcula det(A) mediante todos los métodos disponibles."""
        try:
            respuesta = procesar_determinante_programa_5(
                self.determinante_a.leer()
            )
            metodos = respuesta[
                "metodos"
            ]

            texto_cofactores = (
                "DETERMINANTE DE A\n"
                "det(A)\n"
                + "=" * 60
                + "\n\n"
                + formatear_procedimiento_determinante(
                    metodos["cofactores"]
                )
            )
            self._colocar_texto(
                self.txt_cofactores,
                texto_cofactores,
            )

            if metodos["sarrus"] is None:
                texto_sarrus = (
                    "DETERMINANTE DE A\n"
                    "det(A)\n"
                    + "=" * 60
                    + "\n\n"
                    + "La regla de Sarrus solamente "
                    "se aplica a matrices de orden 3."
                )
            else:
                texto_sarrus = (
                    "DETERMINANTE DE A\n"
                    "det(A)\n"
                    + "=" * 60
                    + "\n\n"
                    + formatear_sarrus(
                        metodos["sarrus"]
                    )
                )

            self._colocar_texto(
                self.txt_sarrus,
                texto_sarrus,
            )

            texto_triangular = (
                "DETERMINANTE DE A POR TRIANGULARIZACIÓN\n"
                "det(A)\n"
                + "=" * 60
                + "\n\n"
                + formatear_triangular(
                    metodos["triangular"]
                )
            )
            self._colocar_texto(
                self.txt_triangular,
                texto_triangular,
            )

            comparacion = (
                "COMPARACIÓN DE MÉTODOS PARA det(A)\n"
                + "=" * 60
                + "\n\n"
                + formatear_comparacion_determinantes(
                    metodos
                )
                + "\n\n"
                + "Número de posiciones pivote: "
                + str(
                    respuesta["diagnostico"]["num_pivotes"]
                )
                + "\n\n"
                + respuesta["diagnostico"]["diagnostico"]
            )

            self._colocar_texto(
                self.txt_comparacion_det,
                comparacion,
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )

    def _crear_pestana_cramer(self):
        """Construye una herramienta adicional para la regla de Cramer."""
        pestana = ttk.Frame(
            self.cuaderno
        )
        self.cuaderno.add(
            pestana,
            text="Método de Cramer",
        )

        controles = ttk.Frame(
            pestana
        )
        controles.pack(
            fill="x",
            padx=10,
            pady=5,
        )

        ttk.Label(
            controles,
            text="Orden n:",
        ).pack(
            side="left",
            padx=4,
        )

        self.cramer_orden = tk.StringVar(
            value="2"
        )

        ttk.Entry(
            controles,
            textvariable=self.cramer_orden,
            width=6,
            justify="center",
        ).pack(
            side="left",
            padx=4,
        )

        ttk.Button(
            controles,
            text="Crear sistema",
            command=self._crear_sistema_cramer,
        ).pack(
            side="left",
            padx=6,
        )

        ttk.Button(
            controles,
            text="Resolver por Cramer",
            command=self._resolver_cramer,
        ).pack(
            side="left",
            padx=6,
        )

        self.marco_cramer = ttk.LabelFrame(
            pestana,
            text="Sistema Ax = b",
            padding=8,
        )
        self.marco_cramer.pack(
            fill="x",
            padx=10,
            pady=5,
        )

        self.cramer_coeficientes = []
        self.cramer_independientes = []

        self._crear_sistema_cramer()

        self.txt_cramer = self._crear_area_texto(
            pestana
        )

    def _crear_sistema_cramer(self):
        """Crea las entradas de A y b para un sistema cuadrado."""
        try:
            orden = int(
                self.cramer_orden.get()
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "El orden debe ser un número entero positivo.",
            )
            return

        if orden <= 0:
            messagebox.showerror(
                "Error",
                "El orden debe ser un número entero positivo.",
            )
            return

        for elemento in self.marco_cramer.winfo_children():
            elemento.destroy()

        self.cramer_coeficientes = []
        self.cramer_independientes = []

        for columna in range(orden):
            ttk.Label(
                self.marco_cramer,
                text=f"x{columna + 1}",
            ).grid(
                row=0,
                column=columna + 1,
                padx=4,
                pady=3,
            )

        ttk.Label(
            self.marco_cramer,
            text="|",
        ).grid(
            row=0,
            column=orden + 1,
            padx=4,
        )

        ttk.Label(
            self.marco_cramer,
            text="b",
        ).grid(
            row=0,
            column=orden + 2,
            padx=4,
            pady=3,
        )

        for fila in range(orden):
            ttk.Label(
                self.marco_cramer,
                text=f"E{fila + 1}",
            ).grid(
                row=fila + 1,
                column=0,
                padx=4,
                pady=3,
            )

            fila_coeficientes = []

            for columna in range(orden):
                entrada = ttk.Entry(
                    self.marco_cramer,
                    width=8,
                    justify="center",
                )
                entrada.grid(
                    row=fila + 1,
                    column=columna + 1,
                    padx=3,
                    pady=3,
                )
                fila_coeficientes.append(
                    entrada
                )

            self.cramer_coeficientes.append(
                fila_coeficientes
            )

            ttk.Label(
                self.marco_cramer,
                text="|",
            ).grid(
                row=fila + 1,
                column=orden + 1,
                padx=4,
            )

            independiente = ttk.Entry(
                self.marco_cramer,
                width=8,
                justify="center",
            )
            independiente.grid(
                row=fila + 1,
                column=orden + 2,
                padx=3,
                pady=3,
            )
            self.cramer_independientes.append(
                independiente
            )

    def _leer_sistema_cramer(self):
        """Devuelve A y b tal como fueron escritos por el usuario."""
        matriz_a = [
            [
                entrada.get()
                for entrada in fila
            ]
            for fila in self.cramer_coeficientes
        ]

        vector_b = [
            entrada.get()
            for entrada in self.cramer_independientes
        ]

        return matriz_a, vector_b

    def _formatear_matriz_simple(self, matriz):
        """Convierte una matriz en texto para la salida de Cramer."""
        return "\n".join(
            "[ "
            + "   ".join(
                str(valor)
                for valor in fila
            )
            + " ]"
            for fila in matriz
        )

    def _formatear_cramer(self, resultado):
        """Construye el procedimiento completo de la regla de Cramer."""
        lineas = [
            "MÉTODO DE CRAMER",
            "Ax = b",
            "=" * 60,
            "",
            "A =",
            "",
            self._formatear_matriz_simple(
                resultado["matriz_a"]
            ),
            "",
            "b =",
            "",
            "[ "
            + "   ".join(
                str(valor)
                for valor in resultado["vector_b"]
            )
            + " ]ᵀ",
            "",
            "det(A) = "
            + str(
                resultado["determinante_a"]
            ),
            "",
        ]

        for calculo in resultado["calculos"]:
            numero = calculo["variable"] + 1

            lineas.extend(
                [
                    f"A{numero} =",
                    "",
                    self._formatear_matriz_simple(
                        calculo["matriz"]
                    ),
                    "",
                    f"det(A{numero}) = {calculo['determinante']}",
                    f"x{numero} = det(A{numero}) / det(A)",
                    f"x{numero} = {calculo['valor']}",
                    "",
                ]
            )

        lineas.extend(
            [
                "=" * 60,
                "",
                "SOLUCIÓN",
                "",
            ]
        )

        for indice, valor in enumerate(
            resultado["solucion"],
            start=1,
        ):
            lineas.append(
                f"x{indice} = {valor}"
            )

        lineas.extend(
            [
                "",
                "=" * 60,
                "",
                "VERIFICACIÓN",
                "",
            ]
        )

        for ecuacion in resultado["verificacion"]["ecuaciones"]:
            estado = (
                "Correcta"
                if ecuacion["correcta"]
                else "Incorrecta"
            )

            lineas.append(
                "Ecuación "
                + str(ecuacion["ecuacion"])
                + ": "
                + str(ecuacion["lado_izquierdo"])
                + " = "
                + str(ecuacion["lado_derecho"])
                + f" ({estado})"
            )

        lineas.append("")

        if resultado["verificacion"]["correcta"]:
            lineas.append(
                "La solución satisface todas las ecuaciones."
            )
        else:
            lineas.append(
                "La solución no satisface todas las ecuaciones."
            )

        return "\n".join(
            lineas
        )

    def _resolver_cramer(self):
        """Resuelve el sistema ingresado mediante la regla de Cramer."""
        try:
            matriz_a, vector_b = self._leer_sistema_cramer()

            resultado = procesar_cramer(
                matriz_a,
                vector_b,
            )

            self._colocar_texto(
                self.txt_cramer,
                self._formatear_cramer(
                    resultado
                ),
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )

    def _crear_pestana_gauss_jordan(self):
        """Construye la opción 7 para la inversa por Gauss-Jordan."""
        pestana = ttk.Frame(
            self.cuaderno
        )
        self.cuaderno.add(
            pestana,
            text="7. Inversa por Gauss-Jordan",
        )

        self.gauss_a = EntradaMatrizCuadrada(
            pestana,
            "Matriz A",
            3,
        )
        self.gauss_a.pack(
            fill="x",
            padx=10,
            pady=5,
        )

        ttk.Button(
            pestana,
            text="Calcular A⁻¹",
            command=self._resolver_gauss,
        ).pack(
            pady=5
        )

        self.txt_gauss = self._crear_area_texto(
            pestana
        )

    def _resolver_gauss(self):
        """Calcula y presenta A⁻¹ mediante Gauss-Jordan."""
        try:
            respuesta = procesar_inversa_gauss_jordan_programa_5(
                self.gauss_a.leer()
            )

            texto = (
                "INVERSA DE A POR GAUSS-JORDAN\n"
                "A⁻¹\n"
                + "=" * 60
                + "\n\n"
                + formatear_procedimiento_inversa(
                    respuesta["resultado"]
                )
            )

            texto += (
                "\n\n"
                + "=" * 60
                + "\nDIAGNÓSTICO\n"
                + "=" * 60
                + "\n\n"
                + "Número de posiciones pivote: "
                + str(
                    respuesta["diagnostico"]["num_pivotes"]
                )
                + "\n\n"
                + respuesta["diagnostico"]["diagnostico"]
            )

            self._colocar_texto(
                self.txt_gauss,
                texto,
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )

    def _crear_pestana_adjunta(self):
        """Construye la opción 8 para la inversa mediante adj(A)."""
        pestana = ttk.Frame(
            self.cuaderno
        )
        self.cuaderno.add(
            pestana,
            text="8. Inversa por Matriz Adjunta",
        )

        self.adjunta_a = EntradaMatrizCuadrada(
            pestana,
            "Matriz A",
            3,
        )
        self.adjunta_a.pack(
            fill="x",
            padx=10,
            pady=5,
        )

        ttk.Button(
            pestana,
            text="Calcular A⁻¹ por adjunta",
            command=self._resolver_adjunta,
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

        procedimiento = ttk.Frame(
            resultados
        )
        comparacion = ttk.Frame(
            resultados
        )

        resultados.add(
            procedimiento,
            text="Procedimiento",
        )
        resultados.add(
            comparacion,
            text="Comparación",
        )

        self.txt_adjunta = self._crear_area_texto(
            procedimiento
        )
        self.txt_comparacion_inversa = self._crear_area_texto(
            comparacion
        )

    def _resolver_adjunta(self):
        """Calcula A⁻¹ por adjunta y compara ambos métodos."""
        try:
            respuesta = procesar_inversa_adjunta_programa_5(
                self.adjunta_a.leer()
            )

            texto = (
                "INVERSA DE A POR MATRIZ ADJUNTA\n"
                "A⁻¹ = (1/det(A)) adj(A)\n"
                + "=" * 60
                + "\n\n"
                + formatear_inversa_adjunta(
                    respuesta["resultado"]
                )
            )

            texto += (
                "\n\n"
                + "=" * 60
                + "\nDIAGNÓSTICO\n"
                + "=" * 60
                + "\n\n"
                + "Número de posiciones pivote: "
                + str(
                    respuesta["diagnostico"]["num_pivotes"]
                )
                + "\n\n"
                + respuesta["diagnostico"]["diagnostico"]
            )

            self._colocar_texto(
                self.txt_adjunta,
                texto,
            )

            self._colocar_texto(
                self.txt_comparacion_inversa,
                formatear_comparacion_inversas(
                    respuesta["comparacion"]
                ),
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error),
            )

    def _crear_pestana_propiedades(self):
        """Construye la opción 9 con nombres descriptivos."""
        pestana = ttk.Frame(
            self.cuaderno
        )
        self.cuaderno.add(
            pestana,
            text="9. Verificador de propiedades",
        )

        controles = ttk.Frame(
            pestana
        )
        controles.pack(
            fill="x",
            padx=8,
            pady=5,
        )

        ttk.Label(
            controles,
            text="Propiedad:",
        ).pack(
            side="left",
            padx=4,
        )

        self.propiedad_seleccionada = tk.StringVar(
            value="1. Inversa de la inversa — (A⁻¹)⁻¹ = A"
        )

        self.propiedades_modulo_4 = {
            "1. Inversa de la inversa — (A⁻¹)⁻¹ = A":
                1,
            "2. Inversa de un producto — (AB)⁻¹ = B⁻¹A⁻¹":
                2,
            "3. Inversa de la transpuesta — (Aᵀ)⁻¹ = (A⁻¹)ᵀ":
                3,
            "4. Determinante de la inversa — det(A⁻¹) = 1/det(A)":
                4,
            "5. Determinante y operaciones elementales de fila":
                5,
            "6. Determinante de una matriz triangular":
                6,
        }

        propiedades = ttk.Combobox(
            controles,
            textvariable=self.propiedad_seleccionada,
            state="readonly",
            width=68,
            values=list(
                self.propiedades_modulo_4.keys()
            ),
        )
        propiedades.pack(
            side="left",
            padx=4,
            fill="x",
            expand=True,
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

        self.propiedad_a = EntradaMatrizCuadrada(
            matrices,
            "Matriz A",
            2,
        )
        self.propiedad_a.grid(
            row=0,
            column=0,
            padx=5,
            sticky="nsew",
        )

        self.propiedad_b = EntradaMatrizCuadrada(
            matrices,
            "Matriz B",
            2,
        )
        self.propiedad_b.grid(
            row=0,
            column=1,
            padx=5,
            sticky="nsew",
        )

        self._crear_controles_propiedad_5(
            pestana
        )

        ttk.Button(
            pestana,
            text="Verificar propiedad",
            command=self._resolver_propiedad,
        ).pack(
            pady=5
        )

        self.txt_propiedades = self._crear_area_texto(
            pestana
        )

    def _crear_controles_propiedad_5(self, contenedor):
        """Crea los valores configurables para la propiedad 5."""
        marco = ttk.LabelFrame(
            contenedor,
            text="Datos para la propiedad 5",
            padding=5,
        )
        marco.pack(
            fill="x",
            padx=10,
            pady=4,
        )

        ttk.Label(
            marco,
            text="Fila 1:",
        ).pack(
            side="left",
            padx=3,
        )
        self.fila_1 = ttk.Entry(
            marco,
            width=5,
            justify="center",
        )
        self.fila_1.insert(
            0,
            "1",
        )
        self.fila_1.pack(
            side="left",
            padx=3,
        )

        ttk.Label(
            marco,
            text="Fila 2:",
        ).pack(
            side="left",
            padx=3,
        )
        self.fila_2 = ttk.Entry(
            marco,
            width=5,
            justify="center",
        )
        self.fila_2.insert(
            0,
            "2",
        )
        self.fila_2.pack(
            side="left",
            padx=3,
        )

        ttk.Label(
            marco,
            text="k reemplazo:",
        ).pack(
            side="left",
            padx=3,
        )
        self.k_reemplazo = ttk.Entry(
            marco,
            width=7,
            justify="center",
        )
        self.k_reemplazo.insert(
            0,
            "-3",
        )
        self.k_reemplazo.pack(
            side="left",
            padx=3,
        )

        ttk.Label(
            marco,
            text="Fila a escalar:",
        ).pack(
            side="left",
            padx=3,
        )
        self.fila_escalar = ttk.Entry(
            marco,
            width=5,
            justify="center",
        )
        self.fila_escalar.insert(
            0,
            "1",
        )
        self.fila_escalar.pack(
            side="left",
            padx=3,
        )

        ttk.Label(
            marco,
            text="k:",
        ).pack(
            side="left",
            padx=3,
        )
        self.k_escalar = ttk.Entry(
            marco,
            width=7,
            justify="center",
        )
        self.k_escalar.insert(
            0,
            "3",
        )
        self.k_escalar.pack(
            side="left",
            padx=3,
        )

    def _resolver_propiedad(self):
        """Ejecuta y presenta una de las seis propiedades."""
        try:
            nombre_propiedad = (
                self.propiedad_seleccionada.get()
            )
            numero = self.propiedades_modulo_4[
                nombre_propiedad
            ]

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
                escalar_fila=self.k_escalar.get(),
            )

            self._colocar_texto(
                self.txt_propiedades,
                formatear_propiedad(
                    numero,
                    resultado,
                ),
            )

        except (ValueError, KeyError) as error:
            messagebox.showerror(
                "Error",
                str(error),
            )
