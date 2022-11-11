#importing libraries
import qrcode

#taking inputs like data and path to save from user
data = input("Enter data: ")
path = input("Name your qrcode: ")

#make the qrcode and save it in storage path
img = qrcode.make(f"{data}")
img.save(f"data/{path}.png")
