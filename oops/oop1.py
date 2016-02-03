class items:
    def add(self,item_code,item_name):
        self.id=item_code
        self.name=item_name
        item[self.id]=self.name 
    def delete(self,item_code):
        self.id=item_code
        del item[self.id] 
        print "delete item %d succesfully"%(self.id)
    def view(self,item_code):
        self.id=item_code
        print item[self.id]
    def viewall(self):
        print "items available are:\n"
        for self.id in item:
            print self.id,item[self.id]
ch="y"
item={}
while(ch=="y"):
    print "MENU:\n1.Add Item\n2.View Item\n3.Delete Item\n4.List All Items \n5.Exit " 
    c=int(raw_input("enter your choice:"))
    if(c==1):
        m=int(raw_input("enter new item code\n"))
        n=raw_input("enter new item name\n")
        itm=items()
        itm.add(m,n)
        ch=raw_input("do you want to continue:y/n\n") 
    elif(c==2):
        n=int(raw_input("enter item code\n"))
        ittm=items()
        ittm.view(n)
        ch=raw_input("do you want to continue:y/n\n")  
    elif(c==3):
        n=int(raw_input("enter item code\n"))
        it=items()
        it.delete(n) 
        ch=raw_input("do you want to continue:y/n\n")
    elif(c==4):
        i=items()
        i.viewall()
        ch=raw_input("do you want to continue:y/n\n")
    elif(c==5):
        break            
