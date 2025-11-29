# EXERCICE 1 — Vérifier si un mot apparaît dans une phrase

phrase = input("Entrez une phrase : ")
mot = input("Entrez un mot : ")

if mot in phrase :
  print("Le mot est présent")

else : 
  print("Le mot est absent")

#  EXERCICE 2 — Transformer une phrase en majuscules et minuscules 

phrase = input("Entrez une phrase : ")

print(phrase.upper())
print(phrase.lower())

# EXERCICE 3 — Compter combien de fois un mot apparaît

phrase = input("phrase : ")
mot = input("mot : ")

mots = phrase.split()
l1 = mots.count(mot)
print(l1)
