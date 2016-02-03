from gi.repository import Gtk
import datetime
b=Gtk.Builder()
b.add_from_file("smpl_date.glade")

w =b.get_object("window1")
t=b.get_object("entry1")
s=b.get_object("button1")


def valid(s):
    submit=1
    today = datetime.date.today()
    tyr=today.year
    tmnth=today.month
    tday=today.day
    dob1=t.get_text()
    try:
        dob=datetime.datetime.strptime(dob1,'%d/%m/%Y').date()
        yr=dob.year
        mnth=dob.month
        day=dob.day
        if yr-tyr>=0:
            if mnth-tmnth>=0 and yr-tyr==0:
                if day-tday>0 and mnth-tmnth==0:
                    b.get_object("label2").set_text("please enter valid dob")
                    submit=-1
                else:
                    b.get_object("label2").set_text("please enter valid dob")
                    submit=-1    
            else:
                b.get_object("label2").set_text("please enter valid date of birth")
                submit=-1
        if submit==1:
            print "successfully registered"
    except ValueError:
        b.get_object("label2").set_text("please enter a existing date")
w.connect("delete-event",Gtk.main_quit)
s.connect("clicked",valid)

w.show_all()
Gtk.main() 
