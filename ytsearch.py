import os
from pytube import YouTube,Search
import webbrowser

search = input("enter search term: ")

print("\nsearching pls wait.........")

s = Search(search)

id = str(s.results[0]).split("=")[1]

if os.name == "nt":
    os.system("cls")
if os.name == "posix":
    os.system("clear")

url = "http://youtube.com/watch?v="+id

yt = YouTube(url)

vid_title = yt.title
thumbnail = yt.thumbnail_url
channelUrl = yt.channel_url
channelName = yt.author

print("")

print("title: "+vid_title+"\n\nurl: "+url+"\n\nthumbnail: "+thumbnail+"\n\nchannel url: "+channelUrl+"\n\nchannel name: "+channelName)

print("")

choice = input("Do You want to visit video or channel or thumbnail [v/c/t] or type QUIT: ")

rep = True

while rep == True:
    if choice == "v":
        webbrowser.open_new_tab(url)
        print("url opened in browser")
    elif choice == "c":
        webbrowser.open_new_tab(channelUrl)
        print("channel url opened in browser")
    elif choice == "t":
        webbrowser.open_new_tab(thumbnail)
        print("thumbnail opened in browser")
    elif choice == "QUIT":
        print("Quitting!!!!")
        rep = False
    else:
        print("incorrect command try again")

    if choice != "QUIT":
        choice = input("Do You want to visit video or channel or thumbnail [v/c/t] or type QUIT: ")

print("bye bye")
