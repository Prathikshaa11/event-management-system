import os
class Item:
    
    def write_items(self):
        print("List of Events:")
        events = ["Business-Event", "Community-Event", "Personal-Event"]
        file_obj = open(os.getcwd() + "\events.txt", "w")
        str1 = " "
        file_obj.write(str1.join(events))
    event_registered = []

    def item_Register(self):
        file_obj = open(os.getcwd() + "\events.txt", "r")
        event = file_obj.read()
        print(event)
        event = list(event.split(" "))
        print(event)
        items = input("Enter the event to register \n")
        if items in event:
            if items in self.event_registered:
                print("Event already Exists")
            else:
                self.event_registered.append(items)
            option = input("Do you want to register for any events Yes or NO ")
            if option == "Yes" or option == "YES" or option == "yes":
                from booking import booking
                obj=booking()
                obj.information()
                
            else:
                from login import login
                obj=login()
                obj.log()

        else:
            print("Events not in the List")
            self.item_Register()

    def get_Item_Registered(self):
        return self.event_registered


    
