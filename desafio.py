# DESAFIO 1 - função 4 operações
def operations(a,b):
  adicionar = a+b
  subtrair = a-b
  multiplicar = a*b
  dividir = a/b
  return adicionar, subtrair, multiplicar, dividir

try:
  a = int(input("Digite um número inteiro: "))
  b = int(input("Digite outro número inteiro: "))
  calcular = operations(a, b)
  print("Adição: ", calcular[0])
  print("Subtração: ", calcular[1])
  print("Multiplicação: ", calcular[2])
  print(f"Divisão: {calcular[3]:.2f}")

except:
  print("Entradas inválidas (devem ser números inteiros)!\n Tente novamente.")


# DESAFIO 2 - idades
def classifica_idade(idade):
  if idade <= 12:
    classificacao = "Criança"
  elif 13 <= idade <= 17:
    classificacao = "Adolescente"
  else:
    classificacao = "Adulto"
  
  return classificacao

try:
  idade = int(input("Digite a idade: "))
  if idade <= 0:
    print("A idade deve ser positiva!")
  else:
    print("Classificação: ", classifica_idade(idade))
except:
    print("A idade deve ser um número inteiro positivo!")


# DESAFIO 3 - conversão horário para segundos
def time_converter(t):
  segundos = horas * 3600
  return segundos

try:
  horas = float(input("Digite horas ou fração de horas (formato exemplo: 0.5 = meia hora): "))
  segundos = time_converter(horas)
  print(f"{horas} hora(s) é igual a {segundos:.0f} segundos.")
except:
    print("Formato inválido!")


# DESAFIO 4 - Média aritmética
def calcula_media(M1,M2,M3):
  media = (M1+M2+M3)/3
  if 0 <= media <= 4:
    print(f"Aluno(a) reprovado(a)! Média de {media:.1f}")
  elif 4 < media <= 6:
    print(f"Média de {media:.1f} - pegou exame.")
    exame = float(input("Digite a nota no exame de recuperação (entre 0 e 10):"))
    if exame > 6:
      print(f"Aluno(a) aprovado(a)!")
    else:
      print(f"Aluno(a) reprovado(a)!")
  elif 6 < media < 10:
    print(f"Aluno(a) aprovado(a)!")
  else:
    print(f"Entrada(s) inválida(s)! Tente novamente com números positivos entre 0 e 10, usando ponto no lugar de vírgula.")

calcula_media(8, 9, 10)


# DESAFIO 5 - Contagem de letras e equipes
def contador(equipes):
  incidencias = []
  for item in equipes:
    contadorItem = 0
    for letra in item:
      if letra == 'a':
        contadorItem += 1
    incidencias.append(contadorItem)
    
  return incidencias

def distribuir(alunas, equipes):
  equipesFormadas = {}
  alunasOrd = sorted(alunas)
  i = 0
  equipe = equipes[i]
  for aluna in alunasOrd:
    if equipe not in equipesFormadas:
      equipesFormadas[equipe] = []
    equipesFormadas[equipe].append(aluna)
    if len(equipesFormadas[equipe]) >= 3:
      i += 1
      if i < len(equipes):
        equipe = equipes[i]
  return equipesFormadas
    
equipes = ['BerthaLutz', 'GraceHopper', 'JaquelineGoes', 'SarahGilbert']
alunas = ['Maria', 'Ana','Camila','Mariana','Elaine','Patricia','Marina','Erica','Larissa','Luiza', 'Nicole','Bruna']

print("Alunas do bootcamp:")
for aluna in alunas:
  print(aluna)

qtdLetraA = contador(equipes)
print(f"A quantidade de letras 'A' nas equipes, respectivamente, é {qtdLetraA}.")

equipesFormadas = distribuir(alunas, equipes)
print(f"As equipes ficaram: {equipesFormadas}")


# DESAFIO 6 - Conversão de temperatura / F = (9 * C + 160) / 5, F em Fahrenheit e C em Celsius
def conversor_temperatura(temperatura):
  fahrenheit = (9 * temperatura + 160) / 5
  return fahrenheit

try:
  temperatura = float(input("Digite a temperatura que deseja converter em Fahrenheit (formato X ou X.X): "))
  calcular = conversor_temperatura(temperatura)
  print(f"A temperatura de {temperatura} graus Celcius convertida, fica {calcular} em Fihrenheit.")
except:
  print("Entrada inválida, deve ser um número inteiro ou com ponto no lugar de vírgula.")
