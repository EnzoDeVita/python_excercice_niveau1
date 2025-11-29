# EXERCICE 1 — Vérifier si une phrase finit par un point

phrase = input("Entrez une phrase : ")

if phrase.endswith(".") : 
  print("La phrase est correcte ! ")
else : 
  print("La phrase est incorrecte ! ")


# EXERCICE 2 — Afficher les 3 premiers mots d’une phrase

phrase = input("Entrez une phrase : ")

mots = phrase.split()

if len(mots) >= 3:
  print(mots[:3]) # on affiche les 3 premiers mots

else : 
  print("Phrase trop courte")

# EXERCICE 3 — Remplacer un mot dans une phrase

phrase = input("Entrez une phrase : ")
m1 = input("Mot à remplacer : ")
m2 = input("Mot nouveau : ")

phrase_modify = phrase.replace(m1, m2)

print("Phrase modifié :" , phrase_modify)
