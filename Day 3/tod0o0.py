import random
import tkinter
window = tkinter.Tk()
window.title("TO DO LIST")
label1=tkinter.Label(text="Your todo list is",font =("Aerial",16))
label1.place(x=50,y=100)

t1= tkinter.Entry()
t1.place(x=50,y=150)
window.minsize(400,600)
def add():
    task=t1.get()
    todo.append(task)
    listbox.insert(tkinter.END, task)
    t1.delete(0, tkinter.END)

def remove():
    taskrem=t1.get()
    if taskrem:
        if taskrem in todo:
            index = todo.index(taskrem)
            listbox.delete(index)
            todo.remove(taskrem)
        else:
            print(f"{taskrem} not found in the list.")
   
    
    
todo = []
listbox = tkinter.Listbox(window, selectbackground="yellow")
listbox.place(x=50,y=250)
btn =tkinter.Button(text = "ADD",command=add)
btn.place(x=50,y=200)
btn =tkinter.Button(text = "REMOVE",command=remove)
btn.place(x=150,y=200)
btn =tkinter.Button(text = "DONE")
btn.place(x=250,y=200)

window.mainloop()