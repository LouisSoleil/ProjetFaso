import datetime 

date = str(datetime.datetime.now())

avant = "temperature corporelle avant effort : str(tavant)"
apres = "temperature corporelle apres effort : str(tapres)"

nbe = "Nombre de pompes : 15" 
lol = 14
fichier = open("valeur.txt", "a")
fichier.write(date + " ; " + nbe + "\n")

print ("Nombre de pompes :" + " " +str(lol)) 
