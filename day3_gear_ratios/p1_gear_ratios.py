
e = []

with open('inputs.txt', 'r') as archivo:
    for linea in archivo:
        e.append(linea.strip())


numbers = '1234567890'
no_numeros = '#$%&./=*@-+'
simbolos = '#$%&/=*@-+'
output = 0
i = 0

while i < len(e):  # Recorro filas
    j = 0
    while j < len(e[i]):  # Recorro columnas
        if e[i][j] in no_numeros:
            j += 1
            continue

        # Construir el numero
        numero = e[i][j]
        numero_pos = [[i,j]]
        while True:
            j += 1
            if (j>=len(e[1])) or (e[i][j] in no_numeros):
                break
            else:
                numero= numero + e[i][j]
                numero_pos.append([i,j])
        
        
        # Verificar si el numero tienen simbolos
        for pos in numero_pos:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if (k==0 and l==0) or (pos[0]+k < 0 or pos[1]+l < 0) or (pos[0]+k > len(e)-1 or pos[1]+l > len(e[i])-1):
                        continue
                    if (e[pos[0]+k][pos[1]+l] in simbolos):
                        output += int(numero)
                        print(f'{numero}: {numero_pos}')
                        break

                else:
                    continue
                
                
                break

            else:
                continue
            
            
            break
        
    
    i += 1
    
    
print(output)