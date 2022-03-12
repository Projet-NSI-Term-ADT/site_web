# -*- coding: utf-8 -*-
#import sys
#sys.stdout.reconfigure(encoding='utf-8')
from fonctions import *

html = """
  <section class="home-section home-parallax home-fade home-full-height bg-dark-30" id="home" data-background="assets/images/section-2.jpg">
        <div class="titan-caption">
          <div class="caption-content">
            <div class="font-alt mb-30 titan-title-size-1">Bienvenue !<br>Ici, vous trouverez ...</div>
            <div class="font-alt mb-40 titan-title-size-3"><span class="rotate">Pleins de jeux | Une communauté passionée | Encore des jeux | Une équipe attentive</span>
            </div><a class="section-scroll btn btn-border-w btn-circle" href="#login">Connexion</a>
          </div>
        </div>
      </section>
      <div class="main">
        <section class="module" id="login">
          <div class="container">
            <div class="row">
              <div class="col-sm-8 col-sm-offset-2">
                <h2 class="module-title font-alt">ADT Games</h2>
                <div class="module-subtitle font-serif large-text">vous invite à vous connecter ou créer un compte pour accéder à la bibliothèque.<br>Le simple but de cette démarche est de créer un environnement plus sécurisé, pour nous, et surtout pour vous tous.</div>
              </div>
            </div>
          </div>
          <div class="container">
            <div class="row">
              <div class="col-sm-5 col-sm-offset-1 mb-sm-40">
                <h4 class="font-alt">Connexion</h4>
                <hr class="divider-w mb-10">
                <form class="form">
                  <div class="form-group">
                    <input class="form-control" id="username" type="text" name="username" placeholder="Adresse mail"/>
                  </div>
                  <div class="form-group">
                    <input class="form-control" id="password" type="password" name="password" placeholder="Mot de passe"/>
                  </div>
                  <div class="form-group">
                    <button class="btn btn-round btn-b">Se connecter</button>
                  </div>
                  <div class="form-group"><a href="">Mot de passe oublié ?</a></div>
                </form>
              </div>
              <div class="col-sm-5">
                <h4 class="font-alt">Créer un compte</h4>
                <hr class="divider-w mb-10">
                <form class="form">
                  <div class="form-group">
                    <input class="form-control" id="E-mail" type="text" name="email" placeholder="Adresse mail"/>
                  </div>
                  <div class="form-group">
                    <input class="form-control" id="username" type="text" name="username" placeholder="Nom d'utilisateur"/>
                  </div>
                  <div class="form-group">
                    <input class="form-control" id="password" type="password" name="password" placeholder="Mot de passe"/>
                  </div>
                  <div class="form-group">
                    <input class="form-control" id="re-password" type="password" name="re-password" placeholder="Mot de passe (vérification)""/>
                  </div>
                  <div class="form-group">
                    <button class="btn btn-block btn-round btn-b">Créer</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </section>
"""

charger_header("Connexion", False)
print(html)
charger_footer()