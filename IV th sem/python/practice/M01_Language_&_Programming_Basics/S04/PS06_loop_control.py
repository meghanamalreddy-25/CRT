'''for password 3 times Once attempt is made, show account locked'''
exsisting_password="S@123"
for i in range(3):
    password=input()
    if password==exsisting_password:
        print("login sucesfull")
        break
else:
    print("Account is Locked")