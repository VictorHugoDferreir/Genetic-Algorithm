import FuncaoBinaria
import random
import Aptidao_Selecao
import Cruzamento_Mutacao
import FuncaoAvalicao
import matplotlib.pyplot as plt

N = 100
Num_ger = 100

taxa_cruzamento = 0.65
intervalo_min = -100
intervalo_max = 100

BITS = 44

def main():
    populacao = []
    count = 1
    melhor_cromossoma = None
    melhor_resultado = 0.0
    melhorX = 0.0
    melhorY = 0.0
    melhores_resultados = []

    # cria população inicial
    for i in range(N):
        cromossoma = ''.join(str(random.randint(0, 1)) for _ in range(BITS))
        populacao.append(cromossoma)

    for _ in range(Num_ger): #avalia a população
        found_solution = False
        
        aptidoes = Aptidao_Selecao.avaliaPopulacao(populacao, BITS)

        selecionados = []
        resultados = []

        # seleção por torneio (mais robusta que roleta)
        for i in range(N):
            cromossoma = Aptidao_Selecao.selecaoTorneio(populacao, aptidoes, k=3)
            selecionados.append(cromossoma)

        # seleciona os 2 melhores indivíduos da população atual (elitismo)
        indices_ordenados = sorted(range(len(aptidoes)), key=lambda i: aptidoes[i], reverse=True)
        melhorPai = populacao[indices_ordenados[0]]
        segundoMelhor = populacao[indices_ordenados[1]]

        nova_populacao = []
        
        # cruzamento e mutação 
        for i in range(0, N, 2):
            pai1 = selecionados[i]
            pai2 = selecionados[i + 1]
            if random.random() < taxa_cruzamento:
                filho1, filho2 = Cruzamento_Mutacao.Crossover(pai1, pai2)
                filho1 = Cruzamento_Mutacao.Mutacao(filho1)
                filho2 = Cruzamento_Mutacao.Mutacao(filho2)
                nova_populacao.append(filho1)
                nova_populacao.append(filho2)
            else:
        
                filho1 = Cruzamento_Mutacao.Mutacao(pai1)
                filho2 = Cruzamento_Mutacao.Mutacao(pai2)
                nova_populacao.append(filho1)
                nova_populacao.append(filho2)

        # elitismo: preserva os 2 melhores da geração anterior
        if len(nova_populacao) > 1:
            nova_populacao[0] = melhorPai
            nova_populacao[1] = segundoMelhor

        print(f"Geracao {count} concluida.")
        count += 1

        #avalia a nova população e atualiza o melhor cromossoma
        for cromossoma in nova_populacao:
            valorX, valorY = FuncaoBinaria.separaCromossoma(cromossoma, BITS)
            valorX, valorY = FuncaoBinaria.decodificaCromossoma(valorX, valorY, BITS//2, intervalo_min, intervalo_max)
            resultado = FuncaoAvalicao.funcaoAvaliacao(valorX, valorY)
            resultados.append(resultado)
            #print(f"Cromossoma: {cromossoma}, ({valorX},{valorY}) => Resultado: {resultado}")
            if resultado > melhor_resultado:
                melhor_resultado = resultado
                melhor_cromossoma = cromossoma
                melhorX = valorX
                melhorY = valorY
            # usa tolerância para comparação de ponto flutuante
            if resultado >= 0.999999:
                print("Solução encontrada!")
                print(f"Cromossoma: {cromossoma}, ({valorX},{valorY}), Resultado: {resultado}")
                found_solution = True
                break

        print(f"Melhor da geracao {count - 1}: Cromossoma: {melhor_cromossoma}, ({melhorX},{melhorY}), Resultado: {melhor_resultado}")
        melhores_resultados.append(melhor_resultado)
        
        # prepara próxima geração
        populacao = nova_populacao
        if found_solution:
            break
    print(f"\nEvolucao concluida. Melhor solucao encontrada:")
    print(f"Cromossoma: {melhor_cromossoma}, ({melhorX},{melhorY}), Resultado: {melhor_resultado}")
    
    plt.style.use('seaborn-v0_8')
    plt.plot(melhores_resultados, marker='o', label='Melhor Resultado por Geração')
    plt.title('Algoritmo Genético - Evolução do Melhor Resultado')
    plt.xlabel('Geração')
    plt.ylabel('Resultado')
    plt.legend()
    plt.show()
        
    return
        
if __name__ == "__main__":
    main()