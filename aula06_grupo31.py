# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:11:25 2020

@author: ruan_
"""
#Exercício 10
"""Recebe a quantidade de alunos que vão ser trabalhados no código"""
n=int(input("Informe o numero de alunos: "))
diario={}
i=1
"""Laço que recebe os valores do diário"""
while i<=n:
    d={}
    print("Informe nome, rga, p1, p2, pf, med e freq")
    #Prof, essa parte eu fiz para facilitar a digitação do código (17-23),
    #Porque muito provavelmente, vão ter vários diferentes códigos de diferentes
    #meios de digitar, se o senhor quiser, remova da linha 12 a 40, e na hora
    #de inserir, digite por exemplo:
    #diario["aluno1"]["rga"]=2334243345
    #ou então, remova da linha 26 a 32 e digite:
    #d["nome"]="jhhjdjhd"
    #...
    #d["freq"]=100
    #d["nome"]="jhhjdjhd" ai começa tudo de novo, ele para quando i==n
    nome=input("Informe o nome: ")
    rga=int(input("Informe o rga: "))
    p1=float(input("Informe a p1: "))
    p2=float(input("Informe a p2: "))
    pf=float(input("Informe a pf: "))
    med=float(input("Informe a média: "))
    freq=float(input("Informe a frequencia: "))
    d["nome"]=nome
    d["rga"]=rga
    d["p1"]=p1
    d["p2"]=p2
    d["pf"]=pf
    d["med"]=med
    d["freq"]=freq
    diario["aluno{}".format(i)]=d
    i=i+1
"""Função que organiza os dados printados"""
print(diario)
print("\n\n\nPARA MODIFICAR, DIGITE : diario['alunoN']['rga']=2, onde N é um valor para o aluno, rga é uma variavel exemplo e 2 é um valor qualquer\n\n\n")
#Exercício 11
def pdiario(diario):
    i=1
    for x in diario:
        print("=================",x.upper(),"=================")
        print("||||Nome: ",diario["aluno{}".format(i)]["nome"])
        print("||||RGA: ",diario["aluno{}".format(i)]["rga"])
        print("||||Prova 1: ",diario["aluno{}".format(i)]["p1"])
        print("||||Prova 2: ",diario["aluno{}".format(i)]["p2"])
        print("||||Prova Final: ",diario["aluno{}".format(i)]["pf"])
        print("||||Média: ",diario["aluno{}".format(i)]["med"])
        print("||||Frequência: ",diario["aluno{}".format(i)]["freq"])
        print("===========================================")
        i=i+1
"""Função que busca um RGA entre os outros"""
#Exercício 12
def sRGA(diario):
    i=1
    a=1
    rg_a=int(input("Informe um rga: "))
    for x in diario:
        if rg_a==diario["aluno{}".format(i)]["rga"]:
            print("RGA ENCONTRADO: ",diario["aluno{}".format(i)]["nome"]
                  ,"de rga", diario["aluno{}".format(i)]["rga"])
            a=0
        i=i+1
    if a!=0:
        print("Nenhum resultado encontrado!")
"""Função que busca a maior média entre as outras"""
#Exercício 13
def media(diario):
    i=1
    lista=[]
    for x in diario:
        """Mecanismo que adiciona as médias em uma lista"""
        lista.append(diario["aluno{}".format(i)]["med"])
        i=i+1
    i=1
    j=0
    """Aqui a lista é ordenada"""
    lista.sort()
    lista.reverse()
    while len(lista)>0:
        if lista[j]==diario["aluno{}".format(i)]["med"]:
            print("================= ALUNO",i,"=================")
            print("||||Nome: ",diario["aluno{}".format(i)]["nome"])
            print("||||RGA: ",diario["aluno{}".format(i)]["rga"])
            print("||||Prova 1: ",diario["aluno{}".format(i)]["p1"])
            print("||||Prova 2: ",diario["aluno{}".format(i)]["p2"])
            print("||||Prova Final: ",diario["aluno{}".format(i)]["pf"])
            print("||||Média: ",diario["aluno{}".format(i)]["med"])
            print("||||Frequência: ",diario["aluno{}".format(i)]["freq"])
            print("===========================================")
            i=1
            del lista[j]
            #j=j+1
        else:
            i=i+1
            
        
        
 