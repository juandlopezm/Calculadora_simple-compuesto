import math as map
ci=10000
ti=18; intervalo="mensual"
time=4; intervalo2="mensual"
iconpuesto=0
cf=0
#Recuerda que el tiempo se,
# debe expresar en las mismas ,
# unidades que la tasa de interés.
ti=round(ti/100,3)
if intervalo=="trimestral":
    if intervalo2=="anual":
        time=time*4
    elif intervalo2=="mensual":
        time=time/3
    elif intervalo2=="semestral":
        time=time/6
    elif intervalo2=="diario":
        time=time/91.25
    elif intervalo2=="bimestral":
        time=time/2
    elif intervalo2=="cuatrimestre":
        time=time/4

elif intervalo=="mensual":
    if intervalo2=="anual":
        time=time*12
    elif intervalo2=="trimestral":
        time=time*3
    elif intervalo2=="semestral":
        time=time*6
    elif intervalo2=="diario":
        time=time/30
    elif intervalo2=="bimestral":
        time=time*2
    elif intervalo2=="cuatrimestre":
        time=time*4

elif intervalo=="anual":
    if intervalo2=="mensual":
        time=time/12
    elif intervalo2=="trimestral":
        time=time/3
    elif intervalo2=="semestral":
        time=time/6
    elif intervalo2=="diario":
        time=time/30
    elif intervalo2=="bimestral":
        time=time*2
    elif intervalo2=="cuatrimestre":
        time=time*4


if cf!=0:
    iconpuesto=cf-ci
if ti==0:
    ti=((cf/ci) ** (1/time)-1)

if ci==0:
    ci=round(cf/((1+ti)**time),2)

if iconpuesto==0:
    iconpuesto=round((ci*((1+ti)**time)),2)
    cf=round(iconpuesto-ci,2)

if time==0:
    time=round(map.log(cf/ci)/map.log(1+ti),3)

print(cf,ci,ti,iconpuesto,time)


