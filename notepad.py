from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import filedialog
from tkinter import font
import os
import subprocess

compiler = Tk()
compiler.title('Notepad Pro')

filepath=''

text_scroll = Scrollbar()
text_scroll.pack(side=RIGHT, fill=Y)

def calc():
	subprocess.Popen("cal")

def fun():
	subprocess.Popen("Appka-EN")

def yessir():
	compiler.destroy()

def nosir():
	root.destroy()

def on_closing():

	global root

	root = Toplevel(compiler)
	root.geometry('300x100')
	root.config()

	poplabel=Label(root, text='Are you sure you have saved your file and want to exit?')
	poplabel.pack(pady=10)

	myframe = Frame(root)
	myframe.pack(pady=5)

	yes = Button(myframe, text='Yes', command=yessir)
	yes.pack()

	no = Button(myframe, text='No', command=nosir)
	no.pack()

	root.mainloop()

def openfile():
	path = askopenfilename()
	with open(path, 'r') as file:

		code = file.read()
		editor.delete('1.0', END)
		editor.insert('1.0', code)

		setfilepath(path)

def setfilepath(path):
	global filepath
	filepath = path

def saver():
	if filepath == '':
		path = asksaveasfilename()
	else:
		path=filepath
	with open(path, 'w') as file:
		code = editor.get('1.0', END)
		file.write(code)
		setfilepath(path)

def saveasr():
	path = asksaveasfilename()
	with open(path, 'w') as file:
		code = editor.get(1.0, END)
		file.write(code)

filemenubar = Menu(compiler)
filename = Menu(filemenubar, tearoff=0)
filename.add_command(label='Open', command=openfile)
filename.add_command(label='Save', command=saver)
filename.add_command(label='Save As', command=saveasr)
filename.add_separator()
filename.add_command(label='Exit', command=on_closing)
filemenubar.add_cascade(label='File', menu=filename)

extraname = Menu(filemenubar, tearoff=0)
extraname.add_command(label='Calculator', command=calc)
extraname.add_command(label='Funny "Appka" app', command=fun)
filemenubar.add_cascade(label='Extra', menu=extraname)
compiler.config(menu=filemenubar)

editor=Text(width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True)
editor.pack()

text_scroll.config(command=editor.yview)

status_bar = Label(compiler, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

compiler.protocol('WM_DELETE_WINDOW', on_closing)
compiler.mainloop()
