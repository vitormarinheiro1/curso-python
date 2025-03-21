# DATETIME
from datetime import datetime

datetime(dia, mes, ano)
datetime.strptime('DATA', 'FORMATO')
datetime.now()
data.timestamp()


# OS / OS.PATH
CAMINHO = os.path.join('C:\\Users\\x396751\\Desktop\\Workspace\\curso-python')
print(os.path.basename(CAMINHO))

os.path.getsize -> tamanho do arquivo
os.stat -> estatistica do arquivo

# os + shutil - Mover, copiar e apagar arquivos
mover/renomear -> shutil.move
mover/renomear -> os.rename
copiar -> shutil.copy
apagar -> os.unlink
apagar diretorio recursivamente -> shutil.rmtree

# CSV (Comma Separated Values)
csv.reader -> lê o CSV

# RANDOM
random.randint(n1, n2) -> numeros aleatorios entre n1 e n2
random.uniform(n1, n2) -> numeros DECIMAIS aleatorios entre n1 e n2
random.shuffle(lista_de_nomes) -> embaralha por exemplo uma lista de nomes
random.sample(lista_de_nomes, k=2) -> embaralha, porem pega somente 2 nomes por conta do K=2
random.choices(lista_de_nomes) -> pode repetir os valores
random.choice(lista_de_nomes) -> escolhe um unico valor

# SECRETS GERA NÚMEROS ALEATÓRIOS SEGUROS
import secrets
from secrets import SystemRandom as sr

random = secrets.SystemRandom() -> APÓS ISSO POSSO USAR OS METODOS DO RANDOM

# VARIAVES DE AMBIENTES
os.getenv(('SENHA'))