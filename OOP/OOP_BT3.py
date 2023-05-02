class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []
    def show(self):
        print(self.__stack)
    def isEmpty(self):
        if (len(self.__stack)==0):
            return True
        else: return False
    def isFull(self):
        if (len(self.__stack)>=self.__capacity):
            return True
        else: return False
    def push(self, val):
        if isinstance(val, list):
            for i in range(len(val)):
                if self.isFull():
                    print("It's fulled")
                    break
                self.__stack.append(val[i])
        else: 
            if self.isFull():
                    print("It's fulled")
            else: self.__stack.append(val)
    def pop(self):
        if self.isEmpty():
            print("There's no top elements")
        else: self.__stack.pop()
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return 
        return self.__stack[-1]
test = MyStack(10)
test.push([1,2,3,4,6,7,8])
test.push([5])
print(test.isEmpty())
print(test.isFull())
test.pop()
print(test.top())
test.show()
    