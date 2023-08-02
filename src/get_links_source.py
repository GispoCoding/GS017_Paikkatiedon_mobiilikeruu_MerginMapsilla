from bs4 import BeautifulSoup
from tkinter import filedialog
import requests
from tkinter import *
import ctypes


root = Tk()
root.withdraw()
ctypes.windll.user32.MessageBoxW(0, "Select your .html file.", "Select file", 1)
file_selected = filedialog.askopenfilename()
ctypes.windll.user32.MessageBoxW(0, "Select a directory where images will be saved.", "Select directory", 1)
folder_selected = filedialog.askdirectory()
file = open(file_selected, encoding='utf-8')
print(folder_selected)

soup = BeautifulSoup(file,'html.parser')
images = soup.select('p img')


n=0
for i in images:
    url = f'{folder_selected}/image{n+1}.png'
    images_url = images[n]['src']
    img_data = requests.get(images_url).content
    with open(url, 'wb') as handler:
        handler.write(img_data)
    n+=1