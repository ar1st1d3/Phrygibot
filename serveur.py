# -*- coding: utf8 -*-
#
#	Serveur Web permettant de gérer des pages dynamiques
#	Il n'y a pas de modifications à faire dans ce fichier
#

from http.server import SimpleHTTPRequestHandler, HTTPServer
from cgi import parse_header, parse_multipart
from urllib.parse import urlparse, parse_qs
from os import curdir, chdir

# Le numéro de port du serveur. Son URL est donc http://localhost:8000/
PORT = 8000

# Se mettre dans le dossier "www". Les chemins des URLs sont donc relatives à ce dossier
# chdir("www")

# Configurer la bibliothèque de gestion des templates
import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Fonctions exportées pour faciliter l'utilisation des patrons
def get_template(t):
	return env.get_template(t)

def render(t, v):
	return t.render(v)

# Mémoriser les chemins qui correspondent à des pages dynamiques
pagesDynamiques = {}
def pageDynamique(path, f):
	print('ok')
	pagesDynamiques[path] = f

# Parse query string and replace 1-element arrays by the value of their element
def parse_query(q):
	query = parse_qs(q, keep_blank_values=1)
	for var in query:
		if len(query[var]) == 1:
			query[var] = query[var][0]
	return query

# Cette classe décrit comment traiter les requêtes reçues par le serveur
class mesRequetes(SimpleHTTPRequestHandler):

    def executeDynamicPage(self, path, vars):
        code, headers, content = pagesDynamiques[path](path, vars)
        self.send_response(code)
        for (header,value) in headers:
            self.send_header(header, value)
        self.end_headers()
        if content is not None:
            self.wfile.write(content.encode("utf-8"))

    # Traitement d'une requête GET
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if len(parsed.query) > 0:
            query = parse_query(parsed.query)
        else:
            query = {}

        # Si le chemin est une page dynamique, exécuter celle-ci pour récupérer son contenu
        if path in pagesDynamiques:
            self.executeDynamicPage(path, query)
            return

        # Si aucun chemin spécifique n'est spécifié, exécuter la page dynamique par défaut
        if path == "/":
            default_dynamic_page = "/home.html"  # Changez "/default_dynamic_page" avec le chemin de votre page dynamique par défaut
            if default_dynamic_page in pagesDynamiques:
                self.executeDynamicPage(default_dynamic_page, query)
                return

        super().do_GET()

# Initialiser le serveur et attendre les requêtes.
# On peut arrêter le serveur en tapant ^C
def lancerServeur():
	try:
		# Créer le serveur HTTP en lui indiquant la classe qui traite les requêtes
		serveur = HTTPServer(('', PORT), mesRequetes)
		print('Serveur prêt sur le port ', PORT)
		
		# Traiter les requêtes
		serveur.serve_forever()

	except KeyboardInterrupt:
		print('Interruption par ^C. Arrêt du serveur.')
		serveur.socket.close()

def OK(content):
	return (200, [], content)

def Redirect(url):
	return (301, [('Location', url)], None)

if __name__ == "__main__":
	lancerServeur()
