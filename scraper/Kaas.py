class Kaas(object):
    # Initializer / Instance Attributes
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price