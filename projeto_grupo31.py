# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:44:42 2020

@author: ruan_
"""

import matplotlib.pyplot as plt
"""Importação da biblioteca que possibilita a utilização de gráficos."""
import numpy as np
"""Importação da biblioteca que possibilita a utilização de matrizes

e funcionalidades da FFT."""
fig=plt.figure()
dados=np.loadtxt('signal.txt')
a=[]
b=[]
i=0
j=0
for beta in dados:
    a.append(dados[i][j])
    j=j+1
    b.append(dados[i][j])
    i=i+1
    j=j-1
"""Laço que divide os dados recebidos em duas listas."""
r=fig.add_subplot(2,1,1)
plt.subplots_adjust(top=1.3)
r.set_title('Dado experimental Re=2000')
r.plot(a,b,color='red')
r.set_xlabel('Tempo (s)',size=9) 
r.set_ylabel('Deslocamento (μm)') 
"""Plotagem do primeiro gráfico."""
fft= np.fft.fft(b)#Cálculo da transformada
x_=np.linspace(0,1/(max(a)/len(a)),len(b))
g=fig.add_subplot(2,1,2)
g.set_xlabel('Freq/F1')
g.set_ylabel('|Z(FREQ)|')
g.plot(x_,2*abs(fft)/len(b))          
plt.xlim(0,100)
plt.ylim(0,0.06)
"""Plotagem do segundo gráfico."""
zeta=(round(abs((max(a)/len(b))-(a[1]-a[0])),14))*len(b)
"""Cálculo de um valor ""zeta" o qual é limite inicial para determinação da

frequência principal."""
#http://www.dsce.fee.unicamp.br/~antenor/pdffiles/qualidade/b3.pdf
#Li sobre um atraso inicial nesse artigo, e decidi tentar aplicá-lo para 
#aperfeiçoamento dos seguintes cálculos. 
top_=[]
t_=0
for x,y in zip(x_,2*abs(fft)/len(b)):
    if x>zeta and x<100:#100 é o valor do limite finale em x.
        if y>t_:
            t_=y
"""laço que encontra y para a frequência principal."""
for x1,y1 in zip(x_,2*abs(fft)/len(b)):
    if y1>=t_ and x1>zeta:
        top_.append(x1)
        break
"""laço que encontra x para a frequência principal."""
plt.annotate('  f={} Hz'.format(round(max(top_),3)),xy=(max(top_),t_),xytext=(max(top_),t_),size=10)
#(Linha 62) Dei dois espaços antes do texto para não ficar em cima da linha.
"""Descobrindo os valores x e y da frequência principal."""
g.grid(True)
r.grid(True)
plt.show()
"""Mostragem dos gráficos com as grades ativadas."""