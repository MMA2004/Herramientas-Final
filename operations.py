def get_ascii():


def get_binary():


def get_results(palabra):
  resultados = []
    for caracter in palabra:
        ascii_valor = get_ascii(caracter)
        binario = get_binary(caracter)
        resultados.append(f"ASCII character value of '{caracter}' is {ascii_valor}. Binary representation of '{caracter}' in a Byte is {binario}")




  
  
