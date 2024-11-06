#Importando a biblioteca Math
import math

#Incluir a função de raiz quadrada
def raizQuadrada(a,b):
    #A função SQRT calcula a raiz quadrada
    raizA = math.sqrt(a)
    print(f"A raiz quadrada do número {a} é igual a {raizA:.2f}")
    raizB = math.sqrt(b)
    print(f"A raiz quadrada do número {b} é igual a {raizB:.2f}")

#Incluir a função de potência
def potencia(a,b):
    #Função POW do módulo MATH calcula a potencia de a e b
    print(f"A potencia de {a} elevado a {b} é igual a {math.pow(a,b)}")


#Função que soma dois números
def soma(a,b):
    print(f"A soma entre os números {a} e {b} é igual a {a+b}\n")

#Função que subtrai dois números
def subtracao(a,b):
    print(f"A subtração entre os números {a} e {b} é igual a {a-b}\n")
    
#Função que multiplica dois número
def multiplicacao(a,b):
    print(f"A Multiplicação entre os números {a} e {b} é igual {a*b}\n")

#Função que divide dois números
def divisao(a,b):
    #Verificação se o usuário tentou dividir por 0
    if(b==0):
        print("Não é possivel dividir por 0\n")
    else:
        print(f"A divisão entre os números {a} e {b} é igual {a/b}\n")

#Criando a variavel de verificação do While
sair = 0

print("Seja Bem Vindo ao Sistema Senai Plus\n")

#Criando o bloco While para sair digite -1
while(sair >= 0):
    #Pedindo as informações ao usuário
    try:
        n1 = float(input("Digite o primeiro número\n"))
        n2 = float(input("Digite o segundo número\n"))
        escolha = int(input("O que você deseja fazer ? \n [1] SOMA \n [2] SUBTRAÇÃO \n [3] MULTIPLICAÇÃO \n [4] DIVISÃO \n [5] Raiz Quadrada \n [6] Potência \n [-1] SAIR \n" ))
    except value
    #Verificando qual foi a escolha do usuário
    if(escolha==1):
        soma(n1,n2)
    elif(escolha==2):
        subtracao(n1,n2)
    elif(escolha==3):
        multiplicacao(n1,n2)
    elif(escolha==4):
        divisao(n1,n2)
    elif(escolha == 5):
        raizQuadrada(n1,n2)
    elif (escolha == 6):
        potencia(n1,n2)
    elif (escolha == -1):
        sair = -1
        print("Obrigado por utilizar o nosso sistema, até mais !!!")
        break
    else:
        print("Por Favor, Digite uma opção válida !!! \n")
    sair = (int(input("Posso ajudar em algo mais ? \n \n [0] SIM [-1] NÃO\n")))
    
    if(sair ==-1):
         print("Obrigado por utilizar o nosso sistema, até mais !!!")