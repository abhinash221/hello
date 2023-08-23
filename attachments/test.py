from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
#import mysql.connector


window = Tk()
window.title("Login Window")
window.geometry("800x600")
window.resizable(1, 1)

files= Image.open("hptl.png")
files=files.resize((1600,1200), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(files)
bgimg= Label(window, image=photo)
bgimg.pack()



def login():
 
    if (usernameEntry.get() == "") or (passwordEntry.get() == ""):
        messagebox.showwarning("Warning", "Fields are empty. Please, insert username and password.")
    else:
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="mydata")
            cur = con.cursor()
        
            cur.execute('select * from users where username=%s and password=%s',(usernameEntry.get(),passwordEntry.get(),))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error !", "No user found ! Please Sign Up First.")

            else:
                messagebox.showinfo("Login", "Login Successfully")
                # self.root.destroy()
                window.withdraw()
                import hospital

        except EXCEPTION as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")



def close():

    user_response = messagebox.askyesno("Exit", "Do you want to exit ? ")
    if user_response == 1:
        window.close()

def register():
   
    window.destroy()
    import registration1
    

  

# labels
usernameLabel = Label(window, text="Username", font=("Times", 22, "bold"), bg="black", fg="white")

passwordLabel = Label(window, text="Password", font=("Times", 22, "bold"), bg="black", fg="white")

# Entries
usernameEntry = Entry(window, font=("times", 20, "bold"), bd=3, relief=SUNKEN)
passwordEntry = Entry(window, font=("times", 20, "bold"), bd=3, relief=SUNKEN, show='•')

# buttons

loginButton = Button(window, text="Login", font=("Copperplate", 20, "bold"), highlightbackground="green", fg="black", command=login)
signupButton = Button(window, text="Signup", font=("Copperplate", 20, "bold"), highlightbackground="yellow", fg="black", command=register)
exitButton = Button(window, text="Forgot Password", font=("Copperplate",13, "bold"), highlightbackground="red", fg="black", command=close)


# locations of labels, entries, button
usernameLabel.place(x=50, y=35)
passwordLabel.place(x=50, y=90)
usernameEntry.place(x=200, y=35)
passwordEntry.place(x=200, y=90)


loginButton.place(x=160, y= 170)
signupButton.place(x= 160, y=240)
exitButton.place(x=160, y=310)




window.mainloop()