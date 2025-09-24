coluna1 = []
coluna2 = []

def processarLinha(linha):
    pos = linha.find(' ') 
    substring1 = linha[0:pos]
    substring2 = linha[pos+1:len(linha)]
    coluna1.append(substring1)
    coluna2.append(substring2)

def lerArquivo():
    coluna1.clear() 
    coluna2.clear()
    with open("arquivo.txt", "r") as arqGram:
        for linha in arqGram:
            linha = linha.rstrip()
            processarLinha(linha)
    print("Arquivo lido com sucesso!")

def tipo1(coluna1, coluna2):
    for i in range(len(coluna1)):
        if len(coluna1[i]) > len(coluna2[i]):
            return False
        if coluna2[i] == 'E':
            if coluna1[i] != 'S':
                return False
            for j in range(len(coluna1)):
                if 'S' in coluna2[j]:
                    return False
            continue
    return True

def tipo2(coluna1):
    for i in range(len(coluna1)):
        for j in range(len(coluna1[i])):
            if coluna1[i][j].islower():
                return False
    return True

def tipo3(coluna1,coluna2):
    for i in range(len(coluna1)):
        if len(coluna1[i]) > 1:
            return False
        if len(coluna2[i]) > 2:
            return False 
        if len(coluna2[i]) == 2:
            if coluna2[i][1].islower() or (coluna2[i][0].isupper() and coluna2[i][1].isupper()):
                return False
        if len(coluna2[i]) == 1:
            if coluna2[i].isupper() and coluna2[i] != 'E':
                return False
    return True
    
def tipo_gramatica(coluna1, coluna2):

    tipo_gramatica = 0
    print("\nÉ tipo 0")
    if tipo1(coluna1, coluna2) == True:
        tipo_gramatica = 1
        print("É tipo 1")
    if tipo2(coluna1) == True:
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
