import sqlite3
bdd= sqlite3.connect("BD_SITE.db")
curseur=bdd.cursor()

def charger_header(nom_page):
    file = open("header_fixe.tpl", "r")
    for line in file:
        line=line.replace('$page$',nom_page)
        print(line)
    file.close()

def charger_footer():
    file = open("footer.tpl", "r")
    print(file.read())
    file.close()
    
def charger_jeu_index(jeu):
    file = open("jeu.tpl", "r")
    for line in file:
        line=line.replace('$game$',jeu)
        print(line)
    file.close()

def compter_jeux():
    #Compter le nombre de jeux dans la base
    curseur.execute('SELECT COUNT(*) FROM Jeux')
    return int(curseur.fetchone()[0])

def compter_page(nombre_jeux):
    #Compter le nombre de pages nécessaire en fonction du nombre de jeux
    pages= nombre_jeux//12
    if nombre_jeux%12 !=0:
        pages+=1
    return pages

def jeux_page(page):
    #Compter le nombre de jeux sur chaque page (par exemple quand il y a moins de 12, ça en affiche 7 etc)
    if page==compter_page(compter_jeux()):
        return compter_jeux()%12
    else :
        return 12