import FuncaoBinaria
import random

N = 100
Num_ger = 40

BITS = 22

def main():
    
    populacao = []
    geracao = []
    vetorX = [random.randint(-100, 100) for i in range(N)]
    vetorY = [random.randint(-100, 100) for i in range(N)]
    
    for i in range(N):
        cromossoma = FuncaoBinaria.criaCromossoma(vetorX[i], BITS, vetorY[i])
        populacao.append(cromossoma)
        
    for i in range(Num_ger):
            geracao.append(populacao)
            
            
        
if __name__ == "__main__":
    main()
    