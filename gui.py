from tkinter import *
from tkinter import messagebox
#import main.py

########## FUNCTIONS JUST TO HAVE TEXT/CLEAR TEXT FROM THE ENTRIES	##########
#Still looking for a way to make all of these into 2 functions
def on_entry_click_0(event):				#Cities Entry
	"""function that gets called whenever entry is clicked"""
	if entry_cities.get() == '# of cities':
		entry_cities.delete(0, "end") # delete all the text in the entry
		entry_cities.insert(0, '') #Insert blank for user input
		entry_cities.config(fg = 'black')

def on_entry_click_1(event):				#Cenario Entry
	if entry_cenario.get() == 'Cenario 1 or 2':
		entry_cenario.delete(0, "end") # delete all the text in the entry
		entry_cenario.insert(0, '') #Insert blank for user input
		entry_cenario.config(fg = 'black')

def on_entry_click_2(event):				#Min Distance Entry
	if entry_min_dist.get() == 'Min dist':
		entry_min_dist.delete(0, "end") # delete all the text in the entry
		entry_min_dist.insert(0, '') #Insert blank for user input
		entry_min_dist.config(fg = 'black')

def on_entry_click_3(event):				#Max Distance Entry
	if entry_max_dist.get() == 'Max dist':
		entry_max_dist.delete(0, "end") # delete all the text in the entry
		entry_max_dist.insert(0, '') #Insert blank for user input
		entry_max_dist.config(fg = 'black')


def on_focusout_0(event):				#Cities Entry
	if entry_cities.get() == '':
		entry_cities.insert(0, '# of cities')
		entry_cities.config(fg = 'grey')

	elif not is_int(entry_cities.get()):	#If the input isn't valid, the text goes red
		entry_cities.config(fg = 'red')

def on_focusout_1(event):				#Cenario Entry
	if entry_cenario.get() == '':
		entry_cenario.insert(0, 'Cenario 1 or 2')
		entry_cenario.config(fg = 'grey')

	elif not is_int(entry_cenario.get()):	#If the input isn't valid, the text goes red
		entry_cenario.config(fg = 'red')

def on_focusout_2(event):				#Min Distance Entry
	if entry_min_dist.get() == '':
		entry_min_dist.insert(0, 'Min dist')
		entry_min_dist.config(fg = 'grey')
	
	elif not is_int(entry_min_dist.get()):	#If the input isn't valid, the text goes red
		entry_min_dist.config(fg = 'red')

def on_focusout_3(event):				#Max Distance Entry
	if entry_max_dist.get() == '':
		entry_max_dist.insert(0, 'Max dist')
		entry_max_dist.config(fg = 'grey')

	elif not is_int(entry_max_dist.get()):	#If the input isn't valid, the text goes red
		entry_max_dist.config(fg = 'red')


########## THAT PART OF THE CODE THAT USES THE OTHER .py FILES AND DOES SOMETHING PRODUCTIVE ##########
def is_int(string):
	try:
		int(string)
		return True
	except ValueError:
		return False

def check_values():
	cities = is_int(entry_cities.get())
	cenario = is_int(entry_cenario.get())
	min_dist = is_int(entry_min_dist.get())
	max_dist =is_int(entry_max_dist.get())

	if (cities and cenario and min_dist and max_dist) and int(entry_min_dist.get()) < int(entry_max_dist.get()):
		#do execute the program
		print('hello')

	else:
		if not cities:
			messagebox.showerror("Invalid City Number", "The value of 'Number of cities' is not valid!")

		if not cenario:
			messagebox.showerror("Invalid Cenario", "The value of 'Cenario' is not valid!")

		if not min_dist:
			messagebox.showerror("Invalid Distance", "The value of 'Minimum city distance' is not valid!")

		if not max_dist:
			messagebox.showerror("Invalid Distance", "The value of 'Maximum city distance' is not valid!")

		if not int(entry_min_dist.get()) < int(entry_max_dist.get()):
			messagebox.showerror("Invalid values", "The 'Minimum city distance' value should be lower than the 'Maximum city distance'!")			


########## ACTUAL TKINTER'S CODE STARTS HERE ##########
root = Tk()		#does stuff
root.wm_title("AED - Project #2")	#Window Name

top_frame = Frame(root)		#Creates top frame
top_frame.pack()			#Packs the frame in the window

bottom_frame = Frame(root)		#Creates bottom frame
bottom_frame.pack(side=BOTTOM)	#Packs the frame in the window. undet the other frame

calculate_btn = Button(bottom_frame,text="Calculate",	fg="green", command=check_values) 	#button to start program
exit_btn = Button(bottom_frame,		text="Exit",		fg="green", command=root.quit)		#button to exit the GUI

calculate_btn.pack(side=LEFT)	#places the button as far to the left as it can
exit_btn.pack(side=LEFT)		#places the button as far to the left as it can


#Grid for inputs and stuff
#sticky -> [N,S,W,E]

label_cidades = Label(top_frame,	text="Numero de cidades:   ")
label_cenario = Label(top_frame,	text="Cenario Pretendido:   ")
label_dist_cid = Label(top_frame,	text="Distancia entre cidades:   ")


#Entry boxes text initial color and stuff
entry_cities = Entry(top_frame,		fg='grey')
entry_cenario = Entry(top_frame,	fg='grey')
entry_min_dist = Entry(top_frame,	fg='grey')
entry_max_dist = Entry(top_frame,	fg='grey')


#entry boxes default text
entry_cities.insert(0,		'# of cities')
entry_cenario.insert(0,		'Cenario 1 or 2')
entry_min_dist.insert(0,	'Min dist')
entry_max_dist.insert(0,	'Max dist')


#binds
entry_cities.bind('<FocusIn>',		on_entry_click_0)
entry_cenario.bind('<FocusIn>',		on_entry_click_1)
entry_min_dist.bind('<FocusIn>',	on_entry_click_2)
entry_max_dist.bind('<FocusIn>',	on_entry_click_3)

entry_cities.bind('<FocusOut>',	on_focusout_0)
entry_cenario.bind('<FocusOut>',	on_focusout_1)
entry_min_dist.bind('<FocusOut>',	on_focusout_2)
entry_max_dist.bind('<FocusOut>',	on_focusout_3)


#grid labels
label_cidades.grid(row=0,	pady=10,	sticky=E)
label_cenario.grid(row=2,	pady=10,	sticky=E)
label_dist_cid.grid(row=4,	pady=10,	sticky=E)

#grid inputs
entry_cities.grid(row=0,	column=1)
entry_cenario.grid(row=2,	column=1)
entry_min_dist.grid(row=4,	column=1)
entry_max_dist.grid(row=4,	column=2)




root.mainloop()	#required to run TkInter