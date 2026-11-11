"""Tema oscuro de la calculadora.

Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import sys
import tkinter as tk
from tkinter import ttk


COLORES = {
    "fondo": "#101018",
    "lateral": "#15151F",
    "superficie": "#191923",
    "suave": "#282637",
    "hover": "#38324E",
    "borde": "#393746",
    "texto": "#F4F0F9",
    "secundario": "#B7B0C8",
    "violeta": "#A58BFF",
    "magenta": "#EF82CD",
    "azul": "#7180FF",
    "coral": "#FF98A7",
}


def aplicar_barra_oscura(ventana):
    """Colorea la barra de título en las versiones de Windows que lo permiten."""
    if sys.platform != "win32":
        return

    try:
        import ctypes

        ventana.update_idletasks()
        obtener_padre = ctypes.windll.user32.GetParent
        obtener_padre.argtypes = [ctypes.c_void_p]
        obtener_padre.restype = ctypes.c_void_p
        hwnd = obtener_padre(ventana.winfo_id())
        if not hwnd:
            hwnd = ventana.winfo_id()
        dwm = ctypes.windll.dwmapi.DwmSetWindowAttribute
        dwm.argtypes = [ctypes.c_void_p, ctypes.c_ulong,
                        ctypes.c_void_p, ctypes.c_ulong]
        dwm.restype = ctypes.c_long
        oscuro = ctypes.c_int(1)
        dwm(hwnd, 20, ctypes.byref(oscuro), ctypes.sizeof(oscuro))
        # COLORREF usa el orden BGR: fondo #191923 y texto #F4F0F9.
        fondo = ctypes.c_int(0x231919)
        texto = ctypes.c_int(0xF9F0F4)
        dwm(hwnd, 35, ctypes.byref(fondo), ctypes.sizeof(fondo))
        dwm(hwnd, 36, ctypes.byref(texto), ctypes.sizeof(texto))
    except (AttributeError, OSError, tk.TclError):
        pass


def aplicar_tema(ventana):
    """Configura ttk y los widgets clásicos antes de crear la interfaz."""
    estilo = ttk.Style(ventana)
    estilo.theme_use("clam")
    ventana.configure(background=COLORES["fondo"])

    for clase, opciones in {
        "Text": {
            "background": COLORES["superficie"],
            "foreground": COLORES["texto"],
            "insertBackground": COLORES["magenta"],
            "selectBackground": COLORES["hover"],
            "selectForeground": COLORES["texto"],
            "highlightBackground": COLORES["borde"],
            "highlightColor": COLORES["violeta"],
        },
        "Canvas": {"background": COLORES["superficie"]},
        "Listbox": {
            "background": COLORES["superficie"],
            "foreground": COLORES["texto"],
            "selectBackground": COLORES["hover"],
            "selectForeground": COLORES["texto"],
        },
    }.items():
        for nombre, valor in opciones.items():
            ventana.option_add(f"*{clase}.{nombre}", valor)
    ventana.option_add("*TCombobox*Listbox.background", COLORES["superficie"])
    ventana.option_add("*TCombobox*Listbox.foreground", COLORES["texto"])
    ventana.option_add("*TCombobox*Listbox.selectBackground", COLORES["hover"])
    ventana.option_add("*TCombobox*Listbox.selectForeground", COLORES["texto"])

    fuente = ("Segoe UI", 10)
    estilo.configure(".", font=fuente, background=COLORES["superficie"],
                     foreground=COLORES["texto"])
    estilo.configure("TFrame", background=COLORES["superficie"])
    estilo.configure("TLabel", background=COLORES["superficie"],
                     foreground=COLORES["texto"])
    estilo.configure("Cabecera.TFrame", background=COLORES["fondo"])
    estilo.configure("Lateral.TFrame", background=COLORES["lateral"])
    estilo.configure("Lateral.TLabel", background=COLORES["lateral"],
                     foreground=COLORES["secundario"], font=fuente)
    estilo.configure("MarcaLateral.TLabel", background=COLORES["lateral"],
                     foreground=COLORES["texto"],
                     font=("Segoe UI", 13, "bold"))
    estilo.configure("SeccionLateral.TLabel", background=COLORES["lateral"],
                     foreground=COLORES["secundario"],
                     font=("Segoe UI", 9, "bold"))
    estilo.configure("Ruta.TLabel", background=COLORES["fondo"],
                     foreground=COLORES["secundario"],
                     font=("Segoe UI", 10))
    estilo.configure("Titulo.TLabel", background=COLORES["fondo"],
                     foreground=COLORES["texto"],
                     font=("Segoe UI", 19, "bold"))
    estilo.configure("ResultadoNumero.TLabel", background=COLORES["superficie"],
                     foreground=COLORES["magenta"],
                     font=("Consolas", 20, "bold"))
    estilo.configure("ResultadoDato.TLabel", background=COLORES["superficie"],
                     foreground=COLORES["violeta"],
                     font=("Segoe UI", 11, "bold"))
    estilo.configure("Subtitulo.TLabel", background=COLORES["fondo"],
                     foreground=COLORES["secundario"], font=fuente)
    estilo.configure("TLabelFrame", background=COLORES["superficie"],
                     bordercolor=COLORES["borde"], borderwidth=1,
                     relief="solid")
    estilo.configure("TLabelFrame.Label", background=COLORES["superficie"],
                     foreground=COLORES["violeta"],
                     font=("Segoe UI", 10, "bold"))

    estilo.configure("TButton", background=COLORES["suave"],
                     foreground=COLORES["texto"],
                     bordercolor=COLORES["borde"], borderwidth=1,
                     padding=(11, 6), relief="flat", font=fuente)
    estilo.map("TButton",
               background=[("pressed", COLORES["hover"]),
                           ("active", COLORES["hover"]),
                           ("disabled", COLORES["superficie"])],
               foreground=[("disabled", COLORES["secundario"])],
               bordercolor=[("focus", COLORES["violeta"])])
    estilo.configure("Panel.TButton", background=COLORES["suave"],
                     foreground=COLORES["texto"], padding=(11, 5),
                     bordercolor=COLORES["borde"],
                     font=("Segoe UI", 10, "bold"))
    estilo.map("Panel.TButton",
               background=[("active", COLORES["hover"]),
                           ("pressed", COLORES["hover"])],
               bordercolor=[("focus", COLORES["violeta"])])
    estilo.configure("Navegacion.TButton", background=COLORES["lateral"],
                     foreground=COLORES["secundario"],
                     bordercolor=COLORES["lateral"],
                     padding=(12, 11), anchor="w",
                     font=("Segoe UI", 10))
    estilo.map("Navegacion.TButton",
               background=[("active", COLORES["hover"])],
               foreground=[("active", COLORES["texto"])])
    estilo.configure("NavegacionActiva.TButton", background="#302A41",
                     foreground=COLORES["texto"],
                     bordercolor="#302A41",
                     padding=(12, 11), anchor="w",
                     font=("Segoe UI", 10, "bold"))
    estilo.map("NavegacionActiva.TButton",
               background=[("active", COLORES["hover"])],
               foreground=[("active", COLORES["texto"])])
    estilo.configure("Accion.TButton", background="#644BC1",
                     foreground=COLORES["texto"],
                     bordercolor="#644BC1",
                     font=("Segoe UI", 10, "bold"), padding=(12, 7))
    estilo.map("Accion.TButton",
               background=[("pressed", "#785DDB"),
                           ("active", "#7157CE"),
                           ("disabled", COLORES["suave"])],
               foreground=[("disabled", COLORES["secundario"])])

    estilo.configure("TEntry", fieldbackground=COLORES["suave"],
                     background=COLORES["suave"],
                     foreground=COLORES["texto"],
                     insertcolor=COLORES["magenta"],
                     bordercolor=COLORES["borde"],
                     lightcolor=COLORES["borde"],
                     darkcolor=COLORES["borde"], padding=5)
    estilo.map("TEntry",
               fieldbackground=[("disabled", COLORES["superficie"]),
                                ("readonly", COLORES["suave"])],
               foreground=[("disabled", COLORES["secundario"])],
               bordercolor=[("focus", COLORES["violeta"])],
               lightcolor=[("focus", COLORES["violeta"])])
    estilo.configure("TCombobox", fieldbackground=COLORES["suave"],
                     background=COLORES["suave"],
                     foreground=COLORES["texto"],
                     arrowcolor=COLORES["violeta"],
                     bordercolor=COLORES["borde"], padding=4)
    estilo.map("TCombobox",
               fieldbackground=[("readonly", COLORES["suave"])],
               foreground=[("readonly", COLORES["texto"])],
               background=[("active", COLORES["hover"])],
               bordercolor=[("focus", COLORES["violeta"])])
    for nombre in ("TRadiobutton", "TCheckbutton"):
        estilo.configure(nombre, background=COLORES["superficie"],
                         foreground=COLORES["texto"], font=fuente)
        estilo.map(nombre,
                   background=[("active", COLORES["superficie"])],
                   foreground=[("active", COLORES["violeta"])])

    estilo.configure("TNotebook", background=COLORES["fondo"],
                     bordercolor=COLORES["borde"], borderwidth=1,
                     tabmargins=(4, 4, 4, 0))
    estilo.configure("TNotebook.Tab", background=COLORES["suave"],
                     foreground=COLORES["secundario"],
                     bordercolor=COLORES["borde"],
                     padding=(11, 8), font=("Segoe UI", 9, "bold"))
    estilo.map("TNotebook.Tab",
               background=[("selected", COLORES["superficie"]),
                           ("active", COLORES["hover"])],
               foreground=[("selected", COLORES["magenta"]),
                           ("active", COLORES["texto"])],
               bordercolor=[("selected", COLORES["violeta"])])
    estilo.layout("Explorador.TNotebook.Tab", [])
    estilo.configure("Explorador.TNotebook", background=COLORES["fondo"],
                     bordercolor=COLORES["fondo"], borderwidth=0,
                     tabmargins=(0, 0, 0, 0))
    estilo.configure("TScrollbar", background=COLORES["suave"],
                     troughcolor=COLORES["fondo"],
                     bordercolor=COLORES["fondo"],
                     arrowcolor=COLORES["violeta"])
    estilo.map("TScrollbar", background=[("active", COLORES["hover"])])
    ventana.after(0, lambda: aplicar_barra_oscura(ventana))
    return estilo


def crear_marca(contenedor, fondo=None):
    """Dibuja un pequeño icono matricial sin archivos externos."""
    fondo = fondo or COLORES["fondo"]
    marca = tk.Canvas(contenedor, width=42, height=42,
                      background=fondo, highlightthickness=0)
    marca.create_rectangle(2, 2, 40, 40, fill="#503B9C", outline="")
    for x in (12, 23):
        for y in (12, 23):
            marca.create_rectangle(x, y, x + 6, y + 6,
                                   fill=COLORES["texto"], outline="")
    return marca


def crear_acento(contenedor):
    """Dibuja una línea azul, violeta y magenta que se adapta al ancho."""
    barra = tk.Canvas(contenedor, height=3, highlightthickness=0,
                      background=COLORES["fondo"])

    def redibujar(evento):
        barra.delete("all")
        ancho = max(1, evento.width)
        paradas = ((113, 128, 255), (165, 139, 255), (239, 130, 205))
        for indice in range(48):
            posicion = indice / 47 * 2
            tramo = min(1, int(posicion))
            proporcion = posicion - tramo
            rgb = tuple(round(a * (1 - proporcion) + b * proporcion)
                        for a, b in zip(paradas[tramo], paradas[tramo + 1]))
            color = "#{:02x}{:02x}{:02x}".format(*rgb)
            x0 = round(indice * ancho / 48)
            x1 = round((indice + 1) * ancho / 48)
            barra.create_rectangle(x0, 0, x1 + 1, 3, fill=color, outline="")

    barra.bind("<Configure>", redibujar)
    return barra
