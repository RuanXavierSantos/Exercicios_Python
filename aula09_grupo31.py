# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:56:09 2020

@author: ruan_
"""
def fator_atrito(e,d,re):
    """Função que calcula o fator de atrito para um Regime Turbulento."""
    import math
    f_chute=0.036
    verificadordecondicao=True
    while verificadordecondicao==True:
        """Equação de Colebrook-White"""
        f=(-2*math.log10(((e/d)/3.7)+(2.51/(re*(f_chute**0.5)))))**-2
        """Esquema para determinar o coeficiente de atrito aproximado (17-20).""" 
        if f-f_chute >= 0.0000001: # (1e-5):
            f_chute=f
        else:
            verificadordecondicao=False
    return f
    """É importante retornar f para poder utiliza-lo em perda_de_carga1()."""
def perda_de_carga1():
    """Função que calcula a perda de carga de acordo com Re."""
    import math
    resp=1
    while resp==1:
        e=-1
        d=-1
        vc=-1
        q=-1
        l=-1
        """Essas variáveis recebem valores negativos para entrar no laço de filtragem."""
        while e<0:
            e=float(input("Informe o valor da rugosidade absoluta da tubulação e (em mm): "))
            if e<0:
                print("DIGITE UM VALOR >= A 0!!")
        e=e/1000
        while d<=0:
            d=float(input("Informe o diâmetro(em m): "))
            if d<=0:
                print("DIGITE UM VALOR > QUE 0!!")
        while q<=0:
            q=float(input("Informe a vazão(em m³/s): "))
            if q<=0:
                print("DIGITE UM VALOR > QUE 0!!")
        v=q/(((d**2)/4)*math.pi)
        #usei vc para viscosidade cinemárica porque não estava conseguindo 
        #enxergar a diferença de v e V
        while vc<=0:
            vc=float(input("Informe a viscosidade cinemática do fluido ν (em m²/s): "))
            if vc<=0:
                print("DIGITE UM VALOR > QUE 0!!")
        while l<=0:
            l=float(input("Informe o comprimento do tubo (em m): "))
            if l<=0:
                print("DIGITE UM VALOR > QUE 0!!")
        """Os 5 laços anteriores possibilitam a filtragem de valores (> ou >= 0)."""
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
        resp=int(input("Deseja reutilizar o programa? SIM-1    NÃO-0:  "))
    """Esse laço possibilita a reutilização do programa, de acordo com resp."""
