from doctest import OutputChecker
import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed()
        self.synaptic_weights= 2*np.random.random((3,1))-1
    
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    
    def sigmoid_derivative(self,x):
        return x*(1-x)
    
    def train(self, training_inputs,training_outputs, training_iterations):
        for iteration in range(training_iterations):
            output= self.think(training_inputs)
            error= training_outputs-output
            adjustments= np.dot(training_inputs.T, error*self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments
    
    def think (self, inputs):
        inputs = inputs.astype(float)
        output= self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

if __name__== "__main__":
    #initializing the neuron class
    neural_network = NeuralNetwork()
    print("Beginning Randomly generated Weights: ")
    print(neural_network.synaptic_weights)
    #training data consisting  of 4 examples --3 input values and 1 output

    #training inputs
    training_inputs= np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    #training outputs
    training_outputs= np.array([[0,0,1,0]]).T

    neural_network.train(training_inputs, training_outputs, 15000)
    print("Ending Weighs After Training: ")
    print(neural_network.synaptic_weights)
    user_input_one= str(input("User Input One: "))
    user_input_two= str(input("User Input two: "))
    user_input_three= str(input("User Input three: "))
    print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
    print("New Output data: ")
    print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))