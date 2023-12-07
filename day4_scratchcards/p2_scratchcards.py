
s = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]

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
