import networkx as nx
import matplotlib.pyplot as plt


lineas = {}

lineas['Línea 1'] = [
    'Indios Verdes', 'Deportivo 18 de Marzo', 'Euzkaro', 'Potrero', 'La Raza',
    'Circuito', 'San Simón', 'Manuel González', 'Buenavista', 'El Chopo',
    'Revolución', 'Plaza de la República', 'Reforma', 'Hamburgo',
    'Insurgentes', 'Durango', 'Álvaro Obregón', 'Sonora', 'Campeche',
    'Chilpancingo', 'Nuevo León', 'La Piedad', 'Polifórum', 'Nápoles',
    'Colonia del Valle', 'Ciudad de los Deportes', 'Parque Hundido',
    'Félix Cuevas', 'Río Churubusco', 'Teatro Insurgentes',
    'José María Velasco', 'Francia', 'Olivo', 'Altavista', 'La Bombilla',
    'Doctor Gálvez', 'Ciudad Universitaria', 'Centro Cultural Universitario',
    'Perisur', 'Villa Olímpica', 'Corregidora', 'Ayuntamiento',
    'Fuentes Brotantes', 'Santa Úrsula', 'La Joya', 'El Caminero',
]

lineas['Línea 2'] = [
    'Tacubaya', 'Antonio Maceo', 'De la Salle', 'Parque Lira', 'Patriotismo',
    'Escandón', 'Nuevo León', 'Viaducto', 'Amores', 'Etiopía',
    'Doctor Vértiz', 'Centro SCOP', 'Álamos', 'Xola', 'Las Américas',
    'Andrés Molina Enríquez', 'La Viga', 'Coyuya', 'Metro Coyuya', 'Canela',
    'Tlacotal', 'Goma', 'Iztacalco', 'UPIICSA', 'El Rodeo', 'Río Tecolutla',
    'Río Mayo', 'Rojo Gómez', 'Río Frío', 'Del Moral', 'Leyes de Reforma',
    'CCH Oriente', 'Constitución de Apatzingán', 'Canal de San Juan',
    'General Antonio de León', 'Nicolás Bravo', 'Tepalcates',
]

lineas['Línea 3'] = [
    'Tenayuca', 'San José de la Escalera', 'Progreso Nacional', 'Tres Anegas',
    'Júpiter', 'La Patera', 'Poniente 146', 'Montevideo', 'Poniente 134',
    'Poniente 128', 'Magdalena de las Salinas', 'Coltongo', 'Cuitláhuac',
    'Héroe de Nacozari', 'Hospital La Raza', 'La Raza', 'Circuito',
    'Tolnahuac', 'Tlatelolco', 'Ricardo Flores Magón', 'Guerrero',
    'Buenavista', 'Mina', 'Hidalgo', 'Juárez', 'Balderas', 'Cuauhtémoc',
    'Jardín Pushkin', 'Hospital General', 'Doctor Márquez', 'Centro Médico',
    'Obrero Mundial', 'Etiopía', 'Luz Saviñón', 'Eugenia',
    'División del Norte', 'Miguel Laurent', 'Pueblo Santa Cruz Atoyac',
]

lineas['Línea 4 Norte'] = [
    'Buenavista', 'Alcaldía Cuauhtémoc', 'México Tenochtitlan',
    'Museo San Carlos', 'Hidalgo', 'Bellas Artes', 'Teatro Blanquita',
    'República de Chile', 'República de Argentina',
    'Mercado Abelardo L. Rodríguez', 'Mixcalco', 'Ferrocarril de Cintura',
    'Morelos', 'Archivo General de la Nación', 'San Lázaro', 'Terminal 1',
    'Terminal 2', 'Pantitlán', 'Calle 6', 'Alameda Oriente',
]

lineas['Línea 4 Sur'] = [
    'Buenavista', 'Alcaldía Cuauhtémoc', 'México Tenochtitlan',
    'Plaza de la República', 'Amajac', 'Defensoría Pública', 'Vocacional 5',
    'Juárez', 'Mercado San Juan', 'Eje Central', 'El Salvador',
    'Isabel la Católica', 'Museo de la Ciudad', 'Pino Suárez', 'Las Cruces',
    'La Merced', 'Mercado de Sonora', 'Cecilio Robelo', 'Eduardo Molina',
    'Moctezuma', 'San Lázaro',
]

lineas['Línea 5'] = [
    'Río de los Remedios', '314 Memorial News Divine', '5 de Mayo',
    'Vasco de Quiroga', 'El Coyol', 'Preparatoria 3', 'San Juan de Aragón',
    'Río Guadalupe', 'Talismán', 'Victoria', 'Oriente 101',
    'Río Santa Coleta', 'Río Consulado', 'Canal del Norte',
    'Deportivo Eduardo Molina', 'Mercado Morelos',
    'Archivo General de la Nación', 'San Lázaro', 'Moctezuma',
    'Venustiano Carranza', 'Avenida del Taller', 'Mixiuhca',
    'Hospital G. Troncoso', 'Metro Coyuya', 'Recreo', 'Oriente 116',
    'C. de Bachilleres 3', 'Canal Apatlaco', 'Apatlaco', 'Aculco',
    'Churubusco Oriente', 'Escuadrón 201', 'Atanasio G. Sarabia',
    'Ermita Iztapalapa', 'Ganaderos', 'Pueblo de los Reyes',
    'Barrio San Antonio', 'Calzada Taxqueña', 'Cafetales', 'ESIME Culhuacan',
    'Manuela Sáenz', 'La Virgen', 'Tepetlapa', 'Las Bombas', 'Vista Hermosa',
    'Calzada del Hueso', 'Cañaverales', 'Mayuguarda', 'Circuito Cuemanco',
    'DIF Xochimilco', 'Preparatoria 1',
]

lineas['Línea 6'] = [
    'El Rosario', 'Colegio de Bachilleres 1', 'De las Culturas',
    'Ferrocarriles Nacionales', 'UAM Azcapotzalco', 'Tecnoparque', 'Norte 59',
    'Norte 45', 'Montevideo', 'Lindavista Vallejo', 'Instituto del Petróleo',
    'San Bartolo', 'IPN', 'Riobamba', 'Deportivo 18 de Marzo', 'La Villa',
    'De los Misterios', 'Hospital Infantil La Villa', 'Gustavo A. Madero',
    'Martín Carrera', 'Hospital General La Villa', 'San Juan de Aragón',
    'Gran Canal', 'Casas Alemán', 'Pueblo San Juan de Aragón',
    'Loreto Fabela', '416 Poniente', 'Deportivo Los Galeana',
    'Ampliación Providencia', 'Volcán de Fuego', '482', '414', '416 Oriente',
    'La Pradera', 'Colegio de Bachilleres 9', 'Francisco Morazán',
    'Villa de Aragón',
]

lineas['Línea 7'] = [
    'Indios Verdes', 'De los Misterios', 'Hospital Infantil La Villa',
    'Gustavo A. Madero', 'Garrido', 'Avenida Talismán', 'Necaxa', 'Excélsior',
    'Robles Domínguez', 'Clave', 'Misterios', 'Mercado Beethoven',
    'Peralvillo', 'Tres Culturas', 'Glorieta Cuitláhuac', 'Garibaldi',
    'Glorieta Violeta', 'Hidalgo', 'El Caballito', 'Amajac', 'París',
    'Reforma', 'Hamburgo', 'El Ahuehuete', 'El Ángel', 'La Diana',
    'Chapultepec', 'Gandhi', 'Antropología', 'Auditorio', 'Campo Marte',
]

G = nx.Graph()

for nombre in lineas:
    estaciones = lineas[nombre]
    for i in range(len(estaciones) - 1):
        G.add_edge(estaciones[i], estaciones[i + 1], linea=nombre)

print('Número de estaciones:', G.number_of_nodes())
print('Número de conexiones:', G.number_of_edges())

lineas_de = {}
for nombre in lineas:
    numero = nombre.split(' ')[1]
    for estacion in lineas[nombre]:
        if estacion not in lineas_de:
            lineas_de[estacion] = []
        if numero not in lineas_de[estacion]:
            lineas_de[estacion].append(numero)

transbordos = []
for estacion in lineas_de:
    if len(lineas_de[estacion]) > 1:
        transbordos.append(estacion)
print('Estaciones de transbordo:', len(transbordos))
print(transbordos)

ruta = nx.shortest_path(G, 'Indios Verdes', 'Tepalcates')
print('Ruta más corta de Indios Verdes a Tepalcates:')
print(' -> '.join(ruta))

pos = nx.spring_layout(G, seed=1)
plt.figure(figsize=(14, 10))
nx.draw(G, pos, node_size=20, node_color='steelblue', edge_color='gray')
plt.title('Red del Metrobús CDMX')
plt.show()
