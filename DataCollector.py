class DataCollectorClass:
            
    def collectUserInput(self):
        username =  input("Username: ")
        password = input("Password: ")
        userData = {"Username": username,
                    "Password": password}
        print(username)
        print(password)
        return userData


from DataCollector import DataCollectorClass
datCol = DataCollectorClass()
userData = datCol.collectUserInput
# print(userData["Üsername"])
# # print("Username: " + userData["Username"] + " Password: " + userData["Password"])
