# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:56:09 2020

@author: ruan_
"""

def diagrama(): 
    import matplotlib.pyplot as plt
    i=0
    f_=[0.008,0.009,0.01,0.015,0.02,0.025,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
    while i<len(f_):
        plt.plot(64/f_[i],f_[i]) 
        i=i+1
    i=0
    j=0
    fator_atrito(e,d,re)
    j1=fator_atrito()
    j2=fator_atrito()
    while i<len(j1):
        while j<len(j2):
            plt.plot(j2[j],j1[i]) 
            j=j+1
        j=0
        i=i+1
    plt.show()
def fator_atrito(e,d,re):
    import math
    j1=[]
    j2=[]
    """Função que calcula o fator de atrito para um Regime Turbulento."""
    f_chute=0.036
    verificadordecondicao=True
    while verificadordecondicao==True:
        """Equação de Colebrook-White"""
        f=(-2*math.log10(((e/d)/3.7)+(2.51/(re*(f_chute**0.5)))))**-2
        """Esquema para determinar o coeficiente de atrito aproximado (17-20).""" 
        if abs(f-f_chute) >= 0.0000001: # (1e-5):
            f_chute=f
            j1.append(f)
            j2.append(re)
        else:
            verificadordecondicao=False
    return f
    return j1
    return j2
    """É importante retornar f para poder utiliza-lo em perda_de_carga1()."""
def perda_de_carga1():
    import math
    """Função que calcula a perda de carga de acordo com Re."""
    e=float(input("Informe o valor da rugosidade absoluta da tubulação e (em mm): "))
    e=e/1000
    d=float(input("Informe o diâmetro(em m): "))
    q=float(input("Informe a vazão(em m³/s): "))
    v=q/(((d**2)/4)*math.pi)
    #usei vc para viscosidade cinemárica porque não estava conseguindo 
    #enxergar a diferença de v e V
    vc=float(input("Informe a viscosidade cinemática do fluido ν (em m²/s): "))
    l=float(input("Informe o comprimento do tubo (em m): "))
    re=(v*d)/vc
    if re>2300 and re<4000:
        print("Re = ",re)
        print("Regime de Transição!")
        print("Fator de atrito indeterminado!")
    elif re<=2300:
        print("Re = ",re)
        print("Regime Laminar!")
        f=64/re
        print("Fator de atrito: ",f)
        hf=f*(l*((v**2))/(2*d))
        print("Perda de carga (em m²/s²)= ",hf)
    else: 
        print("Re = ",re)
        print("Regime Turbulento!")
        fator_atrito(e,d,re)
        """Chamada da variável f da função fator_atrito (e,d,re)."""
        f=fator_atrito(e,d,re)
        print("Fator de atrito: ",f)
        hf=f*((l*(v**2))/(2*d))
        print("Perda de carga (em m²/s²)= ",hf)
        """Sequência de condições para determinar a perda de carga em cada caso."""