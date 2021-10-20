# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:45:52 2020

@author: ruan_
"""
#Exercicio 1-Crie a função pot() que retorna a potência de um argumento
#elevado ao outro argumento;
def pot(a,b):
    a=a**b
    print(a)
#Exercicio 2-Crie a função listadinamica() que recebe um número
#indefinido de argumentos e retorna uma lista com esses argumentos;      
def listadinamica(*argumento):
    print(argumento)
#Exercicio 3-Crie a função number() que retorna por escrito um
#número inteiro de 20 a 100 dado como argumento;
def number(n):
    if n<20:
        print("seu numero não esta na lista!")
    elif n>100:
        print("seu numero não esta na lista!")
    else:
        n=n-20
        numberlista=('vinte','vinte e um','vinte e dois','vinte e tres','vinte e quatro',
                     'vinte e cinco','vinte e seis','vinte e sete','vinte e oito',
                     'vinte e nove','trinta','trinta e um','trinta e dois','trinta e tres',
                     'trinta e quatro','trinta e cinco','trinta e seis','trinta e sete','trinta e oito',
                     'trinta e nove','quarenta','quarenta e um','quarenta e dois','quarenta e tres',
                     'quarenta e quatro','quarenta e cinco','quarenta e seis','quarenta e sete',
                     'quarenta e oito','quarenta e nove','cinquenta','cinquenta e um','cinquenta e dois',
                     'cinquenta e tres','cinquenta e quatro','cinquenta e cinco','cinquenta e seis','cinquenta e sete',
                     'cinquenta e oito','cinquenta e nove','sessenta','sessenta e um',
                     'sessenta e dois','sessenta e tres','sessenta e quatro','sessenta e cinco',
                     'sessenta e seis','sessenta e sete','sessenta e oito','sessenta e novo','setenta',
                     'setenta e um','setenta e dois','setenta e tres','setenta e quatro',
                     'setenta e cinco','setenta e seis','setenta e sete','setenta e oito',
                     'setenta e nove','oitenta','oitenta e um','oitenta e dois','oitenta e tres',
                     'oitenta e quatro','oitenta e cinco','oitenta e seis','oitenta e sete',
                     'oitenta e oito','oitenta e nove','noventa','noventa e um','noventa e dois',
                     'noventa e tres','noventa e quatro','noventa e cinco','noventa e seis',
                     'noventa e sete','noventa e oito','noventa e nove','cem')
        print(numberlista[n])
#Exercicio 4-Crie a função sem argumentos asw() que lê repetidamente a
#entrada do usuário até que seja digitado 'yes';
def ans():
    key=0
    while key!="yes":
        key=input("Informe um termo: ")
        if key!="yes":
            print("Tente novamente!")
        else:
           print("Chave correta")
#Exercicio 5-Crie a função lista() que retorna uma lista com os números
#inteiros de 1 até o argumento passado (incluindo o argumento).
def lista():
    kkkk=[]
    x=int(input("Informe um numero: "))
    y=1
    while y<=x:
        kkkk.append(y)
        y=y+1
    print(kkkk)



   

   
    




