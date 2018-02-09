#!python3
from tkinter import *
import tkinter.messagebox
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import filedialog
from idlelib.ToolTip import *
import os
root=Tk()
p=StringVar()
p1=StringVar()
d=StringVar()
d1=StringVar()
p.set('Panel 1')
p1.set('Panel 2')
#first made buttons functions
def run_command():
	cmd=diary2.get('1.0','end')
	os.system(cmd)
def closeleft():
	global p
	p.set('Panel 1')
def closeright():
	global p1
	p1.set('Panel 2')
def lefter():
	global p
	txt=diary.get('1.0','end')
	a=p.get()
	if not os.path.exists(a):
		dirc=filedialog.asksaveasfilename(defaultextension='.py',initialdir="C:\python34")
		infile=open(dirc,'w')
		infile.write(txt)
		infile.close()
		tkinter.messagebox.showinfo('UniPy Terminal','File is saved.')
		p.set(dirc)
	else:
		dirc=p.get()
		infile=open(dirc,'w')
		infile.write(txt)
		infile.close()
		tkinter.messagebox.showinfo('UniPy Terminal','File is saved.')
def righter():
	global p1
	txt1=diary1.get('1.0','end')
	b=p1.get()
	if not os.path.exists(b):
		dirc=filedialog.asksaveasfilename(defaultextension='.py',initialdir='C:\python34')
		infile1=open(dirc,'w')
		infile1.write(txt1)
		infile1.close()
		tkinter.messagebox.showinfo('UniPy Terminal','File is saved.')
		p1.set(dirc)
	else:
		dirc=p1.get()
		infile=open(dirc,'w')
		infile.write(txt1)
		infile.close()
		tkinter.messagebox.showinfo('UniPy Terminal','File is saved.')
def open_left():
	path=filedialog.askopenfilename(defaultextension='.py',initialdir='C:\python34')
	dir=open(path,'r')
	d=dir.read()
	diary.insert(END,d)
	global p
	p.set(path)
def open_right():
	path1=filedialog.askopenfilename(defaultextension='.py',initialdir='C:\python34')
	dir=open(path1,'r')
	d=dir.read()
	diary1.insert(END,d)
	global p1
	p1.set(path1)
main_bg='black'
main_fg='#263e27'
font_size='courier 9 bold'
def help_content():
	tl=Toplevel(root,bg='#60625f')
	label=Label(tl,text='Help',bg=main_bg,fg=main_fg,font='normal 18 bold')
	label.pack(side='top',fill='both',expand=True)
	text=Message(tl,text='All Text Shortcuts are same as any other Text Editor.\n\
It\'s a copy of full product to use full product.\n\
Please visit www.uniproducts.com and download it from there.',fg=main_fg,bg=main_bg,font='times 14 bold')
	text.pack(side='top',fill='both',expand=True)
def about_me():
	tl=Toplevel(root,bg='#60625f')
	label=Label(tl,text='Usman Ali',bg=main_bg,fg=main_fg,font='normal 18 bold')
	label.pack(side='top',fill='both',expand=True)
	text=Message(tl,text='This product is designed,functioned and programmed by Usman Ali.\n \
He is a software developer, technology expert and gifted programmer.\n \
You can contact him at www.bad199614@gmail.com',fg=main_fg,bg=main_bg,font='times 14 bold')
	text.pack(side='top',fill='both',expand=True)
def lopen():
	path=filedialog.askopenfilename(defaultextension='.py',initialdir='C:\python34')
	dir=open(path,'r')
	d=dir.read()
	diary.insert(END,d)
	global p
	p.set(path)
def ropen():
	path1=filedialog.askopenfilename(defaultextension='.py',initialdir='C:\python34')
	dir=open(path1,'r')
	d=dir.read()
	diary1.insert(END,d)
	global p1
	p1.set(path1)
def saleft():
	txt=diary.get('1.0','end')
	path=filedialog.asksaveasfilename(defaultextension='.py',initialdir='C:\python34')
	global p
	infile=open(path,'w')
	infile.write(txt)
	infile.close()
	tkinter.messagebox.showinfo('UniPy Terminal','File is saved.')
	p.set(path)
def saright():
	txt1=diary.get('1.0','end')
	path1=filedialog.asksaveasfilename(defaultextension='.py',initialdir='C:\python34')
	global p1
	infile=open(path1,'w')
	infile.write(txt1)
	infile.close()
	tkinter.messagebox.showinfo('UniPy Terminal','File is saved.')
	p1.set(path1)
root.config(bg='#60625f')
root.title('UniPy Terminal')
root.state("zoomed")
top=Menu(root)
file=Menu(top,tearoff=0,bg='black',fg='green')
file.add_command(label='Open File in Left Panel',command=open_left)
file.add_command(label='Open File in Right Panel',command=open_right)
file.add_command(label='Save Left',command=lefter)
file.add_command(label='Save Left As',command=saleft)
file.add_command(label='Save Right',command=righter)
file.add_command(label='Save Right As',command=saright)
file.add_command(label='Close Left',command=closeleft)
file.add_command(label='Close Right',command=closeright)
top.add_cascade(label='File',menu=file)
root.config(menu=top)
file1=Menu(top,tearoff=0,bg='black',fg='green')
top.add_cascade(label='Settings',menu=file1)
edit=Menu(top,tearoff=0,bg='black',fg='green')
top.add_cascade(label='Edit',menu=edit)
search=Menu(top,tearoff=0,bg='black',fg='green')
top.add_cascade(label='Search',menu=search)
file2=Menu(top,tearoff=0,bg='black',fg='green')
file2.add_command(label='Help Content',command=help_content)
file2.add_command(label='About Me',command=about_me)
top.add_cascade(label='?',menu=file2)
frame=Frame(root)
frame1=Frame(root)
frame1.config(bg='#60625f')
frame2=Frame(root)
frame2.config(bg='#60625f')
#code for nameframe
label=Label(frame,text='UniPy Terminal',bg='#60625f',fg='black',font='terminal 30 bold',width=30)
label.pack(side='top',fill=X,expand=True) #end of nameframe code
#code for labelframe
#code for firstlabelframe
labelframe=Frame(root)
lbl1=Menubutton(labelframe,textvariable=p,bg='black',fg='green',relief=SUNKEN,font='times 14 bold',anchor=W,width=45)
lbl1.pack()
lbl1.menu=Menu(lbl1,tearoff=0,bg='black',fg='green')
lbl1['menu']=lbl1.menu
lbl1.menu.add_command(label='Open',command=lopen)
lbl1.menu.add_command(label='Close',command=closeleft)
lbl1.menu.add_command(label='Save',command=lefter)
lbl1.menu.add_command(label='Save As',command=saleft)
lbl1.pack(side='left',fill=X,expand=True)
#code for second labelframe
lbl2=Menubutton(labelframe,textvariable=p1,bg='black',fg='green',relief=SUNKEN,font='times 14 bold',anchor=W,width=45)
lbl2.pack()
lbl2.menu=Menu(lbl2,tearoff=0,bg='black',fg='green')
lbl2['menu']=lbl2.menu
lbl2.menu.add_command(label='Open',command=ropen)
lbl2.menu.add_command(label='Close',command=closeright)
lbl2.menu.add_command(label='Save',command=righter)
lbl2.menu.add_command(label='Save As',command=saright)
lbl2.pack(side='left',fill=X,expand=True)
#code for first panel
s=Scrollbar(frame1)
diary=Text(frame1,bg=main_bg,fg=main_fg,font=font_size,width=60,wrap='word',insertbackground='#484d4c',insertwidth=10,insertontime=200,insertofftime=200,padx=15,pady=5,selectbackground='green',state=NORMAL,relief=GROOVE)
diary.pack(side='left',fill='both',expand=True)
s.pack(side='left',fill=Y)
s.config(command=diary.yview)
diary.config(yscrollcommand=s.set)
#code for second panel
s1=Scrollbar(frame1)
diary1=Text(frame1,bg=main_bg,fg=main_fg,font=font_size,width=60,wrap='word',insertbackground='#484d4c',insertwidth=10,pady=5,padx=15,selectbackground='green',state=NORMAL,relief=GROOVE)
diary1.pack(side='left',fill='both',expand=True)
s1.pack(side='left',fill=Y)
s1.config(command=diary1.yview)
diary1.config(yscrollcommand=s1.set) #end of code of second panel
frame3=Frame(root)
#let's write code for commandline panel
lbl1=Menubutton(frame2,text='Program Execution Panel',relief=SUNKEN,bg='black',fg='green',font='times 14 bold')
lbl1.pack()
lbl1.menu=Menu(lbl1,tearoff=0,bg='black',fg='green')
lbl1['menu']=lbl1.menu
lbl1.menu.add_command(label='Execute Command',command=run_command)
lbl1.menu.add_command(label='Clear Command Panel')
lbl1.menu.add_command(label='Exit')
lbl1.pack(side='top',fill=X,expand=True)
s2=Scrollbar(frame2)
s2.pack(side='right',fill=Y)
s2.config(bg='green',activebackground='black',highlightbackground='blue',troughcolor='blue')
diary2=Text(frame2,bg=main_bg,fg=main_fg,font=font_size,width=50,wrap='word',insertbackground='#484d4c',insertwidth=10,padx=10,selectbackground=main_fg,state=NORMAL,relief=GROOVE,height=10)
diary2.pack(side='top',fill=X,expand=True)
s2.config(command=diary2.yview)
diary2.config(yscrollcommand=s2.set)
frame.pack(side='top',fill=X,expand=True)
labelframe.pack(side='top',fill=X,expand=True)
frame1.pack(side='top',fill='both',expand=True)
frame2.pack(side='top',fill=X,expand=True)
mainloop()                                                                                                                                                                                                                                                    

