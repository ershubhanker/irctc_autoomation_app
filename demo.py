import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (startPage,IDsPage, passangerPage,paymentPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("startPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


# first window frame IDs
class startPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent,bg="#3d3d5c")
        self.controller=controller

        self.controller.title("Home page")
        self.controller.state('zoomed')

        label1=tk.Label(self,text='first page',font=('orbitron',45,'bold'),foreground='#ffffff',background='#3d3d5c')
        label1.pack(pady=25)

        Button1=tk.Button(self,text='first page',command=lambda:controller.show_frame("startPage"))
        Button1.pack(pady=25)
        Button2=tk.Button(self,text='IDS page',command=lambda:controller.show_frame("IDsPage"))
        Button2.pack(pady=25)
        Button3=tk.Button(self,text='PASSSENGER page',command=lambda:controller.show_frame('passangerPage'))
        Button3.pack(pady=25)
        Button3=tk.Button(self,text='PAYMENT page',command=lambda:controller.show_frame('paymentPage'))
        Button3.pack(pady=25)

# second window 
class IDsPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent,bg="#3d3d5c")
        self.controller=controller

        self.controller.title("ids page")
        self.controller.state('zoomed')

        label1=tk.Label(self,text='ids',font=('orbitron',45,'bold'),foreground='#ffffff',background='#3d3d5c')
        label1.pack(pady=25)

        Button1=tk.Button(self,text='ids',command=lambda:controller.show_frame("startPage"))
        Button1.pack(pady=25)
        Button2=tk.Button(self,text='IDS page',command=lambda:controller.show_frame("IDsPage"))
        Button2.pack(pady=25)
        Button3=tk.Button(self,text='PASSSENGER page',command=lambda:controller.show_frame('passangerPage'))
        Button3.pack(pady=25)
        Button3=tk.Button(self,text='PAYMENT page',command=lambda:controller.show_frame('paymentPage'))
        Button3.pack(pady=25)

# third window 
class passangerPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent,bg="#3d3d5c")
        self.controller=controller

        self.controller.title("passenger page")
        self.controller.state('zoomed')

        label1=tk.Label(self,text='Passeneger',font=('orbitron',45,'bold'),foreground='#ffffff',background='#3d3d5c')
        label1.pack(pady=25)

        Button1=tk.Button(self,text='first page',command=lambda:controller.show_frame("startPage"))
        Button1.pack(pady=25)
        Button2=tk.Button(self,text='IDS page',command=lambda:controller.show_frame("IDsPage"))
        Button2.pack(pady=25)
        Button3=tk.Button(self,text='PASSSENGER page',command=lambda:controller.show_frame('passangerPage'))
        Button3.pack(pady=25)
        Button3=tk.Button(self,text='PAYMENT page',command=lambda:controller.show_frame('paymentPage'))
        Button3.pack(pady=25)

# fourth window 
class paymentPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent,bg="#3d3d5c")
        self.controller=controller

        self.controller.title("payment page")
        self.controller.state('zoomed')

        label1=tk.Label(self,text='payment',font=('orbitron',45,'bold'),foreground='#ffffff',background='#3d3d5c')
        label1.pack(pady=25)

        Button1=tk.Button(self,text='first page',command=lambda:controller.show_frame("startPage"))
        Button1.pack(pady=25)
        Button2=tk.Button(self,text='IDS page',command=lambda:controller.show_frame("IDsPage"))
        Button2.pack(pady=25)
        Button3=tk.Button(self,text='PASSSENGER page',command=lambda:controller.show_frame('passangerPage'))
        Button3.pack(pady=25)
        Button3=tk.Button(self,text='PAYMENT page',command=lambda:controller.show_frame('paymentPage'))
        Button3.pack(pady=25)
    


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()