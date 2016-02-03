from gi.repository import Gtk
b=Gtk.Builder()
b.add_from_file("sample.glade")

w =b.get_object("window1")
text1=b.get_object("entry1")
check_button=b.get_object("button1")


def check_val(check_button):
	name=text1.get_text()
	b.get_object("label3").set_text(name)

w.connect("delete-event",Gtk.main_quit)
check_button.connect("clicked",check_val)

w.show_all()
Gtk.main() 
