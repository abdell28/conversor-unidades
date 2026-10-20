
import tkinter as tk
from tkinter import ttk, messagebox


def convertir():
    try:
        valor = float(campo_valor.get().replace(",", "."))
    except ValueError:
        messagebox.showerror(
            "Error", "Introduce un valor numérico válido."
        )
        return

    origen = unidad_origen.get()
    destino = unidad_destino.get()

    # Convertir el valor a metros
    if origen == "Milímetros (mm)":
        valor_metros = valor / 1000
    elif origen == "Centímetros (cm)":
        valor_metros = valor / 100
    else:
        valor_metros = valor

    # Convertir de metros a la unidad de destino
    if destino == "Milímetros (mm)":
        resultado = valor_metros * 1000
    elif destino == "Centímetros (cm)":
        resultado = valor_metros * 100
    else:
        resultado = valor_metros

    simbolos = {
        "Milímetros (mm)": "mm",
        "Centímetros (cm)": "cm",
        "Metros (m)": "m"
    }

    etiqueta_resultado.config(
        text=f"Resultado: {resultado:g} {simbolos[destino]}"
    )


def limpiar():
    campo_valor.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado: ")
    campo_valor.focus()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de unidades de longitud")
ventana.geometry("430x320")
ventana.resizable(False, False)

# Título
titulo = tk.Label(
    ventana,
    text="Conversor de longitud",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=15)

# Campo para introducir el valor
tk.Label(ventana, text="Introduce el valor:").pack()

campo_valor = tk.Entry(ventana, font=("Arial", 12), justify="center")
campo_valor.pack(pady=5)

# Selección de la unidad de origen
tk.Label(ventana, text="Unidad de origen:").pack(pady=(8, 0))

unidades = [
    "Milímetros (mm)",
    "Centímetros (cm)",
    "Metros (m)"
]

unidad_origen = ttk.Combobox(
    ventana, values=unidades, state="readonly"
)
unidad_origen.current(0)
unidad_origen.pack(pady=5)

# Selección de la unidad de destino
tk.Label(ventana, text="Unidad de destino:").pack()

unidad_destino = ttk.Combobox(
    ventana, values=unidades, state="readonly"
)
unidad_destino.current(1)
unidad_destino.pack(pady=5)

# Botones
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=12)

tk.Button(
    marco_botones,
    text="Convertir",
    command=convertir,
    width=12
).pack(side=tk.LEFT, padx=5)

tk.Button(
    marco_botones,
    text="Limpiar",
    command=limpiar,
    width=12
).pack(side=tk.LEFT, padx=5)

# Mostrar el resultado
etiqueta_resultado = tk.Label(
    ventana,
    text="Resultado: ",
    font=("Arial", 12, "bold")
)
etiqueta_resultado.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()