coluna1 = []
coluna2 = []

def processarLinha(linha):
    pos = linha.find(' ') #Procura pelo espaço dentro da string.
    substring1 = linha[0:pos] #Pega a primeira parte (até a seta) da string linha.
    substring2 = linha[pos+1:len(linha)] #Pega a segunda parte (depois da seta) da string linha.
    coluna1.append(substring1)
    coluna2.append(substring2)

def lerArquivo():
    coluna1.clear() #Para quando o usuário insere outra gramática sem reiniciar o programa.
    coluna2.clear()
    with open("arquivo.txt", "r") as arqGram:
        for linha in arqGram:
            linha = linha.rstrip() #Remove caracteres do lado direito da string (Ex: \n)
            processarLinha(linha)
    print("Arquivo lido com sucesso!")

def tipo1(coluna1, coluna2):
    for i in range(len(coluna1)):
        if len(coluna1[i]) > len(coluna2[i]):
            return False
        if coluna2[i] == 'E' and coluna1[i] != 'S':
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
    return True
    
def tipo3(coluna1, coluna2):
    for i in range(len(coluna1)):
        #Verifica se o lado esquerdo da seta possui apenas um elemento não terminal.
        if not (len(coluna1[i]) == 1 and coluna1[i][0].isupper()):
            return False
        #Caso 1 (A -> aB)
        if sum(1 for c in coluna2[i] if c.isupper()) == 1:
            tam = len(coluna2[i])
            if coluna2[i][tam - 1].isupper():  #Checa se o elemento não terminal está na última posição.
                continue 
            else:
                return False #Caso o não terminal NÃO esteja na última posição do lado direito da seta, retorna falso.
        #Caso 2 (A -> a)
        elif not any(c.isupper() for c in coluna2[i]):
            continue
        #Caso 3 (A -> e)
        elif coluna2[i] == 'E' or coluna2[i] == 'e':
            continue
        else:
            #Caso não atenda nenhum dos casos acima, retorna falso, dizendo que não é uma gramática do tipo 3.
            return False
    #Como o programa chegou até aqui sem retornar falso para nenhuma das regras, então é uma gramática do tipo 3.
    return True

def tipo_gramatica(coluna1, coluna2):

    tipo_gramatica = 0
    print("\nÉ tipo 0")
    if tipo1(coluna1, coluna2) == True:
        tipo_gramatica = 1
        print("É tipo 1")
    if tipo2(coluna1, coluna2) == True:
        tipo_gramatica = 2
        print("É tipo 2")
    if tipo3(coluna1, coluna2) == True:
        tipo_gramatica = 3
        print("É tipo 3")
    return tipo_gramatica

############################################################################

def main():
    print("Olá, Usuário!\n")
    print("Para o correto uso do programa, insira a gramática a ser lida sem setas, como exemplificado no formato abaixo:\n")
    print("S aS\n" \
          "S bS\n" \
          "S e")
    
    bool_menu = True

    while bool_menu:
        print("\n====MENU====\n")
        print("[1] Ler arquivo")
        print("[2] Verificar tipo da gramática")
        print("[3] Sair")
        
        opcao = int(input("\nDigite a opção: "))
        
        if opcao == 1:
            lerArquivo()
            print(coluna1)
            print(coluna2)
        elif opcao == 2:
            print("\nSua gramática é do tipo " + str(tipo_gramatica(coluna1, coluna2)))
        elif opcao == 3:
            bool_menu = False
        else: 
            print("\nOpção inválida!\n")

main()
