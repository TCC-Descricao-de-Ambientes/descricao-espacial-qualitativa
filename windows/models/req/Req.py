import matplotlib

matplotlib.use("Qt5Agg")

import pylab as plt
import matplotlib.ticker as plticker
from cv2 import cv2
import random

try:
    from PIL import Image
except ImportError:
    import Image


class Req:
    def __init__(self, image_path) -> None:
        self.image_path = image_path
        self.width = 1280
        self.height = 720
        self.dpi = 100.0
        self.columns = 5
        self.rows = 3

        self.open_image()
        self.dimensions()
        self.process_image()

    def open_image(self):
        self.image = Image.open(self.image_path)
        self.image.resize(((round(self.width)), round(self.height)), Image.ANTIALIAS)

    def dimensions(self):
        img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
        self.original_height = img.shape[0]
        self.original_width = img.shape[1]

    def process_image(self):

        self.fig = plt.figure(
            figsize=(
                float(self.image.size[0] / self.dpi),
                float(self.image.size[1] / self.dpi),
            ),
            dpi=self.dpi,
        )

        self.axes = self.fig.add_subplot(111)

        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

        x_interval = self.original_width / self.columns
        y_interval = self.original_height / self.rows

        loc_x = plticker.MultipleLocator(base=x_interval)
        loc_y = plticker.MultipleLocator(base=y_interval)

        self.axes.xaxis.set_major_locator(loc_x)
        self.axes.yaxis.set_major_locator(loc_y)

        self.axes.grid(
            which="major", axis="both", linestyle="-", color="r", linewidth=5
        )
        self.axes.imshow(self.image)

    def random_circle(self):
        x = random.randint(0, self.original_width)
        y = random.randint(0, self.original_height)

        circle = plt.Circle((x, y), 3, color="r")
        ax = self.fig.gca()
        ax.add_artist(circle)

        return x, y

    def req(self):
        x, y = self.random_circle()

        for i in range(1, self.columns + 1):
            if x <= self.image.size[0] * i / self.columns:
                x_position = self.messages()["x"][i]
                break

        for i in range(1, self.rows + 1):
            if y <= self.image.size[1] * i / self.rows:
                y_position = self.messages()["y"][i]
                break

        return (x_position, y_position)

    def show(self):
        self.fig.show()

    @staticmethod
    def messages():
        return {
            "x": {
                1: "muito a esquerda",
                2: "na esquerda",
                3: "no centro",
                4: "na direita",
                5: "muito a direita",
            },
            "y": {1: "em cima", 2: "no centro", 3: "embaixo"},
        }
