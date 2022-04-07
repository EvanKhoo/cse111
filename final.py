"""
Program: Final
Author: Evan Khoo
Purpose: Write a significant python program to scrape webpages and deliver specific information
Date: 03/28/2022
IDE: Visual Studios Code
"""
global Entry
from urllib.request import urlopen
import requests
from tkinter import *
from bs4 import BeautifulSoup

# creating the win
win = Tk()
win.title("Python MLA source formatter")
win.geometry("500x500")
win.configure(bg='lightgray')


greeting = Label(win, text="Hello, welcome to Evan's text to MLA formatter")
greeting.pack()

def temp_text(e):
    entry.delete(0,"end")

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40, text="Please enter website URL")
entry.insert(0, "Please enter a valid website URL")
entry.pack()
entry.bind("<FocusIn>", temp_text)

def main():

    page = requests.get(entry.get())
    soup = BeautifulSoup(page.content, "html.parser")
    
    webscraping(win, soup)

#Create a Button to check citations
Button(win, text= "Create Citation", width= 20, command = main).pack(pady=20)


def webscraping(win, soup):
    def organization():
        
        auth_label = auth_entry.get()
        pub_label = pub_entry.get()
        entry_label = entry.get()
        result_title.config(text=f"{auth_label}, {title}, {pub_label}\n\t{entry_label}")
    
    try:
        for title in soup.find("title"):
            titles_label=Label(win,text="The website title is: ")
            titles_label.pack()
            title_label = Label(win, text = title.get_text())
            title_label.pack()
            break
        try:
            for author in soup:
                author = soup.find("a", class_="text-muted")
                auth_label=Label(win,text="The website author is: ")
                auth_label.pack()
                author_label = Label(win, text= author.get_text())
                author_label.pack()
                break
            return author_label
        except:
            auth_manual=Label(win,text="Unable to find author, please enter one manually")
            auth_manual.pack()
            auth_entry= Entry(win, width= 40)
            auth_entry.pack()
        try:
            html=urlopen(entry.get()).read()
            script=BeautifulSoup(html, features="html.parser")
            for publisher in script(["script", "style"]):
                script.extract()
                text=script.get_text()
                publisher = script.find(text, string="publish")
                pub_label=Label(win,text="The website publisher is: ")
                pub_label.pack()
                publisher_label=Label(win,text=publisher.text.strip())
                publisher_label.pack()
                break
        except:
            pub_manual=Label(win,text="Unable to find publisher, please enter one manually")
            pub_manual.pack()
            pub_entry= Entry(win, width= 40)
            pub_entry.pack()
    except:
        title_manual=Label(win,text="Unable to find title, please enter one manually")
        title_manual.pack()
        title_entry= Entry(win, width= 40)
        title_entry.pack()
    
    Button(win, text= "Add to Citation", width= 20, command = organization).pack(pady=20)

    result_title=Label(win,width=50,height=10,text="",wraplength=(300),justify=LEFT,
    font=("Times new roman", "12"))
    result_title.pack(pady=20,side=TOP)

win.mainloop()

if __name__ =="__main__":
    main()