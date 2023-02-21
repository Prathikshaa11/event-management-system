import re
class login():
    def log(self):
        print("Welcome to the Elite company")
        print("1. Register")
        print("2. Login")
        option = input("please make a choice:")
        if option == 1:
            print("Register here")
        elif option == 2:
            print("Login here:")
    
        print("Register here")
        Name = input("Enter your Name:")
        Email = input("Enter your EmailId:")
        new_password = input("Set new password:")
        password2 = input("Confirm your password:")
        print("Registration Successful")

        print("Log in here")

        UserName = input("Enter the UserName:")
        Password = input("Enter the password:")

        x = True
        while x:  
            if (len(Password)<6 or len(Password)>12):
                break
            elif not re.search("[a-z]",Password):
                 break
            elif not re.search("[0-9]",Password):
                break
            elif not re.search("[A-Z]",Password):
                break
            elif not re.search("[$#@]",Password):
                break
            elif re.search("\s",Password):
                break
            else:
                ("Valid Password")
                x=False
                break
                print("Log in successful")

            if x:
                print("Not a Valid Password")
            
obj=login()
obj.log()
