### Argumentos nomeados e não nomeados
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeado recebe apenas o argumento (valor)

### *args

def soma(*args):
    total = 0
    for numero in args:
        total = total + numero
        print(numero, total)

### Termos técnicos
Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

### Closure
Uma closure em Python é uma função que lembra e pode acessar variáveis do seu escopo externo, mesmo após o término desse escopo.

### Dict - Manipulando dicionários
pessoa = {}
chave = 'nome'
pessoa[chave] = 'Vitor Marinheiro'

### Métodos úteis dos dicionários em Python
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Vitor Rodrigues',
    'sobrenome': 'Marinheiro',
    'idade': 900,
}

print(list(pessoa.keys()))

### Set
