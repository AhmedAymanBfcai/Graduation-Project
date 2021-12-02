from tkinter import *
check = 0
#functions
def new_window(n="New Window", x='400x600'):
    window = Toplevel(tkWindow)
    window.geometry(x)
    window.title(n)
    canvas = Canvas(window, height=400, width=600).pack()
    return window

def swap_gui(x,y):
    global check
    y.withdraw()
    check = 0
def open_cam():
    global check
    if (check != 0):
        return
    cam_frame = new_window("Camera Window")
    check = 1
    back_btn1 = Button(cam_frame, text="Back", command=lambda : swap_gui(tkWindow,cam_frame)).pack()
    Exit_btn = Button(cam_frame, text="Exit", command=lambda : exit()).pack()

def select_img():
    global check
    if (check != 0):
        return
    img_frame = new_window("Image Window")
    check = 1
    back_btn2 = Button(img_frame, text="Back", command=lambda : swap_gui(tkWindow,img_frame)).pack()
    Exit_btn = Button(new_window, text="Exit", command=lambda: exit()).pack()

def select_vid():
    global check
    if (check != 0):
        return
    vid_frame = new_window("Video Window")
    check = 1
    back_btn3 = Button(vid_frame, text="Back", command=lambda : swap_gui(tkWindow,vid_frame)).pack()
    Exit_btn = Button(vid_frame, text="Exit", command=lambda : exit()).pack()

tkWindow = Tk()
tkWindow.title("Safety Agent")
tkWindow.geometry('400x600')
canvas = Canvas(tkWindow, height=400, width=600).pack()
Lbl = Label(tkWindow, text="Choose A Source").pack()
cam_btn = Button(tkWindow, text="Camera", command=open_cam).pack()
img_btn = Button(tkWindow, text="Image", command=select_img).pack()
vid_btn = Button(tkWindow, text="Video", command=select_vid).pack()
Exit_btn = Button(tkWindow, text="Exit", command=lambda:exit()).pack()
tkWindow.mainloop()