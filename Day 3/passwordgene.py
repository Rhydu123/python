import random
import tkinter
window = tkinter.Tk()
window.title("PASSWORD GENERATOR")
window.minsize(500,400)
t1= tkinter.Entry()
t1.place(x=160,y=50)
t2= tkinter.Entry()
t2.place(x=160,y=100)
t3= tkinter.Entry()
t3.place(x=160,y=150)
label1=tkinter.Label(text="No.of letters : ",font =("Aerial",8))
label1.place(x=50,y=50)
label2=tkinter.Label(text="No. of symbols: ",font =("Aerial",8))
label2.place(x=50,y=100)
label3=tkinter.Label(text="No. of numbers : ",font =("Aerial",8))
label3.place(x=50,y=150)
def generate():
    let= t1.get()
    sym=t2.get()
    num=t3.get()
    password_list = []
    for char in range(0,int(let)):
        password_list += random.choice(letters)

    for char in range(0, int(sym)):
        password_list += random.choice(symbols)

    for char in range(0,int(num)):
        password_list += random.choice(numbers)

    random.shuffle(password_list)


    password = ""
    for char in password_list:
        password += char
    label4=tkinter.Label(text="Password is : "+ password)
    label4.place(x=150,y=300)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
btn =tkinter. Button(text = "GENERATE",command=generate)
btn.place(x=200,y=250) 
window.mainloop()