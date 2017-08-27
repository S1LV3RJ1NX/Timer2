from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import subprocess, sys, webbrowser,os

root = Tk()
root.title("Break Reminder")
root.geometry("550x180+500+250")

f = "times", 14, "italic"
b = "arial", 10, "bold"
v = IntVar()

choices = [ ('Music',1), ('Motivate',2),('Ignite',3), ('Nothing',4)]

def song_path():
	path = askdirectory() 
	f = open("sng_pth.txt", "w")
	f.write(path)
	f.close()

def ok():
	#multiply wT and bA by 1000 for faster debugging and multiply by 60 for real-time use
	wT = int(workTime.get())*1000
	bA = int(breakAfter.get())*1000
	
	breaks_consumed = 0
	total_breaks_allowed = int(wT / bA)
	global window
	
	root.withdraw()
	#print(total_breaks_allowed)
	root.after(bA)
	window = Toplevel() #for child window
	window.geometry("480x240+500+250")        
	window.title("TIME FOR BREAK")
        
	Label(window, text = 'What you want to do?',padx=25,justify=LEFT,font = (f)).grid(sticky = 'W')

	try:
		import PIL 
		from PIL import Image
		from PIL import ImageTk
		img = Image.open("aa.ico")
		img = img.resize((150, 150), Image.ANTIALIAS)
		photoImg = ImageTk.PhotoImage(img)
		imglabel = Label(window, image=photoImg).place(x = 270, y = 25)
	except ImportError:
		pass

	def task():
		nonlocal breaks_consumed 
		nonlocal total_breaks_allowed
		if (breaks_consumed >= total_breaks_allowed):
			messagebox.showinfo(title = 'End', message= 'Timer Ended!! ')
			window.destroy()
			root.destroy()
		else:
			#print(breaks_consumed)
			root.after(bA)
			window.deiconify()
			breaks_consumed = breaks_consumed + 1

	def process():

		#multiply bD by 1000 for faster debugging and multiply by 60 for real-time use
		bD = int(breakDuration.get())*1000
		temp = bD
		while temp > 0:
			root.after(1000)
			temp = temp - 1000
		messagebox.showinfo(title = 'Reminder', message= 'Break Over Back To Work!!')
		return ( task() )

	def options():
		x = v.get()
		if x == 1:
			path = open("sng_pth.txt","r")

			if sys.platform == 'darwin':
				subprocess.Popen(['open', '--', path.read()])
			elif sys.platform == 'linux':
				subprocess.Popen(['xdg-open', path.read()])
			elif sys.platform == 'win32':
				os.startfile(path.read())

			path.close()
			window.withdraw()
			return ( process() )

		if x == 2:
			webbrowser.open("https://www.youtube.com/channel/UCf9_s9ii6BZ-klpgmtIi3WQ") 
			window.withdraw()
			return ( process() )

		if x == 3:
			webbrowser.open("http://www.geeksforgeeks.org/") 
			window.withdraw()
			return ( process() )
			
		if x == 4:
			window.withdraw()
			return ( process() )
	

	for txt, val in choices:
			Radiobutton(window, text = txt, padx = 25, variable = v, value = val,font = (f), command = options).grid(sticky = 'W')
			
	try:
		import winsound  #for windows system to play alaram
		winsound.PlaySound('analog-watch.wav',winsound.SND_FILENAME)
	except ImportError:
		pass
    
	window.resizable(False, False)
	window.mainloop()
	
Label(root, text="Work Time (min)", font = (f)).grid(row = 0,sticky = W)
workTime = Entry(root, font = (f), justify = RIGHT)
#workTime.insert(0, 0)  #set some default values for trial checking
workTime.grid(row = 0, column = 1)

Label(root, text="Break After (min)", font = (f)).grid(row = 1,sticky = W)
breakAfter = Entry(root, font = (f), justify = RIGHT)
#breakAfter.insert(0, 1)  
breakAfter.grid(row = 1, column = 1)

Label(root, text="Break Duration (min)", font = (f)).grid(row = 2, sticky = W)
breakDuration= Entry(root, font = (f), justify = RIGHT)
#breakDuration.insert(0,2)
breakDuration.grid(row = 2, column = 1)

mymenu = Menu() #To create menu object
list1 = Menu() #To create list of menus
list1.add_command(label = 'Defaults', command = song_path)
mymenu.add_cascade(label = 'Options', menu =list1)

root.config(menu = mymenu)

buttton1 = Button(root, text = "OK", command = ok,font = (b) )
buttton1.grid(row = 4, column = 1)

button2 = Button(root, text = "QUIT", command = root.destroy,font = (b) )
button2.grid(row = 4, column = 0)

root.resizable(False, False)
root.mainloop()
