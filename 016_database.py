import tkinter as tk
import os
import sqlite3
from tkinter.constants import END

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
# root.geometry("400x400")


f_name_label = tk.Label(root, text="First name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name_label = tk.Label(root, text="Last name")
l_name_label.grid(row=1, column=0)
l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1)

address_label = tk.Label(root, text="Address")
address_label.grid(row=2, column=0)
address = tk.Entry(root, width=30)
address.grid(row=2, column=1)

city_label = tk.Label(root, text="City")
city_label.grid(row=3, column=0)
city = tk.Entry(root, width=30)
city.grid(row=3, column=1)

state_label = tk.Label(root, text="State")
state_label.grid(row=4, column=0)
state = tk.Entry(root, width=30)
state.grid(row=4, column=1)

zipcode_label = tk.Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1)


def submit():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            "f_name": f_name.get(),
            "l_name": l_name.get(),
            "address": address.get(),
            "city": city.get(),
            "state": state.get(),
            "zipcode": zipcode.get(),
        },
    )

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    conn.commit()
    conn.close()


submit_btn = tk.Button(root, text="Add record to DB", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


def query_values():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    # c.execute("SELECT f_name, l_name, address, city, state, zipcode FROM addresses")
    c.execute("SELECT *, oid FROM addresses")
    # c.fetchone()
    # c.fetchmany(15)
    records = c.fetchall()
    print_records = ""
    for record in records:
        print_records += " ".join(map(str, record)) + "\n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.close()


query_btn = tk.Button(root, text="Show records", command=query_values)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


def delete_values():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("DELETE FROM addresses where oid=" + delete_entry.get())

    conn.commit()

    delete_entry.delete(0, END)

    conn.close()


delete_entry = tk.Entry(root, width=30)
delete_entry.grid(row=8, column=0, padx=(10, 0))
delete_btn = tk.Button(root, text="Delete record", command=delete_values)
delete_btn.grid(row=8, column=1, pady=10, padx=10, ipadx=20)


def query_chosen():
    global f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zipcode_editor, editor
    editor = tk.Tk()
    editor.title("Update record")

    f_name_label = tk.Label(editor, text="First name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    f_name_editor = tk.Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_label = tk.Label(editor, text="Last name")
    l_name_label.grid(row=1, column=0)
    l_name_editor = tk.Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_label = tk.Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    address_editor = tk.Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_label = tk.Label(editor, text="City")
    city_label.grid(row=3, column=0)
    city_editor = tk.Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_label = tk.Label(editor, text="State")
    state_label.grid(row=4, column=0)
    state_editor = tk.Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_label = tk.Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    zipcode_editor = tk.Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    update_btn = tk.Button(editor, text="Save", command=update_record)
    update_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=20)

    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses WHERE oid = " + chosen_entry.get())
    records = c.fetchone()
    f_name_editor.insert(0, records[0])
    l_name_editor.insert(0, records[1])
    address_editor.insert(0, records[2])
    city_editor.insert(0, records[3])
    state_editor.insert(0, records[4])
    zipcode_editor.insert(0, records[5])

    conn.close()


chosen_entry = tk.Entry(root, width=30)
chosen_entry.grid(row=9, column=0, padx=(10, 0))
chosen_btn = tk.Button(root, text="Search", command=query_chosen)
chosen_btn.grid(row=9, column=1, pady=10, padx=10, ipadx=20)


def update_record():
    global f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zipcode_editor, editor

    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute(
        """UPDATE addresses set 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = :oid""",
        {
            "first": f_name_editor.get(),
            "last": l_name_editor.get(),
            "address": address_editor.get(),
            "city": city_editor.get(),
            "state": state_editor.get(),
            "zipcode": zipcode_editor.get(),
            "oid": chosen_entry.get(),
        },
    )

    conn.commit()
    conn.close()

    editor.destroy()


root.mainloop()
