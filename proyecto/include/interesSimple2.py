import math
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy_financial as np
from PIL import Image, ImageTk
#from PIL import ImageTk, Image

def interes_simple():
    clear_frame()

    btn_volver_menu = tk.Button(
        main_frame, text=" MENU ", command=show_main_menu,bg="#707DFE",font=("Arial", 16, "bold"),
    )
    btn_volver_menu.pack()
    # Función para obtener los valores del formulario
    def limpiar_campos():
        for entry in entries.values():
            entry.delete(0, tk.END)
            entry.insert(tk.END, "0")

    def obtener_valores():
        try:
            ci=0;cf=0;tiempo=0;intervalo="";ti=0;intervalo2="";i=0
            ci = float(entries["CAPITAL INICIAL"].get())
            cf = float(entries["CAPITAL FINAL"].get())
            tiempo = float(entries["TIEMPO"].get())
            intervalo = entries["PERIODO"].get()
            ti = float(entries["TASA DE INTERES"].get())
            intervalo2 = entries["PERIODO TI"].get()
            i = float(entries["INTERES"].get())
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
                tiempo = " " + str(parte_entera) + " " + str(meses) + " " + str(dias)
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
            entries["CAPITAL FINAL"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada tir
            entries["CAPITAL FINAL"].insert(tk.END, str(cf))  # Insertar el nuevo valor de TIR

            entries["CAPITAL INICIAL"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["CAPITAL INICIAL"].insert(tk.END, str(ci))  # Insertar el nuevo valor de VAR

            entries["TASA DE INTERES"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["TASA DE INTERES"].insert(tk.END, str(ti))  # Insertar el nuevo valor de VAR

            entries["INTERES"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["INTERES"].insert(tk.END, str(i))

            entries["PERIODO TI"].delete(0, tk.END)
            entries["PERIODO TI"].insert(tk.END, str(intervalo2))

            entries["TIEMPO"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["TIEMPO"].insert(
                tk.END, str(tiempo)
            )  # Insertar el nuevo valor de VAR  # Insertar el nuevo valor de VAR

            entries["PERIODO"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada tir
            entries["PERIODO"].insert(
                tk.END, str(intervalo)
            )  # Insertar el nuevo valor de TIR

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")

    simple_form_frame = tk.Frame(main_frame)
    simple_form_frame.pack(padx=20, pady=20)

    labels = ["CAPITAL INICIAL", "CAPITAL FINAL", "TIEMPO", "TASA DE INTERES", "INTERES"]
    global entries
    entries = {}
    row = 0
    for label_text in labels:
        label = tk.Label(simple_form_frame, text=label_text, font=("Consolas", 10, "bold"))
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(simple_form_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[label_text] = entry
        row += 1

    opciones_intervalo = [
        "dias",
        "mensual",
        "bimestral",
        "trimestral",
        "cuatrimestral",
        "semestral",
        "anual",
    ]

    label_intervalo = tk.Label(simple_form_frame, text="PERIODO", font=("Consolas", 10, "bold"))
    label_intervalo.grid(row=row, column=0, padx=10, pady=5)

    combo_intervalo = ttk.Combobox(simple_form_frame, values=opciones_intervalo)
    combo_intervalo.grid(row=row, column=1, padx=10, pady=5)
    entries["PERIODO"] = combo_intervalo
    row += 1

    label_intervalo2 = tk.Label(simple_form_frame, text="PERIODO TI", font=("Consolas", 10, "bold"))
    label_intervalo2.grid(row=row, column=0, padx=10, pady=5)

    combo_intervalo2 = ttk.Combobox(simple_form_frame, values=opciones_intervalo)
    combo_intervalo2.grid(row=row, column=1, padx=10, pady=5)
    entries["PERIODO TI"] = combo_intervalo2
    row += 1

    btn_obtener_valores = tk.Button(
        simple_form_frame, text=" CALCULAR ", command=obtener_valores,bg="#5DFF01",font=("Arial", 16, "bold"),
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10)

    btn_limpiar = tk.Button(simple_form_frame, text="LIMPIAR", command=limpiar_campos,bg="#FC4F4F",font=("Arial", 16, "bold"),)
    btn_limpiar.grid(row=row + 1, columnspan=2, padx=10, pady=10)
def interes_compuesto():
    clear_frame()

    btn_volver_menu = tk.Button(
        main_frame, text=" MENU ", command=show_main_menu,bg="#707DFE",font=("Arial", 16, "bold"),
    )

    btn_volver_menu.pack()
    def limpiar_campos():
        for entry in entries.values():
            entry.delete(0, tk.END)
            entry.insert(tk.END, "0")

    # Función para obtener los valores del formulario
    def obtener_valores():
        try:
            ci = float(entries["CAPITAL INICIAL"].get())
            ti = float(entries["TASA DE INTERES"].get())
            intervalo = entries["PERIODO TI"].get()
            time = float(entries["TIEMPO"].get())
            intervalo2 = entries["PERIODO"].get()
            iconpuesto = float(entries["INTERES"].get())
            cf = float(entries["CAPITAL FINAL"].get())
            retiro = float(entries["RETIRO"].get())
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

            entries["CAPITAL FINAL"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada tir
            entries["CAPITAL FINAL"].insert(tk.END, str(cf))  # Insertar el nuevo valor de TIR

            entries["CAPITAL INICIAL"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["CAPITAL INICIAL"].insert(tk.END, str(ci))  # Insertar el nuevo valor de VAR

            entries["TASA DE INTERES"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["TASA DE INTERES"].insert(tk.END, str(ti))  # Insertar el nuevo valor de VAR

            entries["INTERES"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["INTERES"].insert(tk.END, str(iconpuesto))

            entries["PERIODO TI"].delete(0, tk.END)
            entries["PERIODO TI"].insert(tk.END, str(intervalo))

            entries["TIEMPO"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["TIEMPO"].insert(
                tk.END, str(time)
            )  # Insertar el nuevo valor de VAR  # Insertar el nuevo valor de VAR

            entries["PERIODO"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada tir
            entries["PERIODO"].insert(
                tk.END, str(intervalo2)
            )  # Insertar el nuevo valor de TIR

            entries["RETIRO"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada tir
            entries["RETIRO"].insert(
                tk.END, str(iconpuesto - retiro)
            )  # Insertar el nuevo valor de TIR

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")

    compound_form_frame = tk.Frame(main_frame)
    compound_form_frame.pack(padx=20, pady=20)

    labels = ["CAPITAL INICIAL", "CAPITAL FINAL", "TIEMPO", "TASA DE INTERES", "INTERES", "RETIRO"]
    global entries
    entries = {}
    row = 0
    for label_text in labels:
        label = tk.Label(compound_form_frame, text=label_text, font=("Consolas", 10, "bold"))
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(compound_form_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[label_text] = entry
        row += 1

    opciones_intervalo = ["dias", "mensual", "bimestral", "trimestral", "cuatrimestral", "semestral", "anual"]
    label_intervalo = tk.Label(compound_form_frame, text="PERIODO", font=("Consolas", 10, "bold"))
    label_intervalo.grid(row=row, column=0, padx=10, pady=5)

    combo_intervalo = ttk.Combobox(compound_form_frame, values=opciones_intervalo)
    combo_intervalo.grid(row=row, column=1, padx=10, pady=5)
    entries["PERIODO"] = combo_intervalo
    row += 1

    label_intervalo2 = tk.Label(compound_form_frame, text="PERIODO TI", font=("Consolas", 10, "bold"))
    label_intervalo2.grid(row=row, column=0, padx=10, pady=5)

    combo_intervalo2 = ttk.Combobox(compound_form_frame, values=opciones_intervalo)
    combo_intervalo2.grid(row=row, column=1, padx=10, pady=5)
    entries["PERIODO TI"] = combo_intervalo2
    row += 1

    btn_obtener_valores = tk.Button(
        compound_form_frame, text=" CALCULAR ", command=obtener_valores,bg="#5DFF01",font=("Arial", 16, "bold"),
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10)

    btn_limpiar = tk.Button(compound_form_frame, text=" LIMPIAR ", command=limpiar_campos,bg="#FC4F4F",font=("Arial", 16, "bold"),)
    btn_limpiar.grid(row=row + 1, columnspan=2, padx=10, pady=10)

def obtener_valores():
    
    try:
        # Obtener valores ingresados en "ci" y "ti"
        ti = float(entries["TASA DE INTERES"].get())
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
        entries["TIR"].delete(
            0, tk.END
        )  # Borrar el contenido existente en la entrada tir
        entries["TIR"].insert(tk.END, str(tir))  # Insertar el nuevo valor de TIR

        entries["VAR"].delete(
            0, tk.END
        )  # Borrar el contenido existente en la entrada var
        entries["VAR"].insert(tk.END, str(suma_total))  # Insertar el nuevo valor de VAR

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
        flujo = float(entries["FLUJO"].get())
        valor = float(entries["VALOR"].get())

        # Insertar un nuevo elemento en la tabla
        tabla.insert("", "end", text=flujo, values=(valor,))

    except ValueError:
        messagebox.showerror(
            "Error", "Ingresa un nombre válido y un número para el valor"
        )

def eliminar_ultimo_elemento():
    global tabla
    seleccion = tabla.selection()
    if seleccion:  # Verificar si hay una fila seleccionada
        tabla.delete(seleccion[-1])  # Eliminar la última fila seleccionada

def tir():
    clear_frame()

    btn_volver_menu = tk.Button(
        main_frame, text=" MENU ", command=show_main_menu,bg="#707DFE",font=("Arial", 16, "bold"),
    )
    btn_volver_menu.pack()
    global entries
    entries = {}

    tir_form_frame = tk.Frame(main_frame)
    tir_form_frame.pack(padx=20, pady=20)

    labels = ["TASA DE INTERES", "TIR", "VAR"]  # Eliminado "tamaño" de la lista de etiquetas
    row = 0
    for label_text in labels:
        label = tk.Label(tir_form_frame, text=label_text, font=("Consolas", 10, "bold"))
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(tir_form_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        if label_text in ["TIR", "VAR"]:
            entry.insert(
                tk.END, "0"
            )  # Establecer el valor predeterminado en "0" para tir y var
        entries[label_text] = entry
        row += 1

    label_flujo = tk.Label(tir_form_frame, text="FLUJO DE CAJA ", font=("Consolas", 10, "bold"))
    label_flujo.grid(row=row, column=0, padx=10, pady=5)
    entry_flujo = tk.Entry(tir_form_frame)
    entry_flujo.grid(row=row, column=1, padx=10, pady=5)
    entries["FLUJO"] = entry_flujo

    row += 1
    label_valor = tk.Label(tir_form_frame, text="VALOR DE RENOVACION", font=("Consolas", 10, "bold"))
    label_valor.grid(row=row, column=0, padx=10, pady=5)
    entry_valor = tk.Entry(tir_form_frame)
    entry_valor.grid(row=row, column=1, padx=10, pady=5)
    entries["VALOR"] = entry_valor

    btn_agregar_elemento = tk.Button(
        tir_form_frame, text="Agregar Elemento", command=agregar_elemento,bg="#1E32F5",font=("Arial", 16, "bold"),
    )
    btn_agregar_elemento.grid(row=row + 1, column=0, padx=10, pady=10)

    btn_eliminar_elemento = tk.Button(
        tir_form_frame, text="Eliminar Elemento", command=eliminar_ultimo_elemento,bg="#FC4F4F",font=("Arial", 16, "bold"),
    )
    btn_eliminar_elemento.grid(row=row + 1, column=1, padx=10, pady=10)

    # Crear una tabla inicial vacía
    global tabla
    tabla = ttk.Treeview(main_frame, columns=("VALOR"))
    tabla.heading("#0", text="FLUJO")
    tabla.heading("VALOR", text="RENOVAR")
    tabla.pack(padx=20, pady=20)

    btn_obtener_valores = tk.Button(
        tir_form_frame, text=" CALCULAR ", command=obtener_valores,bg="#5DFF01",font=("Arial", 16, "bold"),
    )
    btn_obtener_valores.grid(row=row + 3, columnspan=2, padx=10, pady=10)

def calcular_monto(P, r, n,v,fecha,fecha2):
    r = convertir_tasa_a_decimal(r)
    if v=="VP":
        if fecha=="anual" and fecha2=="semestral":
            resultado = P*((((1 + r)**(n*2)) - 1) / r)
        else:
            resultado = P*((((1 + r)**n) - 1) / r)
    else:
        if fecha=="mensual" and fecha2=="anual":
            resultado = P*((1-((1 + (r/12))**(-n))) / (r/12))
        else:
            resultado = P*((1-((1 + r)**(-n))) / r)
    return resultado
        
def calcular_plazo(P, r, resultado):
    r = convertir_tasa_a_decimal(r)
    n = math.log(P / (P - resultado * r)) / math.log(1 + r)
    return n

def calcular_tasa(P, resultado, n):
    r = ((resultado / P) ** (1 / n)) - 1
    return r

def calcular_renta(resultado, r, n,fecha,fecha2):
    r = convertir_tasa_a_decimal(r)
    if fecha=="anual" and fecha2=="semestral":
        P = resultado / (((1 + r)**(n*2) - 1)/2)
    else:
        P = resultado / (((1 + r)**n - 1) / r)
    return P

def convertir_tasa_a_decimal(r):
    if  str(r).endswith("0"):
        return r / 100  # Divide entre 100 si es un número entero
    return r  # Si es float, mantener el valor

def anualidades():
    clear_frame()

    btn_volver_menu = tk.Button(
        main_frame, text=" MENU ", command=show_main_menu,bg="#707DFE",font=("Arial", 16, "bold"),
    )
    btn_volver_menu.pack()
    # Función para obtener los valores del formulario
    def limpiar_campos():
        for entry in entries.values():
            entry.delete(0, tk.END)
            entry.insert(tk.END, "0")

    def obtener_valores():
        try:
            P = float(entries["RENTA"].get()) #renta
            r = float(entries["INTERES"].get()) # interes
            n = float(entries["TIEMPO"].get()) #  periodo 
            v = str(entries["VP O VF"].get()) # eleccion
            resultado = float(entries["MONTO O CAPITAL"].get()) #monto o capital
            enganche = float(entries["ENGANCHE"].get())
            fecha = str(entries["PERIODO"].get())
            fecha2 = str(entries["PERIODO DE INTERES"].get())

            # Realizar acciones con los valores obtenidos
            # Ejemplo: Imprimir los valores 

            #llamar 
           
            if resultado==0:
                resultado = calcular_monto(P, r, n,v,fecha,fecha2)
                resultado+=enganche
                print(f"El monto de la anualidad es: {resultado:.2f}")
            if n==0:
                n = calcular_plazo(P, r, resultado)
                print(f"El plazo de la anualidad es: {n:.2f}")
            if r==0:
                r = calcular_tasa(P, resultado, n)
                print(f"La tasa de interés es: {r:.4f}")
            if P==0:
                P= calcular_renta(resultado, r, n,fecha,fecha2)
                print(f"La renta de la anualidad es: {P:.2f}")


            entries["RENTA"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada tir
            entries["RENTA"].insert(tk.END, str(P))  # Insertar el nuevo valor de TIR

            entries["INTERES"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["INTERES"].insert(tk.END, str(r))  # Insertar el nuevo valor de VAR

            entries["TIEMPO"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["TIEMPO"].insert(tk.END, str(n))
            
            entries["VP O VF"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["VP O VF"].insert(tk.END, str(v))

            entries["MONTO O CAPITAL"].delete(
                0, tk.END
            )  # Borrar el contenido existente en la entrada var
            entries["MONTO O CAPITAL"].insert(tk.END, str(resultado))

            print(f"p: {P}")
            print(f"r: {r}")
            print(f"n: {n}")
            print(f"v: {v}")
            print(f"resultado {resultado}")

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos")

    simple_form_frame = tk.Frame(main_frame)
    #simple_form_frame.configure(bg="yellow")
    simple_form_frame.pack(padx=20, pady=20)

    labels = ["RENTA", "INTERES","TIEMPO","MONTO O CAPITAL","ENGANCHE"]
    global entries
    entries = {}
    row = 0
    for label_text in labels:
        label = tk.Label(simple_form_frame, text=label_text, font=("Consolas", 10, "bold"))
        label.grid(row=row, column=0, padx=10, pady=5)

        entry = tk.Entry(simple_form_frame)
        entry.grid(row=row, column=1, padx=10, pady=5)
        entries[label_text] = entry
        row += 1

    opciones_intervalo = [
        "dias",
        "mensual",
        "bimestral",
        "trimestral",
        "cuatrimestral",
        "semestral",
        "anual",
    ]

    opciones_intervalo2 = [
        "VP","VF"
    ]

    label_intervalo3 = tk.Label(simple_form_frame, text="VP O VF", font=("Consolas", 10, "bold"))
    label_intervalo3.grid(row=row, column=0, padx=10, pady=5)

    combo_intervalo3 = ttk.Combobox(simple_form_frame, values=opciones_intervalo2)
    combo_intervalo3.grid(row=row, column=1, padx=10, pady=5)
    entries["VP O VF"] = combo_intervalo3
    row += 1


    label_intervalo = tk.Label(simple_form_frame, text="PERIODO", font=("Consolas", 10, "bold"))
    label_intervalo.grid(row=row, column=0, padx=10, pady=5)

    combo_intervalo = ttk.Combobox(simple_form_frame, values=opciones_intervalo)
    combo_intervalo.grid(row=row, column=1, padx=10, pady=5)
    entries["PERIODO"] = combo_intervalo
    row += 1

    label_intervalo2 = tk.Label(simple_form_frame, text="PERIODO DE INTERES", font=("Consolas", 10, "bold"))
    label_intervalo2.grid(row=row, column=0, padx=10, pady=5)

    combo_intervalo2 = ttk.Combobox(simple_form_frame, values=opciones_intervalo)
    combo_intervalo2.grid(row=row, column=1, padx=10, pady=5)
    entries["PERIODO DE INTERES"] = combo_intervalo2
    row += 1

    btn_obtener_valores = tk.Button(
        simple_form_frame, text=" CALCULAR ", command=obtener_valores,bg="#5DFF01",font=("Arial", 16, "bold"),
    )
    btn_obtener_valores.grid(row=row, columnspan=2, padx=10, pady=10)

    btn_limpiar = tk.Button(simple_form_frame, text="LIMPIAR", command=limpiar_campos,bg="#FC4F4F",font=("Arial", 16, "bold"))
    btn_limpiar.grid(row=row + 1, columnspan=2, padx=10, pady=10)




def salir():
    root.destroy()

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def show_form(form_function):
    clear_frame()
    form_function()

def show_interes_simple():
    clear_frame()
    # Lógica para mostrar el formulario de interés simple

def show_interes_compuesto():
    clear_frame()
    # Lógica para mostrar el formulario de interés compuesto

def show_tir():
    clear_frame()
    # Lógica para mostrar el formulario de TIR

def show_anualidades():
    clear_frame()
    # Lógica para mostrar el formulario de anualidades

def show_main_menu():
    clear_frame()
    
    img_interes_simple = Image.open(r"C:\Users\1108j\OneDrive\Escritorio\economia\proyecto\include\img\finance.png") # Ajusta el tamaño si es necesario
    img_interes_simple = ImageTk.PhotoImage(img_interes_simple)

        
    img_interes_compuesto = Image.open(r"C:\Users\1108j\OneDrive\Escritorio\economia\proyecto\include\img\finance4.png") # Ajusta el tamaño si es necesario
    img_interes_compuesto = ImageTk.PhotoImage(img_interes_compuesto)

    img_interes_tir = Image.open(r"C:\Users\1108j\OneDrive\Escritorio\economia\proyecto\include\img\finance2.png") # Ajusta el tamaño si es necesario
    img_interes_tir = ImageTk.PhotoImage(img_interes_tir)

    img_interes_anualidades = Image.open(r"C:\Users\1108j\OneDrive\Escritorio\economia\proyecto\include\img\finance3.png") # Ajusta el tamaño si es necesario
    img_interes_anualidades = ImageTk.PhotoImage(img_interes_anualidades)


    btn_interes_simple = tk.Button(
        main_frame, text="Interés Simple", image=img_interes_simple, compound=tk.TOP,bg="#F7E95D",font=("Arial", 16, "bold"),
        command=lambda: show_form(interes_simple)
    )
    btn_interes_simple.image = img_interes_simple  # Guarda una referencia para evitar que la imagen sea eliminada por el recolector de basura
    btn_interes_simple.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    #########################################################################
    btn_interes_compuesto = tk.Button(
        main_frame, text="Interés Compuesto", image=img_interes_compuesto, compound=tk.TOP,bg="#F7E95D",font=("Arial", 16, "bold"),
        command=lambda: show_form(interes_compuesto)
    )
    btn_interes_compuesto.image = img_interes_compuesto 
    btn_interes_compuesto.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    #########################################################################
    btn_tir = tk.Button(
        main_frame, text="TIR", image=img_interes_tir, compound=tk.TOP,bg="#F7E95D",font=("Arial", 16, "bold"),
        command=lambda: show_form(tir)
    )
    btn_tir.image = img_interes_tir 
    btn_tir.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    ########################################################################
    btn_anualidades = tk.Button(
        main_frame, text="Anualidades", image=img_interes_anualidades, compound=tk.TOP,bg="#F7E95D",font=("Arial", 16, "bold"),
        command=lambda: show_form(anualidades)
    )
    btn_anualidades.image = img_interes_anualidades  
    btn_anualidades.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    btn_salir = tk.Button(main_frame, text="Salir", command=salir,bg="#FC4F4F",font=("Arial", 16, "bold"),)
    btn_salir.grid(row=2, columnspan=2, sticky="nsew", padx=10, pady=10)

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)




def main():
    global root
    global main_frame
    root = tk.Tk()
    root.title("ECONOMIA APLICATIVO DE FINANCIERO")
    root.geometry("900x500")

    main_frame = tk.Frame(root)
    main_frame.configure(bg="#29F5A2")
    main_frame.pack(fill=tk.BOTH, expand=True)

    show_main_menu()

    root.mainloop()

if __name__ == "__main__":
    main()


    """     def show_main_menu():
    clear_frame()



 # Estilo ttk para los botones
    style = ttk.Style()
    style.configure('TButton', padding=6, relief="flat")

 # Estilo de los botones
    btn_style = {
        'bg': '#3498db',  # Color de fondo
        'fg': 'white',   # Color del texto
        'font': ('Arial', 12),  # Fuente y tamaño del texto
        'bd': 3,         # Grosor del borde
        'highlightthickness': 0,  # Grosor del resaltado al pasar el mouse
    }

    # Crear un contenedor para el botón con la imagen encima del texto
    btn_interes_simple_container = tk.Frame(main_frame, bg='#3498db')
    btn_interes_simple_container.pack()

    # Agregar la imagen sobre el texto utilizando un Label
    label_interes_simple = tk.Label(
        btn_interes_simple_container, text="Interés Simple", image=img_interes_simple,
        compound=tk.TOP,  # La imagen estará encima del texto
        **btn_style  # Aplicar el estilo definido
    )
    label_interes_simple.image = img_interes_simple
    label_interes_simple.pack()

    # Asignar el tamaño deseado al contenedor del botón
    btn_interes_simple_container.config(width=200, height=100)

    btn_interes_compuesto = tk.Button(
        main_frame, text="Interés Compuesto", command=interes_compuesto
    )
    btn_interes_compuesto.pack()

    btn_tir = tk.Button(main_frame, text="TIR", command=tir)
    btn_tir.pack()

    btn_anualidades = tk.Button(main_frame, text="Anualidades", command=anualidades)
    btn_anualidades.pack()

    btn_salir = tk.Button(main_frame, text="Salir", command=salir)
    btn_salir.pack()
 """