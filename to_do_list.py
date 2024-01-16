import tkinter as tk
from tkinter import messagebox

# defining the function to add task
def add_task():
    task=enter.get()
    if task:
        listbox.insert(tk,END,task)
        entry.delete(0,tk,END)
    else:
        messagebox.showwarning("Warning","Please enter a task")
        
# defining the function to delete a particular task
def delete_task():
    try :
        select_task_index=listbox.curselection()[0]
        listbox.delete(select_task_index)
    except IndexError:
        messagebox.showwarning("Warning","Please select a task to delete.")
        
#  defining the function to delete all task     
def delete_all_task():
    listbox.delete(0,tk,END)
    
#  defining the function to close the application
def  exit_app():
    if messagebox.askocancel("Quit"," Do you really want to quit?"):
        window.destory()

# Create main window      
root=tk.Tk()
root.title("To-Do List")

#Enter the widges for adding tasks
entry=tk.Entry(root,width=40)
entry.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

#creating button of adding tasks
add_button=tk.Button(root,text="Add Task",command=add_task)
add_button.grid(row=2,column=0,padx=5,pady=10)

#creating button of deleting particular tasks
delete_button=tk.Button(root,text="Delete Task",command=delete_task)
delete_button.grid(row=2,column=1,padx=5,pady=10)

#creating button of deleting all task
delete_all_button=tk.Button(root,text="Delete All Task",command=delete_all_task)
delete_all_button.grid(row=2,column=2,padx=5,pady=10)

#listbox for displaying task
listbox=tk.Listbox(root,width=50,height=10)
listbox.grid(row=3,column=0,padx=10,pady=10,columnspan=4)

#creating button of exit app
exit_button=tk.Button(root,text="Exit",command=exit_app)
exit_button.grid(row=4,column=1,padx=12,pady=15)

#run the main loop
root.mainloop()
