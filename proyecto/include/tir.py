import numpy_financial as np
ti = 0.18  # Tasa de descuento del 15%
ci=-10000  # valor inicial (convertirlo a negativo)


vpn = 0 # valor presente neto
print("Flujo de caja")
suma_total = 0 #suma total de los flujos de caja
i=0 #ciclos
flujos_de_efectivo=[ci]
while True:
    try:
        i+=1
        numero = int(input(f"flujo de caja {i}: "))
        renueva=int(input("valore de renuevacion: "))
        flujos_de_efectivo.append(numero-renueva)
        suma_total += (numero-renueva)/((1 + ti) ** (i))
        print("Suma parcial:", suma_total)
        
        continuar = input("¿Deseas introducir otro flujo? (s/n): ").lower()
        
        if continuar != 's':
            break
    except ValueError:
        print("Por favor, introduce un número válido.")
print(flujos_de_efectivo)
tir = np.irr(flujos_de_efectivo)
suma_total += ci
print("Suma total:", round(suma_total,2))
print("TIR:", round(tir*100,2))