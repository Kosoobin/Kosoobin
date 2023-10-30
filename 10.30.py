# 기말은 팀별 1~3명 커리큘럼에서 배우는 내용을 다룰 것 발표까지 채점
# 공공데이터나 외부 데이터를 이용해서 
# 유의미한 데이터를 뽑아서 정보를 전달할 수 있는 프로젝트를 구성
# 팀별로 참여도를 기재해야함

""" class MyClass:
    count = 0

    def __init__(self, num):
        self.count = num

    @classmethod
    def clsMethod(cls):
        cls.count += 1 
        print(f"cls count = {cls.count}")

    def instMethod(self):
        self.count += 1 
        print(f"instance = {self.count}")

MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count) """


""" class Champion() :
    lV =1
    movSpd = 0
    basicMovSpd = 325
    atkSpd = 0.6
    
    def __init__(self,champNam,speed):
        self.hp =100
        self.champNam = champNam
        self.level =1
        self.setSpeed(speed)
        self.setAtkSpd()
        self.setMovSpd()
	
    def setAtkSpd(self):
        self.atkSpd = 0.6((1.2)**(Champion.lv-1))
    def beAtk(self,dem):
        print ("be attak", dem, 1-100/(100+100))
        self.dem = dem*(100/(100+100))
        print(self.dem)
        self.hp = self.hp-self.dem
    def setSpeed(self,sp):
        if(sp ==1):
            self.speed =50
        else:
            self.speed = 0
    def setMovSpd(self):
        print("set Mov Spd")
        self.movSpd = (20+ self.speed)*(1)*(100)
    def printStatus(self):
        print("chamNam:%s, hp:%f,lv%d,mvSpd%f,stkSpd%f" % (self.champNam, self))
        
ashe = Champion("ashe", 474)
mipo = Champion("mipo", 520)
    
ashe.printStatus()
mipo.printStatus()
    
mipo.beAtk(63)
mipo.printStatus() """
    
    

""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1

class Yasuo(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
        
class Garen(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)

user1 = Yasuo("python")
user2 = Garen("hello")

user1.getName()
user1.getLevel()
user2.getName()
user2.getLevel() """

""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1

    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)
class Yasuo(Champion):()
class Garen(Champion):()

user1 = Yasuo("python")
user2 = Garen("hello")

user1.getName()
user1.getLevel()
user2.getName()
user2.getLevel() """

""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
    
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)

class Yasuo(Champion) :
    def attck(self, key):
        print(f"attack - {key} steel tempest")
        return

class Garen(Champion) :
    def attck(self, key):
        print(f"attack - {key} demacian justice")
        return

user1 = Yasuo("python")
user2 = Garen("hello")

user1.getLevel()
user2.getLevel()

user1.attck("q")
user2.attck("r")

user1.levelup()
user2.levelup()

user1.getLevel()
user2.getLevel() """


""" from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6)

print(circ.area())
print(rect.area())

sett ={circ,rect}
for st in sett:
    print(st.area()) """
    
""" class Person:
    def __init__(self, name, age, num):
        self._name = name
        self._age = age
        self._number = num

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def number(self):
        return self._number

    @name.setter
    def name(self, new):
        self._number = new

    @age.setter
    def age(self, nAge):
        self._age = nAge

user1= Person("Alice",30,"01011112222")
print (user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)
print(user1._number)

user1._age=21
user1.age=23
print(user1.age) """

""" class Person :
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def getNumber(self) :
        return self.number

class Student(Person) : ()

class Teacher(Person) : ()

def getPersonName(person) :
    return person.getName()

user1=Student("alice",23,"010111222")
user2=Teacher("bob",25,"010333444")

print(getPersonName(user1))
print(getPersonName(user2)) """

class Person : 
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    def getName(self) :
        return self.name
    
    def setName(self, newName) :
        self.name =newName
        return

    def getNumber(self) :
     return self.number

    def setNumber(self, newNum) :
       self.number=newNum
       return
   
p1 = Person("python",23,"010111222")
p2 = Person("hello",21,"010333444")
 
print(p1.getName())
print(p1.getNumber())
print(p2.getNumber())
 
p1.setNumber("0101111111")
p2.setNumber("0102222222")
 
print(p1.getNumber())
print(p2.getNumber())

p1.getNumber()
p2.getNumber()

p1.setNumber("11111111111")
p1.setNumber("22222222222")
