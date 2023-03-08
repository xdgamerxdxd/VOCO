import time
def mäng(state):
  stat = state
  while stat:
    õige = ["Õ", "õ", "õige"]
    vale = ["V", "v", "vale"]
    correct = 0 

    nimi = input ("Mis on sinu nimi?") 

    print ("\nOK, " +  nimi +", alustame. Vastused on ainult õige või vale")
    time.sleep(2)

    print ("\n Siin saab õppida 7 osakonnas.")
    choice = input(">>> ")
    if choice in õige:
      correct += 1 #Kui õige, saab mängija 1 punkti.
    else:
      correct += 0
      
    print ("\nOn olemas voco siseveeb.")
    choice = input(">>> ")
    if choice in õige:
      correct += 1
    else:
      correct += 0  

    print ("\nITA JA ITS eriala õpitakse 3 aastad.")
    choice = input(">>> ")
    if choice in vale:
      correct += 1
    else:
      correct += 0 
      
    print ("\nKooli direktor on Raini Jõks.")
    choice = input(">>> ")
    if choice in õige:
      correct += 1
    else:
      correct += 0  
      
    print ("\nKoolis puuduvad huvitegevused.")
    choice = input(">>> ")
    if choice in vale:
      correct += 1
    else:
      correct += 0
      
    print ("\nKoolis on olemas õpilaskodu")
    choice = input(">>> ")
    if choice in õige:
      correct += 1
    else:
      correct += 0
        
    print ("\nSa lõpetasid, " + nimi+". Sa said", correct, "õiged võimalikust 6.")
    time.sleep(2)
    stat = False
