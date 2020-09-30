import pymongo
import json 
from pandas import json_normalize
from bson.json_util import dumps

cluster = pymongo.MongoClient("mongodb://username:password@*************************************************/DatabaseName")

mydb = cluster["DatabaseName"]

collection= mydb["CollectionName"]

document = collection.find({})

json_string = dumps(document)

# Converting JSON String to JSON Object
json_obj = json.loads(json_string)

# Converting JSON Object to Pandas Dataframe
data1 = json_normalize(json_obj)

data1.to_csv("FileName.csv")
