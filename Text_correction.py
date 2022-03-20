import tkinter as tk
from textblob import TextBlob
import nltk

def correct_spell():
    text=entry1.get()
    text=TextBlob(text)
    text=text.lower()
    label1.config(text=text.correct())
    


window=tk.Tk()
window.maxsize(width=450,height=350)
label=tk.Label(master=window,text="NLP Text Correction",font=("Arial", 15))
label.pack()
frame=tk.Frame(master=window,border=2,borderwidth=2,relief=tk.SUNKEN)
label2=tk.Label(master=frame,text="Enter your text here: ")
label2.grid(row=0,column=0)
entry1=tk.Entry(master=frame,width=60)
entry1.grid(row=0,column=1,columnspan=2)
button1=tk.Button(master=frame,text='submit',relief=tk.RAISED,command=correct_spell)
button1.grid(row=1,column=1)
label3=tk.Label(master=frame,text="Corrected text: ")
label3.grid(row=2,column=0)
label1=tk.Label(master=frame,text=" ")
label1.place(x=115,y=50)
frame.pack(padx=10,pady=10)

window.mainloop()
