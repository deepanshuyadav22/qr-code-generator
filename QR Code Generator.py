#Imported Modules and Libraries-------------------------------------------

#to implement GUI
from tkinter import *

#to get image (i.e. file) name while saving
from tkinter.filedialog import asksaveasfilename

#to convert text into QR code
import pyqrcode

#to display QR code images
from PIL import Image, ImageTk

#to delete preview images
import os

#Designing Main Window----------------------------------------------------

#creating main window
w = Tk()

#title of main window
w.title("QR Code Generator")

#size of main window
w.geometry("900x625")

#background colour of main window
w.configure(background = '#fff')

#Functions----------------------------------------------------------------

#it will store names of previewed images in one session
nameOfPreviewImgs = []

def preview(event):
    #generating QR code for entered text
    qrCode = pyqrcode.create(text_enterText.get(1.0, END))

    #getting list of names of all the files of
    #the directory in which this Python file is stored
    filesNameList = os.listdir()

    #we are saving the preview image with filename "qrcodegeneratorpreviewimageortemporaryimage-N"
    #here, 'N' belongs to a natural number
    #this 'N' will help us to assign different names to all preview images

    #initializing 'N' as 'i' from 1
    i = 1

    while True:
        imgName = "qrcodegeneratorpreviewimageortemporaryimage-" + str(i) + ".png"
        i += 1

        #if no filename is matching with the current filename (i.e. 'imgName'),
        #then save the preview image with filename 'imgName'
        #and then append this filename in 'nameOfPreviewImgs' list,
        #so that we can delete these files/images when we'll close this tkinter-app
        #and then break the loop

        if imgName not in filesNameList:
            qrCode.png(imgName, scale = scale_imgSize.get())
            nameOfPreviewImgs.append(imgName)
            break

    #below part will display the preview image in RHS of the window
    outputImg = Image.open(nameOfPreviewImgs[-1])
    outputImg = outputImg.resize((235,235))
    outputImg = ImageTk.PhotoImage(outputImg)
    label_qrCode = Label(image = outputImg)
    label_qrCode.image = outputImg
    label_qrCode.pack()
    label_qrCode.place(x = 610, y = 110)

def save(event):
    try:
        #user can save the image only in PNG format
        imgExtensions = [("PNG File", "*.png")]

        #getting path with filename (image name)
        imgSavePathAndName = asksaveasfilename(filetypes = imgExtensions, defaultextension = imgExtensions)

        #generating QR code for entered text
        qrCode = pyqrcode.create(str(text_enterText.get(1.0, END)))

        #saving the generated QR code at specified path with specified name
        qrCode.png(imgSavePathAndName, scale = scale_imgSize.get())
    except:
        print(end = "")

def onClosing():
    #when user will close the window,
    #then the below part will delete/remove all preview files/images
    for i in range(0, len(nameOfPreviewImgs)):
        os.remove(nameOfPreviewImgs[i])

    #closing the window after deleting all preview files/images
    w.destroy()

#Heading Section----------------------------------------------------------

heading = Label(w, text = "QR Code Generator", bg = '#fff', font = ('algerian', 25))
heading.config(pady = 15)
heading.pack()

#Text Input Section-------------------------------------------------------

label_enterText = Label(w, text = "Enter text to convert in QR code:", bg = '#fff', font = ('segoeui', 14))
label_enterText.pack()
label_enterText.place(x = 50, y = 80)

#to take texts/input
text_enterText = Text(w, padx = 5, pady = 5, width = 50, height = 10, bg = '#f1f1f1', wrap = WORD, bd = '0', font = ('calibri', 14))
text_enterText.insert(END, "I generate QR codes from texts.")
text_enterText.pack()
text_enterText.place(x = 50, y = 110)

#Decide Image's Size------------------------------------------------------

label_selectImgSize = Label(w, text = "Select size for output image:", bg = '#fff', font = ('segoeui', 14))
label_selectImgSize.pack()
label_selectImgSize.place(x = 50, y = 380)

#to set size of output image
scale_imgSize = Scale(w, from_ = 1, to = 10, tickinterval = 9, orient = HORIZONTAL, width = 10, length = 504, bg = '#fff', font = ('calibri', 14))
scale_imgSize.set(5)
scale_imgSize.place(x = 50, y = 412)

#Image Preview Section----------------------------------------------------

label_outputImg = Label(w, text = "QR Code Preview:", bg = '#fff', font = ('segoeui', 14))
label_outputImg.pack()
label_outputImg.place(x = 610, y = 80)

#Buttons------------------------------------------------------------------

button_Preview = Button(w, text = "Preview", width = 15, height = 2, bg = '#077bff', fg = '#fff', activebackground = 'blue', activeforeground = '#fff', font = ('centurygothic', 14), bd = 0)
button_Save = Button(w, text = "Save", width = 15, height = 2, bg = '#077bff', fg = '#fff', activebackground = 'blue', activeforeground = '#fff', font = ('centurygothic', 14), bd = 0)

button_Preview.pack()
button_Save.pack()

button_Preview.bind('<Button-1>', preview)
button_Save.bind('<Button-1>', save)

button_Preview.place(x = 255, y = 525)
button_Save.place(x = 479, y = 525)

#-------------------------------------------------------------------------

#it will call the function 'onClosing' when user closes the window
w.protocol("WM_DELETE_WINDOW", onClosing)

w.mainloop()
