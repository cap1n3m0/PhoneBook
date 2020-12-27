from tkinter import *

gui = Tk()

gui.geometry("800x1250")

signed_in = False

gui.configure(background="#1e558a")

title = Label(gui, text = "Contact keeper", bg = "#1e558a", fg = "#adefd1", font = ("Helvetica", 100))
subtitle = Label(gui, text = "Welcome (back)!",  bg = "#1e558a", fg = "#adefd1", font = ("Helvetica", 60))

last_name_text = Label(gui, bg = "#1e558a", fg = "#adefd1", text = "Enter last name:")
last_name_box = Entry(gui, bg = "#1e558a", fg = "#adefd1",  bd = 5)

first_name_text = Label(gui, bg = "#1e558a", fg = "#adefd1", text = "Enter first name:")
first_name_box = Entry(gui, bg = "#1e558a", fg = "#adefd1",  bd = 5)

phone_box_text = Label(gui,  bg = "#1e558a", fg = "#adefd1", text = "Enter phone number:")
phone_box = Entry(gui, bg = "#1e558a", fg = "#adefd1", bd = 5)

email_box_text = Label(gui,  bg = "#1e558a", fg = "#adefd1", text = "Enter email:")
email_box = Entry(gui, bg = "#1e558a", fg = "#adefd1", bd = 5)

blank_space = Label(gui,  bg = "#1e558a", fg = "#adefd1", text = " ", font = ("Helvetica",50))
enter_username = Label(gui, bg = "#1e558a", fg = "#adefd1", text = "Enter your username: ", font = ("Helvetica", 40))
blank_space2 = Label(gui,  bg = "#1e558a", fg = "#adefd1", text = " ", font = ("Helvetica", 30))
confirm_password = Label(gui,  bg = "#1e558a", fg = "#adefd1",text = "Confirm password: ", font = ("Helvetica", 40))
blank_space3 = Label(gui, bg = "#1e558a", fg = "#adefd1", text = " ", font = ("Helvetica", 30))
blank_space4 = Label(gui,  bg = "#1e558a", fg = "#adefd1", text = " ", font = ("Helvetica", 20))
blank_space5 = Label(gui,  bg = "#1e558a", fg = "#adefd1", text = " ", font = ("Helvetica", 10))
enter_password = Label(gui, bg = "#1e558a", fg = "#adefd1", text = "Enter your password: ", font = ("Helvetica", 40))

my_account = Label(gui, bg=  "#1e558a", fg = "#adefd1", text = "My Contacts", font = ("Helvetica", 140))

username_e = Entry(gui, bg = "#1e558a", fg = "#adefd1",  bd = 7)
password_e = Entry(gui, bg = "#1e558a", fg = "#adefd1",  bd = 7)
password_2_e = Entry(gui, bg = "#1e558a", fg = "#adefd1",  bd = 7)

contact_sheet = Text(gui, bg = "#1e558a", fg = "#adefd1", width = 60, height = 25, font = ("Helvetica", 20))
incorrect = Label(gui, text = "Incorrect!")

view_contacts_clicked = 0
ID = 0
count = 0

FILE = open("accounts", "r+")
FILE.close()

def check_account_exists(username, password): 
	FILE = open("accounts", "r")
	for line in FILE: 
		if username in line: 
			if password in line: 
				return True
	return False


def set_ID(username, password): 
	FILE = open("accounts", "r")
	count = -1
	for line in FILE: 
		count += 1
		if username in line: 
			if password in line: 
				return count


def set_accounts(): 
	FILE = open("accounts", "r")
	password = ""
	for line in FILE: 
		for char in line: 
			if not char == " ":
				password += char 


title.pack()
subtitle.pack()
blank_space.pack()

delete_contact_l1 = Label(gui, text = "Enter the last, first name,", 
	bg = "#1e558a", fg = "#adefd1", font = ("Helvetica", 18)
)

delete_contact_l2 = Label(gui, text = "phone or email", bg = "#1e558a", fg = "#adefd1", font = ("Helvetica", 18))
delete_contact_text = Entry(gui, bg = "#1e558a", fg = "#adefd1", font = ("Helvetica", 15))

def del_contact(): 
	delete_contact_l1.place(relx = "0.03", rely = "0.52", relwidth = "0.32")
	delete_contact_l2.place(relx = "0.03", rely = "0.57", relwidth = "0.33")
	delete_contact_text.place(relx = "0.035", rely = "0.62", relwidth = "0.32")
	delete_b.place(relx = "0.035", rely = "0.8", relwidth = "0.32")
	first_name_text.place_forget()
	first_name_box.place_forget()
	last_name_text.place_forget()
	last_name_box.place_forget()
	phone_box_text.place_forget()
	phone_box.place_forget()
	email_box_text.place_forget()
	email_box.place_forget()
	save_new.place_forget()


def clear_contact(file_name, contact): 
	count = -1
	EDIT = open(file_name, "r")
	data = ""
	for line in EDIT: 
		count += 1 
		if contact in line: 
			contact_sheet.delete('1.0', END)
		else: 
			data += line
	contact_sheet.insert(END, data)
	FILE = open(file_name, "w")
	FILE.write(data)
	FILE.close()


delete_b = Button(gui, text = "Delete", bg = "#1e558a", fg = "#adefd1", font = ("Helvetica", 18), 
	command = lambda: clear_contact(username_e.get(), delete_contact_text.get()))


def clear_all(file_name):
	global contact_sheet
	FILE = open(str(file_name), "w+")
	FILE.write("")
	contact_sheet.delete('1.0', END)
	FILE.close()


def edit_accounts_file(username, password, ID): 
	FILE = open("accounts", "a")
	FILE.write(username + " " + password + " " + str(ID) + "\n")


def edit_text_file(file_name, contact, phone): 
	print("running")
	FILE = open(file_name, "r")
	can_write = True
	for line in FILE: 
		if phone in line: 
			print(line)
			can_write = False
	FILE.close()
	FILE = open(file_name, "a")
	if can_write: 
		FILE.write(str(contact))
	FILE.close()


def show_account(): 
	global no_account
	global login_b
	global sign_out_b
	global enter_username
	global enter_password
	global username_e
	global password_e
	global password_2_e
	global title
	global confirm_password
	global add_contact_b
	global clear_all_contacts
	global delete_contact
	global save_account_b
	global blank_space4
	global blank_space3
	global blank_space
	global blank_space2
	global blank_space5
	global make_account
	global subtitle
	global ID
	if signed_in: 
		title.pack_forget()
		subtitle.pack_forget()
		blank_space4.pack_forget()
		blank_space3.pack_forget()
		blank_space2.pack_forget()
		blank_space.pack_forget()
		login_b.place_forget()
		no_account.place_forget()
		enter_username.place_forget()
		enter_password.place_forget()
		save_account_b.place_forget()
		username_e.place_forget()
		password_e.place_forget()
		confirm_password.place_forget()
		password_2_e.place_forget()
		my_account.pack()
		delete_contact_l1.place_forget()
		delete_contact_l2.place_forget()
		delete_contact_text.place_forget()
		blank_space5.pack()
		sign_out_b.place(relx = "0.03", rely = "0.3", relwidth = "0.2")
		add_contact_b.place(relx = "0.03", rely = "0.35", relwidth = "0.3")
		clear_all_contacts.place(relx = "0.03", rely = "0.4", relwidth = "0.3")
		delete_contact.place(relx = "0.03", rely = "0.45", relwidth = "0.3")
		view_contacts()
	

def make_account(): 
	global password_2_e
	global password_e
	global username_e
	global ID
	global signed_in
	ID = 1
	if not password_e.get() == "" and not password_2_e.get() == "" and not username_e.get() == "":
		if password_e.get() == password_2_e.get(): 
			if not check_account_exists(username_e.get(), password_e.get()): 
				FILE = open("accounts")
				for line in FILE: 
					ID += 1
				FILE = open(username_e.get(), "w")
				edit_accounts_file(username_e.get(), password_e.get(), ID)
				signed_in = True
				show_account()		


save_account_b = Button(gui, border = '0', text = "Save account", highlightbackground = "#00203f", fg = "#adefd1", height = 2, width = 8, font = ("System", 20), command = make_account)

def show_login(): 
	global enter_username
	global my_account
	global blank_space2
	global enter_password
	global username_e
	global password_e
	global login_b
	global no_account
	global contact_sheet
	global sign_out_b
	global title
	my_account.pack_forget()
	title.pack()
	subtitle.pack()
	sign_out_b.place_forget()
	contact_sheet.place_forget()
	enter_username.place(relx = 0.2, rely = 0.35, relwidth = 0.6)
	username_e.place(relx = 0.35, rely = 0.45, relwidth = 0.25)
	blank_space2.place(relx = 0.35, rely = 0.5, relwidth = 0.3)
	enter_password.place(relx = 0.2, rely = 0.55, relwidth = 0.6)
	password_e.place(relx = 0.35, rely = 0.65, relwidth = 0.25)
	blank_space3.pack()
	login_b.place(relx = 0.32, rely = 0.75, relwidth = 0.3)
	blank_space4.pack()
	no_account.place(relx = 0.32, rely = 0.85, relwidth = 0.3)


def sign_in(): 
	global signed_in
	global ID
	global view_contacts_clicked
	if not username_e.get() == "" and not password_e.get() == "": 
		if check_account_exists(username_e.get(), password_e.get()): 
			signed_in = True
			view_contacts_clicked = 0
			ID = set_ID(username_e.get(), password_e.get())
			show_account()


def sign_up(): 
	global signed_in
	global username_e
	global password_e
	global no_account
	no_account.place_forget()
	login_b.place_forget()
	confirm_password.place(relx = 0.25, rely = 0.75, relwidth = 0.5)
	password_2_e.place(relx = 0.35, rely = 0.85, relwidth = 0.25)
	save_account_b.place(relx = 0.35, rely = 0.92, relwidth = 0.25)


def add_contact(): 
	global first_name_text
	global first_name_box
	delete_contact_l1.place_forget()
	delete_contact_l2.place_forget()
	delete_b.place_forget()
	delete_contact_text.place_forget()
	first_name_text.place(relx = "0.03", rely = "0.54", relwidth = "0.2")
	first_name_box.place(relx = "0.03", rely = "0.58", relwidth = "0.2")
	last_name_text.place(relx = "0.03", rely = "0.62", relwidth = "0.2")
	last_name_box.place(relx = "0.03", rely = "0.66", relwidth = "0.2")
	phone_box_text.place(relx = "0.03", rely = "0.7", relwidth = "0.2")
	phone_box.place(relx = "0.03", rely = "0.74", relwidth = "0.2")
	email_box_text.place(relx = "0.03", rely = "0.78", relwidth = "0.2")
	email_box.place(relx = "0.03", rely = "0.82", relwidth = "0.2")
	save_new.place(relx = "0.03", rely = "0.9", relwidth = "0.29")


def add_to_list(file_name, f, l, p, e):
	FILE = open(file_name, "r")
	if not (str(l) in FILE): 
		if not (str(f) in FILE): 
			if not (str(p) in FILE): 
				if not (str(e) in FILE):  
					new_contact = str(l) + " " + str(f) + " " + str(p) + " " + str(e) + "\n"
					edit_text_file(file_name, new_contact, p)
					view_contacts()


save_new = Button(gui, text = "Save new", highlightbackground = "#00203f", fg = "#adefd1", font = ("System", 25), 
	command = lambda: add_to_list(username_e.get(), last_name_box.get(), first_name_box.get(), phone_box.get(), email_box.get())
	)
	

def sign_out(): 
	global signed_in
	global add_contact_b
	global enter_password
	global phone_box
	global email_box 
	global last_name_text
	global first_name_text
	global email_box_text
	global phone_box_text
	global first_name_box
	global last_name_box
	global enter_username
	global save_new
	signed_in = False
	save_new.place_forget()
	clear_all_contacts.place_forget()
	delete_contact_l1.place_forget()
	delete_contact_l2.place_forget()
	delete_contact_text.place_forget()
	delete_contact.place_forget()
	delete_b.place_forget()
	sign_out_b.place_forget()
	password_e.place_forget()
	email_box_text.place_forget()
	phone_box_text.place_forget()
	last_name_text.place_forget()
	first_name_text.place_forget()
	phone_box.place_forget()
	email_box.place_forget()
	last_name_box.place_forget()
	first_name_box.place_forget()
	add_contact_b.place_forget()
	view_all_contacts.place_forget()
	show_login()

sign_out_b = Button(gui, text = "Sign out",  highlightbackground = "#1e558a", fg = "#adefd1", font = ("Helvetica", 20), command = sign_out)
login_b = Button(gui, text = "Proceed", highlightbackground = "#1e558a", fg = "#adefd1", height = 2, width = 10, font = ("System", 20), command = sign_in)
no_account = Button(gui, text = "No account? Make one.", highlightbackground = "#1e558a", fg = "#adefd1", height = 2, width = 20, font = ("System", 20), command = sign_up)
add_contact_b = Button(gui, text = "Add New Contact", highlightbackground = "#1e558a", fg = "#adefd1", font = ("System", 30), command = add_contact)
clear_all_contacts = Button(gui, text = "Clear all contacts", highlightbackground = "#1e558a", fg = "#adefd1", font = ("System", 30), command = lambda: clear_all(username_e.get()))
delete_contact = Button(gui, text = "Delete Contact", highlightbackground = "#1e558a", fg = "#adefd1", font = ("System", 30), command = del_contact)

def view_contacts(): 
	global username_e	
	global contact_sheet
	FILE = open(username_e.get(), "r")
	contact_sheet.delete('1.0', END)
	contact_sheet.insert(END, FILE.read())
	contact_sheet.place(relx = 0.37, rely = 0.22, relwidth = 0.6)
	FILE.close()

view_all_contacts = Button(gui, text = "View all contacts", highlightbackground = "#1e558a", fg = "#adefd1", command = view_contacts)

show_login()

gui.mainloop()