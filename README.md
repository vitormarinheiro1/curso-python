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