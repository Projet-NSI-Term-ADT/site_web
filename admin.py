# -*- coding: utf-8 -*-
#import sys
#sys.stdout.reconfigure(encoding='utf-8')
from fonctions import *

html = """
    <div class="main">
        <section class="module">
          <div class="container">
            <div class="row">
              <div class="col-sm-6 col-sm-offset-3">
                <h2 class="module-title font-alt">Page administrateur</h2>
                <div class="module-subtitle font-serif">Si T'eS pAs AdMiN pArS dE lA</div>
              </div>
            </div>
            <hr class="divider-w pt-20">
            <div class="row mb-60">
              <div class="col-sm-6 col-md-3 col-lg-3">
                <div class="alt-features-item">
                  <div class="alt-features-icon"><span class="icon-scope"></span></div>
                  <h3 class="alt-features-title font-alt">Bannir un joueur</h3>Le marteau s'abbat sur ce petit con.
                </div>
                <div class="alt-features-item">
                  <div class="alt-features-icon"><span class="icon-tools-2"></span></div>
                  <h3 class="alt-features-title font-alt">Accepter un dev</h3>Pour adhérer à la secte des geeks.
                </div>
              </div>
              <div class="col-sm-6 col-md-3 col-lg-3">
                <div class="alt-features-item">
                  <div class="alt-features-icon"><span class="icon-key"></span></div>
                  <h3 class="alt-features-title font-alt">Mettre un admin</h3>Un nouveau gars !
                </div>
                <div class="alt-features-item">
                  <div class="alt-features-icon"><span class="icon-tools"></span></div>
                  <h3 class="alt-features-title font-alt">Supprimer un jeu</h3>Jure que c'est pas parce que t'as ragé.
                </div>
              </div>
              <div class="col-sm-6 col-md-3 col-lg-3">
                <div class="alt-features-item">
                  <div class="alt-features-icon"><span class="icon-happy"></span></div>
                  <h3 class="alt-features-title font-alt">Débannir quelqu'un</h3>Liberté !!!
                </div>
                <div class="alt-features-item">
                  <div class="alt-features-icon"><span class="icon-caution"></span></div>
                  <h3 class="alt-features-title font-alt">Avertir quelqu'un</h3>Lui il commence à être chiant.
                </div>
              </div>
              <div class="col-sm-6 col-md-3 col-lg-3">
                <div class="alt-features-item">
                  <div class="alt-features-icon"><span class="icon-profile-male"></span></div>
                  <h3 class="alt-features-title font-alt">Liste admin</h3>Pour voir les collègues.
                </div>
                <div class="alt-features-item">
                  <div class="alt-features-icon"><span class="icon-basket"></span></div>
                  <h3 class="alt-features-title font-alt">Bouton</h3>si vous avez une idée
                </div>
              </div>
            </div>
          </div>
        </section>
"""

charger_header("Admin")
print(html)
charger_footer()
