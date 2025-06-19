class Computer:
    def __init__(self):
        self.__max_price = 900
    
    def sell(self):
        print(f"Selling at {self.__max_price}")
    
    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.sell()

c.set_max_price("1099")
c.sell()

# Actually changing it directly
c._Computer__max_price = 1149
c.sell()