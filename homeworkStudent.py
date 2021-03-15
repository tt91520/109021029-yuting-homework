class Student:
    def __init__(self, name, gender, height, weight, id):
        self.studentName = name
        self.studentGender = gender
        self.studentHeigh = height
        self.studentWeight = weight
        self.studentId = id

    def showInfo(self):
        print(self.studentName,"\t",self.studentGender,"\t",self.studentHeigh,"\t",self.studentWeight,"\t",self.studentId)

print("姓名", "   性別", "   身高", "  體重", " 座號")
x = Student("陳大民", "男", "175","60","1")
x2 = Student("李小明", "男","177","65","2")
x3 = Student("林阿花", "女","156","52","3")
x.showInfo()
x2.showInfo()
x3.showInfo()
