
# coding: utf-8

# In[3]:

'''
1. 상인(리테일러)와 소비자(바이어)만 존재하는 세상 구현
   그냥 사람은 없다 => person 객체를 못만들도록.

2. 공통 특성만 뽑아서 person에 
   A retailer is a person === ok
   A buyer is a person === ok

3. if __name__ = "__main__": 의 개념

'''

# 공통 속성을 뽑아서 부모 클래스
class Person:
    def __init__(self, name, age, money, product):
        self.name = name
        self.age = age
        self.money = money
        self.product = product
        
    def give_money(self, other, how_much):
        if self.money >= how_much:
            self.money -= how_much
            other.money += how_much
        else:
            print("나 돈없어서 못사")
            
    def __str__(self):
        return '''
My name is {}
I am {} years old
I have {} won'''.format(self.name, self.age, self.money)
    
# test code
if __name__ == "__main__":
    # 메인파일(__main__)이라면 아래 코드를 실행하라. 따라서 retailer.py에서 실행됨. 
    p1 = Person("greg", 18, 5000)
    p2 = Person("kim", 22, 1000)
    print(p1)
    print(p2)
    p1.give_money(p2, 2000)
    print(p1)
    print(p2)


# In[ ]:



