import numpy as np

#E/e: Usado para representar o não terminal

def tipo0(coluna1, coluna2):
    for i in range(len(coluna1)):
        if len(coluna1[i]) > len(coluna2[i]):
            if coluna2[i] == 'E':
                for j in range(len(coluna2)):
                    if coluna1[i] not in coluna1[j] and i != j:
                        return True
            return False
    return True

def tipo1(coluna1, coluna2):
    for i in range(len(coluna1)):
        for j in range(len(coluna1[i])):
            if coluna1[i][j].islower():
                return False
    return True

def tipo2(coluna1,coluna2):
    for i in range(len(coluna1)):
        if len(coluna1[i]) > 2:
            return False
        if len(coluna2[i]) > 2:
            return False
        if len(coluna2[i]) == 2:
            if coluna2[i][1].islower():
                return False
#fazer ao contrario e colocar um not, muito mais fácil
    
def tipo3(coluna1, coluna2):
    for i in range(len(coluna1)):
        #Caso 1:
        #Verifica se possui apenas 1 elemento não terminal do lado direito da seta.
        if(sum(1 for c in coluna2[i] if c.isupper()) == 1):
            tamColuna2 = len(coluna2[i])
            #Verifica se esse elemento não terminal está na última posição da string.
            if((coluna2[i][tamColuna2]).isupper()):
                return True
        #Caso 2:
        #Se o lado direito da seta não possuir um elemento não terminal, retorna true.
        if not any(c.isupper() for c in coluna2[i]):
            return True
        #Caso 3:
        #Verifica se o lado esquerdo da seta possui apenas um elemento não terminal.
        if (coluna1[i] == 1 and (coluna1[i][0]).isupper()):
            #Verifica se o lado direito da seta possui o símbolo de vazio (seja ele maiúsculo ou minúsculo).
            if(coluna2[i][0] == 'E' or coluna2[i][0] == 'e'):
                return True
    return False

def tipo_gramatica(coluna1, coluna2):

    tipo_gramatica = -1
    if tipo0(coluna1, coluna2) == True:
        tipo_gramatica = 0
    if tipo1(coluna1, coluna2) == True:
        tipo_gramatica = 1
    if tipo2(coluna1, coluna2) == True:
        tipo_gramatica = 2
    if tipo3(coluna1, coluna2) == True:
        tipo_gramatica = 4
    return tipo_gramatica