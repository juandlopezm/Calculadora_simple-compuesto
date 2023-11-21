def amortizacion_frances(prestamo, tasa_interes, periodos):
    tasa_interes = tasa_interes / 100 / 12  # Convertir la tasa anual a mensual
    cuota = (prestamo * tasa_interes) / (1 - (1 + tasa_interes) ** -periodos)
    saldo_pendiente = prestamo
    tabla_amortizacion = []

    for periodo in range(1, periodos + 1):
        intereses = saldo_pendiente * tasa_interes
        amortizacion = cuota - intereses
        saldo_pendiente -= amortizacion

        tabla_amortizacion.append({
            'Periodo': periodo,
            'Cuota': round(cuota, 2),
            'Intereses': round(intereses, 2),
            'Amortizacion': round(amortizacion, 2),
            'Saldo Pendiente': round(saldo_pendiente, 2)
        })

    return tabla_amortizacion
