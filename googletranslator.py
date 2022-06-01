#Mahmadshoyev Shohabbos My first project
#from cgitb import text
from tkinter import *
from tkinter import ttk,messagebox
#from tkinter.tix import ButtonBox
#from turtle import window_height
import googletrans
import textblob

#App names
root = Tk()
root.title("Google translator")
root.geometry("1080x400")

#the result of language change
def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    global language
    try:
        text_=text1.get(1.0,END)
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i, j in language.items():
                if(j==c3):
                    lan_=i
            words=words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans","please try again")

# #icon
# image_icon = PhotoImage(file="google.png")
# root.iconphoto(False,image_icon)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

#Lanuguage which to be translated other language
combo1 = ttk.Combobox(root,values=languageV,font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

#place for select language
label1 = Label(root, text="ENGLISH", font="segeo 30 bold" ,bg="white", width=18,bd=5,relief=GROOVE)
label1.place(x=10, y=50)

#place for frame
f = Frame(root, bg="Black",bd=5)
f.place(x=18, y=118,width=440,height=210)

#place for typing words
text1 = Text(f, font="Robote 20", bg="White", relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430, height=200)

scrolbarr1 = Scrollbar(f)
scrolbarr1.pack(side="right",fill="y")

scrolbarr1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrolbarr1.set)


#language which to be translating
combo2 = ttk.Combobox(root,values=languageV,font="RobotV 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT_ LANGUAGE_")

#place for select language 
label2 = Label(root, text="ENGLISH", font="segeo 30 bold" ,bg="white", width=18,bd=5,relief=GROOVE)
label2.place(x=620, y=50)

#place for frame
f1 = Frame(root, bg="Black",bd=5)
f1.place(x=620, y=118,width=430,height=200)

#place for typing words
text2 = Text(f1, font="Robote 20", bg="White", relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430, height=200)

scrolbarr2 = Scrollbar(f1)
scrolbarr2.pack(side="right",fill="y")

scrolbarr2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrolbarr2.set)

#translate button
translate = Button(root,text="Tranlate",font="Roboto 15 bold italic", activebackground="purple",cursor="hand2",bd=5,bg="red",fg="white",command=translate_now)
translate.place(x=480,y=250)

label_change()

root.configure(bg="white")
root.mainloop()