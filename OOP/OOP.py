# class dog:
#     legs = 4 # thuoc tinh co san voi moi class, ko can phai gan khi khai bao doi tuong
    
#     def __init__(self, name): # khoi tao tham so, cac thuoc tinh co thay doi moi khi khai bao doi tuong
#         self.name = name
#     def sua(self): # la mot phuong thuc method
#         print('gau gau gau ....')

# pug = dog('husky')
# print(pug.name)
# print(pug.legs)
# pug.sua()

################## TINH DONG GOI ###################
class HoTen:
    __name = "Anh Tuan"  # private
    _age = 22
    __height = 170

    def __getName(self): # private, only class
        print(self.__name)
    def getName(self): # public
        self.__getName()
    
    def _getAge(self): # protected
        print(self._age)
    
    def _getHeight(self): 
        print(self.__height)
    # def getHeight(self): # public
    #     self.__getHeight()
    

# print(HoTen().__name) #error AttributeError: 'HoTen' object has no attribute '__name'
# print(HoTen().__getName()) #error AttributeError: 'HoTen' object has no attribute '__getName'
HoTen()._age
HoTen()._getAge()
HoTen().getName()
HoTen()._getHeight()

################## TINH KE THUA ###################
# class Truong:
#     def __init__(self):
#         pass
#     def diachi(self):
#         print("So 1 Nguyen Trai")

#     def hieutruong(self):
#         print('nguyen van a')
# class Monhoc:
#     so_mon_hoc = 10
#     def __init__(self):
#         pass
#     def today(self):
#         print('toan')
#     def tomorrow(self):
#         print('vat li')
# class HocSinh(Truong, Monhoc):
#     def __init__(self):
#         Truong.__init__(self)
#         Monhoc.__init__(self)
#         print('hoc sinh')
#     so_mon_hoc = 2
#     def today(self):
#         print('toan, hoa')
#     def diachi(self):
#         print('so 2 nguyen trai')
# T = Truong()
# M = Monhoc()
# H = HocSinh()
# T.diachi() 
# M.today()
# H.today() # ke thua va thay doi ham today
# H.diachi() # ke thua va thay doi ham diachi
# H.tomorrow() # ke thua ham tomorrow
# H.hieutruong() # ke thua ham hieutruong
# print(M.so_mon_hoc)
# print(H.so_mon_hoc) # ke thua va thay doi so mon hoc
