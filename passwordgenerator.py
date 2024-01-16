import tkinter as tk
import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    length=length_scale.get()
    complexity=complexity_scale.get()
    
    if length <= 0:
        return "Invalid length. Please enter a positive integer."
    if complexity<=0:
        return "Error.Password complexity must be greater than zero."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def reset_password():
    length_scale.set(8)
    complexity_scale.set(1)
    password_entry.delete(0,tk.END)
    
def generate_and_display_password():
    try:
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        password = generate_password(use_uppercase, use_digits, use_special_chars)
        
        result_label.config(text=f"Generated Password: {password}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid input.")


# Create the main window
root = tk.Tk()
root.title("Password Generator")

user_label=tk.Label(root,text="User name:")
user_label.grid(row=0,column=0,padx=5,pady=5)
user_entry=tk.Entry(root)
user_entry.grid(row=0,column=1,padx=5,pady=5)

# Create entry widgets for input
length_label = tk.Label(root, text="Enter password length:")
length_label.grid(row=1,column=0,padx=10,pady=10)
length_scale=tk.Scale(root,from_=1,to=10,orient=tk.HORIZONTAL,length=100,bg="grey")
length_scale.set(4)
length_scale.grid(row=1,column=1,padx=10,pady=10)

# Password Complexity level
complexity_label=tk.Label(root,text="password complexity:")
complexity_label.grid(row=2,column=0,padx=10,pady=10)
complexity_scale=tk.Scale(root,from_=1,to=10,orient=tk.HORIZONTAL,length=100,bg="grey")
complexity_scale.set(1)
complexity_scale.grid(row=2,column=1,padx=10,pady=10)

#complexity of password
uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.grid(row=3,column=0,padx=10,pady=10)

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_checkbox.grid(row=4,column=0,padx=10,pady=10)

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.grid(row=5,column=0,padx=10,pady=10)

# Button to generate and display the password
generate_button = tk.Button(root, text="Generate Password",command=generate_and_display_password)
generate_button.grid(row=6,column=0,padx=10,pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=7,column=0,padx=10,pady=10)

# Start the Tkinter event loop
root.mainloop()
