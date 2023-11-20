import math as map
capitalinicial=8000
interes=36; pago_Interes="años"
periodo=4; capitalizable="mensual"
interescompuesto=0
capitalfinal=0



if capitalfinal!=0:
    iconpuesto=capitalfinal-capitalinicial
if interes==0:
    interes=((capitalfinal/capitalinicial) ** (1/periodo)-1)

if capitalinicial==0:
    capitalinicial=round(capitalfinal/((1+interes)**periodo),2)

if iconpuesto==0:
    iconpuesto=round((capitalinicial*((1+(interes))**periodo)),2)
    capitalfinal=round(iconpuesto-capitalinicial,2)

if periodo==0:
    periodo=round(map.log(capitalfinal/capitalinicial)/map.log(1+interes),3)

print(capitalfinal,capitalinicial,interes,iconpuesto,periodo)
