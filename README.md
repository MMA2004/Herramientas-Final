### Herramientas-Final
## Integrantes 
---
##### Nombres:
1. Esteban Arismendi(esteban031)
2. Juan Jose Orjuela(cheerspizza)
3. Mateo Monroy(MMA2004)
---
### Codigos usados en git bash
| codigo | descripcion |
|---|---|
| git clone | para clonar el repositorio |
| git pull | para actualizar el repositorio en local |
| git add | para añadir el archivo |
| git commit -m | para confirmar los cambioes en local |
| git status | para ver el estado de la branch |
| git log | para ver el historal de actualizaciones y cambios |
| vi (nombre del archivo) | para ver el contenido del archivo |
|git checkout -b |para crear y moverse a una branch nueva|
|git push origin (nombre de la branch)|para subir los cambios a la nube|

---


### Explicacion primer codigo en Python y su funcionamiento.
| Código Python                                  | Explicación                                    |
| ---------------------------------------------- | ---------------------------------------------- |
| `from operations import get_results`           | Importa la función `get_results` desde el módulo `operations`.|
| `import sys`                                   | Importa el módulo `sys` para poder salir del programa si es necesario.|
| `menu = int(input("Menu\n1. Character\n2. Word\n"))` | Solicita al usuario que elija entre dos opciones de menú (1 o 2) y almacena la elección en la variable `menu`.|
| `if menu == 1:`                                | Verifica si la elección del usuario es 1.       |
| &nbsp;&nbsp;`char = input('Enter a character: ')` | Si es 1, solicita al usuario que ingrese un carácter y lo almacena en la variable `char`.|
| &nbsp;&nbsp;`word = char`                      | Asigna el valor de `char` a la variable `word`. |
| `elif menu == 2:`                              | Si la elección del usuario no es 1, verifica si es 2.|
| &nbsp;&nbsp;`word = input('Enter a word: ')`   | Si es 2, solicita al usuario que ingrese una palabra y almacena la entrada en la variable `word`.|
| `else:`                                        | Si la elección del usuario no es ni 1 ni 2, ejecuta lo siguiente.|
| &nbsp;&nbsp;`sys.exit()`                       | Sale del programa utilizando el módulo `sys`.   |
| `print('Results\n========')`                   | Imprime un encabezado para los resultados.      |
| `results = get_results(word)`                  | Llama a la función `get_results` con la palabra ingresada por el usuario y almacena los resultados en la variable `results`.|
| `print('Total: {0}'.format(results))`          | Imprime el total de los resultados.             |

---

### Explicacion segundo codigo en Python y su  funcionamiento.
| Código Python                                 | Explicación                                                                                                                                              |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `def get_ascii(caracter):`                    | Función que toma un carácter como entrada y devuelve su valor ASCII correspondiente.                                                                    |
| `    return ord(caracter)`                    | Utiliza la función `ord` para obtener el valor ASCII del carácter.                                                                                        |
|                                                                                                    |
| `def get_binary(caracter):`                   | Función que toma un carácter como entrada y devuelve su representación binaria en 8 bits.                                                                |
| `    ascii_valor = get_ascii(caracter)`       | Obtiene el valor ASCII del carácter utilizando la función `get_ascii`.                                                                                   |
| `    return format(ascii_valor, '08b')`      | Utiliza `format` para obtener la representación binaria del valor ASCII con ceros a la izquierda para completar 8 bits.                                   |
|                                                                                                    |
| `def get_results(palabra):`                   | Función principal que toma una palabra como entrada y devuelve una cadena con información sobre cada carácter y la representación binaria de la palabra.|
| `    resultados = []`                         | Inicializa una lista para almacenar los resultados.                                                                                                      |
|                                                                                                    |
| `    for caracter in palabra:`                | Itera a través de cada carácter en la palabra.                                                                                                            |
| `        ascii_valor = get_ascii(caracter)`   | Obtiene el valor ASCII del carácter utilizando la función `get_ascii`.                                                                                   |
| `        binario = get_binary(caracter)`      | Obtiene la representación binaria del carácter utilizando la función `get_binary`.                                                                       |
| `        resultados.append(f"ASCII character value of '{caracter}' is {ascii_valor}. Binary representation of '{caracter}' in a Byte is {binario}")`   | Agrega una línea al resultado con información sobre el carácter.                                                                                    |
|                                                                                                    |
| `    representacion_binaria_palabra = ' '.join(get_binary(letra) for letra in palabra)`        | Obtiene la representación binaria de la palabra completa y la une con espacios.                                                                        |
| `    resultados.append(f"Total: {representacion_binaria_palabra}")`                            | Agrega una línea al resultado con la representación binaria completa de la palabra.                                                                    |
|                                                                                                    |
| `    return '\n'.join(resultados)`            | Devuelve los resultados como una cadena con saltos de línea.                                                                                            |

