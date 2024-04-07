from Factory.ShapeFactory import ShapeFactory

def main():
    shapeFactory = ShapeFactory()
    shape = shapeFactory.getShape('Circle')
    shape.draw()

if __name__ == '__main__':
    main()