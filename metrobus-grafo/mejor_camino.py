import networkx as nx
from metrobus import lineas


origen = 'Indios Verdes'
destino = 'Tepalcates'


G = nx.Graph()

for nombre in lineas:
    estaciones = lineas[nombre]
    for i in range(len(estaciones) - 1):
        G.add_edge(estaciones[i], estaciones[i + 1], peso=1)


distancia = {}
anterior = {}
for estacion in G.nodes():
    distancia[estacion] = 9999
    anterior[estacion] = None
distancia[origen] = 0

pendientes = list(G.nodes())

while len(pendientes) > 0:
    actual = pendientes[0]
    for estacion in pendientes:
        if distancia[estacion] < distancia[actual]:
            actual = estacion

    pendientes.remove(actual)

    if actual == destino:
        break

    for vecino in G.neighbors(actual):
        nueva = distancia[actual] + G[actual][vecino]['peso']
        if nueva < distancia[vecino]:
            distancia[vecino] = nueva
            anterior[vecino] = actual


ruta = []
estacion = destino
while estacion != None:
    ruta.append(estacion)
    estacion = anterior[estacion]
ruta.reverse()


print('Mejor camino de', origen, 'a', destino)
print(' -> '.join(ruta))
print('Estaciones recorridas:', distancia[destino])

esperado = nx.shortest_path_length(G, origen, destino)
print('Coincide con networkx:', distancia[destino] == esperado)
