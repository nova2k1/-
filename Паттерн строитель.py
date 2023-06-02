class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.salami = False

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.salami:
            toppings.append("salami")
        return f"Size: {self.size}, Toppings: {', '.join(toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_salami(self):
        self.pizza.salami = True
        return self

    def build(self):
        return self.pizza


# Использование строителя для создания объекта с определенными свойствами
pizza_builder = PizzaBuilder()
pizza = pizza_builder.set_size("large").add_cheese().add_pepperoni().build()
print(pizza)  # Выводит "Size: large, Toppings: cheese