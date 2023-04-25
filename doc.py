#Primeiros exercícios de treinamento da fábrica de software resolvidos por Rafaella Veiga

# 1. Somar números
num1 = float (input ("Insira aqui o primeiro número: "))
num2 = float (input ("Insira aqui o segundo número: ")) 
soma = num1 + num2
print ("A soma equivale a: ",soma)

#2. Calcular a média de 3 notas
num1 = float (input ("Insira aqui o primeiro número: "))
num2 = float (input ("Insira aqui o segundo número: ")) 
num3 = float (input ("Insira aqui o terceiro número: ")) 
media = (num1+num2+num3) /3
print ("A media equivale a: ",media)

#3. Sortear um aluno entre 3
import random
aluno1 = str (input("Insira nome do aluno: "))
aluno2 = str (input ("Insira nome de outro aluno: "))
aluno3 = str (input ("Insira nome de outro aluno: "))
lista =[aluno1,aluno2,aluno3]
sorteio = random.choice(lista)
print('aluno sorteado: ',sorteio ) 

#4. Número ímpar ou par 
num = int (input ("Insira aqui o número: "))
sobra = num %2
if sobra == 0:
    print ("O número é par.")
else:  
    print ("O número é ímpar.")
    
#Calcular preço da passagem cobrando R$ 1,50 por viagens até 200km e R$1,25 para mais longas.

km = float (input("Insira a quilometragem: "))
if km >=200: 
    print ("O valor da pssagem será:", km * 1.50)
else: 
    print ("O valor da pssagem será:", km * 1.25)
