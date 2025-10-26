import math

def funcaoAvaliacao(x, y):
    
    resultado = 0.5 - (math.sin(math.sqrt(x**2 + y**2))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2
    return resultado
