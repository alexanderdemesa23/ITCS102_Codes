
from getpass import getpass

isLogin = False

while isLogin == False:
  username = input("enter username --> ")
  password = getpass("enter password --> ")

  if username == "xander" and password == "alex1":
    print("access granted")
    isLogin = True
  else:
    print("access denied")
    isLogin = False
