class Stack(list):
    """list의 내장함수 append 자체를 push에 할당."""
    push = list.append
    # pop = list.pop
    """
    def push(self, data):
        super().append(data)
    """    
        
    def empty(self):
        """객체가 존재하지 않으면 True 반환"""
        if not self:
            return True
        else:
            return False
        
    def peek(self):
        """가장 마지막에 들어온 값을 출력"""
        return self[-1]
    

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    
    while not s.empty():
        data = s.pop()
        print(data, end='  ')