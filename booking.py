import re
class booking():
    def __init__(self):
        pass
    print("Confirm your booking")
    def information(self):
        Name = input("Enter your Name:")
        email = input("Enter your email:")
        MobileNumber = int(input("Enter your MobileNumber:"))
        obj.validate_name(Name,email,MobileNumber)
      
    def validate_name(self,Name,email,MobileNumber):
              if  bool(re.findall('[a-zA-Z]',Name))==True:
                  obj.validate_email(email,MobileNumber)
              else:
                print("invalid name")
      
    def validate_email(self,email,MobileNumber):

        if re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", email):
            obj.validate_MobileNumber(MobileNumber)
            
        else:
            print("Invalid email")

    def validate_MobileNumber(self,MobileNumber):
        r = re.compile("(0|91)?[6-9][0-9]{9}") 
        if r!=None: 
            print("Successfully got the personal details")
        else:
            print("Invalid MobileNumber")
            


obj=booking()
obj.information()
print("Thankyou for registering with us we will contact you soon")


        

    
