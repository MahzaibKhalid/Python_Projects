import getpass

database = {"Mahzaib":1234,"Shoaib":12345}
username= input("Enter the Username:")
password= getpass.getpass("Enter the Password:")
for i in database.keys():
    if username == i:
        while int(password) != database.get(i):
            password = getpass.getpass("Enther Your Password Again:")
        break
print("Verfied!")