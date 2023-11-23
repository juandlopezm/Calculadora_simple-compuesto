import math

#variables que necesita
# P= renta-> float
# r= TASA DE INTERES -> float
# n= PERIODOS -> float
# v= VARIABLE DE CONDICION GUARDA UN STRING "PV"(MONTO) O "FV"(CAPITAL) --> string
# Resultado= Solucion -> float

#Anualidades Vensidas
def calcular_monto(P, r, n,v):
    r = convertir_tasa_a_decimal(r)
    if v=="VF":
        FV = P*((((1 + r)**n) - 1) / r)
        return FV
    else:
        r = convertir_tasa_a_decimal(r)
        FV = P*((1-((1 + r)**(-n))) / r)
        return FV

def capitalizacion(fecha):
    if fecha=="anual":
        r=r/1
    elif fecha=="mensual":
        r=r/12
    elif fecha=="semestral":
        r=r/2
    elif fecha=="trimestral":
        r=r/4
    elif fecha=="cuatrimestral":
        r=r/3
    elif fecha=="bimestral":
        r=r/6
    elif fecha=="diario":
        r=r/360
    elif fecha=="quincenal":
        r=r/24

def calcular_plazo(P, r, FV):
    r = convertir_tasa_a_decimal(r)
    n = math.log(P / (P - FV * r)) / math.log(1 + r)
    return n

def calcular_tasa(P, FV, n):
    r = convertir_tasa_a_decimal(r)
    r = ((FV / P) ** (1 / n)) - 1
    return r

def calcular_renta(FV, r, n):
    r = convertir_tasa_a_decimal(r)
    P = FV * r / ((1 + r)**n - 1)
    return P

def convertir_tasa_a_decimal(r):
    if  str(r).endswith("0"):
        return r / 100  # Divide entre 100 si es un número entero
    return r  # Si es float, mantener el valor


# Ejemplo de uso
def main():
    print("¿Qué desea calcular?")
    print("1. Monto de una anualidad")
    print("2. Plazo de una anualidad")
    print("3. Tasa de interés de una anualidad")
    print("4. Renta de una anualidad")
    
    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        P = float(input("Ingrese el pago periódico: "))
        r = float(input("Ingrese la tasa de interés por período (en decimal): "))
        n = float(input("Ingrese el número de períodos: "))
        v=input("dedea hallar el valor final(VF) o valor presente(VP): " )
        resultado = calcular_monto(P, r, n,v)
        print(f"El monto de la anualidad es: {resultado:.2f}")
    elif opcion == 2:
        P = float(input("Ingrese el pago periódico: "))
        r = float(input("Ingrese la tasa de interés por período (en decimal): "))
        FV = float(input("Ingrese el monto total: "))
        resultado = calcular_plazo(P, r, FV)
        print(f"El plazo de la anualidad es: {resultado:.2f}")
    elif opcion == 3:
        P = float(input("Ingrese el pago periódico: "))
        FV = float(input("Ingrese el monto total: "))
        n = float(input("Ingrese el número de períodos: "))
        resultado = calcular_tasa(P, FV, n)
        print(f"La tasa de interés es: {resultado:.4f}")
    elif opcion == 4:
        FV = float(input("Ingrese el monto total: "))
        r = float(input("Ingrese la tasa de interés por período (en decimal): "))
        n = float(input("Ingrese el número de períodos: "))
        resultado = calcular_renta(FV, r, n)
        print(f"La renta de la anualidad es: {resultado:.2f}")
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()
