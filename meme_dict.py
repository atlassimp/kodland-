meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GH": "Bir oyun oynarken takım arkadaşlarınıza güzel yarı demenin kısa yoludur.", 
            "GL": "Bol şans",
            "IGL": "Oyunlarda bir takımın beyni, vuruşçusu ve her şeyi olan kişiye verilen ad.",
            "FR": "Bir kişiye katıldığını söylemenin bir yolu",
            "NS": "Güzel vuruş",
            }
word = input("Anlamadığın bir kelime yaz!(Büyük harflerle ;): ")

if word in meme_dict:
    print("Aradığın kelime sözlükte mevcut!")
    print(meme_dict)
else:
    print("Aradığın kelimeyi en yakın zamanda ekleyeceğiz :(")
