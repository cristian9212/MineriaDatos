import requests, json

class usersInfo:

    def __init__(self):
      self.listUsers = []

    def getUsers(self):
        responUsers = requests.get("https://datos.gov.co/resource/jtnk-dmga.json")
        dataJson = responUsers.json()
        for ind in range(len(dataJson)):
            self.listUsers.append(dataJson[ind]['email_address'])



prueba = usersInfo()
prueba.getUsers()
