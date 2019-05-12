import numpy as np


##Shape e me entrada 728, 28
class Redes_Neuronales(object):

    ##Se define un constructor en donde se decinira el tamaño de la neurona 
    def __init__(self, size_layers):
        self.number_layers = len(size_layers)
        self.size_layers = size_layers
        self.bias = [np.random.randn(y, 1) for y in size_layers[1:]]
        self.peso = [np.random.randn(y, x) 
                    for x, y in zip(size_layers[:-1], size_layers[1:])]

    def sigmoide(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoide_derivada(self, x):
        return self.sigmoide(x) * (1 - self.sigmoide(x))

    ##x: la entrada 
    def feedforward(self, x):   
        a1 = x.transponse((0,1))
        a1 = np.vstack((1,x))
        z1 = np.matmul(self.peso[0], a1)
        z1 = z1.transpose((0,1))
        a2 = self.sigmoide(z1)
        a2 = np.vstack((1, a2))
        z2 = np.matmul((self.peso[1], a2))
        z2 = z2.transpose((0,1))
        hipotesis = self.sigmoide(z2)
        return a1, a2, z1, z2, hipotesis
    
    
     ##Costo de la derivada
     ##Nos indica cual es el error de nuestro costo 
     ##Prediction: es nuestro sigmoide de nuestra funcion
    def cost_derivative(self, prediction, y):
        return prediction - y
    
    ##Descenso del gradiente
    ##x = nuestro input
    ##y = cual es el resultado 
    def DGradient(self, x, y, alpha = 0.01,  max_iter = 10000):
        i = 0
        current_cost = 100000 
        while (i < max_iter):
            cost, gradient = self.backProp(x,y, theta_0)
            print(gradient)
            self.peso[0] -= alpha* gradient[0]
            self.peso[1] -= alpha* gradient[1]
            i += 1
        return self.peso
            

    ##Back propagation

    def backProp(self, x, y, theta):
        pass

#        biases = [np.zeros(b.shape) for b in self.bias]
#        weight = [np.zeros(w.shape) for w in self.peso]
#        activation = x
#        activations = [x] 
#        zs = [] 
#        for b, w in zip(self.bias, self.peso):
#            z = np.dot(w, activation)+b
#            zs.append(z)
#            activation = self.sigmoide(z)
#            activations.append(activation)
#
#        delta = self.cost_derivative(activations[-1], y) * \
#            self.sigmoide_derivada(zs[-1])
#        biases[-1] = delta
#        weight[-1] = np.dot(delta, activations[-2].transpose())
#
#            z = zs[-l]
#            sp = self.sigmoide_derivada(z)
#            delta = np.dot(self.oesi[-l+1].transpose(), delta) * sp
#            biases[-l] = delta
#            weigths[-l] = np.dot(delta, activations[-l-1].transpose())
#        return biases, weights


    ##Crea la prediccion 
    def evaluate(self, data):
        h = self.feedForward(data)
        return h


