import FuncaoBinaria
import random

N = 100

BITS = 22

def main():
    
    vetorX = [random.randint(-100, 100) for i in range(N)]
    vetorY = [random.randint(-100, 100) for i in range(N)]
    
    for i in range(N):
        cromossoma = FuncaoBinaria.converteCromossoma(vetorX[i], BITS, vetorY[i])
        print(f'Indivíduo {i + 1}: X = {vetorX[i]}, Y = {vetorY[i]}, Cromossoma = {cromossoma}')
        
if __name__ == "__main__":
    main()
    