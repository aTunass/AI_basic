class NhanVien(object):
  '''Lớp mô tả cho mọi nhân viên'''
  dem = 0

  def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      NhanVien.dem += 1

  def hien_thi_so_luong(self):
    print("Tổng số nhân viên được tạo: ", NhanVien.dem)

  def hien_thi_nhan_vien(self):
      print("Tên: ", self.name,  ", Lương: ", self.salary)
nv1 = NhanVien('Tuan', 5)
nv2 = NhanVien('Anh', 7)
print(nv1.name, nv2.name, nv1.salary, nv2.salary)
nv1.hien_thi_so_luong()
nv1.hien_thi_nhan_vien()
nv1.girlfriend = 0
nv1.age = 22
print(getattr(nv1, 'age'))
print(getattr(nv1, 'girlfriend'))
print(hasattr(nv1, 'girlfriend'))
del nv1.girlfriend
print(hasattr(nv1, 'girlfriend'))
# print(getattr(nv1, 'girlfriend'))
#######################################################

class Base(object): 
  
    # Constructor 
    def __init__(self, x): 
        self.x = x     
  
class Derived(Base): 
  
    # Constructor 
    def __init__(self, x, y): 
          
        ''' In Python 3.x, "super().__init__(name)" 
            also works''' 
        super(Derived, self).__init__(x) 
        self.y = y 
  
    def printXY(self): 
  
       # Note that Base.x won't work here 
       # because super() is used in constructor 
       print(self.x, self.y) 
  
t = Base(5) 
# Driver Code 
d = Derived(10, 20) 
d.printXY() 
print(t.x)
#######################################################
# class CSStudent: 
#     stream = 'cse'     # Class Variable  
#     def __init__(self, name, roll): 
#         self.name = name  
#         self.roll = roll 
  
# # New object for further implementation 
# a = CSStudent("check", 3) 
# print "a.tream =", a.stream 
  
# # Correct way to change the value of class variable 
# CSStudent.stream = "mec"
# print "\nClass variable changes to mec"
  
# # New object for further implementation 
# b = CSStudent("carter", 4) 
  
# print "\nValue of variable steam for each object"
# print "a.stream =", a.stream 
# print "b.stream =", b.stream 
class Employee: 
  
    # Initializing  
    def __init__(self): 
        print('Employee created') 
  
    # Calling destructor 
    def __del__(self): 
        print("Destructor called") # goi ham nay khi ket thuc chuong trinh se tu chay va xoa
  
def Create_obj(): 
    print('Making Object...') 
    obj = Employee() 
    print('function end...') 
    return obj 
  
print('Calling Create_obj() function...') 
obj = Create_obj() 
print('Program End...') 