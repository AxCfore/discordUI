from tkinter import *
from tkinter import ttk
import mytools as mt

root = Tk()
root.title('Discord Admin Panel')
root.geometry('300x100')

ttk.Label(root, text="Servers:").grid(row=1, column=1)
ttk.Label(root, text="Users:").grid(row=2, column=1)

servers_list = [""]
users_list = [""]

server_value = StringVar()
user_value = StringVar()
message_val= StringVar()

guilds = mt.getJson("/users/@me/guilds", param={'limit':200})

for guild in guilds:
    servers_list.append(f"{guild['name']} - {guild['id']}")

def getGuildUsers(guild_ID):
    guild_ID = server_value.get()
    users = mt.getJson(f"/guilds/{guild_ID.split('-')[1]}/members", param={'limit': 1000})

    for user in users:
        user_id = user['user']['id']
        user_name = user['user']['username']
        users_list.append(f"{user_name} - {user_id}")

def getUser(userID):
    userID = user_value.get()
    user = mt.getJson(f"/users/{userID.split('-')[1]}")
    print(user)

def refreshUsers():
    users = ttk.OptionMenu(root, user_value, *users_list, command=getUser)
    users.grid(row=2, column=2)
    users.configure(width=20)

def sendMessage():
    userID = user_value.get().split('-')[1]
    getChannel = mt.postData("/users/@me/channels", param={'recipient_id': userID})
    sendmessage = mt.postData(f"/channels/{getChannel['id']}/messages", param={'content':message_val.get()})
    print(sendmessage)
    
servers = ttk.OptionMenu(root, server_value, *servers_list, command=getGuildUsers)
servers.grid(row=1, column=2)
servers.configure(width=20)

ttk.Button(root, text="Yenile", command=refreshUsers).grid(row=2, column=3)

ttk.Label(root, text="Message:").grid(row=3, column=1)
ttk.Entry(root, textvariable=message_val).grid(row=3, column=2)
ttk.Button(root, text="Gönder", command=sendMessage).grid(row=3 ,column=3)

server_value.set("Bir ID Seçin")
user_value.set("Bir Kullanici Seçin")

root.mainloop()