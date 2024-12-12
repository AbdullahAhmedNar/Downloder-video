from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x400")
root.configure(bg="#2c3e50")
root.resizable(0, 0)
root.title("YouTube Video Downloader")

Label(root, text="YouTube Video Downloader", font=('Helvetica', 20, 'bold'),
fg='white', bg="#2c3e50").pack(pady=20)

link = StringVar()
Label(root, text="Paste the link here:", font='Helvetica 15 bold', fg='white',
bg="#2c3e50").pack(pady=5)
link_en = Entry(root, width=60, textvariable=link, font='Helvetica 12', bd=3, relief=SOLID)
link_en.pack(pady=10)

status_label = Label(root, text='', font="Helvetica 15", fg='white', bg="#2c3e50")
status_label.pack(pady=10)

def download_video(quality):
    url = YouTube(str(link.get()))
    try:
        if quality == "high":

            video = url.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        elif quality == "low":

            video = url.streams.filter(progressive=True, file_extension="mp4").get_lowest_resolution()
        else:

            video = url.streams.filter(only_audio=True).first()


        video.download()
        status_label.config(text='Downloaded successfully!', fg='green')
    except Exception as e:
        status_label.config(text='Error: ' + str(e), fg='red')

frame = Frame(root, bg="#2c3e50")
frame.pack(pady=20)

b1 = Button(frame, text='Download High Quality', font='Helvetica 12 bold', bg='#3498db',
fg='white', padx=10, pady=5, relief=RAISED, bd=3, command=lambda: download_video("high"))
b1.grid(row=0, column=0, padx=10, pady=10)

b2 = Button(frame, text='Download Low Quality', font='Helvetica 12 bold', bg='#e74c3c',
fg='white', padx=10, pady=5, relief=RAISED, bd=3, command=lambda: download_video("low"))
b2.grid(row=0, column=1, padx=10, pady=10)

b3 = Button(frame, text='Download Audio Only', font='Helvetica 12 bold', bg='#2ecc71',
fg='white', padx=10, pady=5, relief=RAISED, bd=3, command=lambda: download_video("audio"))
b3.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
