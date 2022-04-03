"""
Program: Final
Author: Evan Khoo
Purpose: Write a significant python program to scrape webpages and deliver specific information
Date: 03/28/2022
IDE: Visual Studios Code
"""

from urllib.request import urlopen
import time
import requests
from tkinter import *
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def main():
    global Entry

    # creating the window
    window = Tk()
    window.title("Python MLA source formatter")
    window.geometry("500x500")
    window.configure(bg='lightgray')
    
    greeting = Label(window, text="Hello, welcome to Evan's text to MLA formatter")
    greeting.pack()

    #Create an Entry widget to accept User Input
    entry= Entry(window, width= 40)
    entry.focus_set()
    entry.pack()

    def webscraping():

        page = requests.get(entry.get())
        soup = BeautifulSoup(page.content, "html.parser")
        
        title(window, soup)
        author(window, soup)
        publisher(window, entry)

        def organization():
            text= Text(window, width=40, height=10)
            text.pack()

            insert_text= f"""
            {author(window , soup)}\n 
            \t{title(window, soup)}\n 
            \t{publisher(window, entry)}
            """
            text.insert(END, insert_text)

        Button(window,text="Continue",width=20,command=organization).pack(pady=20)

    #Create a Button to validate Entry Widget
    Button(window, text= "Create Citation", width= 20, command = webscraping).pack(pady=20)

    window.mainloop()


def title(window, soup):
    try:
        for title in soup.find_all("title"):
            titles_label=Label(window,text="The website title is: ")
            titles_label.pack()
            title_label = Label(window, text = title.get_text())
            title_label.pack()
            break
    except:
        title_manual=Label(window,text="Unable to find title, please enter one manually")
        title_manual.pack()
        title_entry= Entry(window, width= 40)
        title_entry.focus_set()
        title_entry.pack()

def author(window, soup):
    try:
        for author in soup:
            author = soup.find("a", class_="text-muted")
            auth_label=Label(window,text="The website author is: ")
            auth_label.pack()
            author_label = Label(window, text= author.text.strip())
            author_label.pack()
            break
    except:
        auth_manual=Label(window,text="Unable to find author, please enter one manually")
        auth_manual.pack()
        auth_entry= Entry(window, width= 40)
        auth_entry.focus_set()
        auth_entry.pack()

def publisher(window, entry):
    try:
        html=urlopen(entry.get()).read()
        script=BeautifulSoup(html, features="html.parser")
        for publisher in script(["script", "style"]):
            script.extract()
            text=script.get_text()
            publisher = script.find(text, string="publish")
            pub_label=Label(window,text="The website publisher is: ")
            pub_label.pack()
            publisher_label=Label(window,text=publisher.text.strip())
            publisher_label.pack()
            break
    except:
        pub_manual=Label(window,text="Unable to find publisher, please enter one manually")
        pub_manual.pack()
        pub_entry= Entry(window, width= 40)
        pub_entry.focus_set()
        pub_entry.pack()


if __name__ =="__main__":
    main()