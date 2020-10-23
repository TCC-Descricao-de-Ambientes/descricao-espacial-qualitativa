from models.req.Req import Req
from models.object_detection.ObjectDetection import ObjectDetection

class Process:
    def __init__(self, path):
        self.object_detection = ObjectDetection(path)
    
    def run(self):
        objects = self.object_detection.run()
        self.req = Req(objects)
        return self.req.req()
     
    def show(self):
        self.req.show()

