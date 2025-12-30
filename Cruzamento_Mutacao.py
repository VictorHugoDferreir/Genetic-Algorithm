import Main
import random

taxa_mutacao = 0.008

def Crossover(cromossoma1, cromossoma2):
    
    ponto_corte = random.randint(1, len(cromossoma1) - 1)

    filho1 = cromossoma1[:ponto_corte] + cromossoma2[ponto_corte:]
    filho2 = cromossoma2[:ponto_corte] + cromossoma1[ponto_corte:]

    return filho1, filho2

def Mutacao(cromossoma):
    
    cromossoma_mutado = ''
    
    for gene in cromossoma:
        if random.random() < taxa_mutacao:
            gene_mutado = '1' if gene == '0' else '0'
            cromossoma_mutado += gene_mutado
        else:
            cromossoma_mutado += gene
            
    return cromossoma_mutado