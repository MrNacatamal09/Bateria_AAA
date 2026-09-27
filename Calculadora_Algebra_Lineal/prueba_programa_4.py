import tkinter as tk

from interfaz.programa_4_interfaz import (
    Programa4Interfaz
)


ventana = tk.Tk()

ventana.title(
    "Prueba Programa 4"
)

ventana.geometry(
    "1000x700"
)

interfaz = Programa4Interfaz(
    ventana
)

interfaz.pack(
    fill="both",
    expand=True
)

ventana.mainloop()