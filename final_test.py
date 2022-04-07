"""
Program: Final_test
Author: Evan Khoo
Purpose: Write a significant python program to scrape webpages and deliver specific information
Date: 03/28/2022
IDE: Visual Studios Code
"""
import pytest
from pytest import *
import pytest
import unittest
import requests
from bs4 import BeautifulSoup
from tkinter import *
from final import webscraping, main

win = Tk()
win.geometry("500x500")
page = requests.get()
soup = BeautifulSoup(page.content, "html.parser")

class FormattingTestCase(unittest.TestCase):
    def test_main(self):

        self.assertTrue("https://")

    def test_webscraping(self):
        """Verify that the webscraping function works correctly.
        Parameters: win, soup
        Return: nothing
        """
        #Test that it can wont work without proper tag and will work despite lack of information

        scraper=webscraping(win, "https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/#:~:text=First%20you%20need%20to%20create,cases%20of%20your%20function's%20behavior.&text=First%2C%20you%20need%20to%20import,want%20to%20test%2C%20formatted_name()%20.")
        scraper.assertTrue(win,soup)
        self.assertTrue("Jeff Bezos, The Boring Company, https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/#:~:text=First%20you%20need%20to%20create,cases%20of%20your%20function's%20behavior.&text=First%2C%20you%20need%20to%20import,want%20to%20test%2C%20formatted_name()%20.")

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
if __name__=="__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])