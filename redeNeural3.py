import numpy as np

class RedeNeural():
    
    def __init__(self):
        #seed do numpy para numeros aleatorios, caso um
        np.random.seed(1)

        # criando os valores das sinapses em uma matriz 3,1
        # os valores vão de -1 ate 1 
        self.peso_sinapse = 2 * np.random.random((4, 2)) - 1
        # print(len(self.train.treino_entrada[0]))

    def sigmoid(self, x):
        """ pega os valores das somas do input e normaliza esses valores atraves de uma sigmoid
            ou seja os valores das somas dos inputs estarão entre 0 e 1 """
        return 1 / (1 + np.exp(-x))

    def derivada_sigmoid(self, x):
        """ 
        A derivação da sigmoid para calcular o ajuste dos erros """
        return x * (1 - x)

    def train(self, treino_entrada, treino_saida, treino_iteracao):
        """
        treinamos o modelo atraves de tentativa e erro, ajustando o peso das sinapses para resultados melhores
        """
        #   print(len(treino_entrada[0]))
     
        # l2=len(self.treino_entrada[0])
        for iteracao in range(treino_iteracao):
            # passa o processo de treinamento na redeneural 
            output = self.pensamento(treino_entrada)

            # Calcula o erro do processo
            error = treino_saida - output

            # Multiplica o erro do input e os gradientes da função sigmoid com objetivo de ajustar o erro
            adjustments = np.dot(treino_entrada.T, error * self.derivada_sigmoid(output))

            # ajusta o peso das sinapses
            self.peso_sinapse += adjustments

    def pensamento(self, inputs):
        """
        Passa as entradas atraves da rede neural para oder fazer as analises
        """
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.peso_sinapse))
        return output


if __name__ == "__main__":

    # inicializa a rede neural
    neural_network = RedeNeural()

    print("Inicio aleatorio dos pesos das sinapses")
    print(neural_network.peso_sinapse)

    # o treino consiste de q exemplos  com com quatro entradas de entrada e uma de saida,
    # cada exemplo é constituido de 4 valores, 
    treino_entrada = np.array([[0,0,1,1],
                                [1,1,1,0],
                                [1,0,1,0],
                                [0,1,1,10]])

    # treino_saida = np.array([[0,1,1,0],[0,0,1,1]).T
    treinosaida = np.array([    [0,1],
                                [1,0],
                                [0,0],
                                [1,1]])


    # Train the neural network
    neural_network.train(treino_entrada, treinosaida, 10000000)

    print("Valores das Sinapses apos o treino: ")
    print(neural_network.peso_sinapse)

    A = str(input("Entrada 1: "))
    B = str(input("Entrada 2: "))
    C = str(input("Entrada 3: "))
    D = str(input("Entrada 4: "))
    # A=1
    # B=1
    # C=0
    # D=0

    print("Novos eventos = ", A, B, C,D)
    print("Saida e avisos: ")
    print(neural_network.pensamento(np.array([A, B, C, D])).T )
   