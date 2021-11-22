from tkinter import *

#functions
def new_frame(n="", path="", x='', y=''):
    frame = Tk()
    frame.title(n)
    if (x != 0 and y != 0):
        frame.geometry(x + 'x' + y)
    if (path != ""):
        frame.iconbitmap(path)
    frame.tkraise()
    return frame

def open_cam():
    tkWindow.withdraw()
    cam_frame = new_frame("Camera", "", '400', '600')
    #back_btn1 = Button(cam_frame, text="Back", command=swap_frame(cam_frame,prev)).grid(row=7, column=7)

def select_img():
    tkWindow.withdraw()
    img_frame = new_frame("Image", "", '400', '600')
    #back_btn2 = Button(img_frame, text="Back", command=swap_frame(img_frame, prev)).grid(row=7, column=7)

def select_vid():
    tkWindow.withdraw()
    vid_frame = new_frame("Video", "", '400', '600')
    #back_btn3 = Button(vid_frame, text="Back", command=swap_frame(vid_frame, prev)).grid(row=7, column=7)

tkWindow = Tk()
tkWindow.title("Safety Agent")
tkWindow.geometry('400x600')
Lbl = Label(tkWindow, text="Choose A Source").grid(row=3, column=7)
cam_btn = Button(tkWindow, text="Camera", command=open_cam).grid(row=7, column=7)
img_btn = Button(tkWindow, text="Image", command=select_img).grid(row=10, column=7)
vid_btn = Button(tkWindow, text="Video", command=select_vid).grid(row=13, column=7)
tkWindow.mainloop()