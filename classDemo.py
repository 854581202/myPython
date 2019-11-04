#!/etc/bin/env python3
# -*- coding:utf-8 *-*


#--------------------------------------
#-------------类和实例------------------
#--------------------------------------
class Student(object):
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def print_grade(self):
        print("%s the grade is %s"%(self.name,self.grade))

    def print_level(self):
        if self.grade<60:
            print("不及格")
        elif self.grade<80:
            print("及格")
        else:
            print("优秀")

"""
Bob=Student("Bob",60)
Alice=Student("Alice",90)
Bob.print_level()
Bob.print_grade()
"""




#--------------------------------------
#-------------限制访问------------------
#--------------------------------------

class Student1(object):
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def get_gender(self):
        print("%s's gender is %s"%(self.__name,self.__gender))

    def set_gender(self,newGender):
        if newGender == "male" or newGender == "female":
            self.__gender=newGender
            print("already set %s's gender to %s"%(self.__name,self.__gender))
        else:
            print("ilegal arg ,expect 'male' or 'female'")


"""
Alice=Student1("Alice","female")
Bob=Student1("Bob","male")
Bob.get_gender()
Bob.set_gender("female")
Bob.get_gender()
Bob.__gender="male"
Bob.get_gender()
Bob.set_gender("dog")
"""

#--------------------------------------
#------------继承和多态------------------
#--------------------------------------

class Animal(object):
    def run(self):
        print("Animal is runing")

class Dog(Animal):
    def run(self):
        print("Dog is runing")

class Cat(Animal):
    def run(self):
        print("Cat is runing")

class Monkey(Animal):
    def run(self):
        print("Monkey is runing")

def runTwice(Animal):
    Animal.run()
    Animal.run()
"""
Alice=Dog()
Bob=Cat()
LiLei=Monkey()
Alice.run()
Bob.run()
runTwice(LiLei)
"""


#--------------------------------------
#------------实例属性和类属性------------
#--------------------------------------
class Student2():
    count = 0
    def __init__(self,name):
        self.__name=name
        self._count()

    def _count(self):
        Student2.count += 1

Alice=Student2("Alice")
Bob=Student2("Bob")
print(Student2.count)


