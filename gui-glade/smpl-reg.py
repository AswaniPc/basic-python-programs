from gi.repository import Gtk
import re
b=Gtk.Builder()
b.add_from_file("smpl_reg.glade")
w =b.get_object("window1")
e1=b.get_object("entry1")
e2=b.get_object("entry2")
e3=b.get_object("entry3")
c1=b.get_object("comboboxtext1")
c2=b.get_object("comboboxtext2")
c3=b.get_object("comboboxtext3")
r1=b.get_object("radiobutton1")
r2=b.get_object("radiobutton2")
fb=b.get_object("filechooserbutton1")
b1=b.get_object("button1")
def register(b1):
    create=1
    name=e1.get_text()
    pswd=e2.get_text()
    mail=e3.get_text()
    date=c1.get_active()
    month=c2.get_active()
    year=c3.get_active()
    f=r1.get_active()
    m=r2.get_active()
    photo=fb.get_filename()
    if(name==""):
        b.get_object("label7").set_text("Enter your name")
        create=-1
    elif(len(name)<5):
        b.get_object("label7").set_text("Enter valid name") 
        create=-1
           
    if(pswd==""):
        b.get_object("label8").set_text("Enter a password")
        create=-1
    elif(len(pswd)<8):
        b.get_object("label8").set_text("password is too short")
        create=-1
        
    if(date==-1 or month==-1 or year==-1):
        b.get_object("label9").set_text("select your date of birth")
        create=-1
        
    if(mail==""):
        b.get_object("label11").set_text("Enter your email-id")
        create=-1 
    elif(re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",mail) == None): 
        b.get_object("label11").set_text("email address is not valid")  
        create=-1
    
    if(photo==None):
        b.get_object("label12").set_text("please attach your photo")
        create=-1 
    if(create==1):
        print "successfully registered"             
w.connect("delete-event",Gtk.main_quit)
b1.connect("clicked",register)

w.show_all()
Gtk.main() 
