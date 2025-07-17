import random,string,logging
import tkinter as tk
from tkinter import messagebox

logging.basicConfig(level=logging.INFO)

def get_password_length():
      length =length_entry.get()
      if not length.isdigit():
           raise ValueError("just number is allowed>>>")
      length =int(length)
      if length > 10:
           raise ValueError("you put 10 max length")

      return length    

def generate_password(length,pool):
    r =random.choices(pool,k=length)  
    return ''.join(r)    



def get_pool_String():
    
    stringPool =""
    if uppercase_var.get():
        stringPool+=string.ascii_uppercase
    if lowercase_var.get():
        stringPool+=string.ascii_lowercase
    if number_var.get():
        stringPool+=string.digits
    if symbols_var.get():
        stringPool+=string.punctuation
    return stringPool
    

def password_geenrator():
        try:
            
            length =get_password_length()        
            stringPool = get_pool_String()
            if not stringPool:
                 raise ValueError('select at least one character!')
            r=generate_password(length,stringPool)
            result_var.set(r)
            logging.info(r)        
        except ValueError as e:
            messagebox.showerror("Input ERROR",e)
    
# password_geenrator()
root = tk.Tk()
root.title("password generator")
tk.Label(root,text="PAssword length (Max 10):").grid(row=0 ,column=0 , sticky='w')
length_entry=tk.Entry(root)
length_entry.grid(row=0, column=1)
uppercase_var =tk.BooleanVar()
tk.Checkbutton(root,text="Include upper case",variable=uppercase_var).grid(row=1 ,column=0 , sticky='w')
lowercase_var =tk.BooleanVar()
tk.Checkbutton(root,text="Include lower case",variable=lowercase_var).grid(row=2 ,column=0 , sticky='w')
number_var =tk.BooleanVar()
tk.Checkbutton(root,text="Include number case",variable=number_var).grid(row=3 ,column=0 , sticky='w')
symbols_var =tk.BooleanVar()
tk.Checkbutton(root,text="Include symbol case",variable=symbols_var).grid(row=4 ,column=0 , sticky='w')
tk.Button(root,text="Generate Password",command=password_geenrator).grid(row=5 ,columnspan=2 , pady='3')
result_var =tk.StringVar()
tk.Entry(root,textvariable=result_var,width=30).grid(row=6 ,column=2 , sticky='w')
root.mainloop()