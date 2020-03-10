''' video aula sobre como implementar um sistema para aprender a ler escritas manuais e interpretar como numeros
    usando tensorflow
'''
import tensorflow as tf 
mnist= tf.keras.datasets.mnist # 28x28 imagens de numeros escritos 0 a 9
(x_train, y_train), (x_test, y_test) =mnist.load_data()

x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1
)