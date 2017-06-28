import tkinter as tk
from tkinter import *
class Interface(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
    def startMainWindow(self, observer):
        mainw= getattr(self, "mainWindow", None)
        if mainw == None:
            self.mainWindow = Application(observer, master=self.container)
            self.mainWindow.grid(row=0, column=0, sticky="nsew")

        self.mainWindow.tkraise()
        self.mainWindow.mainloop()
    def startBrowserWindow(self, observer):
        brw= getattr(self, "browserWindow", None)
        if brw == None:
            self.browserWindow = Browser(observer, master=self.container)
            self.browserWindow.grid(row=0, column=0, sticky="nsew")

        self.browserWindow.tkraise()
        self.browserWindow.mainloop()
class Application(tk.Frame):
    def __init__(self, observer, master=None):
        super().__init__(master)
        self.master = master
        self.observer = observer
        #self.pack()
        self.create_widgets()

    def create_widgets(self, bexpanded=1):
        self.expanded = IntVar(value=bexpanded)
        for widget in self.winfo_children():
            widget.destroy()
        self.titleLabel = tk.Label(self, text="Title: ")
        self.titleText = tk.Text(self, height=1)
        self.commentLabel = tk.Label(self, text="Comment: ")
        self.commentText = tk.Text(self,height=6)
        self.startButton = tk.Button(self, text="START", command=self.toggle_button)
        self.browseHistoryButton = tk.Button(self, text="Browse History", command=self.browseHistory)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.quit_button)
        self.expandViewCheckb = Checkbutton(self, text="Expanded View", variable=self.expanded, command=self.expandView)

        self.titleLabel.grid(row=0)
        self.titleText.grid(row=0, column=1)
        self.startButton.grid(row=0, column=2)
        if bexpanded == 1:
            self.commentLabel.grid(row=1)
            self.commentText.grid(row=1, column=1, columnspan=2)
            self.browseHistoryButton.grid(row=2, column=0)
            self.quit.grid(row=2, column=1)
            self.expandViewCheckb.grid(row=2, column=2)
        else:
            self.browseHistoryButton.grid(row=1, column=0)
            self.quit.grid(row=1, column=1)
            self.expandViewCheckb.grid(row=1, column=2)
    def quit_button(self):
        self.observer.quit()
    def toggle_button(self):
        print("toggle")
        if self.startButton["text"] == "START":
            self.startButton["text"] = "STOP"
            self.observer.toggleButton(0)
        else:
            self.startButton["text"] = "START"
            self.observer.toggleButton(1)
    def browseHistory(self):
        print("browse")
        self.observer.browseHistory()
    def expandView(self):
        print("expand" + str(self.expanded.get()))
        self.create_widgets(self.expanded.get())
class Browser(tk.Frame):
    def __init__(self, observer, master=None):
        super().__init__(master)
        self.master = master
        self.observer = observer
        #self.pack()
        self.create_widgets()
    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.titleLabel = tk.Label(self, text="Title: ")
        self.titleText = tk.Text(self, height=1)
        self.mainButton = Button(self, text="Main Window", command=self.mainButton)

        self.titleLabel.grid(row=0)
        self.titleText.grid(row=0, column=1)
        self.mainButton.grid(row=1, column=0)
    def mainButton(self):
        self.observer.mainButton()
