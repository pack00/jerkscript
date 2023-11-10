#rustskingenerator
import time
import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.withdraw()
messagebox.askyesnocancel("Do You Want To Install This Program?", "Press Yes TO Install")
messagebox.showinfo("Installed Program", "The Program Has Installed")
time.sleep(1)
print("Loading Generator... ")
time.sleep(2.5)
print("Generator Loaded... ")
time.sleep(2)
print("You Need To Enter Your Email First")
time.sleep(1)
email = input("Enter Your Email: ")
f = open("email.txt", "x")
time.sleep(0.1)
f = open("email.txt", "w")
f.write(email)
f.close()
time.sleep(1)
item = input("[1]Rust Skin Or [2]Rust Gun Skin")
if item.__contains__("1"):
    print("eje9i3j984ukm4390")
else:
    print("jsdnjder2i3354325fgv")


time.sleep(20)

