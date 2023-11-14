def get_ascii(carcater):
    return ord(caracter)

def get_binary(caracter):
    ascii_valor = get_ascii(caracter)
    return format(ascii_valor, '08b')
    
def get_results(palabra):
    resultados = []
    for caracter in palabra:
        ascii_valor = get_ascii(caracter)
        binario = get_binary(caracter)
        resultados.append(f"ASCII character value of '{caracter}' is {ascii_valor}. Binary representation of '{caracter}' in a Byte is {binario}")

