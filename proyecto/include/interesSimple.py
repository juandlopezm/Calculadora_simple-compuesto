import tkinter as tk
from tkinter import messagebox




def interes_simple():
    # Función para obtener los valores del formulario

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

                # Mostrar el desglose de la fecha
                print(f"Años: {parte_entera}")
                print(f"Meses: {meses}")
                print(f"Días: {dias}")

            # Calculo el interés simple
            if i == 0:
                i = round((ci * tasai * tiempo), 2)
            cf = i + ci
            porcentaje_i = round((i * 100) / ci, 2)

            print(cf, ci, ti, "valor", i, "porcentaje", porcentaje_i, tiempo)

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")

    # Crear un nuevo marco en la ventana principal para el formulario
    formulario_frame = tk.Frame(root)
    formulario_frame.pack(padx=20, pady=20)

    # Crear y posicionar etiquetas y campos de entrada para cada variable
    labels = ["ci", "cf", "tiempo", "intervalo", "ti", "intervalo2", "i"]
    global entries
    entries = {}
    row = 0
    for label_text in labels:
        label = tk.Label(formulario_frame, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(formulario_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[label_text] = entry
        row += 1

    # Botón para obtener los valores del formulario
    btn_obtener_valores = tk.Button(
        formulario_frame, text="Obtener Valores", command=obtener_valores
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10)


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

    # Crear un nuevo marco en la ventana principal para el formulario
    formulario_frame = tk.Frame(root)
    formulario_frame.pack(padx=20, pady=20)

    # Crear y posicionar etiquetas y campos de entrada para cada variable
    labels = ["ci", "cf", "tiempo", "intervalo", "ti", "intervalo2", "i", "retiro"]
    global entries
    entries = {}
    row = 0
    for label_text in labels:
        label = tk.Label(formulario_frame, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(formulario_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[label_text] = entry
        row += 1

    # Botón para obtener los valores del formulario
    btn_obtener_valores = tk.Button(
        formulario_frame, text="Obtener Valores", command=obtener_valores
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10)


def clear_frame():
    # Limpia el contenido del frame
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
    root.geometry("600x400")  # Establece un tamaño inicial para la ventana principal

    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(
        label="Interés Simple", command=lambda: show_form(interes_simple)
    )
    file_menu.add_command(
        label="Interés Compuesto", command=lambda: show_form(interes_compuesto)
    )
    file_menu.add_command(label="TIR", command=lambda: show_form(interes_compuesto))
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=salir)

    menubar.add_cascade(label="Menú", menu=file_menu)
    root.config(menu=menubar)

    # Frame para organizar los formularios
    global main_frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
