import funcoes
import matriz

print('\033[35m')

def divisoria():
    print(20 * '=-=')


#Função para a execução do menu principal
def menuPrincipal():
    while True:
        #Dados do menu
        divisoria()
        print('Bem vindo a Calculadora RMC')
        divisoria()
        print("Estas sao as opcoes de calculo disponiveis neste calculadora:")
        print("1-Funcoes de segundo grau.")
        print("2-Funcoes exponenciais.")
        print("3-Matrizes.")
        print("4-Encerrar.")
        print("Digite o respectivo numero para realizar a escolha")
        #Leitura do valor do usuario
        divisoria()
        opcao =  input("Qual opcao deseja utilizar?")

        #Verifica se a opcao é valida (numerica)
        if opcao.isnumeric():
            #Tranforma a escolha lida em string em inteiro
            opcao = int(opcao)
            #Verifica se é uma das opções
            if opcao <=4 and opcao >=1:
                #Retorna a opcao informada pelo usuario
                return opcao

        #Informa que a opção não é válida
        print("Opcao invalida, informe a opcao de acordo com o menu informado")
    
print("Calculadora de RMC")
#Laço de execução principal da calculadora
while True:

    #Chama a função que realiza a leitura das opcoes do usuário
    opcao = menuPrincipal() 

    #Seleção de execução da calculadora de acordo com a opção do usuário
    #Se a opção for equação do segundo grau
    if opcao == 1:
        funcoes.funcaoSegundoGrau()

    #Se a opção for equação exponencial
    elif opcao == 2:
        funcoes.funcaoExponencial()
    
    #Se a opção for matrizes
    elif opcao == 3:
        matriz.matrizes()
    
    #Se a opção for parar
    elif opcao == 4:
        break
