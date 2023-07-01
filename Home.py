import tkinter as tk
from tkinter import *
# from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image
import subprocess

filename = None
filter_type = None
def selectPic():
    global img,filename
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("Image files", ("*.png", "*.jpg", "*.jpeg")), ("All files", "*.*")))
    img = Image.open(filename)
    img = img.resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic['image'] = img
    print(filename)

def makeChange():
    if(filename == None):
        print("Select file first!")
    elif(filter_type == None):
        print("Select option!")
    else:
        print(filename)
        if filter_type == 'gaussian':
            subprocess.call(["python", "gauss.py", filename])
        if filter_type == 'median':
            subprocess.call(["python", "median_filter.py", filename])
        if filter_type == 'mean':
            subprocess.call(["python", "convolution.py", filename])
        if filter_type == 'laplacian':
            subprocess.call(["python", "laplacian.py", filename])
        if filter_type == 'sobel':
            subprocess.call(["python", "sobel.py", filename])
        if filter_type == 'equalizehistogram':
            subprocess.call(["python", "equalize_hist.py", filename])
        if filter_type == 'homomorphicfilter':
            subprocess.call(["python", "Homomorphic_filtering.py", filename])
        if filter_type == 'bilateralfilter':
            subprocess.call(["python", "bilateral_filter.py", filename])
        if filter_type == 'idealnotch':
            subprocess.call(["python", "ideal_notch_reject_filter.py", filename])
        if filter_type == 'butterworthnotch':
            subprocess.call(["python", "butter_worth_notch_reject_filter.py", filename])
        if filter_type == 'contraststretching':
            subprocess.call(["python", "contrast_stretching.py", filename])
        if filter_type == 'gammacorrected':
            subprocess.call(["python", "gamma_corrected.py", filename])
        if filter_type == 'inverselog':
            subprocess.call(["python", "inverse_log.py", filename])
        if filter_type == 'hitmiss':
            subprocess.call(["python", "hit_miss_transform.py", filename])
        if filter_type == 'holefilling':
            subprocess.call(["python", "holefilling.py", filename])
        if filter_type == 'skeleton':
            subprocess.call(["python", "skeleton.py", filename])
        if filter_type == 'ripple':
            subprocess.call(["python", "Ripple.py", filename])
        if filter_type == 'tapestry':
            subprocess.call(["python", "tapestry.py", filename])
        if filter_type == 'twirl':
            subprocess.call(["python", "twirled.py", filename])
        if filter_type == 'angularwave':
            subprocess.call(["python", "angular_wave.py", filename])



root = Tk()  # create root window
root.title("Image Output Checker")  # title of the GUI window
root.maxsize(900, 600)

root.config(bg="white")  # specify background color




# frame = tk.Frame(root, bg='#45aaf2')

left_frame = Frame(root, width=50, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root ,width=200, height=400, bg='white')
right_frame.grid(row=0, column=1, padx=10, pady=5)

right_frame2 = Frame(root ,width=200, height=400, bg='white')
right_frame2.grid(row=0, column=2, padx=5, pady=5)


# radio button..........
def printResults():
    global filter_type
    if var1.get() == 'mean':
        filter_type = 'mean'
    if var1.get() == 'median':
        filter_type = 'median'
    if var1.get() == 'gaussian':
        filter_type = 'gaussian'
    if var1.get() == 'laplacian':
        filter_type = 'laplacian'
    if var1.get() == 'sobel':
        filter_type = 'sobel'
    if var1.get() == 'equalizehistogram':
        filter_type = 'equalizehistogram'
    if var1.get() == 'bilateralfilter':
        filter_type = 'bilateralfilter'
    if var1.get() == 'homomorphicfilter':
        filter_type = 'homomorphicfilter'
    if var1.get() == 'idealnotch':
        filter_type = 'idealnotch'
    if var1.get() == 'butterworthnotch':
        filter_type = 'butterworthnotch'
    if var1.get() == 'contraststretching':
        filter_type = 'contraststretching'
    if var1.get() == 'gammacorrected':
        filter_type = 'gammacorrected'
    if var1.get() == 'inverselog':
        filter_type = 'inverselog'
    if var1.get() == 'hitmiss':
        filter_type = 'hitmiss'
    if var1.get() == 'holefilling':
        filter_type = 'holefilling'
    if var1.get() == 'skeleton':
        filter_type = 'skeleton'
    if var1.get() == 'ripple':
        filter_type = 'ripple'
    if var1.get() == 'tapestry':
        filter_type = 'tapestry'
    if var1.get() == 'twirl':
        filter_type = 'twirl'
    if var1.get() == 'angularwave':
        filter_type = 'angularwave'
    print(filter_type)


Label(right_frame, text="Spatial filtering: ").pack(anchor='w')

var1 = StringVar(right_frame, " ")  # Create a variable for strings, and initialize the variable
Radiobutton(right_frame, text="Mean", variable=var1, value="mean", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame, text="Median", variable=var1, value="median", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame, text="Gaussian", variable=var1, value="gaussian", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame, text="Laplacian", variable=var1, value="laplacian", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame, text="Sobel", variable=var1, value="sobel", command=printResults,bg='white').pack(anchor='w')

Label(right_frame, text="Histogram equalization: ").pack(anchor='w')
Radiobutton(right_frame, text="EqualizedHistogram", variable=var1, value="equalizehistogram", command=printResults,bg='white').pack(anchor='w')

Label(right_frame, text="Fourier Transform: ").pack(anchor='w')
Radiobutton(right_frame, text="Bilateral filter", variable=var1, value="bilateralfilter", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame, text="Homomorphic filter", variable=var1, value="homomorphicfilter", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame, text="Ideal notch reject filter", variable=var1, value="idealnotch", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame, text="Butter worth notch reject filter", variable=var1, value="butterworthnotch", command=printResults,bg='white').pack(anchor='w')

Label(right_frame2, text="Point processing: ").pack(anchor='w')
Radiobutton(right_frame2, text="Contrast stretching", variable=var1, value="contraststretching", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame2, text="Gamma corrected", variable=var1, value="gammacorrected", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame2, text="Inverse log", variable=var1, value="inverselog", command=printResults,bg='white').pack(anchor='w')

Label(right_frame2, text="Morphological Image Processing: ").pack(anchor='w')
Radiobutton(right_frame2, text="Hir-or-miss(specific kernel and img)", variable=var1, value="hitmiss", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame2, text="Holefilling", variable=var1, value="holefilling", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame2, text="Skeleton", variable=var1, value="skeleton", command=printResults,bg='white').pack(anchor='w')

Label(right_frame2, text="Geometric transformation: ").pack(anchor='w')
Radiobutton(right_frame2, text="Ripple", variable=var1, value="ripple", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame2, text="Tapestry", variable=var1, value="tapestry", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame2, text="Twirl", variable=var1, value="twirl", command=printResults,bg='white').pack(anchor='w')
Radiobutton(right_frame2, text="Angular wave", variable=var1, value="angularwave", command=printResults,bg='white').pack(anchor='w')


# lbl_pic_path = tk.Label(left_frame, text='Image Path:', padx=25, pady=25,
#                         font=('verdana',16), bg='#45aaf2')
lbl_show_pic = tk.Label(left_frame, bg='grey',text="selected image...",fg='white')


btn_browse = tk.Button(left_frame, command=selectPic ,text='Select Image',bg='grey', fg='#ffffff',
                       font=('verdana',12))
apply_button = tk.Button(left_frame,text="Apply",command=makeChange,bg='grey', fg='#ffffff')

guide_text = tk.Label(left_frame,text="Choose one option and\n click apply to get output result through new window",fg='black',wraplength=150,bg='white')



# lbl_pic_path.grid(row=0, column=0)
# entry_pic_path.grid(row=0, column=1, padx=(0,20))
lbl_show_pic.grid(row=1, column=0, columnspan="2")

btn_browse.grid(row=2, column=0, columnspan="2", padx=10, pady=10)
apply_button.grid(row=3, column=0, columnspan="2")
guide_text.grid(row=4,column=0)

root.mainloop()