"""Interfaz del Programa 7: bisección, gráfica, bases y errores.

Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from controladores.modulo_numerico_controller import (
    procesar_biseccion, procesar_grafica, procesar_posicional,
    procesar_errores, ejemplos_punto_flotante,
)
from utilidades.formato_numerico import (
    formatear_biseccion, formatear_posicional, formatear_errores,
)


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
        """Crea el formulario y la tabla del método de bisección."""
        pestaña = ttk.Frame(self.cuaderno)
        self.cuaderno.add(pestaña, text="1. Bisección")
        fila1 = ttk.Frame(pestaña)
        fila1.pack(fill="x", pady=(8, 3))
        self.funcion_b = self._campo(fila1, "f(x):", "x**3 - 2*x - 5", 35)
        self.a_b = self._campo(fila1, "a:", "2")
        self.b_b = self._campo(fila1, "b:", "3")
        fila2 = ttk.Frame(pestaña)
        fila2.pack(fill="x", pady=3)
        self.tolerancia_b = self._campo(fila2, "Tolerancia absoluta E:", "0.0001")
        self.maximo_b = self._campo(fila2, "Iteraciones máximas:", "100", 9)
        ttk.Button(fila2, text="Calcular bisección", command=lambda:
                   self._ejecutar(self._calcular_biseccion)).pack(side="left", padx=10)
        ttk.Label(pestaña, text="Una reducción de intervalo solo garantiza raíz si la función es continua; "
                  "verifique el dominio de la función elegida.", wraplength=1000).pack(anchor="w", padx=12)
        self.salida_b = self._salida(pestaña)

    def _calcular_biseccion(self):
        """Ejecuta el algoritmo y conserva la raíz para la gráfica."""
        resultado = procesar_biseccion(self.funcion_b.get(), self.a_b.get(),
                                       self.b_b.get(), self.tolerancia_b.get(),
                                       self.maximo_b.get())
        self.ultima_biseccion = resultado
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
        ttk.Button(controles, text="Graficar", command=lambda:
                   self._ejecutar(self._graficar)).pack(side="left", padx=8)
        ttk.Button(controles, text="Usar última bisección", command=lambda:
                   self._ejecutar(self._usar_biseccion)).pack(side="left", padx=3)
        self.estado_g = tk.StringVar(value="Se evalúan 1201 puntos; los valores fuera del dominio se omiten.")
        ttk.Label(pestaña, textvariable=self.estado_g, wraplength=1050).pack(anchor="w", padx=12)
        self.canvas = tk.Canvas(pestaña, background="white", highlightthickness=1,
                                highlightbackground="#999")
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
            canvas.create_line(px, y0, px, y1, fill="#e5e7eb")
            canvas.create_line(x0, py, x1, py, fill="#e5e7eb")
            canvas.create_text(px, y1 + 17, text=f"{minimo + (maximo-minimo)*i/5:.3g}",
                               font=("Arial", 9))
            canvas.create_text(x0 - 8, py, text=f"{superior - (superior-inferior)*i/5:.3g}",
                               anchor="e", font=("Arial", 9))
        if minimo <= 0 <= maximo:
            canvas.create_line(sx(0), y0, sx(0), y1, fill="#555", width=2)
        if inferior <= 0 <= superior:
            canvas.create_line(x0, sy(0), x1, sy(0), fill="#555", width=2)
        canvas.create_text(ancho / 2, 17, text=f"f(x) = {datos['expresion']}",
                           font=("Arial", 12, "bold"))
        canvas.create_text(ancho / 2, alto - 12, text="x", font=("Arial", 11))
        canvas.create_text(16, alto / 2, text="f(x)", angle=90, font=("Arial", 11))
        canvas.create_line(x1 - 135, y0 + 14, x1 - 110, y0 + 14,
                           fill="#1672b8", width=2)
        canvas.create_text(x1 - 105, y0 + 14, text="Función", anchor="w")
        anterior = None
        salto = (superior - inferior) * 0.65
        for x, y in datos["puntos"]:
            if y is None or abs(y) > limite or y < inferior or y > superior:
                anterior = None
                continue
            actual = (sx(x), sy(y), y)
            if anterior is not None and abs(y - anterior[2]) <= salto:
                canvas.create_line(anterior[0], anterior[1], actual[0], actual[1],
                                   fill="#1672b8", width=2)
            anterior = actual
        raiz = self.ultima_biseccion
        if raiz and raiz["convergio"] and raiz["expresion"] == datos["expresion"]:
            rx = raiz["raiz"]
            ry = raiz["valor_funcion"]
            if minimo <= rx <= maximo and inferior <= ry <= superior:
                canvas.create_oval(sx(rx)-5, sy(ry)-5, sx(rx)+5, sy(ry)+5,
                                   fill="#d32f2f", outline="#d32f2f")
                canvas.create_text(sx(rx)+8, sy(ry)-10,
                                   text=f"Raíz ≈ {rx:.7g}", anchor="w", fill="#a11919")
            a, b = raiz["intervalo_inicial"]
            if minimo <= a <= maximo and minimo <= b <= maximo:
                canvas.create_line(sx(a), y1+3, sx(b), y1+3, fill="#d32f2f", width=3)
                canvas.create_text((sx(a)+sx(b))/2, y1+32,
                                   text="Intervalo inicial de bisección", fill="#a11919")

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
        ttk.Button(controles, text="Descomponer", command=lambda:
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
        ttk.Button(segunda, text="Analizar errores", command=lambda:
                   self._ejecutar(self._calcular_errores)).pack(side="left", padx=10)
        self.salida_e = self._salida(pestaña)

    def _calcular_errores(self):
        """Calcula y explica los tres errores y la propagación."""
        errores, propagacion = procesar_errores(
            self.verdadero_e.get(), self.aproximado_e.get(),
            self.x_e.get(), self.delta_e.get())
        self._mostrar(self.salida_e, formatear_errores(
            errores, propagacion, ejemplos_punto_flotante()))
