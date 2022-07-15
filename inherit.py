'''class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
'''


class college:
  def __init__(self,clas,sec):
    self.kill = clas
    self.bill = sec.upper()

  def printfun(cricket):
    print('in a college'+ ' of', cricket.kill,"and sec of", cricket.bill )


class principal(college):
  def __init__(mouse,fname,lname,yop):
    mouse.fname=fname
    mouse.lname=lname
    super().__init__(fname,lname)
    mouse.yop=yop
  
  def printfun2(baseball):
    print('in a college'+ ' of', baseball.kill,"and sec of", baseball.bill ,'yearofpass', baseball.yop)
    
obj = principal('inter','a',2000)
obj.printfun()
obj.printfun2()

print(obj.fname)
print(obj.kill)



