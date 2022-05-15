import jpype
from typing import List
from jpype import JClass, java
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
db = client["FilmArsivSistemi"]
summary = db["stop_words2"]

ZEMBEREK_PATH = 'zemberek-full.jar'
jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))
TurkishMorphology = JClass('zemberek.morphology.TurkishMorphology')
morphology = TurkishMorphology.createWithDefaults()

for x in summary.find({}):
    for key, value in x.items():
        if key == "Özet":
            myquery = {"Özet": value}
            try:
                analysis: java.util.ArrayList = (
                    morphology.analyzeAndDisambiguate(value).bestAnalysis()
                )
            except:
                print(value)

            pos: List[str] = []
            for i, analysis in enumerate(analysis, start=1):
                pos.append(
                    f'{str(analysis.getLemmas()[0])}'
                )
            kelimeduz = ""

            for i in pos:
                kelimeduz += i
                kelimeduz += " "
            value = kelimeduz
            newvalues = {"$set": {"Özet": value}}
            x = summary.update_one(myquery, newvalues)
            print(value)