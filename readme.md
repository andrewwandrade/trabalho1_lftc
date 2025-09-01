# Trabalho de L.F.T.C.

 Trabalho produzido com o objetivo de classificar uma gramática de acordo com a Hierarquia de Chomsky.

### O que é uma gramática?

No contexto da disciplina de Linguagens Formais e Teoria da Computação, uma gramática é um procedimento que enumera elementos de uma linguagem, sendo o tipo mais comum de gerador.

### Hierarquia de Chomsky

De acordo com a Hierarquia de Chomsky, a classificação de uma gramática é dividida em 4 tipos: 0, 1, 2, 3.

####  Tipo 0

- Gramática sem restrição.
- As regras são do tipo: α -> β.
- Sendo α, β quaisquer.
- Observação: Todas as gramáticas são do Tipo 0.

#### Tipo 1

- Gramática sensível ao contexto.
- As regras são do tipo: α -> β.
- Sendo α, β quaisquer e |α| <= |β|.
- Exceção: Será aceito a regra S -> ε se o não terminal S não aparecer do lado direito de uma regra.

####  Tipo 2

- Gramática livre de contexto.
- As regras são do tipo: α -> β.
- Sendo β quaisquer e A não terminal.

#### Tipo 3

- Gramática regular.
- As regras são de UM dos seguintes três tipos: A -> aB, A -> a, A -> ε

### Funcionamento do programa
