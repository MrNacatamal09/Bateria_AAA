"""Interfaz del Programa 8: Jacobi y Gauss-Seidel para sistemas lineales.

Tema de clase: métodos iterativos, errores y comparación de soluciones.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import math
import tkinter as tk
from tkinter import ttk

from controladores.modulo_iterativos_controller import procesar_metodos_iterativos
from modulos.modulo_iterativos import obtener_teoremas_clave
from utilidades import dialogos_interfaz as messagebox
from utilidades.tema_interfaz import COLORES


SUBINDICES = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
CASOS = {
    "1. Convergencia": (
        [[10, 1, 1], [2, 10, 1], [2, 2, 10]],
        [15, 25, 36],
    ),
    "2. Reordenamiento": (
        [[0, 4, 1], [5, 1, 1], [1, 1, 6]],
        [11, 10, 21],
    ),
    "3. Diagonal imposible": (
        [[0, 1], [0, 2]],
        [1, 2],
    ),
}


def _numero(valor):
    """Da formato compacto a un dato numérico sin modificar su valor."""
    return "—" if valor is None else f"{valor:.9g}"


def _vector(valores):
    """Presenta las componentes de una solución en el orden recibido."""
    return "—" if valores is None else "[" + ",  ".join(_numero(x) for x in valores) + "]"


def _variable(indice):
    """Escribe el índice de una variable con subíndices Unicode."""
    return ("x" + str(indice).translate(SUBINDICES))


class EntradaSistemaIterativo(ttk.LabelFrame):
    """Mantiene sincronizadas las entradas de A, b y x⁽⁰⁾."""

    def __init__(self, contenedor, al_cambiar=None):
        """Construye un editor tabular con desplazamiento en ambos ejes."""
        super().__init__(contenedor, text="Sistema Ax = b", padding=6)
        self.al_cambiar = al_cambiar
        self.variable_orden = tk.StringVar(value="3")
        self.entradas_a = []
        self.entradas_b = []
        self.entradas_x0 = []
        self._variables_celdas = []

        controles = ttk.Frame(self)
        controles.pack(fill="x", pady=(0, 5))
        ttk.Label(controles, text="Orden n:").pack(side="left", padx=(2, 5))
        ttk.Entry(
            controles, textvariable=self.variable_orden,
            width=7, justify="center",
        ).pack(side="left", padx=(0, 8))
        ttk.Button(
            controles, text="Crear / ajustar sistema", command=self._ajustar,
        ).pack(side="left")
        ttk.Label(
            controles, text="A  |  b  |  x⁽⁰⁾",
            foreground=COLORES["secundario"],
        ).pack(side="right", padx=6)

        visor = ttk.Frame(self)
        visor.pack(fill="x")
        visor.rowconfigure(0, weight=1)
        visor.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(
            visor, height=145, highlightthickness=1,
            highlightbackground=COLORES["borde"],
            background=COLORES["superficie"],
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")
        vertical = ttk.Scrollbar(visor, orient="vertical", command=self.canvas.yview)
        vertical.grid(row=0, column=1, sticky="ns")
        horizontal = ttk.Scrollbar(visor, orient="horizontal", command=self.canvas.xview)
        horizontal.grid(row=1, column=0, sticky="ew")
        self.canvas.configure(
            yscrollcommand=vertical.set, xscrollcommand=horizontal.set,
        )
        self.contenido = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.contenido, anchor="nw")
        self.contenido.bind("<Configure>", self._actualizar_scroll)

    def _actualizar_scroll(self, _evento=None):
        """Actualiza el recorrido cuando cambian las filas o columnas."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _avisar_cambio(self, *_args):
        """Invalida un cálculo previo cuando cambia el texto de una celda."""
        if self.al_cambiar is not None:
            self.al_cambiar()

    def _ajustar(self):
        """Aplica el orden elegido sin descartar las celdas compartidas."""
        try:
            self.crear_sistema()
        except ValueError as error:
            messagebox.showerror(
                "Orden inválido", str(error), parent=self.winfo_toplevel())

    def _valores_actuales(self):
        """Recoge texto previo para conservarlo al cambiar la dimensión."""
        return (
            [[celda.get() for celda in fila] for fila in self.entradas_a],
            [celda.get() for celda in self.entradas_b],
            [celda.get() for celda in self.entradas_x0],
        )

    def crear_sistema(self, valores=None):
        """Crea n filas de A, b y x⁽⁰⁾ con una única dimensión común."""
        try:
            orden = int(self.variable_orden.get().strip())
        except ValueError:
            raise ValueError("El orden n debe ser un entero positivo.") from None
        if orden <= 0:
            raise ValueError("El orden n debe ser un entero positivo.")

        anteriores = self._valores_actuales() if valores is None else valores
        for elemento in self.contenido.winfo_children():
            elemento.destroy()
        self.entradas_a, self.entradas_b, self.entradas_x0 = [], [], []
        self._variables_celdas = []

        ttk.Label(self.contenido, text="Fila", foreground=COLORES["secundario"]).grid(
            row=0, column=0, padx=5, pady=3)
        for j in range(orden):
            ttk.Label(
                self.contenido, text=f"A · {_variable(j + 1)}",
                foreground=COLORES["secundario"],
            ).grid(row=0, column=j + 1, padx=3, pady=3)
        ttk.Label(self.contenido, text="b", foreground=COLORES["violeta"]).grid(
            row=0, column=orden + 1, padx=5)
        ttk.Label(self.contenido, text="x⁽⁰⁾", foreground=COLORES["magenta"]).grid(
            row=0, column=orden + 2, padx=5)

        antigua_a, antiguo_b, antiguo_x0 = anteriores
        for i in range(orden):
            ttk.Label(self.contenido, text=str(i + 1)).grid(
                row=i + 1, column=0, padx=5, pady=2)
            fila = []
            for j in range(orden):
                valor = antigua_a[i][j] if i < len(antigua_a) and j < len(antigua_a[i]) else "0"
                variable = tk.StringVar(value=str(valor))
                variable.trace_add("write", self._avisar_cambio)
                self._variables_celdas.append(variable)
                entrada = ttk.Entry(
                    self.contenido, width=10, justify="center", textvariable=variable,
                )
                entrada.grid(row=i + 1, column=j + 1, padx=3, pady=2)
                fila.append(entrada)
            self.entradas_a.append(fila)
            for columna, fuente, destino in (
                (orden + 1, antiguo_b, self.entradas_b),
                (orden + 2, antiguo_x0, self.entradas_x0),
            ):
                variable = tk.StringVar(value=str(fuente[i] if i < len(fuente) else "0"))
                variable.trace_add("write", self._avisar_cambio)
                self._variables_celdas.append(variable)
                entrada = ttk.Entry(
                    self.contenido, width=10, justify="center", textvariable=variable,
                )
                entrada.grid(row=i + 1, column=columna, padx=5, pady=2)
                destino.append(entrada)

        self.update_idletasks()
        self._actualizar_scroll()
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        self._avisar_cambio()

    def cargar(self, matriz, vector):
        """Carga un caso reproducible y pone x⁽⁰⁾ en cero."""
        self.variable_orden.set(str(len(matriz)))
        self.crear_sistema((matriz, vector, [0] * len(matriz)))

    def leer(self):
        """Entrega las cadenas visibles al controlador para validarlas."""
        try:
            orden = int(self.variable_orden.get().strip())
        except ValueError:
            raise ValueError("El orden n debe ser un entero positivo.") from None
        if orden <= 0:
            raise ValueError("El orden n debe ser un entero positivo.")
        if orden != len(self.entradas_a):
            raise ValueError(
                "El orden n cambió. Pulse «Crear / ajustar sistema» antes de resolver.")
        return self._valores_actuales()


class ModuloIterativosInterfaz(ttk.Frame):
    """Presenta Jacobi, Gauss-Seidel, su comparación y la gráfica."""

    def __init__(self, contenedor):
        """Construye las pestañas del Programa 8 y carga el primer caso."""
        super().__init__(contenedor)
        self.ultimo_resultado = None
        self._lienzo_grafica = None
        ttk.Label(
            self, text="Módulo 7 · Métodos Iterativos · Programa 8",
            font=("Segoe UI", 15, "bold"),
        ).pack(pady=(8, 3))
        ttk.Label(
            self, text="Jacobi y Gauss-Seidel para aproximar soluciones de Ax = b",
            foreground=COLORES["secundario"],
        ).pack(pady=(0, 7))
        self.cuaderno = ttk.Notebook(self)
        self.cuaderno.pack(fill="both", expand=True, padx=10, pady=(0, 8))
        self._crear_teoremas()
        self._crear_calculo()
        self._cargar_caso()

    def _crear_teoremas(self):
        """Muestra el resumen matemático del módulo en texto desplazable."""
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="0. Teoremas clave")
        pagina.rowconfigure(0, weight=1)
        pagina.columnconfigure(0, weight=1)
        texto = tk.Text(pagina, wrap="word", font=("Consolas", 10), padx=15, pady=10)
        texto.grid(row=0, column=0, sticky="nsew")
        barra = ttk.Scrollbar(pagina, orient="vertical", command=texto.yview)
        barra.grid(row=0, column=1, sticky="ns")
        texto.configure(yscrollcommand=barra.set)
        texto.insert("1.0", obtener_teoremas_clave())
        texto.configure(state="disabled")

    def _crear_calculo(self):
        """Separa datos, diagnóstico y resultados de los dos métodos."""
        pagina = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pagina, text="1. Jacobi y Gauss-Seidel")

        self.entrada = EntradaSistemaIterativo(
            pagina, al_cambiar=self._invalidar_resultado,
        )
        self.entrada.pack(fill="x", padx=8, pady=(8, 5))

        controles = ttk.Frame(pagina)
        controles.pack(fill="x", padx=10, pady=(0, 6))
        fila_casos = ttk.Frame(controles)
        fila_casos.pack(fill="x", pady=(0, 5))
        ttk.Label(fila_casos, text="Caso:").pack(side="left", padx=(0, 4))
        self.variable_caso = tk.StringVar(value=next(iter(CASOS)))
        ttk.Combobox(
            fila_casos, textvariable=self.variable_caso, values=tuple(CASOS),
            state="readonly", width=23,
        ).pack(side="left", padx=(0, 5))
        ttk.Button(fila_casos, text="Cargar", command=self._cargar_caso).pack(
            side="left")
        fila_parametros = ttk.Frame(controles)
        fila_parametros.pack(fill="x")
        ttk.Label(fila_parametros, text="Tolerancia ε:").pack(side="left", padx=(0, 4))
        self.variable_tolerancia = tk.StringVar(value="0.0001")
        ttk.Entry(
            fila_parametros, textvariable=self.variable_tolerancia, width=11,
        ).pack(side="left", padx=(0, 10))
        ttk.Label(fila_parametros, text="Máx. iteraciones:").pack(side="left", padx=(0, 4))
        self.variable_maximo = tk.StringVar(value="100")
        ttk.Entry(
            fila_parametros, textvariable=self.variable_maximo, width=7,
        ).pack(side="left", padx=(0, 10))
        ttk.Button(
            fila_parametros, text="Resolver ambos", style="Accion.TButton",
            command=self._resolver,
        ).pack(side="left")

        self.variable_diagnostico = tk.StringVar(value="Cargue un sistema y ejecute ambos métodos.")
        diagnostico = ttk.Label(
            pagina, textvariable=self.variable_diagnostico,
            foreground=COLORES["secundario"], wraplength=1000,
            justify="left",
        )
        diagnostico.pack(fill="x", padx=12, pady=(0, 5))
        diagnostico.bind(
            "<Configure>",
            lambda evento: diagnostico.configure(wraplength=max(250, evento.width - 12)),
        )

        self.resultados = ttk.Notebook(pagina)
        self.resultados.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        self.vistas_metodos = {}
        self._crear_pestana_metodo("jacobi", "Jacobi")
        self._crear_pestana_metodo("gauss_seidel", "Gauss-Seidel")
        self._crear_comparacion()
        self._crear_grafica()
        self.entrada.variable_orden.trace_add("write", self._invalidar_resultado)
        self.variable_tolerancia.trace_add("write", self._invalidar_resultado)
        self.variable_maximo.trace_add("write", self._invalidar_resultado)

    def _invalidar_resultado(self, *_args):
        """Retira resultados si el usuario cambia los datos calculados."""
        if self.ultimo_resultado is not None:
            self._limpiar_resultados()

    def _crear_pestana_metodo(self, clave, nombre):
        """Prepara resumen y tabla de iteraciones para un método."""
        pagina = ttk.Frame(self.resultados)
        self.resultados.add(pagina, text=nombre)
        resumen = ttk.LabelFrame(pagina, text=f"Resultado · {nombre}", padding=8)
        resumen.pack(fill="x", padx=5, pady=(6, 5))
        solucion = tk.StringVar(value="Solución aproximada: —")
        metricas = tk.StringVar(value="Iteraciones: —   Error: —   Residuo: —")
        estado = tk.StringVar(value="Estado: esperando cálculo")
        etiqueta_solucion = ttk.Label(
            resumen, textvariable=solucion, style="ResultadoDato.TLabel",
            wraplength=850,
        )
        etiqueta_solucion.pack(anchor="w")
        ttk.Label(resumen, textvariable=metricas).pack(anchor="w", pady=(4, 0))
        etiqueta_estado = ttk.Label(resumen, textvariable=estado, wraplength=850)
        etiqueta_estado.pack(anchor="w", pady=(4, 0))
        resumen.bind(
            "<Configure>",
            lambda evento: (
                etiqueta_solucion.configure(wraplength=max(250, evento.width - 24)),
                etiqueta_estado.configure(wraplength=max(250, evento.width - 24)),
            ),
        )

        marco = ttk.Frame(pagina)
        marco.pack(fill="both", expand=True, padx=5, pady=(0, 5))
        marco.rowconfigure(0, weight=1)
        marco.columnconfigure(0, weight=1)
        tabla = ttk.Treeview(marco, show="headings", columns=("iteracion", "error"))
        tabla.grid(row=0, column=0, sticky="nsew")
        vertical = ttk.Scrollbar(marco, orient="vertical", command=tabla.yview)
        vertical.grid(row=0, column=1, sticky="ns")
        horizontal = ttk.Scrollbar(marco, orient="horizontal", command=tabla.xview)
        horizontal.grid(row=1, column=0, sticky="ew")
        tabla.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)
        self.vistas_metodos[clave] = (solucion, metricas, estado, tabla)

    def _crear_comparacion(self):
        """Prepara una lectura conjunta de métodos y solución de referencia."""
        pagina = ttk.Frame(self.resultados)
        self.resultados.add(pagina, text="Comparación")
        pagina.rowconfigure(0, weight=1)
        pagina.columnconfigure(0, weight=1)
        self.texto_comparacion = tk.Text(
            pagina, wrap="word", font=("Consolas", 10), padx=15, pady=12,
        )
        self.texto_comparacion.grid(row=0, column=0, sticky="nsew")
        barra = ttk.Scrollbar(pagina, orient="vertical", command=self.texto_comparacion.yview)
        barra.grid(row=0, column=1, sticky="ns")
        self.texto_comparacion.configure(yscrollcommand=barra.set, state="disabled")

    def _crear_grafica(self):
        """Reserva una pestaña para la gráfica comparativa embebida."""
        self.pagina_grafica = ttk.Frame(self.resultados)
        self.resultados.add(self.pagina_grafica, text="Gráfica de error")
        self._mensaje_grafica("Ejecute ambos métodos para comparar sus errores.")

    def _mensaje_grafica(self, mensaje):
        """Sustituye una gráfica anterior por un mensaje legible."""
        for widget in self.pagina_grafica.winfo_children():
            widget.destroy()
        self._lienzo_grafica = None
        ttk.Label(
            self.pagina_grafica, text=mensaje,
            foreground=COLORES["secundario"], wraplength=700,
        ).pack(anchor="center", expand=True)

    def _cargar_caso(self):
        """Carga uno de los tres casos de prueba sin ejecutar el cálculo."""
        matriz, vector = CASOS[self.variable_caso.get()]
        self.entrada.cargar(matriz, vector)
        self._limpiar_resultados()

    def _limpiar_resultados(self):
        """Retira resultados anteriores cuando cambian los datos."""
        self.ultimo_resultado = None
        self.variable_diagnostico.set("Cargue un sistema y ejecute ambos métodos.")
        for solucion, metricas, estado, tabla in self.vistas_metodos.values():
            solucion.set("Solución aproximada: —")
            metricas.set("Iteraciones: —   Error: —   Residuo: —")
            estado.set("Estado: esperando cálculo")
            for fila in tabla.get_children():
                tabla.delete(fila)
        self._mostrar_texto(self.texto_comparacion, "")
        self._mensaje_grafica("Ejecute ambos métodos para comparar sus errores.")

    @staticmethod
    def _mostrar_texto(caja, contenido):
        """Actualiza un texto de solo lectura."""
        caja.configure(state="normal")
        caja.delete("1.0", "end")
        caja.insert("1.0", contenido)
        caja.configure(state="disabled")

    def _resolver(self):
        """Entrega entradas al controlador y distribuye sus resultados."""
        try:
            matriz, vector, inicial = self.entrada.leer()
            resultado = procesar_metodos_iterativos(
                matriz, vector, inicial,
                self.variable_tolerancia.get(), self.variable_maximo.get(),
            )
        except (ValueError, OverflowError, ArithmeticError) as error:
            messagebox.showerror(
                "Datos no válidos", str(error), parent=self.winfo_toplevel())
            return

        self.ultimo_resultado = resultado
        self._actualizar_diagnostico(resultado)
        for clave in ("jacobi", "gauss_seidel"):
            self._actualizar_metodo(clave, resultado[clave])
        self._actualizar_comparacion(resultado)
        self._actualizar_grafica(resultado)

    def _actualizar_diagnostico(self, resultado):
        """Expone la diagonal y el orden de filas realmente usados."""
        orden = resultado["reordenamiento"]
        original = ("sí" if resultado["dominancia_original"] else "no")
        usada = ("sí" if resultado["dominancia_usada"] else "no")
        texto = (
            f"Diagonal estrictamente dominante: A original {original}; "
            f"A preparada {usada}. {orden['mensaje']}"
        )
        if orden["ejecutable"]:
            texto += f" Orden de filas originales utilizado: {orden['orden']}."
        else:
            texto += " No se ejecutaron los métodos por diagonal inválida."
        if not resultado["dominancia_usada"]:
            texto += (" La ausencia de dominancia estricta no implica "
                      "automáticamente divergencia.")
        self.variable_diagnostico.set(texto)

    def _actualizar_metodo(self, clave, resultado):
        """Llena el resumen y la tabla dinámica de una ejecución."""
        solucion, metricas, estado, tabla = self.vistas_metodos[clave]
        solucion.set("Solución aproximada: " + _vector(resultado["solucion"]))
        metricas.set(
            f"Iteraciones: {resultado['numero_iteraciones']}    "
            f"Error final: {_numero(resultado['error_final'])}    "
            f"Residuo ||Ax-b||∞: {_numero(resultado['residuo_final'])}"
        )
        estado.set("Estado: " + resultado["estado"])
        for fila in tabla.get_children():
            tabla.delete(fila)

        orden = len(self.ultimo_resultado["x0"])
        columnas = ["iteracion"] + [f"x{i}" for i in range(1, orden + 1)] + ["error", "residuo"]
        tabla.configure(columns=columnas)
        for columna in columnas:
            nombre = (
                "Iteración" if columna == "iteracion" else
                "Error ||Δx||∞" if columna == "error" else
                "Residuo ||Ax-b||∞" if columna == "residuo" else
                _variable(int(columna[1:]))
            )
            tabla.heading(columna, text=nombre)
            tabla.column(
                columna, anchor="center", stretch=False,
                width=150 if columna == "residuo" else 130 if columna == "error" else 95,
                minwidth=75,
            )
        for paso in resultado["iteraciones"]:
            valores = [str(paso["numero"])]
            valores.extend(_numero(x) for x in paso["x"])
            valores.extend((_numero(paso["error"]), _numero(paso["residuo"])))
            tabla.insert("", "end", values=valores)

    def _actualizar_comparacion(self, resultado):
        """Muestra los datos comparativos ya calculados por el módulo."""
        jacobi = resultado["jacobi"]
        seidel = resultado["gauss_seidel"]
        comparacion = resultado["comparacion"]
        referencia = resultado["referencia"]
        lineas = [
            "COMPARACIÓN DE MÉTODOS",
            "",
            f"Jacobi convergió: {'sí' if jacobi['convergio'] else 'no'}",
            f"Gauss-Seidel convergió: {'sí' if seidel['convergio'] else 'no'}",
            f"Iteraciones Jacobi: {jacobi['numero_iteraciones']}",
            f"Iteraciones Gauss-Seidel: {seidel['numero_iteraciones']}",
            f"Menos iteraciones para converger: {comparacion['metodo_menos_iteraciones']}",
            "",
            f"Solución Jacobi: {_vector(jacobi['solucion'])}",
            f"Solución Gauss-Seidel: {_vector(seidel['solucion'])}",
            f"||x_J - x_GS||∞: {_numero(comparacion['diferencia'])}",
            f"Residuo Jacobi: {_numero(jacobi['residuo_final'])}",
            f"Residuo Gauss-Seidel: {_numero(seidel['residuo_final'])}",
            "",
            "VALIDACIÓN CON GAUSS-JORDAN",
            f"{referencia['estado']}",
            f"Solución de referencia: {_vector(referencia['solucion'])}",
            f"||x_J - x_ref||∞: {_numero(referencia['diferencia_jacobi'])}",
            f"||x_GS - x_ref||∞: {_numero(referencia['diferencia_gauss_seidel'])}",
        ]
        self._mostrar_texto(self.texto_comparacion, "\n".join(lineas))

    def _actualizar_grafica(self, resultado):
        """Dibuja los errores de ambos historiales válidos con Matplotlib."""
        series = []
        for clave, nombre, color in (
            ("jacobi", "Jacobi", COLORES["violeta"]),
            ("gauss_seidel", "Gauss-Seidel", COLORES["magenta"]),
        ):
            puntos = [
                (paso["numero"], paso["error"])
                for paso in resultado[clave]["iteraciones"]
                if paso["error"] is not None and math.isfinite(paso["error"])
            ]
            if not puntos:
                self._mensaje_grafica(
                    "La gráfica requiere iteraciones válidas de Jacobi y Gauss-Seidel.")
                return
            series.append((nombre, color, puntos))

        try:
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            from matplotlib.figure import Figure
        except ImportError:
            self._mensaje_grafica(
                "Matplotlib no está instalado; las tablas y resultados siguen disponibles.")
            return

        for widget in self.pagina_grafica.winfo_children():
            widget.destroy()
        figura = Figure(figsize=(7, 4), dpi=100, facecolor=COLORES["superficie"])
        ejes = figura.add_subplot(111)
        ejes.set_facecolor(COLORES["superficie"])
        for nombre, color, puntos in series:
            ejes.plot(
                [numero for numero, _ in puntos],
                [error for _, error in puntos],
                marker="o", markersize=3, linewidth=2,
                color=color, label=nombre,
            )
        ejes.set_xlabel("Iteración", color=COLORES["texto"])
        ejes.set_ylabel("Error ||x⁽ᵏ⁾ - x⁽ᵏ⁻¹⁾||∞", color=COLORES["texto"])
        ejes.set_title("Error por iteración", color=COLORES["texto"])
        ejes.tick_params(colors=COLORES["secundario"])
        for borde in ejes.spines.values():
            borde.set_color(COLORES["borde"])
        ejes.grid(color=COLORES["borde"], alpha=0.6)
        leyenda = ejes.legend(facecolor=COLORES["suave"], edgecolor=COLORES["borde"])
        for etiqueta in leyenda.get_texts():
            etiqueta.set_color(COLORES["texto"])
        figura.tight_layout()
        self._lienzo_grafica = FigureCanvasTkAgg(figura, master=self.pagina_grafica)
        self._lienzo_grafica.get_tk_widget().pack(fill="both", expand=True)
        self._lienzo_grafica.draw_idle()
