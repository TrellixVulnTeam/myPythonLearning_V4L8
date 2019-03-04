try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)
button1 = tkinter.Button(rightFrame, text='Button1')
button2 = tkinter.Button(rightFrame, text='Button2')
button3 = tkinter.Button(rightFrame, text='Button3')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
# canvas.pack(side='left', fill=tkinter.Y, expand=True)
# canvas.pack(side='left', fill=tkinter.X, expand=True)
# canvas.pack(side='left', fill=tkinter.BOTH, expand=True)

mainWindow.mainloop()

