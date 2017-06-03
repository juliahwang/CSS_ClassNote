
# coding: utf-8

# In[1]:

# 같은 코드인데 어떤 객체에 적용하느냐에 따라 결과가 달라지는 것.

# abstract_class : 객체를 만들 수 없는 클래스.
                 # 기본 클래스, 부모 클래스의 역할을 함. 
    # 게임에 그냥 캐릭터는 없다. 직업이나 특징이 있지만 현실과 너무 다르기 때문에


# In[9]:

from abc import * # abstract base class


class Character(metClass = ABCMeta):
    def __init__(self):
        self.hp = 100
        self.attack_power = 20
        
    def attack(self, other, attack_kind):
        other.get_damage(self.attack_power, attack_kind)
        
    @abstractmethod
    def get_damage(self, attack_power, attack_kind):
        pass
    
if __name__ == "__main__":
    ch1 = Character


# In[ ]:



