from .Rectangle import Rectangle
from .Circle import Circle
from .Square import Square

class ShapeFactory:

    def getShape(self, shape_input):
        if shape_input == 'Circle':
            return Circle()
        elif shape_input == 'Rectangle':
            return Rectangle()
        elif shape_input == 'Square':
            return Square()
        else:
            return None
    