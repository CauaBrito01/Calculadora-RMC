import numpy as np

#Função auxiliar para verificar se a entrada do usuário é um número
def isNumber(n):
  try:
    float(n)
  except ValueError:
        return False
  return True

#Função para realizar a leitura de um coeficiente do usuário
def leituraCoeficiente(coeficiente):
    #Laço para leitura dos valores do coeficiente
    while True:
        valorCoeficiente = input("informe o valor de : {} :".format(coeficiente))

        #Verifica se o valor informado é numérico
        if isNumber(valorCoeficiente):
            return float(valorCoeficiente)
        
        #Caso não passe no if de verificação informa que o valor não é válido
        print("O valor informado deve ser numérico e não alphanumérico")

#Função para execução do menu de escolhas para matrizes
def menuMatrizes():
    while True:
        #Dados do menu
        print("Estas sao as opcoes de calculo disponiveis para matrizes:")
        print("1-Determinante.")
        print("2-Multiplicação.")
        print("3-Transposta.")
        print("4-Retornar ao menu anterior")
        
        #Leitura do valor do usuario
        opcao =  input("Qual opcao deseja utilizar?")

        #Verifica se a opcao é valida (numerica)
        if opcao.isnumeric():
            #Tranforma a escolha lida em string em inteiro
            opcao = int(opcao)
            #Verifica se é uma das opções
            if opcao <=4 and opcao >=1:
                #Retorna a opcao informada pelo usuario
                return opcao

        #Informa que a opção escolhida não é válida
        print("Opcao invalida, informe a opcao de acordo com o menu informado")

def coletaMatriz():
    numeroLinhas = int(leituraCoeficiente("Linhas"))
    numeroColunas = int(leituraCoeficiente("Colunas"))
    
    #Define a matriz e a coluna que será utilizada na estrutura de coleta
    auxMatriz = []
    linha = []
    #Estrutura de varredura para coletar os valores da matriz
    for i in range(0,numeroLinhas):
        for j in range(0,numeroColunas):
            linha.append(leituraCoeficiente("valor da posição {} x {}".format(i,j)))
        auxMatriz.append(linha)
        linha = []

    #Transforma a matriz em array de acordo com o numpy
    auxMatriz= np.array(auxMatriz)
    print("\n",auxMatriz,"\n")
    return auxMatriz

#Função que calcula o determinante da matriz
def calcularDeterminante(auxMatriz):

    if len(auxMatriz) == len(auxMatriz[0]):

        #Calcula o determinante com uso do numpy
        determinante = round(np.linalg.det(auxMatriz))

        #Imprime o determinate da matriz
        print("\n")
        print("O determinante da matriz é igual a {}".format(determinante))
        print("\n")
        #Retorna o determinante
        return determinante

    else:
        print("\n")
        print("A matriz não é quadrada, logo não podemos calcular o determinante")
        print("\n")

        #Retorna a funcao sem valor definido
        return

def calcularMultiplicacao(matrizA):
    while True:
        print("Informe os dados para a segunda matriz:")
        numeroLinhas = int(leituraCoeficiente("Linhas"))
        numeroColunas = int(leituraCoeficiente("Colunas"))

        if len(matrizA[0]) == numeroLinhas: 
            #Define a matriz e a coluna que será utilizada na estrutura de coleta
            matrizB = []
            linha = []
            #Estrutura de varredura para coletar os valores da matriz
            for i in range(0,numeroLinhas):
                for j in range(0,numeroColunas):
                    linha.append(leituraCoeficiente("valor da posição {} x {}".format(i,j)))
                matrizB.append(linha)
                linha = []

            matrizB = np.array(matrizB)
            z = matrizA.dot(matrizB)
            print('\nz =', z)

            return
        else: 
            print("\n")
            print("O número de colunas da primeira matriz não equivale ao número de linhas da segunda matriz") 
            print("\n")

def calcularTransposta(auxMatriz):

    print("\n")
    print("A matriz transposta de:")
    print("\n")
    print(auxMatriz)
    print("\n")
    print("É igual a:")
    print("\n")
    print(auxMatriz.T)


def matrizes():
    print("Informe a matriz que irá utilizar, com seu número de linhas, colunas e seus coeficientes")
    matriz = coletaMatriz()
    
    while True:

        #Chama a função que executa o menu
        opcao = menuMatrizes()

        #Se o usuário informou 1 
        if opcao == 1:
            calcularDeterminante(matriz)
        #Se o usuário informou 2
        elif opcao == 2:
            calcularMultiplicacao(matriz)
        #Se o usuário informou 3
        elif opcao == 3:
            calcularTransposta(matriz)

        elif opcao == 4:
            return

