# NIVEAU 1 : Écrire un programme qui demande une url à l'utilisateur 

# 1) 

import requests

url = ["https://google.com"]

for u in url : 
  try : 
    r = requests.get(u)
    print("Le site est bon")
  except:
    print("Le site est inaccessible")

# 2)

phrase = input("Entrez une phrase : ")

# Couper une phrase

mots = phrase.split()
print(mots)

# Compter 

nombre = len(mots) 
print(nombre)

# 4 Premier et dernier occurence 

premier = mots[0]
dernier = mots[-1]
print(premier, dernier)


