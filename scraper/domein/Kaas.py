class Kaas(object):
    # Initializer / Instance Attributes
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __init__(self,name,price,pricePerKilo):
        self.name = name
        self.price = price
        self.pricePerKilo=pricePerKilo

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price