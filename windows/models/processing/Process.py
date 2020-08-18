from models.gui.exc.FileNotSelected import FileNotSelected
from models.req.Req import Req

class Process:
    def run(self, a):
        print(f"Processando {a}...")
        req = Req(a)
        x, y = req.random_circle()
        req.req(x, y)
