import FuncaoAvalicao
import FuncaoBinaria
import Main
import random


def calculaAptidao(cromossoma, BITS):

    valorX, valorY = FuncaoBinaria.separaCromossoma(cromossoma, BITS)

    aptidao = FuncaoAvalicao.funcaoAvaliacao(valorX, valorY)

    return aptidao

def avaliaPopulacao(populacao, BITS):

    aptidoes = []

    for cromossoma in populacao:
        aptidao = calculaAptidao(cromossoma, BITS)
        aptidoes.append(aptidao)
    return aptidoes

 
def selecaoRoleta(aptidoes, populacao):
 
    soma_aptidoes = sum(aptidoes)
    selecao = random.uniform(0, soma_aptidoes)
    somatorio = 0
    
#    print("Seleção por roleta - valor sorteado:", selecao) para ver o valor sorteado na roleta
    
    for aptidao in aptidoes:
        somatorio += aptidao
        if somatorio >= selecao:
            indice = aptidoes.index(aptidao)
            selecionado = populacao[indice]
            return selecionado