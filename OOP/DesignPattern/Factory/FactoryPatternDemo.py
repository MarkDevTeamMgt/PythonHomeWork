

class Shape:

    def draw(self):
        pass


class Rectangle(Shape):

    def draw(self):
        print 'This is a rectangle'


class Square(Shape):

    def draw(self):
        print 'This is a square'


class Circle(Shape):

    def draw(self):
        print 'This is a circle'


class ShapeFactory:

    @classmethod
    def getShape(cls,shapeType):
        if shapeType is None:
            return None
        elif shapeType == 'CIRCLE':
            return  Circle()
        elif shapeType == 'RECTANGLE':
            return  Rectangle()
        elif shapeType == 'SQUARE':
            return Square()


if __name__ == '__main__':
    shapeFactory = ShapeFactory()
    shape1 = shapeFactory.getShape("CIRCLE")
    shape2 = shapeFactory.getShape("RECTANGLE")
    shape3 = shapeFactory.getShape("SQUARE")

    shape1.draw()
    shape2.draw()
    shape3.draw()

