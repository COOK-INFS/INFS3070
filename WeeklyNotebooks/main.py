from dbConfig import create_conn

import tkinter as tk
import customtkinter as ctk

# Create the connection items
conn = create_conn()
cursor = conn.cursor()

# Build the basics of the window
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")

window = ctk.CTk() # Create the CTk window similar in Tkinter
window.geometry("850x400")
window.title("My first UI")
window.iconbitmap("images/uccs.ico")
#window.wm_iconbitmap("images/uccs.ico")

# -------------------------------------------------------------------------
# Create a function to make the button below work
def display_records():
    cursor.execute("SELECT * FROM STUDENTS")
    records = cursor.fetchall()
    msg=""
    for record in records:
        msg += f"ID: {record[0]}, Name: {record[2]} {record[1]}, Email: {record[3]}\n"
    text_widget.delete('1.0', tk.END) # Deletes any records currently in the text widget.
    text_widget.insert(tk.END, msg) # Inserts new records into the widget


# Create a button that will display database records
display_button = ctk.CTkButton(master=window, text="Display Records", command=display_records)
display_button.grid(
    row=0,
    rowspan=1,
    column=7,
    padx=5,
    pady=5,
    sticky="e"
)

# Create an empty row to align objects
placeholder_label = ctk.CTkLabel(master=window, text="")
placeholder_label.grid(row=0, column=2, columnspan=3, ipadx=5, padx=5, ipady=10, pady=10, sticky="e")

# Create a text widget to display database records
text_widget = ctk.CTkTextbox(master=window, width=450)
text_widget.grid(
    row=1,
    rowspan=5,
    column=5,
    columnspan=3,
    ipadx=5,
    ipady=5,
    padx=5,
    pady=5,
    sticky="e"
)

# ---------------------------INSERT RECORDS-------------------------------------
# Create the text input elements in the UI.

# Label and input for StudentID
studentID_label = ctk.CTkLabel(master=window, text="Student ID:")
studentID_label.grid(row=0, column=0, ipadx=1, padx=15, ipady=2, pady=2, stick="w")
studentID_input = ctk.CTkEntry(master=window)
studentID_input.grid(row=0, column=1, ipadx=5, padx=2, ipady=2, pady=2, stick="w")

# Create label and input for First name
firstName_label = ctk.CTkLabel(master=window, text="First Name:")
firstName_label.grid(row=1, column=0, ipadx=1, padx=15, ipady=2, pady=2, stick="w")
firstName_input = ctk.CTkEntry(master=window)
firstName_input.grid(row=1, column=1, ipadx=5, padx=2, ipady=2, pady=2, stick="w")

# Create label and input for last name
lastName_label = ctk.CTkLabel(master=window, text="Last Name:")
lastName_label.grid(row=2, column=0, ipadx=1, padx=15, ipady=2, pady=2, stick="w")
lastName_input = ctk.CTkEntry(master=window)
lastName_input.grid(row=2, column=1, ipadx=5, padx=2, ipady=2, pady=2, stick="w")

# Create label and input for Email
email_label = ctk.CTkLabel(master=window, text="Email:")
email_label.grid(row=3, column=0, ipadx=1, padx=15, ipady=2, pady=2, stick="w")
email_input = ctk.CTkEntry(master=window)
email_input.grid(row=3, column=1, ipadx=5, padx=2, ipady=2, pady=2, stick="w")

# Create a function to insert records
def insert_records():
    firstName = firstName_input.get()
    lastName = lastName_input.get()
    email = email_input.get()
    sql = "INSERT INTO STUDENTS (firstName, lastName, email) VALUES (%s, %s, %s)"
    val = (firstName, lastName, email)
    cursor.execute(sql, (val))
    conn.commit()
    clear_inputs()

# Create a function to clear the input fields
def clear_inputs():
    firstName_input.delete(0, tk.END)
    lastName_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    studentID_input.delete(0, tk.END)

# Create a button to insert the records
insert_button = ctk.CTkButton(master=window, text="INSERT", command=insert_records)
insert_button.grid(row=5, column=0, padx=10, pady=10)

# Ensure the window renders
window.mainloop()