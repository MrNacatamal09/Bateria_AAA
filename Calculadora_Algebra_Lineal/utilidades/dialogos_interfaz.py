"""Diálogos modales oscuros para mensajes de la calculadora.

Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import tkinter as tk
from tkinter import ttk

from utilidades.tema_interfaz import COLORES, aplicar_barra_oscura


def showerror(titulo, mensaje, parent=None):
    """Muestra un error legible y modal sin abrir un cuadro claro del sistema."""
    padre = parent if parent is not None else tk._default_root
    if padre is None:
        raise RuntimeError("No hay una ventana principal para mostrar el error.")

    dialogo = tk.Toplevel(padre)
    dialogo.title(str(titulo))
    dialogo.configure(background=COLORES["fondo"])
    dialogo.resizable(False, False)
    dialogo.transient(padre)

    tk.Frame(dialogo, height=3, background=COLORES["coral"]).pack(fill="x")
    contenido = tk.Frame(dialogo, background=COLORES["superficie"],
                         padx=22, pady=20)
    contenido.pack(fill="both", expand=True, padx=8, pady=8)

    encabezado = tk.Frame(contenido, background=COLORES["superficie"])
    encabezado.pack(fill="x", pady=(0, 12))
    tk.Label(encabezado, text="!", font=("Segoe UI", 15, "bold"),
             foreground=COLORES["fondo"], background=COLORES["coral"],
             width=2).pack(side="left", padx=(0, 12))
    tk.Label(encabezado, text=str(titulo), font=("Segoe UI", 13, "bold"),
             foreground=COLORES["texto"],
             background=COLORES["superficie"]).pack(side="left", anchor="w")

    tk.Label(contenido, text=str(mensaje), font=("Segoe UI", 10),
             foreground=COLORES["texto"], background=COLORES["superficie"],
             justify="left", wraplength=430).pack(fill="x", anchor="w")

    boton = ttk.Button(contenido, text="Entendido", style="Accion.TButton",
                       command=dialogo.destroy)
    boton.pack(anchor="e", pady=(20, 0))
    dialogo.bind("<Return>", lambda _evento: dialogo.destroy())
    dialogo.bind("<Escape>", lambda _evento: dialogo.destroy())
    dialogo.protocol("WM_DELETE_WINDOW", dialogo.destroy)

    dialogo.update_idletasks()
    ancho = dialogo.winfo_width()
    alto = dialogo.winfo_height()
    x = padre.winfo_rootx() + (padre.winfo_width() - ancho) // 2
    y = padre.winfo_rooty() + (padre.winfo_height() - alto) // 2
    dialogo.geometry(f"+{max(0, x)}+{max(0, y)}")
    aplicar_barra_oscura(dialogo)
    dialogo.grab_set()
    boton.focus_set()
    dialogo.wait_window()
    return "ok"
