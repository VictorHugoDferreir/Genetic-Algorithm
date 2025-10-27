import FuncaoBinaria
import random
import Aptidao_Selecao
import Cruzamento_Mutacao
import FuncaoAvalicao

N = 100
Num_ger = 40
taxa_cruzamento = 0.65

BITS = 22

def main():
    
    populacao = []
    geracao = [0] * Num_ger
    count = 1
    resultados = []
    selecionados = []
    nova_populacao = []
    vetorX = [random.randint(-100, 100) for i in range(N)]
    vetorY = [random.randint(-100, 100) for i in range(N)]
    
    for i in range(N):
        cromossoma = FuncaoBinaria.criaCromossoma(vetorX[i], BITS, vetorY[i])
        populacao.append(cromossoma)
    
    for geracao in range(Num_ger):   
        for i in range(N):  #realizo o calculo de aptidão e gero a roleta
            cromossoma = Aptidao_Selecao.selecaoRoleta(Aptidao_Selecao.avaliaPopulacao(populacao, BITS), populacao)
            #print("Cromossoma selecionado:", cromossoma)   Para ver os cromossomas selecionados na roleta
            selecionados.append(cromossoma) 
        i = 0
        melhorPai = max(selecionados, key=selecionados.count)
        #print("melhor pai:", melhorPai)
        for i in range(0, N, 2): # realizo o cruzamento e a mutação
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
            
        nova_populacao[0] = melhorPai  # Elitismo: mantém o melhor pai na nova população
        geracao = nova_populacao #salvo a populacao da geração atual
        print(f"Geração {count} concluída.")
        count += 1
                
        for cromossoma in nova_populacao:
            valorX, valorY = FuncaoBinaria.separaCromossoma(cromossoma, BITS)
            resultado = FuncaoAvalicao.funcaoAvaliacao(valorX, valorY)
            resultados.append(resultado)
            print(f"Cromossoma: {cromossoma}, ({valorX},{valorY}), Resultado: {resultado}")
            if resultado == 1:
                print("Solução encontrada!")
                return
        populacao.clear()
        nova_populacao.clear()
        selecionados.clear()
        populacao = geracao
        resultados.clear()
        
    return
        
if __name__ == "__main__":
    main()
    