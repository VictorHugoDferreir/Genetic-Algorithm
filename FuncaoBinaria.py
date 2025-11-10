import Main

def separaCromossoma(cromossoma, BITS):
    meio = len(cromossoma) // 2

    binarioX = cromossoma[:meio]
    binarioY = cromossoma[meio:]

    valorX = int(binarioX, 2)
    valorY = int(binarioY, 2)

    return valorX, valorY

def decodificaCromossoma(valorX_int, valorY_int, BITS, intervalo_min, intervalo_max):
    
    max_valor = 2**BITS - 1

    valorX = intervalo_min + (((intervalo_max - intervalo_min) / max_valor) * valorX_int)
    valorY = intervalo_min + (((intervalo_max - intervalo_min) / max_valor) * valorY_int)

    return valorX, valorY