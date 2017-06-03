from person import Person

class Buyer(Person):
    def __init__(self, name, age, money, product):
        super().__init__(name, age, money, product)
        
    
    def buy(self, other, how_many):
        total = other.price * how_many
        
        if self.money >= total:
            self.money -= total
            other.money += total
            other.product = how_many
        
        else:
            print("돈이 모자란다.")
    
    
    def __str__(self):
        return '''
My name is {}
I am {} years old
I have {} won
I have {} products'''.format(self.name, self.age, self.money, self.product)
    
    
    
from retailer import Retailer
if __name__ == "__main__":
    b1 = Buyer("greg", 18, 10000, 0)
    r1 = Retailer("kim", 25, 2000, 20)
    print(b1)
    print(r1)
    b1.buy(r1, 3)
    print(b1)
    print(r1)