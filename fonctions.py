jeux=('Morio', 'Sanic', 'Fortday', 'Meincraft', 'Pacwoman', 'Nickey Mousse')

def charger_header(nom_page, fixe='True'):
    if fixe==True:
        file = open("header_fixe.tpl", "r")
    else:
        file = open("header.tpl", "r")
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