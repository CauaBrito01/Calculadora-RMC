import matplotlib.pyplot as plt

#Função para plotar o grafico com base nas listas de dados informadas
def plotar(eixoX,eixoY):

    #Plota os dados informados
    plt.plot( eixoX, eixoY)

    #Determina os limites do plot
    # plt.axis([eixoX[0], eixoX[len(eixoX)-1], eixoY[0], eixoY[len(eixoY)-1]])
    
    #Título do Gráfico
    plt.title("Grafico da função")
    #Gera o grid
    plt.grid(True)
    #Nomeia os rótulos do graficos
    plt.xlabel("X")
    plt.ylabel("Y")
    #Ilustra o grafico
    plt.show()
