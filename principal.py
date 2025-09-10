import numpy as np

def tipo1(coluna1, coluna2):
    for i in range(len(coluna1)):
        if len(coluna1[i]) > len(coluna2[i]):
            if coluna2[i] == 'E':
                for j in range(len(coluna2)):
                    if coluna1[i] not in coluna1[j] and i != j:
                        return True
            return False
    return True

def tipo2(coluna1, coluna2):
    for i in range(len(coluna1)):
        for j in range(len(coluna1[i])):
            if coluna1[i][j].islower():
                return False
    return True

def tipo3(coluna1,coluna2):
    for i in range(len(coluna1)):
        if len(coluna1[i]) > 2:
            return False
        if len(coluna2[i]) > 2:
            return False
        if len(coluna2[i]) == 2:
            if coluna2[i][1].islower():
                return False
#fazer ao contrario e colocar um not, muito mais fácil

def tipo_gramatica(coluna1, coluna2):

    tipo_gramatica = 0
    if tipo1(coluna1, coluna2)==True:
        tipo_gramatica = 1
    if tipo2(coluna1, coluna2)==True:
        tipo_gramatica = 2
    if tipo3(coluna1, coluna2)==True:
        tipo_gramatica = 3
    return tipo_gramatica