import numpy as np
import matplotlib.pyplot as plt
import random

edad_actual = 25
edad_retiro = 65
edad_maxima = 90
saldo_inicial = 50000
aporte_mensual = 3000
retiro_mensual = 25000
rendimiento = 0.10
volatilidad = 0.15
inflacion = 0.04
simulaciones = 10000

rend_real = rendimiento - inflacion
años_ahorro = edad_retiro - edad_actual
años_retiro = edad_maxima - edad_retiro

saldos_retiro = []
saldos_finales = []
exitos = 0


for i in range(simulaciones):
    saldo = saldo_inicial

    for a in range(años_ahorro):
        r = np.random.normal(rend_real,  volatilidad)
        saldo = saldo * (1 + r) + aporte_mensual * 12

    saldos_retiro.append(saldo)

    for a in range(años_retiro):
        r = np.random.normal(rend_real, volatilidad)
        saldo = saldo * (1 + r) - retiro_mensual * 12
        if saldo < 0:
            saldo = 0

    saldos_finales.append(saldo)
    if saldo > 0 :
        exitos = exitos + 1

prob_exito = exitos / simulaciones

print ("Promedio al retiro:", np.mean(saldos_retiro))
print ("Mediana al retiro:", np.median(saldos_retiro))
print ("Peor 5%:", np.percentile(saldos_retiro, 5))
print ("Mejor 5%:", np.percentile(saldos_retiro, 95))
print ("Probabilidad de exito:", prob_exito * 100, "%")

plt.hist(saldos_retiro, bins = 50)
plt.title("Saldo al retiro")
plt.xlabel("Pesos")
plt.ylabel("Frecuencia")
plt.show()
