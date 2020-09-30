import pymongo
import json 
from pandas import json_normalize
from bson.json_util import dumps

cluster = pymongo.MongoClient("mongodb://username:password@*************************************************/DatabaseName")

# Enter DataBase Name
mydb = cluster["DatabaseName"]

# Enter Collection Name
collection= mydb["CollectionName"]

# Fill query or for all data leave empty
document = collection.find({})

json_string = dumps(document)

# Converting JSON String to JSON Object
json_obj = json.loads(json_string)

# Converting JSON Object to Pandas Dataframe
data1 = json_normalize(json_obj)

# Enter File Name
data1.to_csv("FileName.csv")
