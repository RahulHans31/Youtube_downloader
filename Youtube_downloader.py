#importing Youtube for getting the video 
# importing tkinter for GUI
from tkinter import *
from pytube import YouTube

root = Tk()#making a screen
root.geometry('500x300')#passing the screen geometry
root.resizable(0,0)
root.title("Youtube video downloader")#title for the window


link = StringVar() #making a variable link 

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

#making a function for downloading
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()