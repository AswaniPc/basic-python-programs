class student:
    def __init__(self):
        self.no=None
        self.name=None
        self.dob=None
        self.age=None
        self.stnd=None
        self.marks=[]
    def add(self):
        self.no=int(raw_input("enter roll no:\n"))
        self.name=raw_input("enter name:\n")
        self.dob=raw_input("enter dob:\n")
        self.age=int(raw_input("enter age:\n"))
        self.stnd=stnd=raw_input("enter standard:\n")
        print "enter marks of 5 subjects:"
        for j in range(0,5):
            self.marks.append(int(raw_input()))
    
    def view(self):
        print self.marks
    def total(self):
	    self.sum = 0
	    self.total = self.marks
	    for i in range(len(self.total)):
	        self.sum += self.total[i]
	    return self.sum

    def avg(self):
	    return self.sum/len(self.total)

    def grade(self):
	    self.per = (self.sum * 100)/250
	    if self.per > 80 :
	        return self.per, "distinction"
	    elif self.per > 60 and self.per < 80 :
	        return self.per, "firstclass"
	    elif self.per > 40 and self.per < 60 :
	        return self.per, "second class"
	    else :
	        return self.per, "fail"

    def sclr(self):
	    if self.per > 90 :
	        return 1
	    else :
	        return 0 
	        
n=input("enter the limit of students:\n")
std={}
for i in range(n):
    std[i]=student()
    std[i].add()
for i in range(n):
    print std[i].no,std[i].name,std[i].age,std[i].stnd,std[i].total(),std[i].avg(),std[i].grade(),std[i].sclr()

