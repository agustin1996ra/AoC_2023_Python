
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

posibles = {}

for juego in juegos:
    for id_juego, listas in juego.items():
        posibles[id_juego] = True
        for lista in listas:
            for cubos in lista:
                cubos = cubos.split(' ')
                if cubos[1] == 'red' and int(cubos[0]) > 12:
                    posibles[id_juego] = False
                    break
                if cubos[1] == 'green' and int(cubos[0]) > 13:
                    posibles[id_juego] = False
                    break
                if cubos[1] == 'blue' and int(cubos[0]) > 14:
                    posibles[id_juego] = False
                    break
            
print(posibles)
output = 0
for juego, cuenta in posibles.items():
    if cuenta:
        output = output + int(juego)

print(output)
