import requests
from decouple import config
import os

ruta_actual = os.path.dirname(os.path.abspath(__file__))
url = 'https://adventofcode.com/2023/day/3/input'
session=config('SESSION')
cookies = {'session': session}

response = requests.get(url, cookies=cookies)

if response.status_code == 200:
    data = response.text
    nombre_archivo = f'{ruta_actual}/inputs.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(response.text)
    print(f'Se creo el archivo {nombre_archivo}')
else:
    print(f'No se pudo obtener el contenido. Código de estado: {response.status_code}')
