class Shape:
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class ShapeFactory:
    def create_rectangle(self):
        return Rectangle()

    def create_circle(self):
        return Circle()


class ShapeClient:
    def __init__(self, factory):
        self.factory = factory

    def draw_shapes(self):
        rectangle = self.factory.create_rectangle()
        rectangle.draw()

        circle = self.factory.create_circle()
        circle.draw()


# Использование абстрактной фабрики для создания объектов
shape_factory = ShapeFactory()
client = ShapeClient(shape_factory)
client.draw_shapes()  # Выводит "Drawing a rectangle" и "Drawing a circle"