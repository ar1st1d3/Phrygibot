from serveur import get_template, render, OK, Redirect, pageDynamique, lancerServeur
from gestion_demande import gestion_demande
# Les messages de la conversation
conversation = []
# La page dynamique qui ajoute un message
def nouveau_message(url, vars):
	""" Ajouter un message à la conversation et afficher celle-ci """
	# récuperer le texte du message envoyé par le navigateur
	message = vars['msg']
	# l'insérer au début de la conversation
	reponse = gestion_demande(message)
	conversation.insert(0,[message, reponse])
	# renvoyer la page conversation.html, ce qui aura pour effet
	# d'appeler `page_conversation` pour afficher la nouvelle liste de messages
	return Redirect('/home.html')

# Définir la page dynamique
pageDynamique('/message', nouveau_message)  # associer la page dynamique
# La page dynamique qui affiche une conversation
def page_conversation(url, vars):
	""" Retourner la page de la conversation """
	# charger le patron
	template = get_template('home.html')
	# définir les variables
	vars['messages'] = conversation
	# appliquer le patron
	html = render(template, vars)
	# retourner la page au navigateur
	return OK(html)

# Définir la page dynamique :
# Le serveur appelera la fonction `page_conversation` 
# lorsqu'il recevra un requête pour la page `/conversation.html`.
pageDynamique('/home.html', page_conversation)

# Lancer le serveur
lancerServeur()
