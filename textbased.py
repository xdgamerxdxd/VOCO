import random

# küsib mängijalt nime
name = input("Tere! Mis on sinu nimi? ")

# tervitab mängijat
print(f"Tere tulemast, {name}! Sinu eesmärk on jõuda kooliaasta lõpuni ja saada hea hinne.")

# defineerib erinevad ülesanded ja vastused
tasks = {
    "matemaatika": [
        {
            "question": "Mis on kolmnurga pindala valem?",
            "answer": "a*h/2"
        },
        {
            "question": "Mis on ruutjuur arvust 64?",
            "answer": "8"
        },
        {
            "question": "Mis on ruutjuur arvust 100?",
            "answer": "10"
        }
    ],
    "ajalugu": [
        {
            "question": "Millal toimus Esimene Maailmasõda?",
            "answer": "1914-1918"
        },
        {
            "question": "Millal toimus Eesti Vabariigi taasiseseisvumine?",
            "answer": "1991"
        },
        {
            "question": "Millal toimus Teine Maailmasõda?",
            "answer": "1939-1945"
        }
    ],
    "bioloogia": [
        {
            "question": "Mis on evolutsioon?(vasta ühe sõnaga)",
            "answer": "areng"
        },
        {
            "question": "Mis on inimese keha kõige suurem organ?",
            "answer": "nahk"
        },
        {
            "question": "Kas kopsudesse mahub õhku a)Ühepalju , b) Vasakusse kopsu rohkem , c) Paremasse kopsurohkem?",
            "answer": "c "
        }
        
    ],
        }
        

# Defineerib funktsioon, mis küsib ülesannet ja kontrollib vastust
def ask_task(subject, tasks):
    task = random.choice(tasks[subject])
    print(task["question"])
    answer = input("Sisesta oma vastus: ")
    if answer.lower() == task["answer"].lower():
        print("Õige vastus! Sa said punkti.")
        return 1
    else:
        print("Vale vastus. Kaotasid punkti.")
        return -1

#alustab mängu
points = 0
for subject in tasks.keys():
    print(f"Tere tulemast {subject} väljakutsesse!")
    response = input("Kas soovid seda väljakutset proovida? (jah/ei) ")
    if response.lower() == "jah":
        points += ask_task(subject, tasks)
    else:
        print("Väljakutsest loobuti.")

#mängu lõpp
if points >= 3:
    print("Palju õnne! Sa said hea hinde.")
elif points > 0:
    print("Tubli töö! Sa said rahuldava hinde.")
else:
    print("Kahjuks ei saanud sa head hinnet.")
print(f"Said kokku {points} punkti.")








