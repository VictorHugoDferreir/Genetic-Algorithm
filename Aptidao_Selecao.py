import FuncaoAvalicao
import FuncaoBinaria
import Main
import random


def calculaAptidao(cromossoma, BITS):

    valorX, valorY = FuncaoBinaria.separaCromossoma(cromossoma, BITS)

    valorX, valorY = FuncaoBinaria.decodificaCromossoma(valorX, valorY, BITS//2, Main.intervalo_min, Main.intervalo_max)

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

    
    for i, aptidao in enumerate(aptidoes):
        somatorio += aptidao
        if somatorio >= selecao:
            return populacao[i]