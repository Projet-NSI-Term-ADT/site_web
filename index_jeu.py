# -*- coding: utf-8 -*-
#import sys
#sys.stdout.reconfigure(encoding='utf-8')
from fonctions import *

html1="""
    <div class="main">
        <section class="module">
          <div class="container">
            <div class="row multi-columns-row post-columns">
"""

html2="""
    </div>
            <div class="pagination font-alt"><a href="#"><i class="fa fa-angle-left"></i></a><a class="active" href="#">1</a><a href="#">2</a><a href="#">3</a><a href="#">4</a><a href="#"><i class="fa fa-angle-right"></i></a></div>
          </div>
        </section>
"""

charger_header("Jeux")
print(html1)
for jeu in jeux:
    charger_jeu_index(jeu)
print(html2)
charger_footer()