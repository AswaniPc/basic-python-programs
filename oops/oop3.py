import datetime 
class Student:
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
        self.stnd=raw_input("enter standard:\n")
        print "enter marks of 5 subjects:"
        self.marks=[]
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
class Scholarship(Student):
    def __init__(self):
        #self.stdt=None
        self.scno= None
        self.scdate=None
        self.scdur= None
        self.amnt=None
    def add_sclr(self):
        self.scno=input("enter scholarship number:\n")
        sdate=str(raw_input("enter scholarship date:\n"))
        self.scdate= datetime.datetime.strptime(sdate, '%d/%m/%Y').date()
        self.scdur=int(raw_input("enter scholarship duration\n"))
        self.amnt=int(raw_input("enter scholarship amount:\n"))
        print "scholarship details are successfully saved"
    def check_expiry(self,rno):
        d=self.scdate
        dur=self.scdur
        yr=d.year
        mnth=d.month
        today = datetime.date.today()
        tyr=today.year
        tmnth=today.month
        if tyr-yr>=dur and tmnth-mnth>0:
            print "expired"
            return 1
        else:
            print "not expired"
            return 0
n=int(raw_input("enter the limit:\n"))
sch={}
c=='y'
for i in range(n):
    sch[i]=Scholarship()
    sch[i].add()
    sch[i].total()
    sch[i].avg()
    sch[i].grade()
    if sch[i].sclr()==1:
        sch[i].add_sclr()
        sch[i].check_expiry()
    else:
        print "not eligible for scholarship"
    




    


