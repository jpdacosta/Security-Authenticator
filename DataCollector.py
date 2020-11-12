class DataCollector:
            
    def collectUserInput(self):
        username =  input("Username: ")
        password = input("Password: ")
        userData = {"Username": username,
                    "Password": password}
        return userData


from DataCollector import DataCollector
datCol = DataCollector()
userData = datCol.collectUserInput
print("Username: " + userData["Username"] + " Password: " + userData["Password"])
