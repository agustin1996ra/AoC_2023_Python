
juegos = []

with open('inputs.txt', 'r') as archivo:
    for linea in archivo:
        juegos.append(linea.strip())

i=0
for juego in juegos:
    juego_lista = juego.split(':')
    id_juego = juego_lista[0].split(' ')[1]
    lista_rondas = juego_lista[1].strip().split('; ')
    listas_rondas = [] # lista de listas
    for rondas in lista_rondas:
        p = rondas.split(', ')
        listas_rondas.append(p)
    juegos[i] = {id_juego: listas_rondas}
    i=i+1

output = 0

for juego in juegos:
    for id_juego, listas in juego.items():
        min_red = 0
        min_green = 0
        min_blue = 0
        for lista in listas:
            for cubos in lista:
                cubos = cubos.split(' ')
                if cubos[1] == 'red' and int(cubos[0]) > min_red:
                    min_red = int(cubos[0])
                if cubos[1] == 'green' and int(cubos[0]) > min_green:
                    min_green = int(cubos[0])
                if cubos[1] == 'blue' and int(cubos[0]) > min_blue:
                    min_blue = int(cubos[0])
        potencia = min_blue * min_green * min_red
        output = output + potencia
            

print(output)
