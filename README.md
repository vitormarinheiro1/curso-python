# PYTHON -> Van Rossum, 1991

### Conversão tipos
print(int('1') + 1)
print(bool('')) // False

### Formatação de números
number = f'{imc:,2f}'

### Operador lógico Not
print(not True) -> False
print(not False) -> True

### Operadores in e not in
in -> está entre
not in -> não está entre

### Interpolação com %
s - string
d e i - int
f - float
x e X - Hexadecimal

nome = 'Vitor'
idade = 18
variavel = '%s, o preço é R$%f' % (nome, preco)

### Formatação de strings
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.2040240420:0=+10,.1f}')

### Fatiamento de strings [i:f:p] [::]
o p é de quantos caracteres ele irá pular

variavel = 012456789
print(variavel[0:5])

### Constantes

Valores que não são alterados

### ID - Identidade na memória
v1 = 'a'
print(id(v1))

### Flags, is, is not e None
variavel = None
print(variavel is None) -> True

### While -> usado quando não sei a quantidade de repetições

while contador < 10:
    if contador == 5:
    continue

continue (não mostrar algo)

### for in

Iteravel -> str, range, etc
Iterado -> quem sabe entregar um valor por vez
next - me entregue o próximo valor
iter -> me entregue seu iterador

texto = 'Python'
for letra in texto:
    print(letra)

### range
range -> range(start, stop, step)

### listas
* criar
lista = [10, 20, 30, 40, 50]

* alterar
lista[2] = 300

* deletar
del lista[2]

* adicionar
lista.append(60)

* remove o ultimo item da lista
lista.pop()

* insert - adiciona um item no indice escolhido
* clear - limpa a lista
* extend - estende a lista

### tuplas -> imutável
tupla = (10, 20, 30, 40, 50)

### enumerate - enumera iteráveis (índices)
lista = [10, 20, 30, 40]
lista_enumerada = enumerate(lista)

### decimais + ponto flutuante
print(round(f'{numero:.2f}))
print(round(numero, 2))

### split, joins, strip
split -> faz uma lista com cada palavra
strip -> deixa sem espaço no meio e no fim
rstrip -> deixa sem espaço na direita
lstrip -> deixa sem espaço na esquerda
join -> une uma string