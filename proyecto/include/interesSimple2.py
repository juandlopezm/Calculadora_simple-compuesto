import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy_financial as np


def interes_simple():
    # Función para obtener los valores del formulario
    def limpiar_campos():
        for entry in entries.values():
            entry.delete(0, tk.END)
            entry.insert(tk.END, "0")

    def obtener_valores():
        try:
            ci = float(entries["ci"].get())
            cf = float(entries["cf"].get())
            tiempo = float(entries["tiempo"].get())
            intervalo = entries["intervalo"].get()
            ti = float(entries["ti"].get())
            intervalo2 = entries["intervalo2"].get()
            i = float(entries["i"].get())
            ti = ti / 100
            tasai = ti

            # Realizar acciones con los valores obtenidos
            # Ejemplo: Imprimir los valores
            print(f"ci: {ci}")
            print(f"cf: {cf}")
            print(f"tiempo: {tiempo}")
            print(f"intervalo: {intervalo}")
            print(f"ti: {ti}")
            print(f"intervalo2: {intervalo2}")
            print(f"i: {i}")

            if intervalo2 == "dias":
                tasai = tasai / 365
                fecha = 365
            elif intervalo2 == "mensual":
                tasai = tasai / 12
                fecha = 30
            elif intervalo2 == "bimestral":
                tasai = (tasai * 60) / 365  # 2 meses
            elif intervalo2 == "trimestral":
                tasai = (tasai * 90) / 365  # 3 meses
            elif intervalo2 == "cuatrimestral":
                tasai = (tasai * 120) / 365  # 4 meses
            elif intervalo2 == "semestral":
                tasai = (tasai * 180) / 365  # 6 meses

            # Calculo el interés teniendo el valor final
            if intervalo == "dias":
                tiempo = tiempo / 365
                fecha = 365
            elif intervalo == "mensual":
                tiempo = tiempo / 12
                fecha = 30
            elif intervalo == "bimestral":
                tiempo = (tiempo * 60) / 365
            elif intervalo == "trimestral":
                tiempo = (tiempo * 90) / 365
            elif intervalo == "cuatrimestral":
                tiempo = (tiempo * 120) / 365
            elif intervalo == "semestral":
                tiempo = (tiempo * 180) / 365

            if cf != 0:
                i = cf - ci

            if ci == 0:
                ci = round((i / (ti * tiempo)), 2)
            # Calculo la tasa de interés
            if ti == 0:
                ti = round((i / (ci * tiempo)) * 100, 2)

            if tiempo == 0:
                tiempo = i / (ci * ti)
                numero_decimal = tiempo
                # Obtener la parte entera y decimal del número
                parte_entera = int(numero_decimal)
                parte_decimal = numero_decimal - parte_entera
                dias_totales = int(parte_decimal * 365)
                anos = dias_totales // 365
                meses = (dias_totales % 365) // 30
                dias = (dias_totales % 365) % 30
                # Convertir la parte decimal a días, horas, minutos, segundos y milisegundos
                tiempo = " " + str(anos) + " " + str(meses) + " " + str(dias)
                intervalo = " AÑO  MES DIA"
                # Mostrar el desglose de la fecha
                print(f"Años: {anos}")
                print(f"Meses: {meses}")
                print(f"Días: {dias}")

            # Calculo el interés simple
            if i == 0:
                i = round((ci * tasai * tiempo), 2)
            cf = i + ci
            porcentaje_i = round((i * 100) / ci, 2)

            print(cf, ci, ti, "valor", i, "porcentaje", porcentaje_i, tiempo)
            entries["cf"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada tir
            entries["cf"].insert(tk.END, str(cf))  # Insertar el nuevo valor de TIR

            entries["ci"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["ci"].insert(tk.END, str(ci))  # Insertar el nuevo valor de VAR

            entries["ti"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["ti"].insert(tk.END, str(ti))  # Insertar el nuevo valor de VAR

            entries["i"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["i"].insert(tk.END, str(i))

            entries["intervalo2"].delete(
                0, tk.END
            )  
            entries["intervalo2"].insert(
                tk.END, str(intervalo2)
            )  

            entries["tiempo"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["tiempo"].insert(
                tk.END, str(tiempo)
            )  # Insertar el nuevo valor de VAR  # Insertar el nuevo valor de VAR

            entries["intervalo"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada tir
            entries["intervalo"].insert(
                tk.END, str(intervalo)
            )  # Insertar el nuevo valor de TIR

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")

    simple_form_frame = tk.Frame(main_frame)
    simple_form_frame.pack(padx=20, pady=20)

    labels = ["ci", "cf", "tiempo", "intervalo", "ti", "intervalo2", "i"]
    global entries
    entries = {}
    row = 0
    for label_text in labels:
        label = tk.Label(simple_form_frame, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(simple_form_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[label_text] = entry
        row += 1

    btn_obtener_valores = tk.Button(
        simple_form_frame, text="Obtener Valores", command=obtener_valores
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10)

    btn_obtener_valores = tk.Button(
        simple_form_frame, text="Obtener Valores", command=obtener_valores
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10)

    btn_limpiar = tk.Button(simple_form_frame, text="Limpiar", command=limpiar_campos)
    btn_limpiar.grid(row=row + 1, columnspan=2, padx=10, pady=10)


def interes_compuesto():
    # Función para obtener los valores del formulario
    def obtener_valores():
        try:
            ci = float(entries["ci"].get())
            ti = float(entries["ti"].get())
            intervalo = entries["intervalo2"].get()
            time = float(entries["tiempo"].get())
            intervalo2 = entries["intervalo"].get()
            iconpuesto = float(entries["i"].get())
            cf = float(entries["cf"].get())
            retiro = float(entries["retiro"].get())
            n = 1
            print(f"ci: {ci}")
            print(f"cf: {cf}")
            print(f"tiempo: {time}")
            print(f"intervalo: {intervalo}")
            print(f"ti: {ti}")
            print(f"intervalo2: {intervalo2}")
            print(f"i: {iconpuesto}")
            print(f"retiro: {iconpuesto}")

            ti = round(ti / 100, 3)
            if intervalo == "trimestral":
                if intervalo2 == "anual":
                    time = time * 4
                elif intervalo2 == "mensual":
                    time = time / 3
                elif intervalo2 == "semestral":
                    time = time / 6
                elif intervalo2 == "diario":
                    time = time / 91.25
                elif intervalo2 == "bimestral":
                    time = time / 2
                elif intervalo2 == "cuatrimestre":
                    time = time / 4
                n = 3

            elif intervalo == "mensual":
                if intervalo2 == "anual":
                    time = time * 12
                elif intervalo2 == "trimestral":
                    time = time * 3
                elif intervalo2 == "semestral":
                    time = time * 6
                elif intervalo2 == "diario":
                    time = time / 30
                elif intervalo2 == "bimestral":
                    time = time * 2
                elif intervalo2 == "cuatrimestre":
                    time = time * 4
                n = 12

            elif intervalo == "anual":
                if intervalo2 == "mensual":
                    time = time / 12
                elif intervalo2 == "trimestral":
                    time = time / 3
                elif intervalo2 == "semestral":
                    time = time / 6
                elif intervalo2 == "diario":
                    time = time / 30
                elif intervalo2 == "bimestral":
                    time = time * 2
                elif intervalo2 == "cuatrimestre":
                    time = time * 4
            else:
                iconpuesto = round((ci * (1 + ti * time)), 2)

            if cf != 0:
                iconpuesto = ci - cf
            if ti == 0:
                ti = (cf / ci) ** (1 / time) - 1

            if ci == 0:
                ci = round(cf / ((1 + ti) ** time), 2)

            if iconpuesto == 0:
                iconpuesto = round((ci * ((1 + (ti / n)) ** time)), 2)
                cf = round(iconpuesto - ci, 2)

            if time == 0:
                time = round(map.log(cf / ci) / map.log(1 + ti), 3)

            print(cf, ci, ti, (iconpuesto - retiro), time)

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")

    compound_form_frame = tk.Frame(main_frame)
    compound_form_frame.pack(padx=20, pady=20)

    labels = ["ci", "cf", "tiempo", "intervalo", "ti", "intervalo2", "i", "retiro"]
    global entries
    entries = {}
    row = 0
    for label_text in labels:
        label = tk.Label(compound_form_frame, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(compound_form_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[label_text] = entry
        row += 1

    btn_obtener_valores = tk.Button(
        compound_form_frame, text="Obtener Valores", command=obtener_valores
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10)


""" def tir():
    # Función para obtener los valores del formulario

    def obtener_valores():
        try:
            ci = float(entries["ci"].get())
            ti = float(entries["ti"].get())


            # Realizar acciones con los valores obtenidos
            # Ejemplo: Imprimir los valores
            print(f"ci: {ci}")
            print(f"ti: {ti}")

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")

    tir_form_frame = tk.Frame(main_frame)
    tir_form_frame.pack(padx=20, pady=20)

    labels = ["ci","ti"]
    global entries
    entries = {}
    row = 0
    for label_text in labels:
        label = tk.Label(tir_form_frame, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(tir_form_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[label_text] = entry
        row += 1

    btn_obtener_valores = tk.Button(
        tir_form_frame, text="Obtener Valores", command=obtener_valores
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10) """


def obtener_valores():
    try:
        # Obtener valores ingresados en "ci" y "ti"
        ti = float(entries["tasa"].get())
        suma_total = 0
        i = 0

        # Imprimir los valores ingresados
        print(f"ti: {ti}")

        # Obtener valores de la tabla y mostrar en la consola
        valores_tabla = []
        for child in tabla.get_children():
            attribute = float(tabla.item(child, "text"))
            # Convertir el valor a entero permitiendo valores negativos
            value = float(tabla.item(child, "values")[0])
            valores_tabla.append((attribute - value))
            suma_total += (attribute - value) / ((1 + ti) ** (i))
            i += 1

        tir = round((np.irr(valores_tabla) * 100), 2)
        print("Valores de la tabla:")
        for attribute in valores_tabla:
            print(f"{attribute}")
        print(
            "---------------------------------------------------------------------------------"
        )
        print("TIR: ", tir, "\nVAR: ", suma_total)
        # Actualizar las entradas de la interfaz con los valores calculados
        entries["tir"].delete(
            0, tk.END
        )  # Borrar el contenido existente en la entrada tir
        entries["tir"].insert(tk.END, str(tir))  # Insertar el nuevo valor de TIR

        entries["var"].delete(
            0, tk.END
        )  # Borrar el contenido existente en la entrada var
        entries["var"].insert(tk.END, str(suma_total))  # Insertar el nuevo valor de VAR

    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos")


def actualizar_tabla(ci, ti):
    # Limpiar la tabla actual
    for row in tabla.get_children():
        tabla.delete(row)

    # Crear una lista con elementos para agregar a la tabla
    valores = [("ci", ci), ("ti", ti)]

    # Insertar los nuevos valores en la tabla
    for key, value in valores:
        tabla.insert("", "end", text=key, values=(value,))


def agregar_elemento():
    try:
        flujo = float(entries["flujo"].get())
        valor = float(entries["valor"].get())

        # Insertar un nuevo elemento en la tabla
        tabla.insert("", "end", text=flujo, values=(valor,))

    except ValueError:
        messagebox.showerror(
            "Error", "Ingresa un nombre válido y un número para el valor"
        )


def tir():
    global entries
    entries = {}

    tir_form_frame = tk.Frame(main_frame)
    tir_form_frame.pack(padx=20, pady=20)

    labels = ["tasa", "tir", "var"]  # Eliminado "tamaño" de la lista de etiquetas
    row = 0
    for label_text in labels:
        label = tk.Label(tir_form_frame, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(tir_form_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        if label_text in ["tir", "var"]:
            entry.insert(
                tk.END, "0"
            )  # Establecer el valor predeterminado en "0" para tir y var
        entries[label_text] = entry
        row += 1

    label_flujo = tk.Label(tir_form_frame, text="flujo de caja ")
    label_flujo.grid(row=row, column=0, padx=10, pady=5)
    entry_flujo = tk.Entry(tir_form_frame)
    entry_flujo.grid(row=row, column=1, padx=10, pady=5)
    entries["flujo"] = entry_flujo

    row += 1
    label_valor = tk.Label(tir_form_frame, text="Valor de renovacion")
    label_valor.grid(row=row, column=0, padx=10, pady=5)
    entry_valor = tk.Entry(tir_form_frame)
    entry_valor.grid(row=row, column=1, padx=10, pady=5)
    entries["valor"] = entry_valor

    btn_agregar_elemento = tk.Button(
        tir_form_frame, text="Agregar Elemento", command=agregar_elemento
    )
    btn_agregar_elemento.grid(row=row + 1, columnspan=2, padx=10, pady=10)

    btn_obtener_valores = tk.Button(
        tir_form_frame, text="Obtener Valores", command=obtener_valores
    )
    btn_obtener_valores.grid(row=row + 2, columnspan=2, padx=10, pady=10)

    # Crear una tabla inicial vacía
    global tabla
    tabla = ttk.Treeview(main_frame, columns=("Valor"))
    tabla.heading("#0", text="flujo")
    tabla.heading("Valor", text="renovar")
    tabla.pack(padx=20, pady=20)


def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()


def salir():
    root.destroy()


def show_form(form_function):
    clear_frame()
    form_function()


def main():
    global root
    root = tk.Tk()
    root.title("Menú con Opciones")
    root.geometry("600x400")

    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(
        label="Interés Simple", command=lambda: show_form(interes_simple)
    )
    file_menu.add_command(
        label="Interés Compuesto", command=lambda: show_form(interes_compuesto)
    )
    file_menu.add_command(label="TIR", command=lambda: show_form(tir))
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=salir)

    menubar.add_cascade(label="Menú", menu=file_menu)
    root.config(menu=menubar)

    global main_frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
