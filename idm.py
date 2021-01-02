try:
	import wget
	from tkinter import *
	import sys
	import os
	from tkinter.filedialog import *

	root = Tk()
	root.minsize(790,148)
	root.maxsize(790,148)

	root.title("IDM BY AADITYA KANDEL")
	f1 = Frame(borderwidth=10,bg="black")
	f2 = Frame(borderwidth=10,bg="black")

	def sve():
		name = askdirectory(initialdir="C:/Users",
	                           )
		loc.set(name)
		os.system(f"echo {(loc.get())}>dir.data")

	def progress(current, total, width=80):
	  progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
	  root.update()
	  if b1['text']=="100":
	  	b1.config(text="Downloading 100%")
	  else:
	  	b1.config(text=f"{progress_message[0:16]}")
	  sys.stdout.flush()

	def er():
		b1.config(text="Download",command=dwnn)
		lb1.config(state=NORMAL)
		lb2.config(state=NORMAL)
		en1.config(state=NORMAL)
		en2.config(state=NORMAL)
		b2.config(state=NORMAL)
	def dwnn():
		try:
			lb1.config(state=DISABLED)
			lb2.config(state=DISABLED)
			en1.config(state=DISABLED)
			en2.config(state=DISABLED)
			b1.config(state=DISABLED)
			b2.config(state=DISABLED)
			url = f"{(dwn.get())}"
			root.update()
			d = wget.download(url,f"{(loc.get())}",bar=progress)
			root.update()
			b1.config(text="Successfully Downloaded [ Press Here To Continue ]",command = er,state=NORMAL)
		except:
			b1.config(text="Error..",command=er)
			b1.config(state=NORMAL)

	dwn = StringVar()
	loc = StringVar()
	try:
		f = open('dir.data','r+')
		for words in f:
			pass
		loc.set(f'{words[0:-1]}')
		f.close()
	except:
		loc.set('')
	dwn.set('https://github.com/AadityaKandel/AutoWriter/archive/main.zip')

	en1 = Entry(f1,textvariable = dwn,bg = "white",fg = "black",font ="comicsansms 11 bold",width=80)
	lb1 = Label(f1,text="Url: ",bg = "black",fg = "white",font ="comicsansms 11 bold")
	en2 = Entry(f2,textvariable = loc,bg = "white",fg = "black",font ="comicsansms 11 bold",width=75)
	lb2 = Label(f2,text="Location: ",bg = "black",fg = "white",font ="comicsansms 11 bold")
	lb22 = Label(f2,text="",bg = "black",fg = "white",font ="comicsansms 11 bold")
	b2 = Button(f2,text="Browse",bg="black",fg="white",font = "comicsansms 11 bold",command=sve)

	lb1.pack(side=LEFT)
	en1.pack(side=LEFT)
	lb2.pack(side=LEFT)
	en2.pack(side=LEFT)
	lb22.pack(side=LEFT)
	b2.pack(side=LEFT)

	f1.pack(anchor="w")
	f2.pack(anchor="w")


	b1 = Button(text="Download",bg = "black",fg = "white",font ="comicsansms 11 bold",relief=SUNKEN,padx=8,pady=8,command=dwnn)
	b1.pack()

	root.config(bg="black")
	root.mainloop()
except:
	quit()