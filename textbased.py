import sys

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
answer_E = ["E", "e"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nKasuta ainult A, B, C, D, E\n")

def intro():
    print("Tere tulemast avastus mängule!")
    print("Alustame mänguga!")
    print("Esimeseks vali mis päeval soovid kooli minna.")
    print("Tähtis on, et igal päeval on erinev sündmus toimunud ja see võib mõjutada sinu päeva.")
    
    print("Valige mis päeval lähete kooli: ")

intro()

print(""" 
A. esmaspäev
B. teisipäev
C. kolmapäev
D. neljapäev
E. reede """)

valik = input(">>> ")
if valik in answer_A:
    print("\nTäna on spordipäev selleks lähed kooli 10:00 ja tunnid jäävad ära")
elif valik in answer_B:
    option_riietus()
elif valik in answer_C:
    print("\nTäna on tavaline koolipäev aga sul on matemaatika ja bioloogia kontrolltöö")
elif valik in answer_D:
    option_sünnipäev()
elif valik in answer_E:
    print("Täna on klassiõhtu")
else:
    print(required)
    intro()



def option_riietus():
    print("\nValin endale riietus õpetajate päevaks: " )
    print(""" A. teksad ja pusa
    B. ülikond
    C. lühikesed püksid ja T-särk""")
    valik = input(">>> ")
  if valik in answer_A:
    print("\nNüüd")
  elif valik in answer_B:
    print ("\n")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_riietus()






