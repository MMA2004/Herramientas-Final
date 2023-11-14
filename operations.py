def get_ascii(carcater):
    return ord(caracter)

def get_binary(caracter):
    ascii_valor = get_ascii(caracter)
    return format(ascii_valor, '08b')

def get_results():
