from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

compiler = Tk()
compiler.title('Notepad Pro')

filepath=''

def yessir():
	compiler.destroy()

def nosir():
	root.destroy()

def on_closing():

	global root

	root = Toplevel(compiler)
	root.geometry('250x150')
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
filename.add_command(label='Exit', command=on_closing)
menubar.add_cascade(label='File', menu=filename)
compiler.config(menu=menubar)

editor=Text()
editor.pack()

compiler.protocol('WM_DELETE_WINDOW', on_closing)
compiler.mainloop()
