from urllib.request import urlopen
import time
import requests
from tkinter import *
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# creating the win
win = Tk()
win.title("Python MLA source formatter")
win.geometry("500x500")
win.configure(bg='lightgray')
def organization():
    title_label = title_entry.get()
    entry_label = entry.get()
    t.config(text= f"{title_label}\n\t {entry_label}")

title_entry= Entry(win, width= 40)
title_entry.pack()
entry= Entry(win, width= 40)
entry.pack()

Button(win, text= "Add to Citation", width= 20, command=organization).pack(pady=20)

t = Label(win, width=40, height=20, text="")
t.pack()

win.mainloop()