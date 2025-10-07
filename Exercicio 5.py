#Exercicio 5

Nome = input("Nome: ")
gender = input("insire genero (M) (F) :")
while gender not in ("M", "F", "m", "f"):
    print("genero invalido, tente de novo")
    gender = input("insire genero (M) (F) :")
altura = int(input("insira sua altura em cm : "))
if gender == "M" or gender == "m" :
    if altura <= 174 : tamanho = "Baixo"
    else : tamanho = "Alto"
if gender == "F" or gender == "f":
    if altura <= 164 : tamanho = "Baixa"
    else : tamanho = "Alta"
if gender == "M" or gender == "m" :
    print ("O ", Nome, " é ", tamanho)
if gender == "F" or gender == "f":
    print ("A ", Nome, " é ", tamanho)
