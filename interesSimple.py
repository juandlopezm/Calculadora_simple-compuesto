porcentaje_i=0.0
#valor inicial
ci=50000
#valor final
cf=0
#tiempo
time=3
intervalo="año"
#tasa de interes
ti=30
ti=ti/100
tasai=ti
intervalo2='años'
##################
#Iteres
i=0
#############
fecha=12

if intervalo2 == 'dias':
        tasai=tasai/365
        fecha=365
elif intervalo2 == 'mensual':
        tasai=tasai/12
        fecha=30
elif intervalo2 == 'bimestral':
        tasai=(tasai*60)/365  # 2 meses
elif intervalo2 == 'trimestral':
        tasai=(tasai*90)/365  # 3 meses
elif intervalo2 == 'cuatrimestral':
        tasai=(tasai*120)/365  # 4 meses
elif intervalo2 == 'semestral':
        tasai=(tasai*180)/365 # 6 meses

#Calculo el intes teniedo el valor final
if intervalo == 'dias':
        time=time/365
        fecha=365
elif intervalo == 'mensual':
        time=time/12  
        fecha=30
elif intervalo == 'bimestral':
        time=(time*60)/365
    
elif intervalo == 'trimestral':
        time=(time*90)/365  
elif intervalo == 'cuatrimestral':
        time=(time*120)/365  
elif intervalo == 'semestral':
        time=(time*180)/365 

if cf!=0:
    i=cf-ci

if ci==0:
       ci=round((i/(ti*time)),2)
#Calculo la tasa de interes
if ti==0:
    ti=round((i/(ci*time))*100,2)

if time==0:
    tiempo=(i/(ci*ti))
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

#Calculo el interes simple
if i==0:
    i=round((ci*tasai*time),2)
cf=i+ci
porcentaje_i=round((i * 100)/ci, 2)

print(cf,ci,ti,"valor",i,"porsentaje",porcentaje_i,time)
