

palabras = []

with open('inputs.txt', 'r') as archivo:
    for linea in archivo:
        palabras.append(linea.strip())


num = '1234567890'
output = 0

for palabra in palabras:
    str_num = ''

    for letra in palabra:
        if letra in num:
            str_num = str_num + letra
            break

    palabra_invertida = palabra[::-1]

    for letra in palabra_invertida:
        if letra in num:
            str_num = str_num + letra
            break
    
    output = output + int(str_num)

print(output)