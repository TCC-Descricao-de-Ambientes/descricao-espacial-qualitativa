from models.req.Req import Req
from models.ssd_mobilenet.SsdMobileNet import SsdMobileNet

class Process:
    def __init__(self, path):
        self.mobilenet = SsdMobileNet(path)
    
    def run(self):
        objects = self.mobilenet.run()
        return ("X", "Y")
        # TODO: Integração do REQ
        # return Req(objects).req()
    
    # TODO: Integração do REQ   
    def show(self):
        # self._r.show()
        pass
