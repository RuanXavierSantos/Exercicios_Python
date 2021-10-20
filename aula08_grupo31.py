# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:36:47 2020

@author: ruan_
"""
import numpy as np
"""Importação da biblioteca que possibilita a utilização de matrizes."""
dados=np.loadtxt('dados.txt')
i=1
j=0
media1=0
while j<50:
    """Laço que calcula a média da segunda coluna."""
    media1=media1+dados[j][i]
    j=j+1
media1=media1/j
print("A média dos termos da segunda coluna é: ",media1)
i=2
j=0
media2=0
while j<50:
    """Laço que calcula a média da terceira coluna."""
    media2=media2+dados[j][i]
    j=j+1
media2=media2/j
print("A média dos termos da terceira coluna é: ",media2)
i=0
j=0
cont=1
arquivo = open('desvio.txt', 'w')
"""Linha responsável por criar um arquivo vazio txt chamado de desvio."""
desvio = np.zeros((50,3))
"""Trecho que cria uma matriz zerada para receber os futuros dados."""
while j<50:
    while i<3:
        desvio[j][i]=cont
        i=i+1
        desvio[j][i]=round(dados[j][i]-media1,2)
        i=i+1
        desvio[j][i]=round(dados[j][i]-media2,2)
        i=i+1
    i=0
    j=j+1
    cont=cont+1
"""Laços que adicionam os elementos calculados na matriz zerada."""   
j=0
cont=1
i=1
k=2
while j<50:
    arquivo.write("{} {} {}\n".format(repr(cont).rjust(2),repr(desvio[j][i]).rjust(8),repr(desvio[j][k]).rjust(8)))
    j=j+1
    cont=cont+1
"""Laço responsável por adicionar os elementos no arquivo desvio,txt."""
arquivo.close()






