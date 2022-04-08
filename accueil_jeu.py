# -*- coding: utf-8 -*-
#import sys
#sys.stdout.reconfigure(encoding='utf-8')
from fonctions import *

nombre_jeux= compter_jeux()

html1="""
    <div class="main">
          <div class="container">
            <div class="well well-sm">
                <h1>Jeux du moment</h1>
                <div class="row multi-columns-row post-columns">
"""

html2="""
    </div>
            <div class="alert alert-danger" role="alert"><h6><a href="navig_jeu.py">Plus</a></h6></div>
            </div>
          </div>
        <div class="container">
            <div class="well well-sm">
                <h1>D'autres jeux</h1>
                <div class="row multi-columns-row post-columns">
"""

html3="""
                </div>
            <div class="alert alert-danger" role="alert"><h6><a href="navig_jeu.py">Plus</a></h6></div>
            </div>
          </div>
"""


charger_header("Jeux")
print(html1)
for i in range(4):
    charger_jeu_index("test")
print(html2)
for i in range(4):
    charger_jeu_index("test")
print(html3)
charger_footer()