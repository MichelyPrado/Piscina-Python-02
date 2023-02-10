class HotBeverage:

    def __init__(self, name="HotBeverage", price=0.30):
        self.name = name
        self.price = price
    
    def __str__(self):
        return "name : " + self.name + "\nprice : " +format(self.price, '.2f') + "\ndescription : " + self.description()
    
    def description(self):
        return "Just some hot water in a cup."

class Coffee(HotBeverage):
    
    #super() - retorna uma instância da classe pai
    # a partir da instância eu chamo o construtor
    def __init__(self):
        super().__init__(name="coffee", price=0.40)
    
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    
    def __init__(self):
        super().__init__(name="tea")

class Chocolate(HotBeverage):
    
    def __init__(self):
        super().__init__(name="chocolate", price=0.50)
    
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    
    def __init__(self):
        super().__init__(name="cappuccino", price=0.45)
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"

if __name__ == '__main__':
    
    instance_hot = HotBeverage()
    print(instance_hot, "\n")

    instance_coffee = Coffee()
    print(instance_coffee, "\n")

    instance_tea = Tea()
    print(instance_tea, "\n")

    instance_chocolate = Chocolate()
    print(instance_chocolate, "\n")

    instance_cappuccino = Cappuccino()
    print(instance_cappuccino)

