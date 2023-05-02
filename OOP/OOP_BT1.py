# class Manufacturer:
#     def __init__(self, identity: int, location: str):
#         self.__identity = identity
#         self.__location = location
#     def describle(self):
#         print('identity: %s --- location: %s' %(self.__identity, self.__location))
#     @staticmethod
#     def hello(num: int):
#         print('hello %s people')
# class Device:
#     def __init__(self, name: str, price: int, identity: int, location: str):
#         self.__name = name
#         self.__price = price
#         self.__manufacturer = Manufacturer(identity, location)
#     def describle(self):
#         print('Name: %s --- Price: %s' %(self.__name, self.__price))
#         self.__manufacturer.describle()
# dv1 = Device('Keyboard', 2500, 10, 'Viet Nam')
# dv1.describle()
#################################################################################################
class Manufacturer:
    def __init__(self, identity: int, location: str):
        self.identity = identity
        self.location = location
    def describleManufacturer(self):
        print('identity: %s --- location: %s' %(self.identity, self.location))
    @staticmethod
    def hello(num: int):
        print('hello %s people' %num)
class Device(Manufacturer):
    def __init__(self, name: str, price: int, identity: int, location: str):
        self.__name = name
        self.__price = price
        super().__init__(identity, location)
    def describle(self):
        print('Name: %s --- Price: %s' %(self.__name, self.__price))
        self.describleManufacturer()
dv1 = Device('Keyboard', 2500, 10, 'Viet Nam')
dv1.describle()
dv1.hello(10)