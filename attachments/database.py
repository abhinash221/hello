-mimport tkinter
from tkinter import*
import sqlite3

WIN = Tk()
logo_image = PhotoImage(file="ab.png")
WIN.iconphoto(False, logo_image)

WIN.title('Underwater Adventure')


'''
c.execute("""CREATE TABLE IF NOT EXISTS profile (
    full_name text,
    age integer,
    user_name text,
    password text
)""")
'''

def delete():
    conn = sqlite3.connect('current_user.db')
    c = conn.cursor()

    c.execute('DELETE FROM user_data;', );
    conn.commit()
    conn.close()
    conn = sqlite3.connect('player_details.db')
    c = conn.cursor()

    #c.execute('DELETE FROM profile;', );

    '''
    dropTableStatement = "DROP TABLE profile"
    c.execute(dropTableStatement)

    '''
    '''

    c.execute("INSERT INTO profile VALUES (:full_name, :age, :user_name, :password)",
              {
                  'full_name':full_name.get(),
                  'age':age.get(),
                  'user_name':user_name.get(),
                  'password':password.get()
              })
    '''


    conn.commit()
    conn.close()
    '''

    full_name.delete(0,END)
    age.delete(0, END)
    user_name.delete(0, END)
    password.delete(0, END)
'''

def query():
    conn = sqlite3.connect('player_details.db')

    c1 = conn.cursor()


    c1.execute("SELECT *,oid FROM profile")
    records_data = c1.fetchall()
    print(records_data)

    '''
    print_record = ''
    for record in records:
        print_record += str(record[3]+' '+ str(record[4]) )

    query_label = Label(WIN,text=print_record)
    query_label.grid(row = 8,column = 0)

    '''
    conn.commit()
    conn.close()

    conn = sqlite3.connect('current_user.db')

    c1 = conn.cursor()
    c1.execute("SELECT *,oid FROM user_data")
    record_data = c1.fetchall()
    print(record_data)
    conn.commit()
    conn.close()


'''
full_name = Entry(WIN,width=20)
full_name.grid(row = 0,column=1,padx=20)
age = Entry(WIN,width=20)
age.grid(row = 1,column=1)
'''
user_name = Entry(WIN,width=20)
user_name.grid(row = 2,column=1)
password = Entry(WIN,width=20)
password.grid(row = 3,column=1)

'''
full_name_label = Label(WIN,text = "Full NAme")
full_name_label.grid(row=0,column=0)
age_label = Label(WIN,text = "Age")
age_label.grid(row=1,column=0)
'''
user_name_label = Label(WIN,text = "USer NAme")
user_name_label.grid(row=2,column=0)
password_label = Label(WIN,text = "Password")
password_label.grid(row=3,column=0)

def update():
    record_id = user_name.get()
    conn = sqlite3.connect('player_details.db')
    c = conn.cursor()

    data_to_be_updated = '''UPDATE profile
                            SET score = ?
                            WHERE oid = ?'''
    data = (password.get(), record_id)
    c.execute(data_to_be_updated, data)

    conn.commit()
    conn.close()


delete_btm = Button(WIN,text="Delete",command=delete)
delete_btm.grid(row = 4,column = 0,columnspan=2,pady = 10,padx=10,ipadx=100)

query_btn = Button(WIN,text = "Show Data",command=query)
query_btn.grid(row=5,column=0,columnspan = 2,pady=10,padx=10,ipadx=137)

update_btn = Button(WIN,text = "Update Data",command=update)
update_btn.grid(row=6,column=0,columnspan = 2,pady=10,padx=10,ipadx=137)


WIN.mainloop()