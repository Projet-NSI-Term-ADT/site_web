# -*- coding: utf-8 -*-
#import sys
#sys.stdout.reconfigure(encoding='utf-8')
from fonctions import *

html='''
<div class="main">
        <section class="module bg-dark-60 contact-page-header bg-dark" data-background="assets/images/contact_bg.jpg">
          <div class="container">
            <div class="row">
              <div class="col-sm-6 col-sm-offset-3">
                <h2 class="module-title font-alt">Contactez-nous</h2>
                <div class="module-subtitle font-serif">Si vous avez un problème, des questions ou autre, on essaie de vous répondre au mieux.</div>
              </div>
            </div>
          </div>
        </section>
        <section class="module">
          <div class="container">
            <div class="row">
              <div class="col-sm-6">
                <h4 class="font-alt">Le message</h4><br/>
                <form id="contactForm" role="form" method="post" action="php/contact.php">
                  <div class="form-group">
                    <label class="sr-only" for="email">Sujet</label>
                    <input class="form-control" type="sujet" id="sujet" name="sujet" placeholder="Sujet du message" required="required" data-validation-required-message="Veuillez mettre le sujet du message."/>
                    <p class="help-block text-danger"></p>
                  </div>
                  <div class="form-group">
                    <textarea class="form-control" rows="7" id="message" name="message" placeholder="Votre message" required="required" data-validation-required-message="Entrez un message..."></textarea>
                    <p class="help-block text-danger"></p>
                  </div>
                  <div class="text-center">
                    <button class="btn btn-block btn-round btn-d" id="cfsubmit" type="submit">Envoyer</button>
                  </div>
                </form>
                <div class="ajax-response font-alt" id="contactFormResponse"></div>
              </div>
              <div class="col-sm-6">
                <h4 class="font-alt">Petite info</h4><br/>
                <p>Globalement, nous répondons assez vite. Ne spammez pas les messages ;-)</p>
                <hr/>
              </div>
            </div>
          </div>
        </section>
        <section id="map-section">
          <div id="map"></div>
        </section>
'''

charger_header("Contact")
print(html)
charger_footer()