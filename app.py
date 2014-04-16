# *coding: utf-8*
import webapp2
import jinja2
import json
import os

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Accueil(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('views/index.html')
    self.response.out.write(template.render(template_values))

class JSONApi(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'application/json'
    objet = { 'yes' : 'tu vas comprendre' }
    self.response.write(json.dumps(objet))

routes = [('/', Accueil), ('/api', JSONApi)]

app = webapp2.WSGIApplication( routes, debug="-->" )
