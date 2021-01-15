from pymongo import MongoClient
import json


class MongoConnect:
    def __init__(self, clientUrl, data=0):

        self.client = MongoClient(clientUrl)
        self.db = self.client.star

    def sendData(self, data):
        """

		Function: sendData

		Summary: send data to mongoDb

		Examples:  

		Attributes: 

			@param (self): 

            @param (data): data that beed to be send 


		Returns:  

		"""

        for pep in data:
            for key, item in pep.items():
                self.db.people.update({"name" : key}, {"name" : key, "data" : item}, upsert=True);
                # result = self.db.people.insert_one({"name" : key, 'data' : item})


    def getData(self):
        """
		Function: getData

		Summary: grab data from mongoDb

		Examples:  

		Attributes: 

			@param (self): 


		Returns:  

		"""
        return self.db.people.find()




if __name__ == '__main__':

    client = "mongodb+srv://iutUser:IG0Yo4sdvxvK5sEO@cluster0.ykzqu.mongodb.net/PROJETIUT?retryWrites=true&w=majority"
    app = MongoConnect(client)


    with open('./data.json') as outfile:
        data = json.load(outfile)
        app.sendData(data['people'])
    
    # name = []
    # data = app.getData()
    # j = {}
    # for d in data:
    #     # print(d['name'])
    #     j['people'][d['name']] = d['data']


    # for key, item in j.items():
    #     print(key)