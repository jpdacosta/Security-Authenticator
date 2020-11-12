class DataCollectorClass:
            
    def collectUserInput(self):
        username = input("Username: ")
        password = input("Password: ")
        userData = {"Username": username,
                    "Password": password}
        # print(userData["Username"]+ " " + userData["Password"])
        return userData
    
    
        



