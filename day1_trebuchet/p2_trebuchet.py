palabras = []

with open('inputs.txt', 'r') as archivo:
    for linea in archivo:
        palabras.append(linea.strip())

numeros = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}



output = 0

for palabra in palabras:
    str_num = ''
    primero = ''
    pos = float('inf')
    for numero_palabra, numero_caracter in numeros.items():
        palabra_find = palabra.find(numero_palabra)
        if palabra_find != -1 and palabra_find < pos:
            primero = numero_caracter
            pos = palabra_find
        
    str_num = primero
    segundo = ''
    pos = float('inf')
    palabra_invertida = palabra[::-1]
    
    for numero_palabra, numero_caracter in numeros.items():
        palabra_find = palabra_invertida.find(numero_palabra[::-1])
        if palabra_find != -1 and palabra_find < pos:
            segundo = numero_caracter
            pos = palabra_find
    
    str_num = str_num + segundo
    print(str_num)
    output = output + int(str_num)

print(output)