# Second

import pandas as pd

dosya_ismi = "stop_words_turkish.txt"
dosya = open(dosya_ismi,"r",encoding="utf-8")
df = pd.read_csv("film_verileri.csv")
print(df["Özet"])
while True:
    kelime = dosya.readline()
    if kelime == "":
        break
    kelime = kelime[:-1]
    df["Özet"] = df.Özet.str.replace(" "+kelime+" "," ")
df.to_csv("C:/Users/MacBook/PycharmProjects/Film_Arama_Motoru/stop_data.csv")
dosya.close()

df = pd.read_csv("stop_data.csv")
print(df["Özet"])
