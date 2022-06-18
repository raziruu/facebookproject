from tkinter import *
import sqlite3
from tkinter import messagebox


root = Tk()
root.title("Facebook")
root.iconbitmap('fb.ico')
root.configure(background='blue')

conn = sqlite3.connect('facebook.db')
c = conn.cursor()

### Create table
# c.execute("""CREATE TABLE users(
#     first_name text,
#     last_name text,
#     address text,
#     age text,
#     password text,
#     father_name text,
#     city text,
#     zip_code text
#     )""")
# print("Table created")


def submit():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(:first_name,:last_name,:address,:age,:password,:father_name,:city,:zip_code)", {
        'first_name': f_name.get(),
        'last_name': l_name.get(),
        'address': address.get(),
        'age': age.get(),
        'password': password.get(),
        'father_name': father_name.get(),
        'city': city.get(),
        'zip_code': zip_code.get()
    })
    messagebox.showinfo("Success", "Record has been added")

    conn.commit()
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    age.delete(0, END)
    password.delete(0, END)
    father_name.delete(0, END)
    city.delete(0, END)
    zip_code.delete(0, END)



def query():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM users")
    records = c.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0])+"\t"+str(record[1])+"\t"+str(record[2])+"\t"+str(record[3])+"\t"+str(
            record[4])+"\t"+str(record[5])+"\t"+str(record[6])+"\t"+str(record[7])+"\t"+str(record[8])+"\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


def delete():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE oid="+delete_box.get())
    messagebox.showinfo("Success", "Record has been deleted")
    delete_box.delete(0, END)
    conn.commit()
    conn.close()


def edit():
    global editor
    editor = Toplevel()
    editor.title("Edit Record")
    editor.geometry("500x500")

    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    record_id = edit_box.get()
    c.execute("SELECT * FROM users WHERE oid="+record_id)
    records = c.fetchall()
    global f_name_editor, l_name_editor, address_editor, age_editor, password_editor, father_name_editor, city_editor, zip_code_editor
    # Create entry box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    age_editor = Entry(editor, width=30)
    age_editor.grid(row=3, column=1)
    password_editor = Entry(editor, width=30)
    password_editor.grid(row=4, column=1)
    father_name_editor = Entry(editor, width=30)
    father_name_editor.grid(row=5, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=6, column=1)
    zip_code_editor = Entry(editor, width=30)
    zip_code_editor.grid(row=7, column=1)

    # Create label box
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, sticky=W)
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0, sticky=W)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0, sticky=W)
    age_label = Label(editor, text="Age")
    age_label.grid(row=3, column=0, sticky=W)
    password_label = Label(editor, text="Password")
    password_label.grid(row=4, column=0, sticky=W)
    father_name_label = Label(editor, text="Father Name")
    father_name_label.grid(row=5, column=0, sticky=W)
    city_label = Label(editor, text="City")
    city_label.grid(row=6, column=0, sticky=W)
    zip_code_label = Label(editor, text="Zip Code")
    zip_code_label.grid(row=7, column=0, sticky=W)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        age_editor.insert(0, record[3])
        password_editor.insert(0, record[4])
        father_name_editor.insert(0, record[5])
        city_editor.insert(0, record[6])
        zip_code_editor.insert(0, record[7])
    update_button = Button(editor, text="Update", command=update)
    update_button.grid(row=8, column=1)
    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    record_id = edit_box.get()
    c.execute("""UPDATE users SET
        first_name=:first_name,
        last_name=:last_name,
        address=:address,
        age=:age,
        password=:password,
        father_name=:father_name,
        city=:city,
        zip_code=:zip_code
        WHERE oid=:oid""", {
        'first_name': f_name_editor.get(),
        'last_name': l_name_editor.get(),
        'address': address_editor.get(),
        'age': age_editor.get(),
        'password': password_editor.get(),
        'father_name': father_name_editor.get(),
        'city': city_editor.get(),
        'zip_code': zip_code_editor.get(),
        'oid': record_id
    })
    messagebox.showinfo("Success", "Record has been updated")
    conn.commit()
    conn.close()
    editor.destroy()


# Create Entry box
f_name = Entry(root, width=30)
f_name.grid(row=1, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=2, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)
age = Entry(root, width=30)
age.grid(row=4, column=1, padx=20)
password = Entry(root, width=30, show='*')
password.grid(row=5, column=1, padx=20)
father_name = Entry(root, width=30)
father_name.grid(row=6, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=7, column=1, padx=20)
zip_code = Entry(root, width=30)
zip_code.grid(row=8, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=13, column=1, padx=20)
edit_box = Entry(root, width=30)
edit_box.grid(row=16, column=1, padx=20)
# Create label box
details = Label(root, text="Details", font=("Arial Bold", 20),background="blue",foreground="white")
details.grid(row=0, column=1, padx=20, columnspan=2, pady=20, sticky=W)
f_name_label = Label(root, text="First Name",background="blue",foreground="white")
f_name_label.grid(row=1, column=0)
l_name_label = Label(root, text="Last Name",background="blue",foreground="white")
l_name_label.grid(row=2, column=0)
address_label = Label(root, text="Address",background="blue",foreground="white")
address_label.grid(row=3, column=0)
age_label = Label(root, text="Age",background="blue",foreground="white")
age_label.grid(row=4, column=0)
password_label = Label(root, text="Password",background="blue",foreground="white")
password_label.grid(row=5, column=0)
father_name_label = Label(root, text="Father Name",background="blue",foreground="white")
father_name_label.grid(row=6, column=0)
city_label = Label(root, text="City",background="blue",foreground="white")
city_label.grid(row=7, column=0)
zip_code_label = Label(root, text="Zip Code",background="blue",foreground="white")
zip_code_label.grid(row=8, column=0)
delete_box_label = Label(root, text="Delete",background="blue",foreground="white")
delete_box_label.grid(row=13, column=0)
edit_box_label = Label(root, text="Edit",background="blue",foreground="white")
edit_box_label.grid(row=16, column=0)
# Submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Query button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# delete button
delete_button = Button(root, text="Delete", command=delete)
delete_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# edit button
edit_button = Button(root, text="Edit", command=edit)
edit_button.grid(row=17, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

button_quit = Button(root, text='Quit', command=root.quit)
button_quit.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

conn.commit()
conn.close
mainloop()

# facebook.ico