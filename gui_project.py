import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *  # only import __all__
from tkinter import filedialog
from PIL import Image

def add_file():
    files = filedialog.askopenfilenames(title="select image files", \
                                        filetypes=(("PNG file","*.png"),("All file", "*.*")),\
                                        initialdir=r"C:\Users\PC\Desktop\study\코딩\파이썬\나도 코딩\gui\project")
    for file in files:
        list_file.insert(END,file)

def delete_file():

    for index in reversed(list_file.curselection()):
        list_file.delete(index)

def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':  #enter the cancle
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)

def merge_image():

    try:
        img_width = cmb_width.get()
        if img_width == "original width":
            img_width = -1
        else:
            img_width = int(img_width)

        img_space = cmb_spce.get()
        if img_space == "small":
            img_space = 30
        elif img_space == "middle":
            img_space = 60
        elif img_space == "large":
            img_space = 90
        else:
            img_space = 0

        img_format = cmb_format.get().lower()

        images = [Image.open(x)  for x in list_file.get(0,END)]

        image_sizes = []
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width*x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0],x.size[1]) for x in images]

        #widths = [x.size[0] for x in images]
        #heights = [x.size[1] for x in images]
        widths, heights = zip(*image_sizes)
        max_width, total_height = max(widths), sum(heights)

        if img_space > 0:
            total_height += (img_space * (len(images) -1))

        result_image = Image.new("RGB", (max_width, total_height),(255,255,255))
        y_offset=0


        for idx, img in enumerate(images):

            if img_width > -1:
                img = img.resize((image_sizes[idx]))


            result_image.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx+1)/len(images) *100
            p_bar.set(progress)
            progress_bar.update()

        file_name = "nadophto." + img_format
        dest_path = os.path.join(txt_dest_path.get(),file_name)
        result_image.save(dest_path)

        msgbox.showinfo("Notice","Finish")
    except Exception as err:
        msgbox.showerror("ERROR",err)


def start():


    if list_file.size()==0:
        msgbox.showwarning("warning", "add the image file")
        return
    if len(txt_dest_path.get())==0:
        msgbox.showwarning("warning", "add the save route")
        return
    merge_image()


root = Tk()
root.title("Gui Project")

# file frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="add file", padx=5, pady=5, width=12 , command=add_file)
btn_add_file.pack(side="left")

btn_delete_file = Button(file_frame, text="delete file", padx=5, pady=5, width=12, command=delete_file)
btn_delete_file.pack(side="right")


# list frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# path frame
path_frame = LabelFrame(root, text="save route")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill = "x", expand=True, ipady=4, padx=5, pady=5)

btn_dest_path = Button(path_frame, text="find", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# option frame
option_frame = LabelFrame(root, text="Option")
option_frame.pack(padx=5, pady=5, ipady=5)

lbl_width = Label(option_frame, text="width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_wdith=["original width", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame, state="readonly", values=opt_wdith, width=13)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

lbl_space = Label(option_frame, text="space", width = 8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["none", "small", "middle", "large"]
cmb_spce = ttk.Combobox(option_frame, state="readonly", width=10, values=opt_space)
cmb_spce.current(0)
cmb_spce.pack(side="left", padx=5, pady=5)

lbl_format = Label(option_frame, text="format", width = 8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state="readonly", width=10, values=opt_format)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# progress bar
progress_frame = LabelFrame(root, text="progression")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_bar = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame,maximum=100, variable=p_bar)
progress_bar.pack(fill="x", padx=5, pady=5)

# start frame
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text="close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(run_frame, padx=5, pady=5, text="start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()




'''
2.54.58
'''