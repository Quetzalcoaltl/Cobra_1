import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(x))

def sigmoid_derivation(x):
    return x * (1-x)

'''TI= np.array([    [0,0,1,1],
                [1,1,1,1],
                [1,0,1,1],
                [0,1,1,1]])
'''
TI= np.array([  [0,0,1],
                [1,1,1],
                [1,0,1],
                [0,1,1]])
# print(TI)
# TO=np.arra([[0,1,1,0,1]])
TO=np.array([[0,1,1,0]]).T
np.random.seed(1)
peso_sinapse=2*np.random.random((3,1))-1
print("Pesos aleatorias das sinapses: ")
print(peso_sinapse)
