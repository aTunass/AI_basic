class Pet: 
        #__init__ is an constructor in Python 
        def __init__(self, name, age):      
                self.name = name 
                self.age = age 
  
# Class Cat inheriting from the class Pet 
class Cat(Pet):          
        def __init__(self, name, age): 
                # calling the super-class function __init__  
                # using the super() function 
                super().__init__(name, age)  
  
def Main_baseclass(): 
        thePet = Pet("Pet", 1) 
        jess = Cat("Jess", 3) 
          
        # isinstance() function to check whether a class is  
        # inherited from another class 
        print("Is jess a cat? " +str(isinstance(jess, Cat))) 
        print("Is jess a pet? " +str(isinstance(jess, Pet))) 
        print("Is the pet a cat? "+str(isinstance(thePet, Cat))) 
        print("Is thePet a Pet? " +str(isinstance(thePet, Pet))) 
        print(jess.name) 
###################
# This program will reverse the string that is passed 
# to it from the main function 
class Reverse: 
    def __init__(self, data): 
        self.data = data 
        self.index = len(data)         
  
    def __iter__(self): 
        return self
      
    def __next__(self): 
        if self.index == 0: 
            raise StopIteration     
        self.index-= 1
        return self.data[self.index] 
  
def Main_iterator(): 
    rev = Reverse('Drapsicle') 
    for char in rev: 
        print(char) 
  
if __name__=='__main__': 
        Main_baseclass() 
        Main_iterator()
# def Reverse(data): 
#     # this is like counting from 100 to 1 by taking one(-1)  
#     # step backward. 
#     print(len(data))
#     for index in range(len(data)-1, -1, -1): #bien cuoi 0 thi phai dem toi -1
#         yield data[index] 
  
# def Main(): 
#     rev = Reverse('Harssh') 
#     for char in rev: 
#         print(char) 
#     data ='Harssh'
#     print(list(data[i] for i in range(len(data)-1, -1, -1))) 
  
# if __name__=="__main__": 
#     Main() 