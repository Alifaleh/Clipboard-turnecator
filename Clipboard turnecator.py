# clipboard  truncator

import win32clipboard
from time import sleep
from tkinter import *
import sys



def set_clipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()

def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data

def clean(text):
    texta = text.split("\r\n")
    text=""
    for l in texta:
        text+=" "+l
    text2=""
    while text2!=text:
        text = text.replace("  "," ")
        text2 = text
        text = text.replace("  ", " ")
    return text



root=Tk()
root.title("Clipboard truncator")
root.resizable(False, False)

frame = LabelFrame(root, text="", padx=20, pady=20, bg="#333")
frame.grid(row=1, column=0, columnspan=2, pady=0, padx=0)

label = Label( frame, text="Welcome to Clipboard truncator\n\nBy : Ali A.faleh\n\nEmail : Alifalih783783@gmail.com", bg="#333", fg="#fff")
label.config(font=("Courier", 18))
label.grid(row=0, column=0, columnspan="3", pady=10)

lt=""

try:
    while root.state()=="normal" or root.state()=="iconic":
        root.update()
        try:
            text=get_clipboard()
            if lt!=text:
                text=clean(text)
                set_clipboard(text)
                lt=text
            sleep(0.05)
        #except TypeError:
        #    win32clipboard.OpenClipboard()
        #    win32clipboard.EmptyClipboard()
        #    win32clipboard.SetClipboardText("Type error")
        #    win32clipboard.CloseClipboard()
        #   sleep(0.25)
        #    continue
        except:
            sleep(0.25)
            continue
except:
    pass




