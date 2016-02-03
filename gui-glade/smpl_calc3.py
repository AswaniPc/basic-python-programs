from gi.repository import Gtk
import re
b=Gtk.Builder()
b.add_from_file("smpl_calc.glade")

w=b.get_object("window1")
t=b.get_object("entry1")
b0=b.get_object("button16")
b1=b.get_object("button2")
b2=b.get_object("button3")
b3=b.get_object("button4")
b4=b.get_object("button5")
b5=b.get_object("button6")
b6=b.get_object("button7")
b7=b.get_object("button8")
b8=b.get_object("button9")
b9=b.get_object("button10")

ba=b.get_object("button11")
bs=b.get_object("button12")
bm=b.get_object("button13")
bd=b.get_object("button14")
bl=b.get_object("button15")
br=b.get_object("button17")

clr=b.get_object("button19")
bk=b.get_object("button18")
fd=b.get_object("button1")
#n=""
p=0
def add(btn):
    global p
    no=btn.get_label()
    #n=n+no
    t.insert_text(no,position=p)
    p=p+1  

def clear(btn):
    global p
    t.set_text("")
    p=0  

def back(btn):
    global p
    t.delete_text(p,p-1)
    p=p-1
    
def calculate(btn):
    global p
    ans=0
    st=t.get_text()
    p=len(st)
    #if re.findall('\d+? *?\+ *?\d+?', st):
    ans=eval(st)
    t.set_text(str(ans))
    p=len(str(ans))
         
w.connect("delete-event",Gtk.main_quit)
b0.connect("clicked",add)
b1.connect("clicked",add)
b2.connect("clicked",add)
b3.connect("clicked",add)
b4.connect("clicked",add)
b5.connect("clicked",add)
b6.connect("clicked",add)
b7.connect("clicked",add)
b8.connect("clicked",add)
b9.connect("clicked",add)

ba.connect("clicked",add)
bs.connect("clicked",add)
bm.connect("clicked",add)
bd.connect("clicked",add)
bl.connect("clicked",add)
br.connect("clicked",add)

clr.connect("clicked",clear)
bk.connect("clicked",back)
fd.connect("clicked",calculate)

w.show_all()
Gtk.main() 
