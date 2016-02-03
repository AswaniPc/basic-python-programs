from gi.repository import Gtk
b=Gtk.Builder()
b.add_from_file("smpl_list.glade")

w =b.get_object("window1")
b1=b.get_object("button1")
b2=b.get_object("button2")
c1=b.get_object("comboboxtext1")
c2=b.get_object("comboboxtext2")


def add(b1):
    data=c1.get_active_text()
    pos=c1.get_active()
    c2.append_text(data)
    c1.remove(pos)
def remove(b2):
    data=c2.get_active_text()
    pos=c2.get_active()
    c1.append_text(data)
    c2.remove(pos)
    
w.connect("delete-event",Gtk.main_quit)
b1.connect("clicked",add)
b2.connect("clicked",remove)

w.show_all()
Gtk.main() 
