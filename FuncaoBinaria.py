import Main

def criaCromossoma(numeroX, BITS, numeroY):

    BITS_VALOR = BITS - 1

    if numeroX < 0:
        sinal = '1'
        numeroX = abs(numeroX)
    else:
        sinal = '0'

    valorBinarioX = format(numeroX, f'0{BITS_VALOR}b')

    binarioX = sinal + valorBinarioX

    if numeroY < 0:
        sinal = '1'
        numeroY = abs(numeroY)
    else:
        sinal = '0'

    valorBinarioY = format(numeroY, f'0{BITS_VALOR}b')
    binarioY = sinal + valorBinarioY

    cromossoma = binarioX + binarioY

    return cromossoma

def separaCromossoma(cromossoma, BITS):

    meio = len(cromossoma) // 2

    binarioX = cromossoma[:meio]
    binarioY = cromossoma[meio:]

    if binarioX[0] == '1':
        sinalX = -1
    else:
        sinalX = 1

    valorX = int(binarioX[1:], 2) * sinalX

    if binarioY[0] == '1':
        sinalY = -1
    else:
        sinalY = 1

    valorY = int(binarioY[1:], 2) * sinalY

    return valorX, valorY