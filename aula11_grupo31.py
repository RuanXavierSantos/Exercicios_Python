# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 09:30:23 2020

@author: ruan_
"""
#Para iniciar o código, digite: a=Diario() (a é uma variavel qualquer) 
#Em seguida, escolha um método de adicionamento de alunos e digite:
#a.add_std() (POR EXEMPLO). 

class Diario:
    """Classe responsável por realizar o diário e seus cálculos."""
    def __init__(self):
        """Método que cria um dicionário vazio e um contador, os quais
        serão utilizados em diversos outros métodos."""
        self.diario={}
        self.conti=1
    def add(self):
        """Método que adiciona 1 único aluno e seu respectivo rga."""
        print("=================RGA E NOME ÚNICOS===============")
        self.diario["aluno{}".format(self.conti)]={'nome':'','rga':'','p1':'','p2':'','pf':'','freq':'','med':'','mediafinal':''}
        nome=input("Informe o nome: ")
        rga=int(input("Informe o rga: "))
        self.diario["aluno{}".format(self.conti)]["nome"]=nome
        self.diario["aluno{}".format(self.conti)]["rga"]=rga
        self.conti=self.conti+1
        print("=================================================")
    def add_std(self):#Correto!
        """Método que adiciona n alunos e seus respectivos rga's de acordo com 
        um valor(n) de estudantes delimitados pelo usuário."""
        n=int(input("Informe o numero de alunos: "))
        while self.conti<=n:
            self.diario["aluno{}".format(self.conti)]={'nome':'','rga':'','p1':'','p2':'','pf':'','freq':'','med':'','mediafinal':''}
            nome=input("Informe o nome: ")
            rga=int(input("Informe o rga: "))
            self.diario["aluno{}".format(self.conti)]['nome']=nome
            self.diario["aluno{}".format(self.conti)]['rga']=rga
            print(self.diario)
            self.conti=self.conti+1
    def std_P1(self):#Correto!
        """Método que adiciona/altera a p1 de um único aluno."""
        verificador=0
        print("=====================P1 ÚNICA====================")
        nome=input("Informe um nome para adicionar ou alterar a nota da p1: ")
        for x in self.diario:
            if self.diario[x]["nome"]==nome:
                p1=float(input("Informe a p1: "))
                self.diario[x]["p1"]=p1
                verificador=1
        if verificador!=1:
            print("Nenhum aluno com esse nome!") 
        print("=================================================")
    def std_P2(self):#Correto!
        """Método que adiciona/altera a p2 de um único aluno."""
        print("=====================P2 ÚNICA====================")
        verificador=0
        nome=input("Informe um nome para adicionar ou alterar a nota da p2: ")
        for x in self.diario:
            if self.diario[x]["nome"]==nome:
                p2=float(input("Informe a p2: "))
                self.diario[x]["p2"]=p2
                verificador=1
        if verificador!=1:
            print("Nenhum aluno com esse nome!") 
        print("=================================================")
    def std_PF(self):#Correto!
        """Método que adiciona/altera a pf de um único aluno."""
        print("=====================PF ÚNICA====================")
        verificador=0
        nome=input("Informe um nome para adicionar ou alterar a nota da pf: ")
        for x in self.diario:
            if self.diario[x]["nome"]==nome:
                med=(self.diario[x]["p1"]+self.diario[x]["p2"])/2
                if med>=3 and med<7 and self.diario[x]["freq"]>=75:
                    pf=float(input("Informe a pf: "))
                    self.diario[x]["pf"]=pf
                    verificador=1
                else:
                    print("Esse aluno não precisa ter nota de pf lançada!")
        if verificador!=1:
            print("Nenhum aluno com esse nome!") 
        print("=================================================")
    def std_Freq(self):
        """Método que adiciona/altera a frequência de um único aluno."""
        verificador=0
        print("=====================FREQUÊNCIA ÚNICA============")
        nome=input("Informe um nome para adicionar ou alterar a frequência: ")
        for x in self.diario:
            if self.diario[x]["nome"]==nome:
                freq=float(input("Informe a frequencia: "))
                self.diario[x]["freq"]=freq
                verificador=1
        if verificador!=1:
            print("Nenhum aluno com esse nome!") 
        print("=================================================")
    def P1(self):#Correto!
        """Método que recebe a nota da p1."""
        print("=========================P1's====================")
        cont=1
        for x in self.diario:
            print("_________________________________________________")
            print("Aluno: ",self.diario["aluno{}".format(cont)]["nome"])
            p1=float(input("Informe a p1: "))
            self.diario["aluno{}".format(cont)]["p1"]=p1
            cont=cont+1
        print("=================================================")
    def P2(self):#Correto!
        """Método que recebe a nota da p2."""
        cont=1
        print("=====================P2's========================")
        for x in self.diario:
            print("_________________________________________________")
            print("Aluno: ",self.diario["aluno{}".format(cont)]["nome"])
            p2=float(input("Informe a p2: "))
            self.diario["aluno{}".format(cont)]["p2"]=p2
            cont=cont+1
        print("=================================================")
    def PF(self):#Correto!
        """Método que define se um aluno precisará fazer pf e recebe o valor 
        da mesma em caso positivo."""
        cont=1
        print("=======================PF's======================")
        for x in self.diario:
            med=(self.diario["aluno{}".format(cont)]["p1"]+self.diario["aluno{}".format(cont)]["p2"])/2
            self.diario["aluno{}".format(cont)]["pf"]=med
            if med>=3 and med<7 and self.diario["aluno{}".format(cont)]["freq"]>=75:
                print("_________________________________________________")
                print(self.diario["aluno{}".format(cont)]["nome"])
                pf=float(input("Informe a nota da PF: "))
                med=(pf+med)/2
                self.diario["aluno{}".format(cont)]["pf"]=med
            cont=cont+1
        print("=================================================")
    def Freq(self):#Correto!
        """Método que recebe os valores das frequências."""
        cont=1
        print("======================FREQUÊNCIAS================")
        for x in self.diario:
            print("_________________________________________________")
            print("Aluno: ",self.diario["aluno{}".format(cont)]["nome"])
            freq=float(input("Informe a frequência: "))
            self.diario["aluno{}".format(cont)]["freq"]=freq
            cont=cont+1
        print("=================================================")
    def media(self):#Correto!
        """Método que faz o cálculo das médias iniciais [(P1+P2)/2]."""
        cont=1
        for x in self.diario:
            med=(self.diario["aluno{}".format(cont)]["p1"]+self.diario["aluno{}".format(cont)]["p2"])/2
            self.diario["aluno{}".format(cont)]["med"]=med
            cont=cont+1
    def aprov1(self):#Correto!
        """Método que printa os aprovados e suas médias finais."""
        cont=1
        self.media()
        print("=================APROVADOS SEM PF================")
        for x in self.diario:
            if self.diario["aluno{}".format(cont)]["med"]>=7 and self.diario["aluno{}".format(cont)]["freq"]>=75:
                print("++++++++++++++++++",x.upper(),"++++++++++++++++++")
                print("||||Nome: ",self.diario["aluno{}".format(cont)]["nome"])
                print("||||Média Final: ",self.diario["aluno{}".format(cont)]["med"])
                print("||||Frequência: ",self.diario["aluno{}".format(cont)]["freq"])
            cont=cont+1
        print("=================================================")
    def aprov2(self):#Correto!
        """Método que printa os aprovados e suas médias finais."""
        cont=1
        self.mediaFinal()
        #Aqui, eu chamei o método mediaFinal para driblar um erro que eu estava
        #tendo, não estava realizando os cálculos porque o algoritmo interpretava
        #as médias como um string.
        print("===========================APROVADOS=============")
        for x in self.diario:
            if self.diario["aluno{}".format(cont)]["mediafinal"]>=5 and self.diario["aluno{}".format(cont)]["freq"]>=75:
                print("++++++++++++++++++",x.upper(),"++++++++++++++++++")
                print("||||Nome: ",self.diario["aluno{}".format(cont)]["nome"])
                print("||||Média Final: ",self.diario["aluno{}".format(cont)]["mediafinal"])
                print("||||Frequência: ",self.diario["aluno{}".format(cont)]["freq"])
            cont=cont+1
        print("=================================================")
    def mediaFinal(self):#Correto!
        """Método que printa e calcula as médias finais."""
        c=1
        print("====================MÉDIAS FINAIS================")
        for x in self.diario:
            if self.diario["aluno{}".format(c)]["med"]<7 and self.diario["aluno{}".format(c)]["med"]>=3:
                med=(self.diario["aluno{}".format(c)]["med"]+self.diario["aluno{}".format(c)]["pf"])/2
                self.diario["aluno{}".format(c)]["mediafinal"]=med
                print("MÉDIA FINAL:  ",self.diario["aluno{}".format(c)]["nome"],"--",self.diario["aluno{}".format(c)]["mediafinal"])
            else:
                med=self.diario["aluno{}".format(c)]["med"]
                self.diario["aluno{}".format(c)]["mediafinal"]=med
                print("MÉDIA FINAL:  ",self.diario["aluno{}".format(c)]["nome"],"--",self.diario["aluno{}".format(c)]["mediafinal"])
            c=c+1
        print("=================================================")
    def print_diario(self):#Correto!
        """Método que printa o diário de classe completo."""
        b=1
        print("==================DIÁRIO DE CLASSE===============")
        for x in self.diario:
            print("++++++++++++++++++",x.upper(),"++++++++++++++++++")
            print("||||Nome: ",self.diario["aluno{}".format(b)]["nome"])
            print("||||RGA: ",self.diario["aluno{}".format(b)]["rga"])
            print("||||Prova 1: ",self.diario["aluno{}".format(b)]["p1"])
            print("||||Prova 2: ",self.diario["aluno{}".format(b)]["p2"])
            print("||||Prova Final: ",self.diario["aluno{}".format(b)]["pf"])
            print("||||Média: ",self.diario["aluno{}".format(b)]["med"])
            print("||||Frequência: ",self.diario["aluno{}".format(b)]["freq"])
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            b=b+1
        print("=================================================")
    def listaPF(self):#Correto!
        """Método que mostra os alunos que farão pf."""
        a=1
        print("=====================VÃO FAZER PF================")
        for x in self.diario:
            if self.diario["aluno{}".format(a)]["med"]>=3 and self.diario["aluno{}".format(a)]["med"]<7 and self.diario["aluno{}".format(a)]["freq"]>=75:
                print("++++++++++++++++++",x.upper(),"++++++++++++++++++")
                print("||||Nome: ",self.diario["aluno{}".format(a)]["nome"])
                print("||||Média: ",self.diario["aluno{}".format(a)]["med"])
                print("||||Frequência: ",self.diario["aluno{}".format(a)]["freq"])              
            a=a+1
        print("=================================================")
    def reprov(self):#Correto!
        """Método que mostra os reprovados."""
        cont=1
        print("=========================REPROVADOS==============")
        for x in self.diario:
            if self.diario["aluno{}".format(cont)]["mediafinal"]<5 or self.diario["aluno{}".format(cont)]["freq"]<75:
                print("++++++++++++++++++",x.upper(),"++++++++++++++++++")
                print("||||Nome: ",self.diario["aluno{}".format(cont)]["nome"])
                print("||||Média: ",self.diario["aluno{}".format(cont)]["mediafinal"])
                print("||||Frequência: ",self.diario["aluno{}".format(cont)]["freq"])
            cont=cont+1 
        print("=================================================")
    def lancamento(self):#Correto!
        """Método que faz o lançamento de notas e frequências, e mostra 
        aprovados e reprovados."""
        self.P1()
        self.P2()
        self.Freq()
        self.PF()
        self.aprov2()
        self.reprov()
