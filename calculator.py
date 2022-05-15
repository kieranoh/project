import tkinter.messagebox as msgbox
from tkinter import *
import keyboard

start = 1
finish = 0
start_end_num = 0
result = 0
error_key = 0


root = Tk()
root.title("Calculator")

def start_end():
    global start_end_num, start, finish
    if start == 1 or finish == 1:
        screen_entry.delete(0,END)
        start = 0
        finish = 0
    if start_end_num == 0:
        screen_entry.insert(END, "(")
        start_end_num +=1
    elif start_end_num == 1:
        screen_entry.insert(END, ")")
        start_end_num = 0
    screen_label.config(text=screen_entry.get())

def click(text):
    global start
    global finish
    global result
    if start == 1:
        screen_entry.delete(0,END)
        start = 0

    if finish == 1:
        screen_entry.delete(0, END)
        screen_entry.insert(END, result)

        finish = 0
    screen_entry.insert(END,text)
    screen_label.config(text=screen_entry.get())

def delete():
    global  finish
    if finish ==1:
        screen_entry.delete(0, END)
        screen_entry.insert(END, result)
        screen_entry.delete(len(screen_entry.get())-1,END)
        finish = 0
    else:
        screen_entry.delete(len(screen_entry.get()) - 1, END)
    screen_label.config(text=screen_entry.get())


def clear():
    screen_entry.delete(0,END)
    global start
    global finish
    finish = 0
    start = 1
    screen_entry.insert(0,"0")
    screen_label.config(text=screen_entry.get())

def enter():
    global error_key
    if error_key == 0:
        formula = screen_entry.get()
        screen_entry.insert(END, "=")
        global result
        try:
            result = eval(formula)
            screen_entry.insert(END,result)
            global finish
            finish = 1
        except SyntaxError:
            error_key = 1
            msgbox.showerror("ERROR","Put the Number in the End or Close the parenthesis")
            screen_entry.delete(len(screen_entry.get()) - 1, END)
        except Exception as err:
            error_key=1
            msgbox.showerror("ERROR", err)
            screen_entry.delete(len(screen_entry.get()) - 1, END)
        screen_label.config(text=screen_entry.get())
    else:
        error_key = 0


def percent():
    global result
    global finish
    formula = screen_entry.get()
    screen_entry.delete(0, END)
    if finish == 1:
        result_percent = "{} % = {}".format(result, result/100)
        result = result /100
        screen_entry.insert(END, result_percent)
    else:
        try:
            result = eval(formula) /100
            print(result)
            screen_entry.insert(END, result)
            finish = 1
        except SyntaxError:
            msgbox.showerror("ERROR", "Put the Number in the End")
        except Exception as err:
            msgbox.showerror("ERROR", err)
    screen_label.config(text=screen_entry.get())

# screen
screen_frame = Frame(root,relief="solid",bd=2, padx=3,pady=3)
screen_frame.pack(expand=True, fill="x",padx=7,pady=5)
screen_label = Label(screen_frame, width=40,text='0')
screen_label.pack(expand=True, fill="x",ipadx=5,ipady=3)
screen_entry = Entry(screen_frame)
screen_entry.insert(0,"0")

# button
btn_frame = Frame(root, relief="solid", bd=2, padx=3, pady=3)
btn_frame.pack(expand=True,fill="x", padx=7, pady=5, ipadx=5, ipady=5)

btn_frame_1 = Frame(btn_frame)
btn_frame_2 = Frame(btn_frame)
btn_frame_3 = Frame(btn_frame)
btn_frame_4 = Frame(btn_frame)
btn_frame_5 = Frame(btn_frame)

btn_frame_1.pack()
btn_frame_2.pack()
btn_frame_3.pack()
btn_frame_4.pack()
btn_frame_5.pack()

btn_percent = Button(btn_frame_1, text="%",width=11,height=3, command=percent)
btn_start_end = Button(btn_frame_1, text="( )",width=11,height=3,command=start_end)
btn_div = Button(btn_frame_1, text="/",width=11,height=3,command=lambda : click('/'))
btn_del = Button(btn_frame_1, text="del",width=11,height=3,command=delete)

btn_7 = Button(btn_frame_2, text="7",width=11,height=3,command=lambda : click('7'))
btn_8 = Button(btn_frame_2, text="8",width=11,height=3,command=lambda : click('8'))
btn_9 = Button(btn_frame_2, text="9",width=11,height=3,command=lambda : click('9'))
btn_mul = Button(btn_frame_2, text="X",width=11,height=3,command=lambda : click('*'))

btn_4 = Button(btn_frame_3, text="4",width=11,height=3,command=lambda : click('4'))
btn_5 = Button(btn_frame_3, text="5",width=11,height=3,command=lambda : click('5'))
btn_6 = Button(btn_frame_3, text="6",width=11,height=3,command=lambda : click('6'))
btn_min = Button(btn_frame_3, text="-",width=11,height=3,command=lambda : click('-'))

btn_1 = Button(btn_frame_4, text="1",width=11,height=3,command=lambda : click('1'))
btn_2 = Button(btn_frame_4, text="2",width=11,height=3,command=lambda : click('2'))
btn_3 = Button(btn_frame_4, text="3",width=11,height=3,command=lambda : click('3'))
btn_plus = Button(btn_frame_4, text="+",width=11,height=3,command=lambda : click('+'))

btn_clear = Button(btn_frame_5, text="C",width=11,height=3,command=clear)
btn_0 = Button(btn_frame_5, text="0",width=11,height=3,command=lambda : click('0'))
btn_dot = Button(btn_frame_5, text=".",width=11,height=3,command=lambda : click('.'))
btn_enter = Button(btn_frame_5, text="=",width=11,height=3,command=enter,)

btn_percent.pack(side="left",expand=True,padx=3,pady=3)
btn_start_end.pack(side="left",expand=True,padx=3,pady=3)
btn_div.pack(side="left",expand=True,padx=3,pady=3)
btn_del.pack(side="left",expand=True,padx=3,pady=3)

btn_7.pack(side="left",expand=True,padx=3,pady=3)
btn_8.pack(side="left",expand=True,padx=3,pady=3)
btn_9.pack(side="left",expand=True,padx=3,pady=3)
btn_mul.pack(side="left",expand=True,padx=3,pady=3)

btn_4.pack(side="left",expand=True,padx=3,pady=3)
btn_5.pack(side="left",expand=True,padx=3,pady=3)
btn_6.pack(side="left",expand=True,padx=3,pady=3)
btn_min.pack(side="left",expand=True,padx=3,pady=3)

btn_1.pack(side="left",expand=True,padx=3,pady=3)
btn_2.pack(side="left",expand=True,padx=3,pady=3)
btn_3.pack(side="left",expand=True,padx=3,pady=3)
btn_plus.pack(side="left",expand=True,padx=3,pady=3)

btn_clear.pack(side="left",expand=True,padx=3,pady=3)
btn_0.pack(side="left",expand=True,padx=3,pady=3)
btn_dot.pack(side="left",expand=True,padx=3,pady=3)
btn_enter.pack(side="left",expand=True,padx=3,pady=3)

keyboard_list = ["1","2","3","4","5","6","7","8","9","0","+","-","*","/","Shift + 9","Shift + 0","Shift + 5","c","Backspace","=","Enter","Shift + ="]

keyboard.add_hotkey(keyboard_list[0],lambda : click(keyboard_list[0]))
keyboard.add_hotkey(keyboard_list[1],lambda : click(keyboard_list[1]))
keyboard.add_hotkey(keyboard_list[2],lambda : click(keyboard_list[2]))
keyboard.add_hotkey(keyboard_list[3],lambda : click(keyboard_list[3]))
keyboard.add_hotkey(keyboard_list[4],lambda : click(keyboard_list[4]))
keyboard.add_hotkey(keyboard_list[5],lambda : click(keyboard_list[5]))
keyboard.add_hotkey(keyboard_list[6],lambda : click(keyboard_list[6]))
keyboard.add_hotkey(keyboard_list[7],lambda : click(keyboard_list[7]))
keyboard.add_hotkey(keyboard_list[8],lambda : click(keyboard_list[8]))
keyboard.add_hotkey(keyboard_list[9],lambda : click(keyboard_list[9]))
keyboard.add_hotkey(keyboard_list[10],lambda : click(keyboard_list[10]))
keyboard.add_hotkey(keyboard_list[11],lambda : click(keyboard_list[11]))
keyboard.add_hotkey(keyboard_list[12],lambda : click(keyboard_list[12]))
keyboard.add_hotkey(keyboard_list[13],lambda : click(keyboard_list[13]))
keyboard.add_hotkey(keyboard_list[14],lambda : click("("))
keyboard.add_hotkey(keyboard_list[15],lambda : click(")"))
keyboard.add_hotkey(keyboard_list[16],percent)
keyboard.add_hotkey(keyboard_list[17],clear)
keyboard.add_hotkey(keyboard_list[18],delete)

keyboard.add_hotkey(keyboard_list[20],enter)
keyboard.add_hotkey(keyboard_list[21],lambda : click("+"))







root.mainloop()