username=""
password=""
x=0
while x<3:
    username=input("Enter Username")
    password=input("Enter Password")
    x=x+1
    if username=="Pushkar" and password=="password":
        print("Welcome",username)
        break
    else:
        print("Enter again")

