import random
import time

# Kooli ja erialade faktid
voco_faktid = {
    "Sisseastumine": [
        "Sisseastumiseks tuleb esitada avaldus ja sooritada vastuvõtukatse.",
        "Võid valida endale sobiva eriala.",
        "Sisse astuda saab läbi kooli kodulehe.",
        "Pakub õppimisvõimalusi ka hariduslike erivajadustega õpilastele.",
        "Õpingute alustamise eeltingimus on omandatud põhiharidus."
    ],
    "ITA_eriala": [
        "ITA eriala õppekava keskendub praktilistele oskustele ja projektidele.",
        "Õpib üldaineid- laia matemaatikat, emakeelt ja inglise keelt ning sooritab õppe lõpus riigieksamid.",
        "ITA eriala tudengitel on võimalus osaleda rahvusvahelistel võistlustel ja konverentsidel.",
        "ITA eriala lõpetanud saavad töötada tarkvaraarendusega, andmeanalüüsi ja projekti juhtimise valdkonnas.",
        "Eriala õppe kestab 4 aastat"
    ],
    "ITS_eriala": [
        "ITS erialal on palju praktilisi töid, kus tudengid saavad oma oskusi rakendada.",
        "ITS erialal on õppejõududena töötamas kogenud spetsialistid oma ala valdkonnast.",
        "Õppeprotsessis kasutatakse kaasaegseid tehnoloogiaid ja metoodikaid, nagu näiteks projektijuhtimistarkvarasid, mis valmistavad lõpetajaid ette töötamiseks tarkvaraarendusprojektidega.",
        "ITS on populaarne eriala, mis keskendub infotehnoloogia süsteemide analüüsile, projekteerimisele ja arendamisele.",
        "Selle eriala lõpetajad on hinnatud spetsialistid IT-sektoris, kuna neil on lai teadmiste pagas programmeerimisest, andmebaasidest, arvutivõrkudest ja tarkvaraarenduse protsessist."
    ],
    "Õppimine": [
        "75 kursust kokku.",
        "Voco pakub 14 tasuta kursust.",
        "Õppimine toimub väikestes gruppides, et tagada individuaalne lähenemine.",
        "Õppekava on välja töötatud koostöös ettevõtetega ning õppetöö sisaldab palju praktilisi ülesandeid ja projekte.",
        "Õppetöö toimub nii päeva- kui kaugõppe vormis. See annab võimaluse töö ja õpingute sobitamiseks ning paindlikkuseks.",
    ],
    "Elu_olu": [
        "Voco koolis on mugavad õpperuumid ja kaasaegne varustus.",
        "Voco kooli tudengid saavad kasutada erinevaid vaba aja veetmise võimalusi.",
        "Voco õpilastel on võimalik taotleda järgmisi toetusi: õppetoetus, eritoetus koolilõuna toetus ja  toetuse sõidukulude hüvitamine.",
        "On olemas tugikeskus, mis  aitab leida võimalusi selleks, et iga õpilane saaks realiseerida oma tegelikku potentsiaali.",
        "On 6 toetavad teenust: arstiabi, haldusteenistus, infokogu, IT-teenistus, kantselei, Sport.",
    ],
}





# Mängufunktsioon
def play_game():
    print("Tere tulemast Voco kooli ja erialade tutvustamise mängu!")
    name = input("Mis on teie nimi? ")

    # Alusta punktide arvestust
    points = 0
    # Käivita mäng, kuni kasutaja soovib mängida
    while True:
        time.sleep(2)
        print("Valige, mida soovite teha:")
        print("1. Tutvu sisseastumisega")
        print("2. Tutvu ITA erialaga")
        print("3. Tutvu ITS erialaga")
        print("4. Tutvu õppimisega") 
        print("5. Elu-oluga Voco koolis")
        print("6. Välju mängust")
        choice = input("Valige number: ")


        if choice == "1":
            fact = random.choice(voco_faktid["Sisseastumine"])
            print(fact)
            points += 10
        elif choice == "2":
            fact = random.choice(voco_faktid["ITA_eriala"])
            print(fact)
            points += 10
        elif choice == "3":
            fact = random.choice(voco_faktid["ITS_eriala"])
            print(fact)
            points += 10
        elif choice == "4":
            fact = random.choice(voco_faktid["Õppimine"])
            print(fact)
            points += 10
        elif choice == "5":
            fact = random.choice(voco_faktid["Elu_olu"])
            print(fact)
            points += 10
        elif choice == 'quit':
            break