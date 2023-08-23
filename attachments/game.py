#Imported Necessary Modules
from tkinter import *
import sqlite3

#Created a Function Named game Which Stores all the Codes of Main Page
# so it can be called later from another program
def game():
    #Created a Tkinter Window named WIN
    WIN = Tk()
    #Placed Image as Iconphoto on Window
    logo_image = PhotoImage(file="ab.png")
    WIN.iconphoto(False, logo_image)
    #Named Tkinter Window
    WIN.title('Underwater Adventure')
    #Set size of Tkinter Window   
    WIN.geometry('360x640')
    #Placed backround.png image as BAckground to a TKinter Window
    background = PhotoImage(file="ab.png")
    label_background = Label(WIN,image=background,borderwidth=0)
    label_background.place(x=0,y=0)

    #Started Database named player_details and created a Table Named profile if mot created with
    #full_name,age,password,score as a value inside it.
    conn = sqlite3.connect('player_details.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS profile (
        full_name text,
        age integer,
        user_name text,
        password text,
        score integer
        )""")
    conn.commit()
    conn.close()

    #Started a database named current_user and created a Table Named user_data if
    #it doesnt't exist and stored user_name_value in it.
    conn = sqlite3.connect('current_user.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS user_data (
            user_name_value text
            )""")
    conn.commit()
    conn.close()

    #tarted a Database name current_user and Deleted all data Stored Before in user_data table
    #so only data of current user is stored in database.
    conn = sqlite3.connect('current_user.db')
    c = conn.cursor()
    c.execute('DELETE FROM user_data;', );
    conn.commit()
    conn.close()

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 12)

    # created a function named login_page
    def login_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from login import login as open_login
        open_login()

    # created a function named register_page
    def register_page():
        '''Destroys the tkinter window and call open_register function i.e. register function from a register page'''
        WIN.destroy()
        from register import register as open_register
        open_register()

    #Created a Function named on_enter_login with 'e' as one parameter
    def on_enter_login(e):
        '''Changed Background and Foreground of Login Button named login_button
        to #ABBC41 and white respectively when function is called.'''
        login_button.config(background='#ABBC41',foreground= "white")

    #Created a Function named on_leave_login with 'e' as one parameter
    def on_leave_login(e):
        '''Changed Background and Foreground of Login Button named login_button to
        green3 and black respectively when function is called.'''
        login_button.config(background= 'green3', foreground= 'black')

    #created a Login Button which calls login_page function when pressed
    login_button = Button(WIN,text="Login",padx=10,borderwidth=0,font=tfont_tup,background= 'green3', foreground= 'black',command=login_page)
    login_button.place(x = 148,y = 360)
    #Created a Bind i.e. When Entered inside a Login button calls on_enter_login function
    #and when leaves the Login button calls on_leave_login function
    login_button.bind('<Enter>',on_enter_login)
    login_button.bind('<Leave>',on_leave_login)

    # Created a Function named on_enter_register with 'e' as one parameter
    def on_enter_register(e):
        '''Changed Background and Foreground of Register Button named register_button
        to #ABBC41 and white respectively when function is called.'''
        register_button.config(background='#ABBC41',foreground= "white")

    # Created a Function named on_leave_register with 'e' as one parameter
    def on_leave_register(e):
        '''Changed Background and Foreground of Register Button named register_button to
        green3 and black respectively when function is called.'''
        register_button.config(background= 'green3', foreground= 'black')

    # created a Register Button which calls register_page function when pressed
    register_button = Button(WIN,text="Register",padx=10,borderwidth=0,font=tfont_tup,background= 'green3', foreground= 'black',command=register_page)
    register_button.place(x=135,y=425)
    #Created a Bind i.e. When Entered inside a Register button calls on_enter_register function
    #and when leaves the Register button calls on_leave_register function
    register_button.bind('<Enter>',on_enter_register)
    register_button.bind('<Leave>',on_leave_register)

    #Updates all Into TKinter Window
    WIN.mainloop()

#calls game Function
game()
