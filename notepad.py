from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

compiler = Tk()
compiler.title('Notepad Pro')

filepath=''

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

def saveas():
	if filepath == '':
		path = asksaveasfilename()
	else:
		path=filepath
	with open(path, 'w') as file:
		code = editor.get('1.0', END)
		file.write(code)
		setfilepath(path)

menubar = Menu(compiler)
filename = Menu(menubar, tearoff=0)
filename.add_command(label='Open', command=openfile)
filename.add_command(label='Save', command=saveas)
filename.add_command(label='Save As', command=saveas)
filename.add_command(label='Exit', command=exit)
menubar.add_cascade(label='File', menu=filename)
compiler.config(menu=menubar)

editor=Text()
editor.pack()
compiler.mainloop()
