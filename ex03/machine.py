import beverages as b
import random

class CoffeeMachine:
    def __init__(self, qtt=0, broken=False):
        self.qtt = qtt
        self.broken = broken
        
    def repair(self):
        if self.broken == True:
            self.broken = False
            self.qtt = 0

    class EmptyCup(b.HotBeverage):
        def __init__(self):
            super().__init__(name="empty cup", price=0.90)

        def description(self):
            return "An empty cup?! Gimme my money back!"

    def serve(self, pedido):
        if self.qtt < 10:
            self.qtt += 1
            return random.choice([pedido(), self.EmptyCup()])
        else:
            self.broken = True
            raise self.BrokenMachineException()

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            self.message = message
            super().__init__(message)


if __name__ == '__main__':
    drinks = (b.Coffee, b.Cappuccino, b.Chocolate, b.HotBeverage)
    instance_machine = CoffeeMachine()

    attempts = 0

    # começando pela primeira tentativa
    while attempts < 22:
        if instance_machine.broken == False:
             # tente:
            try:
                # enquanto o status da máquina for True...
                print(instance_machine.serve(random.choice(drinks)))
            except Exception as e:
                print(instance_machine.BrokenMachineException())
                instance_machine.repair()
            print(attempts)
            attempts += 1
