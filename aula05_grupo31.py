# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:31:00 2020

@author: ruan_
"""
from collections import deque
#exercicio 6
def min_max(lista):
    """Função que terona os valores mínimos e máximos de uma lista."""
    return min(lista),max(lista)
#exercicio 7:
def no_repeat(lista):
    """Esse algoritmo recebe valores repetidos e os retorna unicamente."""
    l = []
    for j in lista:
        """Esse laço for é responsavel por receber em j, os valores de lista
        e adicionalos em l, no entanto, eles só são adicionados em l 
        se não estiverem presentes ainda."""
        if j not in l:
            l.append(j)
    return l
#exercicio 8
def linear(b,a,x):
    lista=[]
    tupla=()
    for j in x:
        """Esse laço for faz com que em cada rotina, j receba um valor
        de x, que é um range, ou seja, os valores de y são definidos 
        por cada vez que o j varia"""
        y=b*j+a
        tupla=(j,y)
        """Aqui eu agrupo os pontos ordenados em tuploas para 
        ficarem bonitinhos na exibição ao usuário"""
        lista.append(tupla)
        """Aqui eu adiciono as tuplas na lista"""
    return lista
def retas(b,a,x):
    y=[]
    y=deque(map(linear,b,a,x))
    """Map possibilita que mais de uma reta seja
    criada por vez, a sua sintaxe é deque(map(função,
    seq,seq, seq,...))"""
    return y
#exercicio 9
def lc(b,a,x): 
    """Esse algoritmo é uma listcomprehension da fução retas."""
    return [(j,b*j+a) for a,b in zip(a,b) for j in x]  
