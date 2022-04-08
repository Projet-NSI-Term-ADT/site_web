from fonctions import *
#-*- coding: utf-8 -*-
#import sys
#sys.stdout.reconfigure(encoding='utf-8')

import cgi
html1="""
    <div class="main">
        <section class="module">
          <div class="container">
            <div class="row multi-columns-row post-columns">
"""

html2="""
    </div>
            <div class="pagination font-alt"><a href="$avant$"><i class="fa fa-angle-left"></i></a><a class="active" href="$page1$">1</a><a href="$page_actuelle$">$page_actuelle$</a><a href="$derniere_page$">$derniere_page$</a><a href="$apres$"><i class="fa fa-angle-right"></i></a></div>
          </div>
        </section>
"""

charger_header("Navigation")
print(html1)
for i in range(12):
#for i in range(jeux_page(page)):
    charger_jeu_index("test")
print(html2)
#print(html2.replace("$page_max$", compter_page(x)).replace("))
charger_footer()