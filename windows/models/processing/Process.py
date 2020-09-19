from models.req.Req import Req
from models.ssd_mobilenet.SsdMobileNet import SsdMobileNet

class Process:
    def __init__(self, path):
        self.mobilenet = SsdMobileNet(path)
    
    def run(self):
        objects = self.mobilenet.run()
        self.req = Req(objects)
        return self.req.req()
     
    def show(self):
        self.req.show()

