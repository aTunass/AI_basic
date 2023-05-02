class Person:
    def __init__(self, name: str, year: int):
        self._name = name
        self._year = year
    def getAge(self):
        return int(2023-self._year)
class Student(Person):
    def __init__(self, name: str, year: int, grade: int):
        self.__grade = grade
        super().__init__(name, year)
    def describle(self):
        print('Name: %s // Year: %s // Grade: %s // Age: %s' %(self._name, self._year, self.__grade, self.getAge()))
class Teacher(Person):
    def __init__(self, name: str, year: int, subject: str):
        self.__subject = subject
        super().__init__(name, year)
    def describle(self):
        print('Name: %s // Year: %s // Subject: %s // Age: %s' %(self._name, self._year, self.__subject, self.getAge()))
class Doctor(Person):
    def __init__(self, name: str, year: int, specialist: str):
        self.__specialist = specialist
        super().__init__(name, year)
    def describle(self):
        print('Name: %s // Year: %s // Specialist: %s // Age: %s' %(self._name, self._year, self.__specialist, self.getAge()))
class Ward:
    def __init__(self, name):
        self.__name = name
        self.__people = []
        print('Day la Ward %s' %self.__name)
    def AddPerson(self, person):
        if isinstance(person, list):
            self.__people += person
        else: self.__people.append(person)
    def describle(self, tag = 'Person'):
        print('Day la mo ta theo tag %s' %tag)
        for i in range(len(self.__people)):
            if (tag == 'Person'):
                self.__people[i].describle()
            elif(tag == 'Teacher'):
                if (isinstance(self.__people[i], Teacher)):
                    self.__people[i].describle()
            elif(tag == 'Student'):
                if (isinstance(self.__people[i], Student)):
                    self.__people[i].describle()
            elif(tag == 'Doctor'):
                if (isinstance(self.__people[i], Doctor)):
                    self.__people[i].describle()
    def CountDoctor(self):
        count = 0
        for i in range(len(self.__people)):
            if (isinstance(self.__people[i], Doctor)):
                    count += 1
        print('So bac si trong Ward %s la: %s' %(self.__name, count))
    def SortAge(self):
        print('Day la sap xep theo tuoi')
        self.__people.sort(reverse=True, key=lambda x:x.getAge())
        for i in range(len(self.__people)):
            self.__people[i].describle()
    def aveTeacherBirth(self):
        count = 0
        tong = 0
        for i in range(len(self.__people)):
            if (isinstance(self.__people[i], Teacher)):
                    tong += self.__people[i].getAge()
                    count += 1
        return float(tong/count)
HS1 = Student('Anh Tuan', 2001, 12)
GV1 = Teacher('Tuan Anh', 1990, 'Toan')
DT1 = Doctor('Anh Khoa', 1988, 'Bac Si Da Khoa')
HS2 = Student('Anh Tung', 2000, 10)
GV2 = Teacher('Tuan Tu', 1995, 'Hoa hoc')
DT2 = Doctor('Anh Khoi', 1980, 'Bac Si Da Lieu')
HS3 = Student('Anh Tuong', 1999, 12)
GV3 = Teacher('Tuan Tung', 1997, 'Vat li')
DT3 = Doctor('Anh Kien', 1960, 'Bac Si Noi')

ward1 = Ward('2023')
ward1.AddPerson([HS1,GV1, DT1, HS2, GV2, DT2])
ward1.AddPerson([HS3, GV3, DT3])
ward1.describle(tag='Student')
ward1.CountDoctor()
ward1.SortAge()
print(ward1.aveTeacherBirth())

# def Describle(obj:list):
#     print(isinstance(obj, list))
#     for i in range(len(obj)):
#         obj[i].describle()
# Describle([HS1, GV1, DT1])