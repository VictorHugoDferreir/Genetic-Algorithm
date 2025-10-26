import Main

def converteCromossoma(numeroX, BITS, numeroY):

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
