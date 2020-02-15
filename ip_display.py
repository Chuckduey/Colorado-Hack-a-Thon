#
# Dipslays the IP address,  Host name and Gateway
import os
import socket
import time
from Tkinter import *
host = "None"
ipaddr = "None"
gateway = "None"
update = 5000

#
def update_ip():
     global clock
     try:
         gw = os.popen("ip -4 route show default").read().split()
         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         s.connect((gw[2], 0))
         ipaddr = s.getsockname()[0]
         gateway = gw[2]
         host = socket.gethostname()
         s.close()
     except:
         gateway = "None"
         host =  "None"
         ipaddr = "None"
     clock.config(text="Host name = "+host+"\nIp Address = "+ ipaddr + "\nGateway =" + gateway, anchor="c")
     clock.after(update,update_ip)
     
def update_ip_nl():
     global clock
     gw = os.popen("ip -4 route show default").read().split()
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     s.connect((gw[2], 0))
     ipaddr = s.getsockname()[0]
     gateway = gw[2]
     host = socket.gethostname()
     s.close()
     clock.config(text="Host Name = "+host+"\nIp Address = "+ ipaddr + "\nGateway =" + gateway, anchor="c")

root = Tk ()
root.title("IP Adresses")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))
 
clock1 = Text(root, height=5, width=41,bg='#2f2f34')
clock = Label(root, font=('times', 20, 'bold'),bg='#2f2f34',fg='#cdcdd1')
clock.pack(fill=BOTH, expand=1)
clock1.pack()
logo = PhotoImage(file='/home/pi/Colorado-Hack-a-Thon/Keysight_Logo.PNG')
clock1.image_create("current",image=logo)
clock.config(text="Host name = "+host+"\nIp Address = "+ ipaddr + "\nGateway =" + gateway, anchor="c")
b=Button(root, text="Refresh", anchor=S, command=update_ip_nl)
b.pack()
#time.sleep(5)
# Main 
clock.after(update,update_ip)

# Start main loop
root.mainloop( )
