import qrcode

user_input = input("Enter the text or URL : ")
img = qrcode.make(user_input)
user_input_file = input("Enter the filename : ")
img.save(user_input_file)
print(f"QR code save as {user_input_file}")