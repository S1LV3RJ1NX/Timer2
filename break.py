from tkinter import *
from tkinter import messagebox
import subprocess
import webbrowser

root = Tk()
root.title("Break Reminder")
root.geometry("600x200+1000+300")

f = "times", 14, "italic"
b = "arial", 10, "bold"
v = IntVar()


choices = [ ('Music',1), ('Motivate',2),('Ignite',3), ('Nothing',4)]


def ok():

	wT = int(workTime.get())*1000
	bA = int(breakAfter.get())*1000
	
	breaks_consumed = 0
	total_breaks_allowed = int(wT / bA)
	global window
	
	root.withdraw()
	print(total_breaks_allowed)
	root.after(bA)
	window = Toplevel() #for child window
	window.geometry("600x250+1000+300")
	window.title("TIME FOR BREAK")
	Label(window, text = 'What you want to do?',padx=25,justify=LEFT,font = (f)).pack(anchor=W)
	
	def task():
		nonlocal breaks_consumed 
		nonlocal total_breaks_allowed
		if (breaks_consumed >= total_breaks_allowed):
			messagebox.showinfo(title = 'Reminder', message= 'Timer Ended!!')
			window.destroy()
			root.destroy()
		else:
			print(breaks_consumed)
			root.after(bA)
			window.deiconify()
			breaks_consumed = breaks_consumed + 1

	def process():
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
			subprocess.Popen( ["xdg-open", '/home/prathamesh/Music/']) 
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
			Radiobutton(window, text = txt, padx = 25, variable = v, value = val,font = (f), command = options).pack(anchor=W)

	
	window.mainloop()
	
	
Label(root, text="Work Time (min)", font = (f)).grid(row = 0,sticky = W)
workTime = Entry(root, font = (f))
workTime.insert(0, 20)
workTime.grid(row = 0, column = 1)

Label(root, text="Break After (min)", font = (f)).grid(row = 1,sticky = W)
breakAfter = Entry(root, font = (f))
breakAfter.insert(0, 5)
breakAfter.grid(row = 1, column = 1)

Label(root, text="Break Duration (min)", font = (f)).grid(row = 2, sticky = W)
breakDuration= Entry(root, font = (f))
breakDuration.insert(0,2)
breakDuration.grid(row = 2, column = 1)

buttton1 = Button(root, text = "OK", command = ok,font = (b) )
buttton1.grid(row = 4, column = 1)

button2 = Button(root, text = "QUIT", command = root.destroy,font = (b) )
button2.grid(row = 4, column = 0)



root.mainloop()