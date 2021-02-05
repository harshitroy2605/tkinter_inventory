from tkinter import *
from tkinter import messagebox
import backend
import json

window=Tk()
frame = Frame(window)
window.geometry("1600x790")



#-------------------global variables-------------------------

OPTIONS = [
"Create",
"Search",
"Edit"
]


list_of_inserted_chategory=[]



#----------------------initial gui parts -------------------------#

entry_section_label=Label(window,text="Entry section",font=("times",20,"bold"))
entry_section_label.place(x=200,y=120)



selected_tuple=[]



def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    '''entry1.delete(0,END)
    entry1.insert(END,selected_tuple[1])
    entry2.delete(0,END)
    entry2.insert(END,selected_tuple[2])
    entry3.delete(0,END)
    entry3.insert(END,selected_tuple[3])
    entry4.delete(0,END)
    entry4.insert(END,selected_tuple[4])
    entry5.delete(0,END)
    entry5.insert(END,selected_tuple[5])
    entry6.delete(0,END)
    entry6.insert(END,selected_tuple[6])'''


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


'''def search_command():
    list1.delete(0,END)
    for row in back.search(name_text.get(),address_text.get(),phone_number_text.get(),roomtype_text.get(),noof_text.get(),amount_text.get()):
        list1.insert(END,row)'''




def get_value(new_label_y,product_category_n):
	global list_of_inserted_chategory
	if product_category_n is not None:
		a=product_category_n.get(1.0,END+"-1c")
		list_of_inserted_chategory.append(a)

	add_more_category_function(new_label_y)




def insert_entry(name,quantity):
	global list_of_inserted_chategory
	backend.insert(name,quantity,list_of_inserted_chategory)
	list_of_inserted_chategory=[]
	



def search_entry(name,chategory):
	print(name,chategory)
	list1.delete(0,END)
	for row in backend.search(name,chategory):
		list1.insert(END,row)












#------------------------function to add more category in create --------#

def add_more_category_function(chategory):
	global list_of_inserted_chategory
	list_of_inserted_chategory.append(chategory)
	return list_of_inserted_chategory



#--------------what to do option----------#

 
what_to_do_label=Label(window,text="What Action you want to Perform",font=("times",18,"bold"))
what_to_do_label.place(x=20,y=200)

choice = StringVar(window)
choice.set("select")

what_to_do_choice = OptionMenu(window, choice, *OPTIONS)
what_to_do_choice.place(x=390,y=202)




#--------------function to iterate between various choices ------------------------#


def option_gui():
	action_want_to_perform=choice.get()
	if choice.get()=="Create":

		product_name_label=Label(window,text="product name",font=("times",18,"bold"))
		product_name_label.place(x=30,y=300)
		
		product_name=Text(window,height=1,width=14)
		product_name.place(x=390,y=300)

		product_quantity_label=Label(window,text="Quantity",font=("times",18,"bold"))
		product_quantity_label.place(x=30,y=350)

		product_quantity=Text(window,height=1,width=14)
		product_quantity.place(x=390,y=350)
		quantity=product_quantity.get(1.0,END+"-1c")


		final_insertion_button=Button(window,text="submit",bg = "white",width=10,command=lambda:[insert_entry(product_name.get(1.0,END+"-1c"),product_quantity.get(1.0,END+"-1c")),product_name.delete('1.0',END),product_quantity.delete('1.0',END)])
		final_insertion_button.place(x=200,y=450)


		product_category_label=Label(window,text="Add Product category ",font=("times",18,"bold"))
		product_category_label.place(x=30,y=400)


		product_category_n=Text(window,height=1,width=14)
		product_category_n.place(x=390,y=400)


		add_more_category_button=Button(window,text="add",bg = "white",width=5,command=lambda:[add_more_category_function(product_category_n.get(1.0,END+"-1c")),product_category_n.delete('1.0',END)])
		add_more_category_button.place(x=520,y=400)


		clear_all_button=Button(window,text="remove all",bg = "white",width=15,command=lambda:[product_name_label.place_forget(),product_name.place_forget(),product_quantity.place_forget(),product_quantity_label.place_forget(),product_category_label.place_forget(),product_category_n.place_forget(),add_more_category_button.place_forget(),final_insertion_button.place_forget(),add_more_category_button.place_forget(),clear_all_button.place_forget()])
		clear_all_button.place(x=340,y=448)



	elif choice.get()=="Search":
		product_name_label=Label(window,text="product name",font=("times",18,"bold"))
		product_name_label.place(x=30,y=300)
		
		product_name=Text(window,height=1,width=14)
		product_name.place(x=390,y=300)


		product_category_label=Label(window,text="Enter any Product category ",font=("times",18,"bold"))
		product_category_label.place(x=30,y=350)


		product_category_n=Text(window,height=1,width=14)
		product_category_n.place(x=390,y=350)


		final_insertion_button=Button(window,text="submit",bg = "white",width=10,command=lambda:search_entry(product_name.get(1.0,END+"-1c"),product_category_n.get(1.0,END+"-1c")))
		final_insertion_button.place(x=200,y=450)

		clear_all_button=Button(window,text="remove all",bg = "white",width=15,command=lambda:[product_name_label.place_forget(),product_name.place_forget(),product_category_label.place_forget(),product_category_n.place_forget(),final_insertion_button.place_forget(),clear_all_button.place_forget()])
		clear_all_button.place(x=340,y=448)



 

#---------- button to final ---------------#

button=Button(window,text="search",bg = "white",width=20,command=option_gui)
button.place(x=300,y=250)




list1=Listbox(window,height=20,width=59)
list1.place(x=600,y=200)

scrl=Scrollbar(window)
scrl.place(x=960,y=200)

list1.configure(yscrollcommand=scrl.set)
scrl.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="view all",width=12, command=view_command)
b1.place(x=700,y=600)





window.mainloop()