# First
import re
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")

db = client["FilmArsivSistemi"]
summary = db["film_verileri"]

# clean datas (delete emojis, symbols, flags etc) and update in mongodb

for x in summary.find({}):
    for key, value in x.items():
        if key == "Özet":
            myquery = { "Özet": value }
            emoji_pattern = re.compile("["
                                       u"\U0001F600-\U0001F64F"  # emoticons
                                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                       u"."
                                       u"("
                                       u"/"
                                       u"'"
                                       u":"
                                       u","
                                       u";"
                                       u")"
                                       "]+", flags=re.UNICODE)
            value = emoji_pattern.sub(r'', value)
            print(value)
            newvalues = {"$set": {"Özet": value}}
            x = summary.update_one(myquery, newvalues)

