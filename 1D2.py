from tkinter import*
import random
root=Tk()
root.geometry("500x500")
root.title("1D Lists")
label1=Label(root)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
list1=["Bottle","Tiffin","ID card","Chocolate,Chips","Tickets","Hankey"]
label1["text"]=list1
label2=Label(root)
label2.place(relx=0.5,rely=0.6, anchor=CENTER)
def bag():
    list2=random.sample(range(0,6),1)
    label2["text"]="put item number"+str(list2)

button=Button(root,text="Generate Random List", command=bag)
button.place(relx=0.5, rely=0.4, anchor=CENTER)










root.mainloop()