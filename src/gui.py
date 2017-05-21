from tkinter import *
from tkinter import messagebox
import main

########## FUNCTIONS JUST TO HAVE TEXT/CLEAR TEXT FROM THE ENTRIES	##########
#Still looking for a way to make all of these into 2 functions
def on_entry_click_0(event):				#Cities Entry
	"""function that gets called whenever entry is clicked"""
	entry_cities.config(fg = 'black')
	if entry_cities.get() == '# of cities':
		entry_cities.delete(0, "end") 		#delete all the text in the entry
		entry_cities.insert(0, '') 			#Insert blank for user input

def on_entry_click_1(event):				#Cenario Entry
	entry_cenario.config(fg = 'black')
	if entry_cenario.get() == 'Cenario 1 or 2':
		entry_cenario.delete(0, "end")		#delete all the text in the entry
		entry_cenario.insert(0, '')			#Insert blank for user input


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


########## CHECKBOX STUFF ###########
def on_check_cenario_1():
	cenario_2_check.deselect()

def on_check_cenario_2():
	cenario_1_check.deselect()


#J#M#S#M#o#n#t#e#i#r#o# THAT PART OF THE CODE THAT USES THE OTHER .py FILES AND DOES SOMETHING PRODUCTIVE #J#M#S#M#o#n#t#e#i#r#o#
def is_int(string):
	try:
		int(string)
		return True
	except ValueError:
		return False

def check_values():
	cities = is_int(entry_cities.get())
	cenario = (cenario_1.get() or cenario_2.get())
	algorithm = (brute.get() or brute_opt.get() or recursive.get() or recursive_g.get())

	if cities and cenario and algorithm:
		#do execute the program
		#0 = brute || 1 = brute_optimised || 2 = recursive || 3 = recursive greedy

		if int(entry_cities.get()) < 2:
			messagebox.showerror("Invalid City Value",	"The city number must be greater or equal to 2.")
			return

		map_graph = main.geraMapa(entry_cities.get(), [cenario_1.get(), cenario_2.get()])


		if brute.get():
			run('Results - Brute Force',				0, map_graph)

		if brute_opt.get():
			run('Results - Brute Force Optimized',		1, map_graph)

		if recursive.get():
			run('Results - Recursive',					2, map_graph)

		if recursive_g.get():
			run('Results - Recursive Greedy',			3, map_graph)


	else:
		if cities:
			if int(entry_cities.get()) < 2:
				messagebox.showerror("Invalid City Value",	"The city number must be greater or equal to 2.")

		if not cities:
			messagebox.showerror("Invalid City Number",	"The value of 'Number of cities' is not valid!")

		if not cenario:
			messagebox.showerror("Invalid Cenario",		"Please select one of the cenarios.")

		if not algorithm:
			messagebox.showerror("Invalid Algorithm",	"Please select at least one of the algorithms.")


def run(window_title, algorithm, map_graph):
	results = main.main(map_graph, [cenario_1.get(), cenario_2.get()], algorithm)

	###Popup Window with results###
	pop_up = Toplevel()
	pop_up.title(window_title)

	#Pop-up labels
	label_origin = Label(pop_up,	text="City of origin: ")
	label_total_dist = Label(pop_up,text="Total distance: ")
	label_path = Label(pop_up,		text="Route chosen: ")
	label_time = Label(pop_up,		text="Calculated in: ")

	#Pop-up info to be displayed
	grafo_info = Message(pop_up, 		width=400, text=str(results[0]))	#Mess arround with the width parameter to fit all your needs
	origin_info = Message(pop_up, 		width=300, text=str(results[1]))
	total_dist_info = Message(pop_up, 	width=300, text=str(results[2]))
	path_info = Message(pop_up, 		width=300, text=str(results[3]))
	time_info = Message(pop_up, 		width=300, text=str(results[4]))

	#Grid it!
	label_origin.grid(row=10,		pady=10, sticky=E)
	label_total_dist.grid(row=12,	pady=10, sticky=E)
	label_path.grid(row=14,			pady=10, sticky=E)
	label_time.grid(row=16,			pady=10, sticky=E)

	grafo_info.grid(row=0, 			columnspan=4, pady=10, padx=10)
	origin_info.grid(row=10,		column=2, pady=10, sticky=W)
	total_dist_info.grid(row=12,	column=2, pady=10, sticky=W)
	path_info.grid(row=14,			column=2, pady=10, sticky=W)
	time_info.grid(row=16,			column=2, pady=10, sticky=W)


	btn = Button(pop_up, text="Dismiss", command=pop_up.destroy)
	btn.grid(row=100,	pady=10, column=1, sticky=W)


########## ACTUAL TKINTER'S CODE STARTS HERE (Most of it anyways)##########
###Main Window with parameter and such###
root = Tk()		#does stuff
root.wm_title("AED - Project #2")	#Window Name

top_frame = Frame(root)		#Creates top frame
top_frame.pack()			#Packs the frame in the window

bottom_frame = Frame(root)		#Creates bottom frame
bottom_frame.pack(side=BOTTOM)	#Packs the frame in the window. under the other frame

calculate_btn = Button(bottom_frame,text="Calculate",	fg="green", command=check_values) 	#button to start program
exit_btn = Button(bottom_frame,		text="Exit",		fg="green", command=root.quit)		#button to exit the GUI

calculate_btn.pack(side=LEFT)	#places the button as far to the left as it can
exit_btn.pack(side=LEFT)		#places the button as far to the left as it can


#Grid for inputs and stuff
#sticky -> [N,S,W,E]
label_cities = Label(top_frame,		text="Number of cities:   ")
label_cenario = Label(top_frame,	text="Cenario:   ")
label_algorithm = Label(top_frame,	text="Algorithm to be used:   ")
label_filler = Label(top_frame,		text="")


#Entry boxes text initial color and stuff
entry_cities = Entry(top_frame,		fg='grey')
entry_min_dist = Entry(top_frame,	fg='grey')
entry_max_dist = Entry(top_frame,	fg='grey')


#entry boxes default text
entry_cities.insert(0,		'# of cities')

#Var for checkboxes
cenario_1 = BooleanVar()
cenario_2 = BooleanVar()
brute = BooleanVar()
brute_opt = BooleanVar()
recursive = BooleanVar()
recursive_g = BooleanVar()

#Checkboxes for different algorithms
cenario_1_check = Checkbutton(top_frame,	text="1",						onvalue=True, offvalue=False, variable=cenario_1, command=on_check_cenario_1)
cenario_2_check = Checkbutton(top_frame,	text="2",						onvalue=True, offvalue=False, variable=cenario_2, command=on_check_cenario_2)
brute_check = Checkbutton(top_frame,		text="Brute Force ",			onvalue=True, offvalue=False, variable=brute)
brute_opt_check = Checkbutton(top_frame,	text="Brute Force Optimized",	onvalue=True, offvalue=False, variable=brute_opt)
recursive_check = Checkbutton(top_frame,	text="Recursive ",				onvalue=True, offvalue=False, variable=recursive)
recursive_g_check = Checkbutton(top_frame,	text="Recursive Greedy",		onvalue=True, offvalue=False, variable=recursive_g)

#binds
entry_cities.bind('<FocusIn>',		on_entry_click_0)

entry_cities.bind('<FocusOut>',		on_focusout_0)

#grid labels
label_cities.grid(row=0,	pady=10,	sticky=E)
label_cenario.grid(row=2,	pady=10,	sticky=E)
label_algorithm.grid(row=6,	pady=10,	sticky=E)
label_filler.grid(row=10,	pady=10,	sticky=E)


#grid Entries
entry_cities.grid(row=0,	column=1)

#grid checkboxes
cenario_1_check.grid(row=2,		column=1, sticky=W)
cenario_2_check.grid(row=2,		column=1, sticky=E)
brute_check.grid(row=6,			column=1, sticky=W)
brute_opt_check.grid(row=8,		column=1, sticky=W)
recursive_check.grid(row=10,	column=1, sticky=W)
recursive_g_check.grid(row=12,	column=1, sticky=W)


root.mainloop() #required to run TkInter