from director import Director
from concrete_pizza_builder import ConcretePizzaBuilder

def main():
    builder = ConcretePizzaBuilder()
    director = Director(builder)

    director.bake_pizza()
    print(builder.get_pizza())
    print(builder.get_price())

if __name__ == "__main__":
    main()