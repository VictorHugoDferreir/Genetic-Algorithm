import FuncaoBinaria
import random
import Aptidao_Selecao
import Cruzamento_Mutacao

N = 100
Num_ger = 40
taxa_cruzamento = 0.65

BITS = 22

def main():
    
    populacao = []
    geracao = []
    selecionados = []
    nova_populacao = []
    vetorX = [random.randint(-100, 100) for i in range(N)]
    vetorY = [random.randint(-100, 100) for i in range(N)]
    
    for i in range(N):
        cromossoma = FuncaoBinaria.criaCromossoma(vetorX[i], BITS, vetorY[i])
        populacao.append(cromossoma)
    
    for geracao in range(Num_ger):   
        for i in range(N):
            cromossoma = Aptidao_Selecao.selecaoRoleta(Aptidao_Selecao.avaliaPopulacao(populacao, BITS), populacao)
        #    print("Cromossoma selecionado:", cromossoma)   Para ver os cromossomas selecionados na roleta
            selecionados.append(cromossoma) 
    i = 0
    for i in range(0, N, 2):
        if random.random() < taxa_cruzamento:
            filho1, filho2 = Cruzamento_Mutacao.Crossover(selecionados[i], selecionados[i + 1])
            #print(f"Filho {i} antes da mutação: {filho1}")  # Para ver o filho 1 antes da mutação
            #print(f"Filho {i + 1} antes da mutação: {filho2}")  # Para ver o filho 2 antes da mutação
            Cruzamento_Mutacao.Mutacao(filho1)
            Cruzamento_Mutacao.Mutacao(filho2)
            nova_populacao.append(filho1)
            nova_populacao.append(filho2)
        else:
            Cruzamento_Mutacao.Mutacao(selecionados[i])
            Cruzamento_Mutacao.Mutacao(selecionados[i + 1])
            nova_populacao.append(selecionados[i])
            nova_populacao.append(selecionados[i + 1])

    print("Nova população:", nova_populacao)
        
if __name__ == "__main__":
    main()
    