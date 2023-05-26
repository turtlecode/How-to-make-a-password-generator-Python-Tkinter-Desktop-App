from tkinter import *
from random import randint
import screeninfo

screenWidth = screeninfo.get_monitors()[0].width
screenHeight = screeninfo.get_monitors()[0].height

root = Tk()
root.geometry(f"500x450+{int(screenWidth/2-500/2)}+{int(screenHeight/2-450/2)}")
root.title("Password generator")
root.resizable(False, False)

def new_rand():
	pw_entry.delete(0, END)

	try:
		pw_length = int(characters_entry.get())
	except:
		characters_entry.delete(0, END)
		characters_entry.insert(0, "Only numbers")

		return
	
	my_password = ''

	for x in range(pw_length):
		my_password += chr(randint(33,126))

	pw_entry.insert(0, word_entry.get() + my_password)

def clipper():
	root.clipboard_clear()
	root.clipboard_append(pw_entry.get())

lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

characters_entry = Entry(lf, font=("Helvetica", 24))
characters_entry.pack(pady=20, padx=20)

word_lf = LabelFrame(root, text="Write a Word")
word_lf.pack(pady=20)

word_entry = Entry(word_lf, font=("Helvetica", 24))
word_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboad", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()