import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from PIL import Image, ImageTk  # Import the necessary Pillow modules

class Youtube(tk.Tk):
    def __init__(self):
        super(Youtube, self).__init__()
        self.title("Youtube Downloader")
        self.geometry("600x320+500+250")
        self.resizable(False, False)
        self.components()

    def components(self):
        # Open and convert the PNG image to PhotoImage
        img = Image.open("youtube-logo-png-2065.png")
        img = img.resize((250, 250), Image.ANTIALIAS)
        ytlogo = ImageTk.PhotoImage(img)

        self.ytTitle = Label(image=ytlogo)
        self.ytTitle.image = ytlogo  # Keep a reference to prevent garbage collection
        self.ytTitle.place(relx=0.5, rely=0.25, anchor="center")

        # Youtube link
        self.ytlabel = Label(text="Youtube Link")
        self.ytlabel.place(x=25, y=150)

        self.link = Entry(width=60)
        self.link.place(x=140, y=150)


        self.flabel = Label(text="Download Folder")
        self.flabel.place(x=25, y=183)

        self.flink = Entry(width=50)
        self.flink.place(x=140, y=183)


        self.browse = Button(text="Browse", command=self.browse)
        self.browse.place(x=455, y=180)


        resolutions = ["720p", "480p", "360p"]  # Add more resolutions as needed
        self.resolution_label = Label(self, text="Select Resolution:")
        self.resolution_label.place(x=25, y=220)

        self.resolution_var = StringVar(self)
        self.resolution_var.set(resolutions[0])  # Default resolution
        self.resolution_dropdown = OptionMenu(self, self.resolution_var, *resolutions)
        self.resolution_dropdown.place(x=140, y=215)


        self.download = Button(text="Download", command=self.down_yt)
        self.download.place(x=280, y=220)


    def browse(self):
        directory = filedialog.askdirectory(title="Save Video")
        self.flink.delete(0, "end")
        self.flink.insert(0, directory)

    def down_yt(self):
        link = self.link.get()
        folder = self.flink.get()
        resolution = self.resolution_var.get()


        YouTube(link).streams.filter(progressive=True, file_extension="mp4", resolution=resolution).order_by(
            "resolution").desc().first().download(folder)

app = Youtube()
app.mainloop()
