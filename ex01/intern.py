#!/usr/bin/python3

class Intern:

    def __init__(self, name = "My name? I'm nobody, an intern, I have no name."):
        self.name = name
    
    def __str__(self):
        return self.name
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    
    def work(self):#2) o estagiario não trabalha, 
        raise Exception("I'm just an intern, I can't do that...")
        
    def make_coffee(self):
        return self.Coffee()
    

def the_office():
    estagiaria = Intern()
    estagiario = Intern("Mark")
    print(estagiario.name)
    print(estagiaria.name)
    xicara = estagiario.make_coffee()
    print(xicara)
    try: #1)vai tentar fazer o estagiario trabalhar (vai pro 2)
        estagiaria.work()
    except Exception as e: 
            print(e)

if __name__ == "__main__":
    the_office()

    a = Intern()
    c = Intern('Mark')
    print(c)