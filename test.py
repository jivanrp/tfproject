from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import cv2
import PIL
import numpy as np
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
from tkinter import filedialog
import tkinter.font as tkFont
import tensorflow as tf

root = Tk()
root.title('Sistem Ramalan untuk Bangsa \n& Umur rakyat Malaysia')
root.geometry("1280x720")
root.resizable(height=False, width=False)
root.configure(bg='#f8f8f8')
faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')


# ----------------------------------------------------------------------------Classes
# ----------------------------------------------------------------------------Classes

class Facehcc:
    def check_for_face(self):
        faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        img = cv2.imread(self.file_path)
        imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(img, 1.2, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

            new_img = cv2.resize(img, (960, 540))
            cv2.imshow('Result', new_img)
            cv2.waitKey()





# ----------------------------------------------------------------------------Classes
# ----------------------------------------------------------------------------Classes

def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

def addOpenFile():

    model_file = "mobile_graph.pb"
    label_file = "mobile_labels.txt"
    graph = load_graph(model_file)

# ----------------------------------------------------------------------------TF
# ----------------------------------------------------------------------------TF



# ----------------------------------------------------------------------------TF
# ----------------------------------------------------------------------------TF


sidebar = Frame(root, width=400, height=720, borderwidth=2)
mainspace3 = Frame(root, width=880, height=720, bg='#e0e0e0', borderwidth=1)
mainspace2 = Frame(root, width=880, height=720, bg='#e0e0e0', borderwidth=1)
mainspace1 = Frame(root, width=880, height=720, bg='#e0e0e0', borderwidth=1)

sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)
mainspace1.place(relx=0.2, rely=0, relwidth=0.85, relheight=1)
mainspace2.place(relx=0.2, rely=0, relwidth=0.85, relheight=1)
mainspace3.place(relx=0.2, rely=0, relwidth=0.85, relheight=1)




#====================================SIDEBAR THINGS===================================================================
#====================================SIDEBAR THINGS===================================================================

#Sidebar title things
title = Label(sidebar, text="Sistem Ramalan untuk", font="Verdana 15", anchor=W)
title.place(relx=0.0255, rely=0.065, relwidth=0.95, relheight=0.05)
title2 = Label(sidebar, text="Bangsa & Umur ", font="Verdana 15", anchor=W)
title2.place(relx=0.0255, rely=0.11, relwidth=0.95, relheight=0.05,)
title3 = Label(sidebar, text="Rakyat Malaysia", font="Verdana 15", anchor=W)
title3.place(relx=0.0255, rely=0.155, relwidth=0.95, relheight=0.05,)


#button to open Halaman Utama frame
def show_frame():
    frame = mainspace1
    frame.tkraise()
open_pic = Button(sidebar, text="Halaman Utama", bg = '#dedede', command = show_frame)
open_pic.place(relx=0.025, rely=0.29, relwidth=0.95, relheight=0.1)


#button to open Hasil Carian frame
def show_frame():
    frame = mainspace2
    frame.tkraise()
close_btn = Button(sidebar, text="Hasil Ramalan", bg = '#dedede', command = show_frame)
close_btn.place(relx=0.025, rely=0.405, relwidth=0.95, relheight=0.1)


#button to open Sejarah frame
def show_frame():
    frame = mainspace3
    frame.tkraise()
close_btn = Button(sidebar, text="Sejarah", bg = '#dedede', command = show_frame)
close_btn.place(relx=.025, rely=0.52, relwidth=.95, relheight=0.1)


#button to close window
def close_window():
    root.destroy()
close_btn = Button(sidebar, text="Tutup Perisian",  bg = '#dedede', command = close_window)
close_btn.place(relx=0.025, rely=0.635, relwidth=0.95, relheight=0.1)


#====================================MAINSPACE1 THINGS===================================================================
#====================================MAINSPACE1 THINGS===================================================================


def file_path():
    global filepath
    filepath = StringVar()
    if(filepath == ""):
        filepath = filedialog.askopenfilename( initialdir = os.getcwd(), title = "Pilih Gambar", filetypes = [("JPG files", "*.jpg"), ("PNG files", "*.png")])
    else:
        filepath = filedialog.askopenfilename( initialdir=filepath, title = "select a file", filetypes = [("JPG files", "*.jpg"), ("PNG files", "*.png")])



def generate():
    if filepath == "":
        messagebox.showinfo('')
    else:
        generate_image = Facehcc()
        generate_image.file_path = filepath
        generate_image.check_for_face()


# def ageracepredictions():
#


canvas = Canvas(mainspace1, width=360, height=480, bg='#f0f0f0')
canvas.place(relx=0.15, rely=0.16)

Browsebutton = Button(mainspace1, width = 15,text= "Cari Gambar",command = file_path)
Browsebutton.place(relx=0.15, rely=0.86, relwidth= 0.1, relheight= 0.05)

Generatebutton = Button(mainspace1, text="Cari Wajah",command = generate)
Generatebutton.place(relx=0.265, rely=0.86, relwidth= 0.1, relheight= 0.05)

Predictbutton = Button(mainspace1, text="Ramal",command = '')
Predictbutton.place(relx=0.38, rely=0.86, relwidth= 0.1, relheight= 0.05)



#====================================MAINSPACE2 THINGS===================================================================
#====================================MAINSPACE2 THINGS===================================================================


#canvas to show picture
canvas2 = Canvas(mainspace2, width=240, height=360, bg='#f0f0f0')
canvas2.place(relx=0.15, rely=0.16)

#race results
race_label=Label(mainspace2, text="Bangsa: ", width=10, height=1, bg='white')
race_label.place(relx=0.395, rely=0.163)

race_label_result=Label(mainspace2, text="...", width=10, height=1, bg='white') #results call back from database
race_label_result.place(relx=0.47, rely=0.163)

#age results
age_label=Label(mainspace2, text="Umur: ", width=10, height=1, bg='white')
age_label.place(relx=0.395, rely=0.2)

age_label_result=Label(mainspace2, text="...", width=10, height=1, bg='white') #results call back from database
age_label_result.place(relx=0.47, rely=0.2)




#====================================MAINSPACE3 THINGS===================================================================
#====================================MAINSPACE3 THINGS===================================================================
#connect to database(in this case ms access)

age_label=Label(mainspace3, text="1.                                                 ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.05)

age_label=Label(mainspace3, text="2.                                                 ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.15)

age_label=Label(mainspace3, text="3.                                                 ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.25)

age_label=Label(mainspace3, text="4.                                                 ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.35)

age_label=Label(mainspace3, text="5.                                                  ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.45)

age_label=Label(mainspace3, text="6.                                                  ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.55)

age_label=Label(mainspace3, text="7.                                                  ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.65)

age_label=Label(mainspace3, text="8.                                                  ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.75)

age_label=Label(mainspace3, text="9.                                                  ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.85)

age_label=Label(mainspace3, text="10.                                                  ", width=30, height=1, bg='#e0e0e0')
age_label.place(relx=0.1, rely=0.95)

root.mainloop()