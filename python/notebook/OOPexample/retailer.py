from person import Person

class Retailer(Person):
    # 클래스 멤버 : 객체들이 모두 공유하는 데이터
    price = 1000
    
    def __init__(self, name, age, money, product):
        super().__init__(name, age, money, product)
        
    def sell(self, other, how_many):
        total = self.price * how_many
        
        self.product -= how_many
        # 물건을 판만큼 빼준다. 
        other.product += how_many
        
        other.give_money(self, total) # 로 쓰는 게 좋다. 
        self.money += total
        # other.money -= total
        
    def __str__(self):
        return super().__str__() + '''
I am a retailer.
I have {} products'''.format(self.product)
    
    
# Test code - Person의 give_money 함수를 사용. 
if __name__ == "__main__":
    r1 = Retailer("yang", 20, 5000, 20)
    p1 = Person("kim", 14, 10000, 0)
    print(r1)
    print(p1)
    r1.sell(p1, 3)
    print(r1)
    print(p1)