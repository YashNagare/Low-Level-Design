from Pizzas.Margherita import Margherita
from Toppings.ExtraCheese import ExtraCheese
from Toppings.ExtraMushroom import ExtraMushroom


base_pizza = ExtraCheese(Margherita())
print(base_pizza.cost())

base_pizza = ExtraMushroom(ExtraCheese(Margherita()))
print(base_pizza.cost())