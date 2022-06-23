import graficos

#Função auxiliar para verificar se a entrada do usuário é um número
def isNumber(n):
  try:
    float(n)
  except ValueError:
        return False
  return True

#Função para execução do menu de escolhas para funções de segundo grau
def menuFuncaoSegundoGrau():
    while True:
        print('\033[34m')
        #Dados do menu
        print("Estas sao as opcoes de calculo disponiveis para funções do segundo grau:")
        print("1-Raízes da função.")
        print("2-𝑓(𝑥) para um x qualquer.")
        print("3-Vértice da função.")
        print("4-Gerar um gráfico da função.")
        print("5-Retornar ao menu anterior")

        #Leitura do valor do usuario
        opcao =  input("Qual opcao deseja utilizar?")

        #Verifica se a opcao é valida (numerica)
        if opcao.isnumeric():
            #Tranforma a escolha lida em string em inteiro
            opcao = int(opcao)
            #Verifica se é uma das opções
            if opcao <=5 and opcao >=1:
                #Retorna a opcao informada pelo usuario
                return opcao

        print("Opcao invalida, informe a opcao de acordo com o menu informado")

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

def calcularDelta(coeficienteA,coeficienteB,coeficienteC):
    #Determina o delta da função
    delta = (coeficienteB**2 - 4*coeficienteA*coeficienteC)
    return delta

#Função para calcular as raízes da função            
def calcularRaizes(coeficienteA,coeficienteB,coeficienteC):
    
    #Determina o delta da função
    delta = calcularDelta(coeficienteA,coeficienteB,coeficienteC)

    #Se ele for negativo
    if delta < 0:
        #Determina i e j e realiza um complexo destes dois para a raiz x1
        i = -coeficienteB/(2*coeficienteA)
        j = abs(delta)**(1/2)/(2*coeficienteA)
        x1 = complex(i,j)

        #Determina i e j e realiza um complexo destes dois para a raiz x2
        i = -coeficienteB/(2*coeficienteA)
        j = -abs(delta)**(1/2)/(2*coeficienteA)
        x2 = complex(i,j)

        #Imprime as raízes
        print("As raízes desta função são:")
        print("X1 = {}".format(x1))
        print("X2 = {}".format(x2))

    #Se ele for positivo
    else:
        #Determina as raízes x1 e x2
        x1 = (-coeficienteB + delta**(1/2)) / (2*coeficienteA)
        x2 = (-coeficienteB - delta**(1/2)) / (2*coeficienteA)

        #Imprime as raízes
        print("As raízes desta função são:")
        print("X1 = {}".format(x1))
        print("X2 = {}".format(x2))

    return

#Função para cálcular o vértice da função
def calcularVertice(coeficienteA,coeficienteB,coeficienteC):
    #Determina o delta da função
    delta = calcularDelta(coeficienteA,coeficienteB,coeficienteC)

    #Determina x e y do vértice
    xV = -coeficienteB/(2*coeficienteA)
    yV = -delta/(4*coeficienteA)

    #Imprime x e y do vértice
    print("O vértice se encontra em :")
    print("xV = {}".format(xV))
    print("yV = {}".format(yV))

    if coeficienteA >0 :
        print("O ponto do vertice é de minimo")

    else:
        print("O ponto do vertice é de maximo")

    return

#Função que calcula o valor de f(X) para o X informado
def calcularXSegundoGrau(coeficienteA,coeficienteB,coeficienteC):

    while True:
        valorX = input("Informe o valor de X que deseja utilizar para calcular:")
        
        #Verifica se o valor informado é numérico
        if isNumber(valorX):
            valorX = float(valorX)
            #Determina o valor de y para o x
            y = coeficienteA * valorX **2 + coeficienteB * valorX + coeficienteC
            
            #imprime o valor calculado para a função
            print("O valor de  𝑓(𝑥) = {}𝑥2 + {}𝑥 + {}, sendo x = {} é {}.".format(coeficienteA,coeficienteB,coeficienteC,valorX,y))
            return 
        
        print("O valor informado deve ser numérico e não alphanumérico")

#Função para gerar o grafico da equação de segundo grau
def gerarGraficoSegundoGrau (coeficienteA,coeficienteB,coeficienteC):

    #Solicita ao usu[ario o inicio e fim do dominio, assim como seu incremento
    print("Informe o inicio,fim e incremento para determinar o  do domínio da função:")
    inicioDominio = leituraCoeficiente("inicio")
    finDominio = leituraCoeficiente("fim")
    incrementoDominio = leituraCoeficiente("incremento")

    #Define X como o valor de inicio do dominio
    x = inicioDominio
    #Cria eixo X e Y
    eixoX = []
    eixoY = []

    #Laço para criar o eixo do domínio
    while x <= finDominio:
        eixoX.append(x)
        x +=incrementoDominio

    #Para cada valor do eixo X 
    for x in eixoX:
        #Calcula o valor de Y
        y = coeficienteA * x **2 + coeficienteB * x + coeficienteC
        eixoY.append(y)

    #Manda plotar com os dados gerados
    graficos.plotar(eixoX,eixoY)

#Função pai para calculo de uma função de segundo grau de acordo com a calculadora   
def funcaoSegundoGrau():
    
    print("A função de segundo grau é dada na forma de 𝑓(𝑥) = 𝑎𝑥2 + 𝑏𝑥 + c")
    print("Informe os valores de a-b-c para a função que deseja utilizar:")
    coeficienteA = leituraCoeficiente("a")
    coeficienteB = leituraCoeficiente("b")
    coeficienteC = leituraCoeficiente("c")

    #Laço de execução da função de segundo grau
    while True:

        #Le a opção de operação do usuário
        opcao = menuFuncaoSegundoGrau()

        #Se o usuário informou 1 
        if opcao == 1:
            calcularRaizes(coeficienteA,coeficienteB,coeficienteC)
        #Se o usuário informou 2
        elif opcao == 2:
            calcularXSegundoGrau(coeficienteA,coeficienteB,coeficienteC)
        #Se o usuário informou 3
        elif opcao == 3:
            calcularVertice(coeficienteA,coeficienteB,coeficienteC)
        #Se o usuário informou 4
        elif opcao == 4:
            gerarGraficoSegundoGrau(coeficienteA,coeficienteB,coeficienteC)
        elif opcao == 5:
            break

#Função para execução do menu de escolhas para funções exponenciais
def menuFuncaoExponencial():
    while True:
        #Dados do menu
        print("Estas sao as opcoes de calculo disponiveis para funções exponenciais:")
        print("1-Verificar se é crescente ou decrescente.")
        print("2-𝑓(𝑥) para um x qualquer.")
        print("3-Gerar um gráfico da função.")
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

        print("Opcao invalida, informe a opcao de acordo com o menu informado")

#Função que verifica se a funçãoe exponencial é crescente e decrescente
def verificarCrescenteDescrescente(coeficienteA):
    #Verifica se a função é maior que 0 
    if coeficienteA > 0 :
        print("A função é crescente")
    #Se é menor
    else:
        print("A função é decrescente")
    return

#Função que calcula o valor de f(X) para o X informado
def calcularXExponencial(coeficienteA,coeficienteB):

    while True:
        valorX = input("Informe o valor de X que deseja utilizar para calcular:")
        
        #Verifica se o valor informado é numérico
        if isNumber(valorX):
            valorX = float(valorX)
            #Determina o valor de y para o x
            y = coeficienteA * coeficienteB ** valorX
            
            #imprime o valor calculado para a função
            print("O valor de 𝒇(𝒙) = {}*{}^x sendo x = {} é {}.".format(coeficienteA,coeficienteB,valorX,y))
            return 
        
        print("O valor informado deve ser numérico e não alphanumérico")

#Função para gerar o grafico da equação de segundo grau
def gerarGraficoExponencial (coeficienteA,coeficienteB):

    #Solicita ao usu[ario o inicio e fim do dominio, assim como seu incremento
    print("Informe o inicio,fim e incremento para determinar o  do domínio da função:")
    inicioDominio = leituraCoeficiente("inicio")
    finDominio = leituraCoeficiente("fim")
    incrementoDominio = leituraCoeficiente("incremento")

    #Define X como o valor de inicio do dominio
    x = inicioDominio
    #Cria eixo X e Y
    eixoX = []
    eixoY = []

    #Laço para criar o eixo do domínio
    while x <= finDominio:
        eixoX.append(x)
        x +=incrementoDominio

    #Para cada valor do eixo X 
    for x in eixoX:
        #Calcula o valor de Y
        y = coeficienteA * coeficienteB ** x
        eixoY.append(y)

    #Manda plotar com os dados gerados
    graficos.plotar(eixoX,eixoY)

#Função pai para calculo de uma função de segundo grau de acordo com a calculadora   
def funcaoExponencial():
    
    print("A função de segundo grau é dada na forma de 𝒇(𝒙) = 𝒂𝒃^x")
    print("Informe os valores de a-b para a função que deseja utilizar:")
    coeficienteA = leituraCoeficiente("a")
    coeficienteB = leituraCoeficiente("b")

    #Laço de execução da função de segundo grau
    while True:

        #Le a opção de operação do usuário
        opcao = menuFuncaoExponencial()

        #Se o usuário informou 1 
        if opcao == 1:
            verificarCrescenteDescrescente(coeficienteA)
        #Se o usuário informou 2
        elif opcao == 2:
            calcularXExponencial(coeficienteA,coeficienteB)
        #Se o usuário informou 3
        elif opcao == 3:
            gerarGraficoExponencial(coeficienteA,coeficienteB)
        elif opcao == 4:
            break

