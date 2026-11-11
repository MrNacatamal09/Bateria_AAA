"""Interfaz del Programa 7: bisección, gráfica, bases y errores.

Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk
from utilidades import dialogos_interfaz as messagebox

from controladores.modulo_numerico_controller import (
    procesar_biseccion, procesar_grafica, procesar_posicional,
    procesar_errores, ejemplos_punto_flotante,
)
from utilidades.formato_numerico import (
    formatear_biseccion, formatear_posicional, formatear_errores,
)
from utilidades.tema_interfaz import COLORES


class ModuloNumericoInterfaz(ttk.Frame):
    """Organiza cuatro opciones del módulo numérico en pestañas."""

    def __init__(self, contenedor):
        """Construye formularios y áreas de resultados."""
        super().__init__(contenedor)
        self.ultima_biseccion = None
        self.grafica_actual = None
        ttk.Label(self, text="Módulo 6 · Métodos Numéricos · Programa 7",
                  font=("Arial", 15, "bold")).pack(pady=(8, 3))
        ttk.Label(self, text="Funciones: x, pi, e, sin, cos, tan, exp, log, sqrt, abs; potencias con **.",
                  wraplength=1050).pack(pady=(0, 7))
        self.cuaderno = ttk.Notebook(self)
        self.cuaderno.pack(fill="both", expand=True, padx=10, pady=(0, 8))
        self._crear_biseccion()
        self._crear_grafica()
        self._crear_posicional()
        self._crear_errores()

    @staticmethod
    def _campo(marco, etiqueta, valor, ancho=16):
        """Crea una entrada etiquetada y devuelve su variable."""
        ttk.Label(marco, text=etiqueta).pack(side="left", padx=(8, 2))
        variable = tk.StringVar(value=valor)
        ttk.Entry(marco, textvariable=variable, width=ancho).pack(side="left", padx=(0, 5))
        return variable

    @staticmethod
    def _campo_vertical(marco, etiqueta, valor, ancho=None, expandir=False):
        """Agrupa una etiqueta y su entrada para el formulario compacto."""
        grupo = ttk.Frame(marco)
        grupo.pack(side="left", fill="x" if expandir else "none",
                   expand=expandir, padx=(0, 10))
        ttk.Label(grupo, text=etiqueta).pack(anchor="w", pady=(0, 4))
        variable = tk.StringVar(value=valor)
        opciones = {"textvariable": variable}
        if ancho is not None:
            opciones["width"] = ancho
        entrada = ttk.Entry(grupo, **opciones)
        entrada.pack(fill="x" if expandir else "none")
        return variable

    @staticmethod
    def _salida(contenedor):
        """Construye un área desplazable de texto de solo lectura."""
        marco = ttk.Frame(contenedor)
        marco.pack(fill="both", expand=True, padx=8, pady=8)
        texto = tk.Text(marco, font=("Consolas", 10), wrap="none")
        texto.grid(row=0, column=0, sticky="nsew")
        vertical = ttk.Scrollbar(marco, orient="vertical", command=texto.yview)
        vertical.grid(row=0, column=1, sticky="ns")
        horizontal = ttk.Scrollbar(marco, orient="horizontal", command=texto.xview)
        horizontal.grid(row=1, column=0, sticky="ew")
        texto.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set,
                        state="disabled")
        marco.rowconfigure(0, weight=1)
        marco.columnconfigure(0, weight=1)
        return texto

    @staticmethod
    def _mostrar(texto, contenido):
        """Actualiza el resultado sin permitir modificaciones accidentales."""
        texto.configure(state="normal")
        texto.delete("1.0", "end")
        texto.insert("1.0", contenido)
        texto.configure(state="disabled")

    @staticmethod
    def _ejecutar(accion):
        """Muestra errores de entrada sin cerrar la calculadora."""
        try:
            accion()
        except ValueError as error:
            messagebox.showerror("Datos no válidos", str(error))

    def _crear_biseccion(self):
        """Organiza el formulario, el resultado y el procedimiento."""
        pestaña = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pestaña, text="1. Bisección")
        datos = ttk.LabelFrame(pestaña, text="Datos de entrada", padding=10)
        datos.pack(fill="x", padx=8, pady=(8, 6))

        fila_funcion = ttk.Frame(datos)
        fila_funcion.pack(fill="x", pady=(0, 9))
        self.funcion_b = self._campo_vertical(
            fila_funcion, "Función f(x)", "x**3 - 2*x - 5", expandir=True)
        self.a_b = self._campo_vertical(fila_funcion, "Extremo a", "2", ancho=9)
        self.b_b = self._campo_vertical(fila_funcion, "Extremo b", "3", ancho=9)

        fila_parametros = ttk.Frame(datos)
        fila_parametros.pack(fill="x")
        self.tolerancia_b = self._campo_vertical(
            fila_parametros, "Tolerancia absoluta E", "0.0001", ancho=17)
        self.maximo_b = self._campo_vertical(
            fila_parametros, "Iteraciones máximas", "100", ancho=13)
        ttk.Button(
            fila_parametros,
            text="Calcular bisección",
            style="Accion.TButton",
            command=lambda: self._ejecutar(self._calcular_biseccion),
        ).pack(side="left", pady=(17, 0))

        resultado = ttk.LabelFrame(pestaña, text="Resultado", padding=10)
        resultado.pack(fill="x", padx=8, pady=(0, 6))
        resultado.columnconfigure(0, weight=2)
        resultado.columnconfigure(1, weight=1)
        resultado.columnconfigure(2, weight=1)

        self.resumen_raiz_b = tk.StringVar(value="—")
        self.resumen_iteraciones_b = tk.StringVar(value="—")
        self.resumen_cota_b = tk.StringVar(value="—")
        self.resumen_estado_b = tk.StringVar(value="Esperando cálculo")
        ttk.Label(resultado, text="Raíz aproximada").grid(
            row=0, column=0, sticky="w")
        ttk.Label(
            resultado, textvariable=self.resumen_raiz_b,
            style="ResultadoNumero.TLabel",
        ).grid(row=1, column=0, sticky="w", padx=(0, 12))
        ttk.Label(resultado, text="Iteraciones").grid(
            row=0, column=1, sticky="w")
        ttk.Label(
            resultado, textvariable=self.resumen_iteraciones_b,
            style="ResultadoDato.TLabel",
        ).grid(row=1, column=1, sticky="w")
        ttk.Label(resultado, text="Cota del error").grid(
            row=0, column=2, sticky="w")
        ttk.Label(
            resultado, textvariable=self.resumen_cota_b,
            style="ResultadoDato.TLabel",
        ).grid(row=1, column=2, sticky="w")
        ttk.Label(
            resultado, textvariable=self.resumen_estado_b,
            wraplength=550,
        ).grid(row=2, column=0, columnspan=3, sticky="w", pady=(7, 0))

        procedimiento = ttk.LabelFrame(
            pestaña, text="Procedimiento", padding=2)
        procedimiento.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        self.salida_b = self._salida(procedimiento)

    def _calcular_biseccion(self):
        """Ejecuta el algoritmo y conserva la raíz para la gráfica."""
        resultado = procesar_biseccion(self.funcion_b.get(), self.a_b.get(),
                                       self.b_b.get(), self.tolerancia_b.get(),
                                       self.maximo_b.get())
        self.ultima_biseccion = resultado
        self.resumen_raiz_b.set(f"{resultado['raiz']:.12g}")
        self.resumen_iteraciones_b.set(str(len(resultado["tabla"])))
        self.resumen_cota_b.set(f"{resultado['cota']:.6g}")
        self.resumen_estado_b.set(resultado["motivo"])
        self._mostrar(self.salida_b, formatear_biseccion(resultado))

    def _crear_grafica(self):
        """Crea el lienzo y los controles del graficador."""
        pestaña = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pestaña, text="2. Graficador")
        controles = ttk.Frame(pestaña)
        controles.pack(fill="x", pady=8)
        self.funcion_g = self._campo(controles, "f(x):", "1/x", 35)
        self.minimo_g = self._campo(controles, "x mínimo:", "-5")
        self.maximo_g = self._campo(controles, "x máximo:", "5")
        ttk.Button(controles, text="Graficar", style="Accion.TButton", command=lambda:
                   self._ejecutar(self._graficar)).pack(side="left", padx=8)
        ttk.Button(controles, text="Usar última bisección", command=lambda:
                   self._ejecutar(self._usar_biseccion)).pack(side="left", padx=3)
        self.estado_g = tk.StringVar(value="Se evalúan 1201 puntos; los valores fuera del dominio se omiten.")
        ttk.Label(pestaña, textvariable=self.estado_g, wraplength=1050).pack(anchor="w", padx=12)
        self.canvas = tk.Canvas(pestaña, background=COLORES["superficie"],
                                highlightthickness=1,
                                highlightbackground=COLORES["borde"])
        self.canvas.pack(fill="both", expand=True, padx=10, pady=8)
        self.canvas.bind("<Configure>", lambda _event: self._dibujar())

    def _usar_biseccion(self):
        """Pasa la última función y el intervalo inicial al graficador."""
        if self.ultima_biseccion is None:
            raise ValueError("Calcule primero una bisección.")
        resultado = self.ultima_biseccion
        self.funcion_g.set(resultado["expresion"])
        a, b = resultado["intervalo_inicial"]
        ancho = b - a
        self.minimo_g.set(str(a - ancho * 0.15))
        self.maximo_g.set(str(b + ancho * 0.15))
        self.cuaderno.select(1)
        self._graficar()

    def _graficar(self):
        """Muestrea la función y pinta segmentos válidos."""
        self.grafica_actual = procesar_grafica(self.funcion_g.get(),
                                              self.minimo_g.get(), self.maximo_g.get())
        self.estado_g.set(f"{self.grafica_actual['validos']} de 1201 puntos reales finitos; "
                          "se separan dominios inválidos y saltos aparentes.")
        self._dibujar()

    def _dibujar(self):
        """Dibuja ejes, cuadrícula, leyenda y ramas sin cruzar asíntotas."""
        if self.grafica_actual is None:
            return
        canvas = self.canvas
        canvas.delete("all")
        ancho, alto = canvas.winfo_width(), canvas.winfo_height()
        if ancho < 150 or alto < 150:
            return
        margen = (65, 40, 30, 55)
        izq, arr, der, abajo = margen
        x0, x1 = izq, ancho - der
        y0, y1 = arr, alto - abajo
        datos = self.grafica_actual
        minimo, maximo = datos["intervalo"]
        limite = datos["limite_visual"]
        visibles = [y for _, y in datos["puntos"] if y is not None and abs(y) <= limite]
        inferior = min(0, min(visibles, default=-1))
        superior = max(0, max(visibles, default=1))
        if inferior == superior:
            inferior -= 1
            superior += 1
        margen_y = (superior - inferior) * 0.08
        inferior -= margen_y
        superior += margen_y
        sx = lambda x: x0 + (x - minimo) / (maximo - minimo) * (x1 - x0)
        sy = lambda y: y1 - (y - inferior) / (superior - inferior) * (y1 - y0)
        for i in range(6):
            px = x0 + (x1 - x0) * i / 5
            py = y0 + (y1 - y0) * i / 5
            canvas.create_line(px, y0, px, y1, fill=COLORES["borde"])
            canvas.create_line(x0, py, x1, py, fill=COLORES["borde"])
            canvas.create_text(px, y1 + 17, text=f"{minimo + (maximo-minimo)*i/5:.3g}",
                               font=("Arial", 9), fill=COLORES["secundario"])
            canvas.create_text(x0 - 8, py, text=f"{superior - (superior-inferior)*i/5:.3g}",
                               anchor="e", font=("Arial", 9), fill=COLORES["secundario"])
        if minimo <= 0 <= maximo:
            canvas.create_line(sx(0), y0, sx(0), y1, fill=COLORES["secundario"], width=2)
        if inferior <= 0 <= superior:
            canvas.create_line(x0, sy(0), x1, sy(0), fill=COLORES["secundario"], width=2)
        canvas.create_text(ancho / 2, 17, text=f"f(x) = {datos['expresion']}",
                           font=("Arial", 12, "bold"), fill=COLORES["texto"])
        canvas.create_text(ancho / 2, alto - 12, text="x",
                           font=("Arial", 11), fill=COLORES["texto"])
        canvas.create_text(16, alto / 2, text="f(x)", angle=90,
                           font=("Arial", 11), fill=COLORES["texto"])
        canvas.create_line(x1 - 135, y0 + 14, x1 - 110, y0 + 14,
                           fill=COLORES["violeta"], width=2)
        canvas.create_text(x1 - 105, y0 + 14, text="Función",
                           anchor="w", fill=COLORES["texto"])
        anterior = None
        salto = (superior - inferior) * 0.65
        for x, y in datos["puntos"]:
            if y is None or abs(y) > limite or y < inferior or y > superior:
                anterior = None
                continue
            actual = (sx(x), sy(y), y)
            if anterior is not None and abs(y - anterior[2]) <= salto:
                canvas.create_line(anterior[0], anterior[1], actual[0], actual[1],
                                   fill=COLORES["violeta"], width=2)
            anterior = actual
        raiz = self.ultima_biseccion
        if raiz and raiz["convergio"] and raiz["expresion"] == datos["expresion"]:
            rx = raiz["raiz"]
            ry = raiz["valor_funcion"]
            if minimo <= rx <= maximo and inferior <= ry <= superior:
                canvas.create_oval(sx(rx)-5, sy(ry)-5, sx(rx)+5, sy(ry)+5,
                                   fill=COLORES["magenta"], outline=COLORES["magenta"])
                canvas.create_text(sx(rx)+8, sy(ry)-10,
                                   text=f"Raíz ≈ {rx:.7g}", anchor="w",
                                   fill=COLORES["magenta"])
            a, b = raiz["intervalo_inicial"]
            if minimo <= a <= maximo and minimo <= b <= maximo:
                canvas.create_line(sx(a), y1+3, sx(b), y1+3,
                                   fill=COLORES["magenta"], width=3)
                canvas.create_text((sx(a)+sx(b))/2, y1+32,
                                   text="Intervalo inicial de bisección",
                                   fill=COLORES["magenta"])

    def _crear_posicional(self):
        """Construye la entrada de enteros decimales o binarios."""
        pestaña = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pestaña, text="3. Notación posicional")
        controles = ttk.Frame(pestaña)
        controles.pack(fill="x", pady=10)
        self.numero_p = self._campo(controles, "Número entero:", "84506", 22)
        ttk.Label(controles, text="Base de origen:").pack(side="left", padx=6)
        self.base_p = tk.StringVar(value="10")
        ttk.Combobox(controles, textvariable=self.base_p, values=("10", "2"),
                     state="readonly", width=5).pack(side="left")
        ttk.Button(controles, text="Descomponer", style="Accion.TButton", command=lambda:
                   self._ejecutar(self._calcular_posicional)).pack(side="left", padx=10)
        self.salida_p = self._salida(pestaña)

    def _calcular_posicional(self):
        """Muestra las expansiones en potencias de 10 y de 2."""
        resultado = procesar_posicional(self.numero_p.get(), int(self.base_p.get()))
        self._mostrar(self.salida_p, formatear_posicional(resultado))

    def _crear_errores(self):
        """Construye los experimentos de error y propagación."""
        pestaña = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pestaña, text="4. Errores numéricos")
        primera = ttk.Frame(pestaña)
        primera.pack(fill="x", pady=(9, 3))
        self.verdadero_e = self._campo(primera, "Valor verdadero xᵥ:", "3.141592653589793")
        self.aproximado_e = self._campo(primera, "Valor aproximado xₐ:", "3.14")
        segunda = ttk.Frame(pestaña)
        segunda.pack(fill="x", pady=3)
        self.x_e = self._campo(segunda, "Para f(x)=sin(x)+x², x:", "1")
        self.delta_e = self._campo(segunda, "Perturbación Δx:", "0.001")
        ttk.Button(segunda, text="Analizar errores", style="Accion.TButton", command=lambda:
                   self._ejecutar(self._calcular_errores)).pack(side="left", padx=10)
        self.salida_e = self._salida(pestaña)

    def _calcular_errores(self):
        """Calcula y explica los tres errores y la propagación."""
        errores, propagacion = procesar_errores(
            self.verdadero_e.get(), self.aproximado_e.get(),
            self.x_e.get(), self.delta_e.get())
        self._mostrar(self.salida_e, formatear_errores(
            errores, propagacion, ejemplos_punto_flotante()))
