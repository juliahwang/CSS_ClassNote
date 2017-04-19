class Stack(list):
    push = list.append       # 함수자체를 멤버변수로 받았음. 따라서 ()안붙임

# list는 이미 .pop를 내장함수로 지니고 있다. 
# push 랑 pop 선언은 이미 끝남. 

    def is_empty(self):
        if not len(self):    # if len(self) == 0: 와 같음
            return True
        else: 
            return False
    
    def peek(self):
        return self[-1]      # 맨 윗값 살펴보기


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    
    while not s.is_empty(): # 비지 않았으면 계속 실행, 비었으면 break
        data = s.pop()
        print(data, end="  ")