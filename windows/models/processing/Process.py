from models.req.Req import Req

class Process:
    def __init__(self, path):
        self._r = Req(path)
    
    def run(self):
        return self._r.req()
    
    def show(self):
        self._r.show()
