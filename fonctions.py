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