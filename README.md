# Advent of code Python

## Day 1 **

## Day 2 **

## Day 3 ** 

## Day 4 **

### Primera parte

```python
s = []

with open('inputs.txt', 'r') as archivo:
    for linea in archivo:
        s.append(linea.strip())

s = [linea.split(': ') for linea in s]
s = [linea[1].replace('  ', ' ').split(' | ') for linea in s]
s = [[linea[0].split(' '), linea[1].split(' ')] for linea in s]


puntos = 0

for juego in s:
    p = 0
    for numg in juego[0]:
        for nc in juego[1]:
            if numg == nc:
                p += 1
    if p > 0:
        p = (2**(p-1))
    print(p)
    puntos += p
    

print(puntos)
```

### Segunda parte

La segunda parte me costo mucho mas y tuve que ver ejemplos de otras personas para lograr resolverlo, conocí `enumarate()` para los bucles `for`, y me pareció super simple y elegante trabajar los numero ganadores y los propios como conjuntos. Y desde su intersección obtener el valor de ocurrencias.

```python
s = []

with open('./day4_scratchcards/inputs.txt', 'r') as archivo:
    for linea in archivo:
        s.append(linea.strip())

s = [linea.split(': ') for linea in s]
s = [linea[1].replace('  ', ' ').split(' | ') for linea in s]
s = [{'c': 1, 'g': linea[0].split(' '), 'm': linea[1].split(' ')} for linea in s]




for i, card in enumerate(s):
    n = len(set(card['g']) & set(card['m'])) 
    
    for j in range(i+1, min(i+1+n, len(s))):
        s[j]['c'] += s[i]['c']

print(s)
suma = 0
for card in s:
    suma += card['c']

print(suma)

```