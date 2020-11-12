from DataCollector import DataCollectorClass
from DataStorer import DataStorerClass
datCol = DataCollectorClass()
datStore = DataStorerClass()
userData = datCol.collectUserInput()
print("Username: " + userData["Username"] + " Password: " + userData["Password"])
datStore.insertUserData(userData)
