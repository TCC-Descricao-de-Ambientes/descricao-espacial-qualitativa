
from PIL import Image


class Visualizer:
    def __init__(self, path) -> None:
        self.img = Image.open(path)
        
    def show(self):
        self.img.show()