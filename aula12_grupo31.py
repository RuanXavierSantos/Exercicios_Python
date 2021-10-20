# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:25:49 2020

@author: ruan_
"""


def diagrama():
    """Função que cria o diagrama de Moody."""
    import matplotlib.pyplot as plt   
    import math
    x_=[]
    y_=[]
    f_=[]
    re_=[]
    x=[]
    y=[]
    """Conjunto de listas que futuramente receberam os valores dos pares

    ordenados.
    """
    for beta in range(1,2301,30):
        #Sempre 1 como primeiro valor, pois o grádico está em escala log,
        #não existe log de 0.
        gama=64/beta
        y_.append(round(gama,5))
        x_.append(beta)
    """Esse laço cria os dados do regime laminar."""
    rr=[0.05,0.04,0.03,0.02,0.015,0.01,0.008,0.006,0.004,0.002,0.001,0.0008,0.0006,0.0004,0.0002,0.0001,0.00005,0.00001,0.000005,0.000001,0]
    fig,ax=plt.subplots()
    plt.ylabel('FATOR DE ATRITO (f)')
    plt.xlabel('NÚMERO DE REINOLDS (Re)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.title("DIAGRAMA DE MOODY")
    """Aqui o design do gráfico é definido."""
    i=0
    while i<len(rr):
        for re in range(4000, 10**8, 1000):
            f2=0.1
            f=0
            while round(f,5) != round(f2,5):
                f = (-2*math.log10(((rr[i])/3.7)+(2.51/(re*(f2**0.5)))))**(-2)
                f2=f
            y.append(f)
            x.append(re)
        ax.plot(x,y,color='blue')
        x=[]
        y=[]
        i=i+1
    """Esses três laços, alternam o valor de e/D conforme o valor de Re aumenta,

    utilizando a equação de Colebrook-White para fazer as aproximações.
    """
    ax.plot(x_,y_,color='blue')
    plt.annotate('f=64/Re',xy=(820,0.09),xytext=(820,0.09))
    i=0
    while i<len(rr):
        if str(rr[i])!='0' and rr[i]<0.0001:
            plt.text(re_[i],f_[i],'{:.6f}'.format(rr[i]),size=8)
        elif str(rr[i])!='0' and rr[i]>=0.0001:
            plt.text(re_[i],f_[i],rr[i],size=8)
        else:
            plt.annotate("TUBO LISO",xy=(re_[i],f_[i]),xytext=(re_[i],f_[i]),size=8)
        i=i+1
    """Laço de repetição responsável por escrever os valores e/d das linhas."""
    plt.ylim(0.005,0.1)
    plt.xlim(500,10**8)
    plt.show()
