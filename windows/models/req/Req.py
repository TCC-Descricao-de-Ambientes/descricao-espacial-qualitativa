import matplotlib

matplotlib.use("Qt5Agg")

import pylab as plt
import matplotlib.ticker as plticker

try:
    from PIL import Image
except ImportError:
    import Image


class Req:
    def __init__(self, objects, precision=60.0) -> None:
        self._image = Image.open(objects.path)
        self._width = objects.width
        self._height = objects.height
        self._precision = precision

        self._columns = 5
        self._rows = 3

        self._objects = self._filter_objects(objects, precision)
        self._process_image()

    def _process_image(self):
        dpi = 100

        self.fig = plt.figure(
            figsize=(float(self._width / dpi), float(self._height / dpi)), dpi=dpi
        )

        self.axes = self.fig.add_subplot(111)

        self.fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

        x_interval = self._width / self._columns
        y_interval = self._height / self._rows

        loc_x = plticker.MultipleLocator(base=x_interval)
        loc_y = plticker.MultipleLocator(base=y_interval)

        self.axes.xaxis.set_major_locator(loc_x)
        self.axes.yaxis.set_major_locator(loc_y)

        self.axes.grid(
            which="major", axis="both", linestyle="-", color="r", linewidth=5
        )
        self.axes.imshow(self._image)

    def req(self):
        output = []
        for obj in self._objects:
            self.draw_box(obj)

            x_desc = self._get_position(obj.x, "x")
            y_desc = self._get_position(obj.y, "y")

            message = f"Objeto {obj}: está {x_desc} e {y_desc}"
            output.append(message)

        return output

    def draw_box(self, obj):
        x_anchor = obj.box[1] * self._width
        y_anchor = obj.box[2] * self._height
        anchor = (x_anchor, y_anchor)

        rect_width = obj.width * self._width
        rect_height = (obj.height * self._height) * -1
        rect = plt.Rectangle(anchor, rect_width, rect_height, fill=False, lw=3)

        ax = self.fig.gca()
        ax.add_artist(rect)

    def _get_position(self, coord, axis):
        if axis == "x":
            direction = self._columns
            dimension = self._width

        elif axis == "y":
            direction = self._rows
            dimension = self._height
        else:
            return

        for i in range(1, direction + 1):
            if coord * dimension <= dimension * i / direction:
                return self.messages()[axis][i]

    def show(self):
        self.fig.show()

    @staticmethod
    def _filter_objects(detected_objects, desired_precision):
        valid_objects = []
        objects = detected_objects.objects

        for obj in objects:
            obj_precision = round(obj.score * 100, 3)
            if obj_precision >= desired_precision:
                valid_objects.append(obj)

        return valid_objects

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
