##########################################  
# 9.25.20 
# Scrollymouse
# Python # GUI 

###########################################
#Requirements : 

import tkinter as tk
from tkinter import filedialog, Text, Menu 
import tkinter.messagebox
import os

##########################################

root = tk.Tk()
root.title('Name')

###########################################
#           FX
###########################################

def runONE():   
    # run .py script
    os.system('python3 /Users/xxxxx/Desktop/v3nv/bin/XXXXXX.py')    
    
def runTWO():  
    os.system('python3 /Users/xxxxx/Desktop/v3nv/bin/XXXXXX.py')        

def runTHREE():
    os.system('python3 /Users/xxxxx/Desktop/v3nv/bin/XXXXXX.py')        

def runFOUR():
    os.system('python3 /Users/xxxxx/Desktop/v3nv/bin/XXXXXX.py') 
    
    
###########################################   
#canvas
###########################################
canvas = tk.Canvas(root, height=500, width=600, bg="black")
#attach to root
canvas.pack()


###########################################
# frame
###########################################

frame = tk.Frame(root, bg='#263D42')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


###########################################
# Label 
###########################################
label1= tk.Label(frame, text="APP", bg='#263D42', font = 40)
label1.place(relx=0.45, rely=0)

# Label 
label2= tk.Label(frame, text="Section 1: ", bg='#263D42')
# attach 
label2.place(relx=0.05, rely=0.10)

###########################################
#buttonS
###########################################

Button1=tk.Button(frame, text="Run 1",  highlightbackground='#263D42',command= runONE)

Button1.place(relx=0.05, rely=0.15)

###########################################

Button2=tk.Button(frame, text="Run 2",  highlightbackground='#263D42',command= runTWO)

Button2.place(relx=0.05, rely=0.25)

###########################################
# Label 
label3= tk.Label(frame, text="Section 2: ", bg='#263D42')
# attach
label3.place(relx=0.05, rely=0.35)

###########################################

#button
Button3= tk.Button(frame, text="Run 3", highlightbackground='#263D42', command= runTHREE)
#attach to root
Button3.place(relx=0.05, rely=0.40)

#button
Button4= tk.Button(frame, text="Run 4", highlightbackground='#263D42',  command= runFOUR)
#attach to root
Button4.place(relx=0.05, rely=0.50)

###########################################



###########################################
#           NAV/ FILE BAR
###########################################
menu = Menu(root)

filemainmenu = Menu(menu, tearoff=0)
filesubmenu = Menu(filemainmenu, tearoff=0)

menu.add_cascade(label="File", menu=filemainmenu)
filemainmenu.add_command(label=" EXIT APP", command = exit)

root.config(menu=menu)

###########################################

#RUN
root.mainloop()

########################################### 


###########################################
#END

