class DataCollector:
            
    def collectUserInput(self):
        username =  input("Username: ")
        password = input("Password: ")
        userData = {"Username": username,
                    "Password": password}
        return userData



datCol = DataCollector()
userData = datCol.collectUserInput

for items in userData:
    print("Username " + items["username'"] + " Password: " + items["Password"])
