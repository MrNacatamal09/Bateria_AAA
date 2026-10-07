"""
Construye la interfaz gráfica del Módulo III de matrices.
Incluye operaciones básicas y las nueve propiedades generales.
Tema de clase: operaciones y propiedades generales de matrices.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from controladores.modulo_matrices_controller import (
    procesar_operacion_basica,
    procesar_multiplicacion_matrices,
    procesar_transpuesta,
    procesar_propiedad_matrices,
)

from utilidades.formato_determinantes import formatear_matriz


class EntradaMatriz(ttk.LabelFrame):
    """Gestiona una matriz editable con dimensiones configurables."""

    def __init__(
        self,
        contenedor,
        titulo,
        filas=2,
        columnas=2,
    ):
        """Inicializa una entrada matricial con dimensiones editables."""
        super().__init__(
            contenedor,
            text=titulo,
            padding=5,
        )

        self.titulo = titulo
        self.filas = tk.StringVar(value=str(filas))
        self.columnas = tk.StringVar(value=str(columnas))
        self.entradas = []

        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye los controles de dimensión y el área de entradas."""
        controles = ttk.Frame(self)
        controles.pack(fill="x", pady=(0, 5))

        ttk.Label(
            controles,
            text="Filas:",
        ).pack(side="left", padx=3)

        ttk.Entry(
            controles,
            textvariable=self.filas,
            width=6,
            justify="center",
        ).pack(side="left", padx=3)

        ttk.Label(
            controles,
            text="Columnas:",
        ).pack(side="left", padx=3)

        ttk.Entry(
            controles,
            textvariable=self.columnas,
            width=6,
            justify="center",
        ).pack(side="left", padx=3)

        ttk.Button(
            controles,
            text="Crear matriz",
            command=self.crear_matriz,
        ).pack(side="left", padx=6)

        marco_canvas = ttk.Frame(self)
        marco_canvas.pack(fill="both", expand=True)
        marco_canvas.rowconfigure(0, weight=1)
        marco_canvas.columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            marco_canvas,
            height=140,
            highlightthickness=0,
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")

        scroll_vertical = ttk.Scrollbar(
            marco_canvas,
            orient="vertical",
            command=self.canvas.yview,
        )
        scroll_vertical.grid(row=0, column=1, sticky="ns")

        scroll_horizontal = ttk.Scrollbar(
            marco_canvas,
            orient="horizontal",
            command=self.canvas.xview,
        )
        scroll_horizontal.grid(row=1, column=0, sticky="ew")

        self.canvas.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set,
        )

        self.contenido = ttk.Frame(self.canvas)
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

    def _obtener_dimensiones(self):
        """Valida y devuelve las dimensiones solicitadas."""
        try:
            filas = int(self.filas.get())
            columnas = int(self.columnas.get())
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
                str(error),
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
                    justify="center",
                )
                entrada.grid(
                    row=fila,
                    column=columna,
                    padx=3,
                    pady=3,
                )
                fila_entradas.append(entrada)

            self.entradas.append(fila_entradas)

        self.update_idletasks()
        self._actualizar_scroll()
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

    def leer(self):
        """Devuelve el contenido escrito en las entradas de la matriz."""
        if not self.entradas:
            raise ValueError(f"Debe crear {self.titulo}.")

        return [
            [entrada.get() for entrada in fila]
            for fila in self.entradas
        ]


class ModuloMatricesInterfaz(ttk.Frame):
    """Presenta las opciones 1 a 5 y las propiedades generales."""

    def __init__(self, contenedor):
        """Inicializa la interfaz del Módulo III."""
        super().__init__(contenedor)
        self._crear_interfaz()

    def _crear_interfaz(self):
        """Construye las operaciones y propiedades del Módulo III."""
        ttk.Label(
            self,
            text="Módulo III: Álgebra de Matrices",
            font=("Arial", 15, "bold"),
        ).pack(pady=(6, 2))

        ttk.Label(
            self,
            text=(
                "Operaciones fundamentales y propiedades generales de matrices"
            ),
        ).pack(pady=(0, 5))

        self.cuaderno = ttk.Notebook(self)
        self.cuaderno.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=5,
        )

        self._crear_pestana_suma()
        self._crear_pestana_resta()
        self._crear_pestana_escalar()
        self._crear_pestana_producto()
        self._crear_pestana_transpuesta()
        self._crear_pestana_propiedades_generales()

    def _crear_area_texto(self, contenedor):
        """Crea un área de resultados con desplazamiento vertical y horizontal."""
        marco = ttk.Frame(contenedor)
        marco.pack(fill="both", expand=True, padx=5, pady=5)
        marco.rowconfigure(0, weight=1)
        marco.columnconfigure(0, weight=1)

        texto = tk.Text(
            marco,
            wrap="none",
            state="disabled",
            font=("Consolas", 10),
        )
        texto.grid(row=0, column=0, sticky="nsew")

        scroll_vertical = ttk.Scrollbar(
            marco,
            orient="vertical",
            command=texto.yview,
        )
        scroll_vertical.grid(row=0, column=1, sticky="ns")

        scroll_horizontal = ttk.Scrollbar(
            marco,
            orient="horizontal",
            command=texto.xview,
        )
        scroll_horizontal.grid(row=1, column=0, sticky="ew")

        texto.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set,
        )

        return texto

    def _colocar_texto(self, widget, contenido):
        """Reemplaza el contenido de un área de texto de solo lectura."""
        widget.configure(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, contenido)
        widget.configure(state="disabled")
        widget.see("1.0")

    def _crear_dos_matrices(
        self,
        contenedor,
        filas_a=2,
        columnas_a=2,
        filas_b=2,
        columnas_b=2,
    ):
        """Crea dos entradas de matrices colocadas lado a lado."""
        marco = ttk.Frame(contenedor)
        marco.pack(fill="x", padx=8, pady=5)
        marco.columnconfigure(0, weight=1)
        marco.columnconfigure(1, weight=1)

        matriz_a = EntradaMatriz(
            marco,
            "Matriz A",
            filas_a,
            columnas_a,
        )
        matriz_a.grid(
            row=0,
            column=0,
            padx=5,
            sticky="nsew",
        )

        matriz_b = EntradaMatriz(
            marco,
            "Matriz B",
            filas_b,
            columnas_b,
        )
        matriz_b.grid(
            row=0,
            column=1,
            padx=5,
            sticky="nsew",
        )

        return matriz_a, matriz_b

    def _encabezado_operacion(self, titulo, expresion):
        """Construye un encabezado uniforme para una operación matricial."""
        return (
            titulo
            + "\n"
            + expresion
            + "\n"
            + "=" * 60
            + "\n\n"
        )

    def _crear_pestana_suma(self):
        """Construye la opción 1 para sumar matrices."""
        pestana = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pestana, text="1. Suma")

        self.suma_a, self.suma_b = self._crear_dos_matrices(pestana)

        ttk.Button(
            pestana,
            text="Calcular A + B",
            command=self._resolver_suma,
        ).pack(pady=4)

        self.txt_suma = self._crear_area_texto(pestana)

    def _resolver_suma(self):
        """Ejecuta A + B y muestra los datos y el resultado."""
        try:
            resultado = procesar_operacion_basica(
                "suma",
                self.suma_a.leer(),
                self.suma_b.leer(),
            )

            texto = self._encabezado_operacion(
                "SUMA DE MATRICES",
                "A + B",
            )
            texto += "A =\n\n"
            texto += formatear_matriz(resultado["matriz_a"])
            texto += "\n\nB =\n\n"
            texto += formatear_matriz(resultado["matriz_b"])
            texto += "\n\nA + B =\n\n"
            texto += formatear_matriz(resultado["resultado"])

            self._colocar_texto(self.txt_suma, texto)

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def _crear_pestana_resta(self):
        """Construye la opción 2 para restar matrices."""
        pestana = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pestana, text="2. Resta")

        self.resta_a, self.resta_b = self._crear_dos_matrices(pestana)

        ttk.Button(
            pestana,
            text="Calcular A - B",
            command=self._resolver_resta,
        ).pack(pady=4)

        self.txt_resta = self._crear_area_texto(pestana)

    def _resolver_resta(self):
        """Ejecuta A - B y muestra los datos y el resultado."""
        try:
            resultado = procesar_operacion_basica(
                "resta",
                self.resta_a.leer(),
                self.resta_b.leer(),
            )

            texto = self._encabezado_operacion(
                "RESTA DE MATRICES",
                "A - B",
            )
            texto += "A =\n\n"
            texto += formatear_matriz(resultado["matriz_a"])
            texto += "\n\nB =\n\n"
            texto += formatear_matriz(resultado["matriz_b"])
            texto += "\n\nA - B =\n\n"
            texto += formatear_matriz(resultado["resultado"])

            self._colocar_texto(self.txt_resta, texto)

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def _crear_pestana_escalar(self):
        """Construye la opción 3 para multiplicar una matriz por un escalar."""
        pestana = ttk.Frame(self.cuaderno)
        self.cuaderno.add(
            pestana,
            text="3. Multiplicación por Escalar",
        )

        self.escalar_a = EntradaMatriz(
            pestana,
            "Matriz A",
        )
        self.escalar_a.pack(fill="x", padx=10, pady=5)

        controles = ttk.Frame(pestana)
        controles.pack(pady=5)

        ttk.Label(
            controles,
            text="Escalar r:",
        ).pack(side="left", padx=4)

        self.valor_escalar = ttk.Entry(
            controles,
            width=10,
            justify="center",
        )
        self.valor_escalar.insert(0, "2")
        self.valor_escalar.pack(side="left", padx=4)

        ttk.Button(
            controles,
            text="Calcular rA",
            command=self._resolver_escalar,
        ).pack(side="left", padx=6)

        self.txt_escalar = self._crear_area_texto(pestana)

    def _resolver_escalar(self):
        """Ejecuta rA y muestra el escalar, A y el resultado."""
        try:
            resultado = procesar_operacion_basica(
                "escalar",
                self.escalar_a.leer(),
                escalar=self.valor_escalar.get(),
            )

            texto = self._encabezado_operacion(
                "MULTIPLICACIÓN POR ESCALAR",
                "rA",
            )
            texto += "r = " + str(resultado["escalar"])
            texto += "\n\nA =\n\n"
            texto += formatear_matriz(resultado["matriz_a"])
            texto += "\n\nrA =\n\n"
            texto += formatear_matriz(resultado["resultado"])

            self._colocar_texto(self.txt_escalar, texto)

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def _crear_pestana_producto(self):
        """Construye la opción 4 para calcular AB."""
        pestana = ttk.Frame(self.cuaderno)
        self.cuaderno.add(
            pestana,
            text="4. Producto Matricial",
        )

        self.producto_a, self.producto_b = self._crear_dos_matrices(
            pestana,
            2,
            3,
            3,
            2,
        )

        ttk.Button(
            pestana,
            text="Calcular AB",
            command=self._resolver_producto,
        ).pack(pady=4)

        resultados = ttk.Notebook(pestana)
        resultados.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5,
        )

        pestana_resultado = ttk.Frame(resultados)
        pestana_procedimiento = ttk.Frame(resultados)

        resultados.add(
            pestana_resultado,
            text="Resultado",
        )
        resultados.add(
            pestana_procedimiento,
            text="Regla fila-columna",
        )

        self.txt_producto = self._crear_area_texto(
            pestana_resultado
        )
        self.txt_producto_procedimiento = self._crear_area_texto(
            pestana_procedimiento
        )

    def _resolver_producto(self):
        """Calcula AB y presenta el resultado y el procedimiento."""
        try:
            resultado = procesar_multiplicacion_matrices(
                self.producto_a.leer(),
                self.producto_b.leer(),
            )

            texto = self._encabezado_operacion(
                "PRODUCTO MATRICIAL",
                "AB",
            )
            texto += "A =\n\n"
            texto += formatear_matriz(resultado["matriz_a"])
            texto += "\n\nB =\n\n"
            texto += formatear_matriz(resultado["matriz_b"])
            texto += "\n\nAB =\n\n"
            texto += formatear_matriz(resultado["resultado"])
            texto += "\n\nDimensiones de AB: "
            texto += str(len(resultado["resultado"]))
            texto += " × "
            texto += str(len(resultado["resultado"][0]))

            self._colocar_texto(self.txt_producto, texto)
            self._colocar_texto(
                self.txt_producto_procedimiento,
                self._formatear_producto(resultado["procedimiento"]),
            )

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def _formatear_producto(self, pasos):
        """Convierte el procedimiento fila-columna en texto legible."""
        lineas = [
            "PRODUCTO MATRICIAL",
            "AB",
            "=" * 60,
            "",
            "REGLA FILA-COLUMNA",
            "",
        ]

        for paso in pasos:
            fila = paso["fila_resultado"] + 1
            columna = paso["columna_resultado"] + 1

            productos = [
                "("
                + str(producto["valor_a"])
                + ")(" 
                + str(producto["valor_b"])
                + ")"
                for producto in paso["productos"]
            ]

            lineas.append(
                f"Entrada ({fila}, {columna}) de AB:"
            )
            lineas.append(
                " + ".join(productos)
                + " = "
                + str(paso["resultado"])
            )
            lineas.append("")

        return "\n".join(lineas)

    def _crear_pestana_transpuesta(self):
        """Construye la opción 5 para obtener Aᵀ."""
        pestana = ttk.Frame(self.cuaderno)
        self.cuaderno.add(
            pestana,
            text="5. Transposición",
        )

        self.transpuesta_a = EntradaMatriz(
            pestana,
            "Matriz A",
            2,
            3,
        )
        self.transpuesta_a.pack(fill="x", padx=10, pady=5)

        ttk.Button(
            pestana,
            text="Calcular Aᵀ",
            command=self._resolver_transpuesta,
        ).pack(pady=5)

        self.txt_transpuesta = self._crear_area_texto(pestana)

    def _resolver_transpuesta(self):
        """Obtiene Aᵀ y muestra A y su transpuesta."""
        try:
            resultado = procesar_transpuesta(
                self.transpuesta_a.leer()
            )

            texto = self._encabezado_operacion(
                "TRANSPUESTA DE A",
                "Aᵀ",
            )
            texto += "A =\n\n"
            texto += formatear_matriz(resultado["matriz_a"])
            texto += "\n\nAᵀ =\n\n"
            texto += formatear_matriz(resultado["resultado"])

            self._colocar_texto(self.txt_transpuesta, texto)

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def _crear_pestana_propiedades_generales(self):
        """Construye la pestaña con diez propiedades generales de matrices."""
        pestana = ttk.Frame(self.cuaderno)
        self.cuaderno.add(
            pestana,
            text="Propiedades generales",
        )

        controles = ttk.Frame(pestana)
        controles.pack(fill="x", padx=8, pady=5)

        ttk.Label(
            controles,
            text="Propiedad:",
        ).pack(side="left", padx=4)

        self.propiedad_general = tk.StringVar(
            value="Asociativa del producto — A(BC) = (AB)C"
        )

        self.propiedades_generales = {
            "Asociativa del producto — A(BC) = (AB)C":
                "asociativa",
            "Distributiva izquierda — A(B + C) = AB + AC":
                "distributiva_izquierda",
            "Distributiva derecha — (B + C)A = BA + CA":
                "distributiva_derecha",
            "Compatibilidad con escalar — r(AB) = (rA)B = A(rB)":
                "escalar_producto",
            "Identidad multiplicativa — IA = A = AI":
                "identidad",
            "Transpuesta doble — (Aᵀ)ᵀ = A":
                "transpuesta_doble",
            "Transpuesta de una suma — (A + B)ᵀ = Aᵀ + Bᵀ":
                "transpuesta_suma",
            "Transpuesta de un múltiplo — (rA)ᵀ = rAᵀ":
                "transpuesta_escalar",
            "Transpuesta de un producto — (AB)ᵀ = BᵀAᵀ":
                "transpuesta_producto",
            "Distributiva de escalar y transpuesta — (r(A + B))ᵀ = rAᵀ + rBᵀ":
                "distributiva_escalar_transpuesta",
        }

        selector = ttk.Combobox(
            controles,
            textvariable=self.propiedad_general,
            state="readonly",
            width=63,
            values=list(self.propiedades_generales.keys()),
        )
        selector.pack(
            side="left",
            padx=4,
            fill="x",
            expand=True,
        )

        ttk.Label(
            controles,
            text="Escalar r:",
        ).pack(side="left", padx=4)

        self.escalar_propiedad_general = ttk.Entry(
            controles,
            width=8,
            justify="center",
        )
        self.escalar_propiedad_general.insert(0, "2")
        self.escalar_propiedad_general.pack(
            side="left",
            padx=4,
        )

        matrices = ttk.Frame(pestana)
        matrices.pack(fill="x", padx=8, pady=5)

        for columna in range(3):
            matrices.columnconfigure(columna, weight=1)

        self.prop_general_a = EntradaMatriz(
            matrices,
            "Matriz A",
        )
        self.prop_general_a.grid(
            row=0,
            column=0,
            padx=4,
            sticky="nsew",
        )

        self.prop_general_b = EntradaMatriz(
            matrices,
            "Matriz B",
        )
        self.prop_general_b.grid(
            row=0,
            column=1,
            padx=4,
            sticky="nsew",
        )

        self.prop_general_c = EntradaMatriz(
            matrices,
            "Matriz C",
        )
        self.prop_general_c.grid(
            row=0,
            column=2,
            padx=4,
            sticky="nsew",
        )

        ttk.Button(
            pestana,
            text="Verificar propiedad",
            command=self._resolver_propiedad_general,
        ).pack(pady=5)

        self.txt_propiedades_generales = self._crear_area_texto(
            pestana
        )

    def _agregar_matriz_propiedad(
        self,
        lineas,
        titulo,
        matriz,
    ):
        """Agrega el nombre de una expresión y su matriz a la salida."""
        lineas.append(titulo)
        lineas.append("")
        lineas.append(formatear_matriz(matriz))
        lineas.append("")

    def _formatear_propiedad_general(self, codigo, resultado):
        """Muestra las operaciones intermedias y los lados de una propiedad."""
        lineas = [
            "PROPIEDAD GENERAL DE MATRICES",
            resultado["propiedad"],
            "=" * 60,
            "",
        ]

        if codigo == "asociativa":
            self._agregar_matriz_propiedad(
                lineas,
                "BC =",
                resultado["producto_bc"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "A(BC) =",
                resultado["lado_izquierdo"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "AB =",
                resultado["producto_ab"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "(AB)C =",
                resultado["lado_derecho"],
            )

        elif codigo == "distributiva_izquierda":
            self._agregar_matriz_propiedad(
                lineas,
                "B + C =",
                resultado["suma_bc"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "A(B + C) =",
                resultado["lado_izquierdo"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "AB =",
                resultado["producto_ab"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "AC =",
                resultado["producto_ac"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "AB + AC =",
                resultado["lado_derecho"],
            )

        elif codigo == "distributiva_derecha":
            self._agregar_matriz_propiedad(
                lineas,
                "B + C =",
                resultado["suma_bc"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "(B + C)A =",
                resultado["lado_izquierdo"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "BA =",
                resultado["producto_ba"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "CA =",
                resultado["producto_ca"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "BA + CA =",
                resultado["lado_derecho"],
            )

        elif codigo == "escalar_producto":
            lineas.append("r = " + str(resultado["escalar"]))
            lineas.append("")
            self._agregar_matriz_propiedad(
                lineas,
                "AB =",
                resultado["producto_ab"],
            )
            lineas.extend(["MIEMBRO 1", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "r(AB) =",
                resultado["resultado_1"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "rA =",
                resultado["r_a"],
            )
            lineas.extend(["MIEMBRO 2", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "(rA)B =",
                resultado["resultado_2"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "rB =",
                resultado["r_b"],
            )
            lineas.extend(["MIEMBRO 3", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "A(rB) =",
                resultado["resultado_3"],
            )

        elif codigo == "identidad":
            self._agregar_matriz_propiedad(
                lineas,
                "I izquierda =",
                resultado["identidad_izquierda"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "IA =",
                resultado["producto_izquierdo"],
            )
            lineas.extend(["MATRIZ A", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "A =",
                resultado["producto_izquierdo"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "I derecha =",
                resultado["identidad_derecha"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "AI =",
                resultado["producto_derecho"],
            )

        elif codigo == "transpuesta_doble":
            self._agregar_matriz_propiedad(
                lineas,
                "Aᵀ =",
                resultado["transpuesta_a"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "(Aᵀ)ᵀ =",
                resultado["transpuesta_doble"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "A =",
                resultado["resultado_esperado"],
            )

        elif codigo == "transpuesta_suma":
            self._agregar_matriz_propiedad(
                lineas,
                "A + B =",
                resultado["suma_ab"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "(A + B)ᵀ =",
                resultado["lado_izquierdo"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "Aᵀ =",
                resultado["transpuesta_a"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "Bᵀ =",
                resultado["transpuesta_b"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "Aᵀ + Bᵀ =",
                resultado["lado_derecho"],
            )

        elif codigo == "transpuesta_escalar":
            lineas.append("r = " + str(resultado["escalar"]))
            lineas.append("")
            self._agregar_matriz_propiedad(
                lineas,
                "rA =",
                resultado["r_a"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "(rA)ᵀ =",
                resultado["lado_izquierdo"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "Aᵀ =",
                resultado["transpuesta_a"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "rAᵀ =",
                resultado["lado_derecho"],
            )

        elif codigo == "transpuesta_producto":
            self._agregar_matriz_propiedad(
                lineas,
                "AB =",
                resultado["producto_ab"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "(AB)ᵀ =",
                resultado["lado_izquierdo"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "Aᵀ =",
                resultado["transpuesta_a"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "Bᵀ =",
                resultado["transpuesta_b"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "BᵀAᵀ =",
                resultado["lado_derecho"],
            )

        elif codigo == "distributiva_escalar_transpuesta":
            lineas.append("r = " + str(resultado["escalar"]))
            lineas.append("")
            self._agregar_matriz_propiedad(
                lineas,
                "A + B =",
                resultado["suma_ab"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "r(A + B) =",
                resultado["r_suma"],
            )
            lineas.extend(["LADO IZQUIERDO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "(r(A + B))ᵀ =",
                resultado["lado_izquierdo"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "Aᵀ =",
                resultado["transpuesta_a"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "Bᵀ =",
                resultado["transpuesta_b"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "rAᵀ =",
                resultado["r_transpuesta_a"],
            )
            self._agregar_matriz_propiedad(
                lineas,
                "rBᵀ =",
                resultado["r_transpuesta_b"],
            )
            lineas.extend(["LADO DERECHO", ""])
            self._agregar_matriz_propiedad(
                lineas,
                "rAᵀ + rBᵀ =",
                resultado["lado_derecho"],
            )

        lineas.append("=" * 60)
        lineas.append("")
        lineas.append(
            "Se cumple"
            if resultado["cumple"]
            else "No se cumple"
        )

        return "\n".join(lineas)

    def _resolver_propiedad_general(self):
        """Procesa la propiedad general seleccionada."""
        try:
            codigo = self.propiedades_generales[
                self.propiedad_general.get()
            ]

            necesita_b = codigo in (
                "asociativa",
                "distributiva_izquierda",
                "distributiva_derecha",
                "escalar_producto",
                "transpuesta_suma",
                "transpuesta_producto",
                "distributiva_escalar_transpuesta",
            )

            necesita_c = codigo in (
                "asociativa",
                "distributiva_izquierda",
                "distributiva_derecha",
            )

            necesita_escalar = codigo in (
                "escalar_producto",
                "transpuesta_escalar",
                "distributiva_escalar_transpuesta",
            )

            matriz_a = self.prop_general_a.leer()
            matriz_b = self.prop_general_b.leer() if necesita_b else None
            matriz_c = self.prop_general_c.leer() if necesita_c else None
            escalar = (
                self.escalar_propiedad_general.get()
                if necesita_escalar
                else None
            )

            resultado = procesar_propiedad_matrices(
                codigo,
                matriz_a,
                matriz_b,
                matriz_c,
                escalar,
            )

            self._colocar_texto(
                self.txt_propiedades_generales,
                self._formatear_propiedad_general(
                    codigo,
                    resultado,
                ),
            )

        except (ValueError, KeyError) as error:
            messagebox.showerror("Error", str(error))
