'''This code uses an Observer pattern to isolate the data Model from the Interface with the help of the controller Object (the Main class)
and the use of Binders, which are way to communicate events in the interface to the Main class.
'''

from database import Database
from interface import Interface

class MainBinder:
    def __init__(self, interface):
        self.interface = interface

    def toggleButton(self, value):
        print("toggled Main")
    def browseHistory(self):
        print("browsed Main")
        bBinding = BrowserBinder(self.interface)
        self.interface.startBrowserWindow(bBinding)
    def quit(self):
        self.interface.destroy()

class BrowserBinder:
    def __init__(self, interface):
        self.interface = interface
    def mainButton(self):
        mBinding = MainBinder(self.interface)
        self.interface.startMainWindow(mBinding)

class Main:
    def __init__(self):
        interf = Interface()
        mBinding = MainBinder(interf)
        bBinding = BrowserBinder(interf)
        interf.startBrowserWindow(bBinding)
        #interf.startMainWindow(mBinding)

Main()
