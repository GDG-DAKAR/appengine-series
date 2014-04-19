# *coding: utf-8*
import webapp2
import json
import jinja2
import os

from google.appengine.ext import db

class Personne(db.Model):
  nom = db.StringProperty()

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Accueil(webapp2.RequestHandler):
  def get(self):
    lenom = self.request.get('nom')
    p = Personne(nom = lenom)
    p.put()
    template = jinja_environment.get_template('views/index.html')
    self.response.write(template.render( {} ))

  def post(self):
    le_nom = self.request.get('nom', '')
    self.response.write( le_nom )

class JSONApi(webapp2.RequestHandler):
  def get(self):
    token = self.request.get('token', None)
    if token:
      res = [ { 'nom' : p.nom } for p in Personne.all() ]
    else:
      res = { 'code': 1, 'message': "Tu fais quoi ici ? hein" }

    self.response.headers["Content-Type"] = "application/json"
    self.response.write( json.dumps( res ) )

routes = [("/", Accueil), ("/api", JSONApi)]
app = webapp2.WSGIApplication( routes, debug="-->" )
