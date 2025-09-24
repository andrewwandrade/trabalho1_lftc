# Trabalho de L.F.T.C.

 Trabalho produzido com o objetivo de classificar uma gramática de acordo com a Hierarquia de Chomsky.

### O que é uma gramática?

No contexto da disciplina de Linguagens Formais e Teoria da Computação, uma gramática é um procedimento que enumera elementos de uma linguagem, sendo o tipo mais comum de gerador.

### Hierarquia de Chomsky

De acordo com a Hierarquia de Chomsky, a classificação de uma gramática é dividida em 4 tipos: 0, 1, 2, 3.

####  Tipo 0

- Gramática sem restrição.
- As regras são do tipo: `α -> β`.
- Sendo α, β quaisquer.
- Observação: Todas as gramáticas são do Tipo 0.

#### Tipo 1

- Gramática sensível ao contexto.
- As regras são do tipo: `α -> β`.
- Sendo α, β quaisquer e `|α| <= |β|`.
- Exceção: Será aceito a regra `S -> ε` se o não terminal S não aparecer do lado direito de uma regra.

####  Tipo 2

- Gramática livre de contexto.
- As regras são do tipo: `α -> β`.
- Sendo β quaisquer e A não terminal.

#### Tipo 3

- Gramática regular.
- As regras tem que ser UM dos seguintes três tipos: `A -> aB`, `A -> a`, `A -> ε`

### Funcionamento do programa

O programa presume que o arquivo `.txt` tenha uma gramática apta a ser examinada pelo programa

#### Leitura de arquivos

``` python
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
```

- Lê o arquivo linha a linha, usando vetores para armazenar as duas colunas
- A separação é feita usando o `' '` entre as duas colunas no arquivo `.txt`

#### Tipo 1

``` python
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
```
- Verifica se a coluna dos não-terminais é menor que a outra coluna
- Além dessa verificação, é levado em cosideração a exceção

#### Tipo 2

``` python
def tipo2(coluna1):
    for i in range(len(coluna1)):
        for j in range(len(coluna1[i])):
            if coluna1[i][j].islower():
                return False
    return True
```
- Verifica cada elemento da coluna 1, enquanto também verifica se há algum terminal na mesma coluna

#### Tipo 3

``` python
def tipo3(coluna1,coluna2):
    for i in range(len(coluna1)):
        if len(coluna1[i]) > 1:
            return False
        if len(coluna2[i]) > 2:
            return False 
        if len(coluna2[i]) == 2:
            if coluna2[i][1].islower():
                return False
        if len(coluna2[i]) == 1:
            if coluna2[i].isupper() and coluna2[i] != 'E':
                return False
    return True
```
- Faz o pente fino averiguando se alguma das regras foge do padrão: `A -> aB`, `A -> a`, `A -> ε`.
