from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import os

# Define the root window
root = Tk()
root.title("To-Do LIST")
root.configure(bg="powder blue")
root.geometry("500x500")  # Adjusted size to fit menu, heading, and footer

# Define a smaller, aesthetic font
my_font = Font(
    family="Helvetica",
    size=16,
    weight="bold"
)

# Add a heading label with an emoji
heading_label = Label(
    root,
    text="📝 To-Do List",
    font=("Helvetica", 24, "bold"),
    bg="powder blue",
    fg="#333333"
)
heading_label.pack(pady=10)

# Create a frame to hold the listbox
my_frame = Frame(root, bg="powder blue", bd=2, relief="solid")
my_frame.pack(pady=10)

# Create a listbox with an updated font and colors
my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=6,
    bg="#E6E6FA",
    fg="#333333",
    highlightthickness=0,
    bd=2,
    relief="groove",
    selectbackground="#FFAEB9",
    activestyle="none"
)
my_list.pack(side=LEFT, fill=BOTH)

# Add dummy list items to the listbox with emojis
stuff = [
    "🐕 Walk the dog",
    "💻 Learn Tkinter",
    "😴 Take a nap",
    "🍎 Buy fruits",
    "📚 Get good marks",
    "🍔 Eat",
    "✅ Finish all the work",

]
for item in stuff:
    my_list.insert(END, item)

# Add scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create entry box to add items to the list
my_entry = Entry(root, font=("Helvetica", 16))
my_entry.pack(pady=10)

# Create a button frame
button_frame = Frame(root, bg="powder blue")
button_frame.pack(pady=10)

# Button styling and hover effect
def on_enter(e):
    e.widget['bg'] = "#FFD1DC"  # Light pink on hover

def on_leave(e):
    e.widget['bg'] = "#FFAEB9"  # Original color

# Create a button function to avoid repetition
def create_button(parent, text, command):
    button = Button(
        parent, text=text, command=command,
        font=("Helvetica", 12, "bold"),
        bg="#FFAEB9",  # Light pink background
        fg="black",    # Black text
        relief="ridge",
        width=12,
        bd=2
    )
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button

# FUNCTIONS
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    if my_entry.get():
        my_list.insert(END, my_entry.get())
        my_entry.delete(0, END)

def cross_off_item():
    my_list.itemconfig(my_list.curselection(), fg="#dedede")
    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(my_list.curselection(), fg="#333333")
    my_list.selection_clear(0, END)

def delete_crossed():
    counter = 0
    while counter < my_list.size():
        if my_list.itemcget(counter, "fg") == "#dedede":
            my_list.delete(my_list.index(counter))
        counter += 1

# Save and load functions
def save_list():
    file_path = filedialog.asksaveasfilename(
        initialdir=os.getcwd(),
        title="Save File",
        filetypes=(("DAT Files", "*.dat"), ("All Files", "*.*")),
        defaultextension=".dat"
    )
    if file_path:
        with open(file_path, "w") as file:
            for item in my_list.get(0, END):
                file.write(item + "\n")

def open_list():
    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Open File",
        filetypes=(("DAT Files", "*.dat"), ("All Files", "*.*"))
    )
    if file_path:
        my_list.delete(0, END)
        with open(file_path, "r") as file:
            for line in file:
                my_list.insert(END, line.strip())

def clear_list():
    my_list.delete(0, END)

# Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File 📂", menu=file_menu)
file_menu.add_command(label="Open File 📂", command=open_list)
file_menu.add_command(label="Save File 💾", command=save_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List 🗑️", command=clear_list)

# Add styled buttons
delete_button = create_button(button_frame, "❌ Delete", delete_item)
add_button = create_button(button_frame, "➕ Add", add_item)
cross_off_button = create_button(button_frame, "✔️ Cross Off", cross_off_item)
uncross_button = create_button(button_frame, "❌ Uncross", uncross_item)
delete_crossed_button = create_button(button_frame, "Delete Crossed", delete_crossed)

# Place buttons side by side with no gaps
delete_button.grid(row=0, column=0, padx=0, pady=0)
add_button.grid(row=0, column=1, padx=0, pady=0)
cross_off_button.grid(row=0, column=2, padx=0, pady=0)
uncross_button.grid(row=0, column=3, padx=0, pady=0)
delete_crossed_button.grid(row=0, column=4, padx=0, pady=0)

# Add a footer label with emojis
footer_label = Label(
    root,
    text="🌟 Made by Paridhi, Kanak, and Anjali 🌟",
    font=("Helvetica", 12, "italic"),
    bg="powder blue",
    fg="#333333"
)
footer_label.pack(side=BOTTOM, pady=10)

# Start the Tkinter event loop
root.mainloop()
