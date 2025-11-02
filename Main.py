import FuncaoBinaria
import random
import Aptidao_Selecao
import Cruzamento_Mutacao
import FuncaoAvalicao

N = 100
Num_ger = 40
taxa_cruzamento = 0.65
intervalo_min = -100
intervalo_max = 100

BITS = 22

def main():
    populacao = []
    count = 1
    melhor_cromossoma = None
    melhor_resultado = 0.0
    melhorX = 0.0
    melhorY = 0.0

    # cria população inicial
    for i in range(N):
        cromossoma = ''.join(str(random.randint(0, 1)) for _ in range(BITS))
        populacao.append(cromossoma)

    for _ in range(Num_ger): #avalia a população
        
        aptidoes = Aptidao_Selecao.avaliaPopulacao(populacao, BITS)

        selecionados = []
        resultados = []

        # seleção por roleta
        for i in range(N):
            cromossoma = Aptidao_Selecao.selecaoRoleta(aptidoes, populacao)
            selecionados.append(cromossoma)

        #cromossoma mais frequente entre os selecionados
        melhorPai = max(selecionados, key=selecionados.count)

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

        #elitismo
        if len(nova_populacao) > 0:
            nova_populacao[0] = melhorPai

        print(f"Geracao {count} concluida.")
        count += 1

        #avalia a nova população e atualiza o melhor cromossoma
        for cromossoma in nova_populacao:
            valorX, valorY = FuncaoBinaria.separaCromossoma(cromossoma, BITS)
            valorX, valorY = FuncaoBinaria.decodificaCromossoma(valorX, valorY, BITS//2, intervalo_min, intervalo_max)
            resultado = FuncaoAvalicao.funcaoAvaliacao(valorX, valorY)
            resultados.append(resultado)
            if resultado > melhor_resultado:
                melhor_resultado = resultado
                melhor_cromossoma = cromossoma
                melhorX = valorX
                melhorY = valorY
            if resultado == 1:
                print("Solução encontrada!")
                print(f"Cromossoma: {cromossoma}, ({valorX},{valorY})")
                return

        print(f"Melhor da geracao {count - 1}: Cromossoma: {melhor_cromossoma}, ({melhorX},{melhorY}), Resultado: {melhor_resultado}")

        # prepara próxima geração
        populacao = nova_populacao
        
    return
        
if __name__ == "__main__":
    main()