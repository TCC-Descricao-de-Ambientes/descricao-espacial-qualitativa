from models.req.Req import Req
from models.neural_network.NeuralNetwork import NeuralNetwork

class Process:
    def __init__(self, path):
        self.neural_network = NeuralNetwork(path)
    
    def run(self):
        objects = self.neural_network.run()
        self.req = Req(objects)
        return self.req.req()
     
    def show(self):
        self.req.show()

