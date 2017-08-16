#!/usr/bin/env python

import pygtk
import gtk
import fizz_buzz

lable = ""
class PyApp(gtk.Window):
    """fizz_buzz gui"""
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_default_size(500,500)
        self.set_title("fizz_buzz")
        self.label = gtk.Label("Prepare for fizz_buzz")
        self.entry = gtk.Entry()

        self.btn = gtk.Button("Get class")
        self.btn.connect("clicked", self.process_input)

        fixed = gtk.Fixed()
        fixed.put(self.label, 100,100)
        fixed.put(self.entry, 100,150)
        fixed.put(self.btn, 100, 200)
        dialog = gtk.Dialog(lable)
        dialog.add


        self.add(fixed)
        self.show_all()

    def process_input(self, widget):
	""" Pass input to fizz_buzz function """
        global lable
        try:
            # if (isnumeric(self.entry.get_text())):
            lable = fizz_buzz.fizz_buzz(int(self.entry.get_text()))
            print(lable)
            return lable
        except:
            return "Please input an integer number"



PyApp()
gtk.main()
