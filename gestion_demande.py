from data import data

'''
    Ce programme est le fichier python qui permet de generer une reponse à votre demande sur les JO 2024
    Copyright (C) 2024  Verove

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

i = 0
#LISTE DES SPORTS ET DES SPORTS COMPOSEES
liste_sport = [ 
    'athleti', 'badminton',  'boxe',
    'vtt', 'mountain', 'escrime', 'foot', 'golf', 
    'trampoline', 'halter', 'hand', 'hockey', 'judo', 'pentha', 
    'rugby', 'plongeon',  'waterpolo', 'equitation', 'escalade'
    'equestre' , 'taekw', 'ping', 'voile', 'aviron', 'breaking',
    'beach', 'skate', 'surf', 'escalade', 'breaking', 'lutte', 'triat'
    ]
#liste_sport_composé = ['basket', 'volley', 'bmx', 'gym', 'natation', 'tennis', 'tir']
liste_sport_composé = {
    'canoe' : {
        "sport" : ['canoe_sprint', 'canoe_kayak_slalom'],
        'zone' : 10,
        'letter' : ['ay'],
        'signe' : '+'
    },
    'cyclisme' : {
        'sport' : ['cyclisme_piste' , 'cyclisme_route'],
        'zone' : 15,
        'letter' : ['ro'],
        'signe' : '+'
    },
    'basket' : {
        'sport' : ['basket','basket3*3'],
        'zone' : 10,
        'letter' : ['3'],
        'signe' : '+'
    },
    'bmx' : {
        'sport' : ['bmx_racing', 'bmx_freestyle'],
        'zone' : 10,
        'letter' : ['fr'],
        'signe' : '+'
    },
    'volley' : {
        'sport' : ['volley', 'beach'],
        'zone' : 15,
        'letter' : ['pl'],
        'signe' : '+'
    },
    'gym' : {
        'sport' : ["gym_artistique", 'gym_rythm'],
        'zone' : 15,
        'letter' : ['ry'],
        'signe' : '+'
    },
    'natation' : {
        'sport' : ['natation', "natation_artistique", 'natation_marathon'],
        'zone' : 20,
        'letter' : ['qu', 'ma'],
        'signe' : '+'
    },
    'tennis' : {
        'sport' : ['tennis', 'ping'],
        'zone' : 15,
        'letter' : ['bl'],
        'signe' : '+'
    },
    'tir' : {
        'sport' : ['tir', 'tir_arc'],
        'zone' : 15,
        'letter' : ['cr'],
        'signe' : '-'
    }
}
liste_mot_clé = {
    "date" : ['quand', 'date'] , 
    'debut' : ['commence', 'debut'] ,
    'fin' : ['fin', 'termin'] ,
    'lieux' : ['où','ou', 'lieu', 'dans', 'site', 'lieux'],
    'medaille'  : ['medaille', 'recompense','victoire'],
    'histore' : ['apparition', 'histoire'],
    'epreuves' : ['epreuve']
    }



def clear_text(texte):
    text = texte.lower()
    text = list(texte)
    impurte = '124567879/*-+§/:;,%$£`^¨¤&"#\'{\}()[~]`_\\^)°'
    e_impur = 'éèëêe'
    a_impur = 'à@äâ'
    i_impur = 'ïîì'
    u_impur = 'üûµ'
    o_impur = 'ôöò'
    ans = []

    for elm in text:
        if elm in impurte:
            continue
        elif elm in e_impur:
            ans.append('e')
        elif elm in o_impur:
            ans.append('o')
        elif elm in a_impur:
            ans.append('a')
        elif elm in i_impur:
            ans.append('i')
        elif elm in u_impur:
            ans.append('u')
        elif elm == 'ÿ':
            ans.append('y')
        elif elm == 'ñ':
            ans.append('n')
        else:
            ans.append(elm)

    return ''.join(ans)

def extraire_phrase(text) :
    liste = list(text)
    for i in range(len(liste)) : 
        elem = liste[i]
        if elem in ['!', '?', ';'] :
            liste[i] = '.'
        if elem == ' ' : 
           liste[i] = ''
    text = ''.join(liste)
    return text.split('.')

def search_mot_clé(text) : 

    def init_k(taille, j, maxi) : 
        if taille - j < maxi :
            return taille
        else :
            return j+ maxi
    
    mot_clé = [] 

    for phrase1 in text :
        mot_clé_phrase = []
        phrase = clear_text(phrase1)
        taille = len(phrase)
        i = 0 
        while i < taille :  
            mot = phrase[i]
            j = i + 1
            continuer = True
            while j < taille and continuer and j - i <= 15 :
                mot += phrase[j]
                #DETECTION DES SPORTS CLASSIQUE
                if mot in liste_sport : 
                    continuer = False
                    mot_clé_phrase.append(mot)
                    if mot == 'beach' : 
                        j += 5
                #DETECTION DES SPORTS COMPOSES
                elif mot in liste_sport_composé :

                    not_trouve = True
                    sport = liste_sport_composé[mot]
                    k = init_k(taille, j , sport['zone'])
                    for l in range(len(sport['sport']) - 1 ) : 
                        letters = sport['letter'][l]
                        
                        if len(letters) == 1 : 
                            if letters[0] in phrase[j:k+1] : 
                                mot_clé_phrase.append(sport['sport'][l+1])
                                not_trouve = False
                                print(8)
                        else :      
                            letters = list(letters)
                            if letters[0] in phrase[j+1:k+1] :
                                print(phrase[j+1:k+1])
                                ind = j + phrase[j+1:k+1].index(letters[0]) +1 
                                if ind < taille - 1  :
                                    if sport['signe'] == '+' and letters[-1] == phrase[ind+1] : 
                                        mot_clé_phrase.append(sport['sport'][l+1])
                                        not_trouve = False
                                     
                                if sport['signe'] == '-' and letters[-1] == phrase[ind - 1] : 
                                    mot_clé_phrase.append(sport['sport'][l+1])
                                    not_trouve  = False
                    if not_trouve : 
                        mot_clé_phrase.append(sport['sport'][0])

                elif mot == 'artistique' :
                    if mot_clé_phrase[-1] == 'natation' : 
                        mot_clé_phrase.pop()
                        mot_clé_phrase.append('natation_artistique')
                    elif mot_clé_phrase[-1] == 'natation_marathon' :
                        mot_clé_phrase.append('natation_artistique')
                    elif mot_clé_phrase[-1] == 'gym_rythmique' : 
                        mot_clé_phrase.append('gym_artistique')
                elif mot == 'rythmique' and mot_clé_phrase[-1] == 'gym_artistique' :
                    mot_clé_phrase.append('gym_rythmique')
                elif mot == 'marathon' :
                    if mot_clé_phrase[-1] == 'natation' :
                        mot_clé_phrase.pop()
                        mot_clé_phrase.append('natation_marathon')
                    elif mot_clé_phrase[-1] == 'natation_artistique' :
                        mot_clé_phrase.append('natation_rythmique')
                #DETECTION DES AUTRES MOTS CLES
                else : 
                    for key in liste_mot_clé : 
                        if mot in liste_mot_clé[key] : 
                            mot_clé_phrase.append(key)
                            continuer = False
                    
                j += 1
            if continuer : 
                i += 1
            else :
                i = j
        mot_clé.append(mot_clé_phrase)
    return mot_clé

def organisation_mot_clé(mot_clé) : 
    non_sport = ['date','debut','fin','lieux', 'medaille','epreuves']
    dico = {}
    for mots in mot_clé : 
        if len(mots) > 0 : 
            last_sport = '0'
            liste_elm = [] 
            #RANGEMENT DES MOTS CLES QUAND ILS COMMENCENT PAR UN MOT QUI N EST PAS UN NOM DE SPORT
            if mots[0] in non_sport :
                liste_elm = [mots[0]] 
                j = 0
                for i in range(1,len(mots)) : 
                    mot = mots[i]

                    if mot in non_sport : 
                        if j == 0 : 
                            liste_elm.append(mot)
                        else :
                            j = 0 
                            liste_elm = [mot]
                    else  : 
                        j = 1
                        last_sport = mot
                        if mot in dico : 
                            dico[mot].extend(liste_elm)
                        else :
                            dico[mot] = liste_elm
                if j == 0 : 
                    if last_sport in dico :
                        dico[last_sport].extend(liste_elm)
                    else : 
                        dico[last_sport] = liste_elm
            #RANGEMENT DES MOTS CLES QUAND ILS COMMENCENT PAR UN SPORT
            else : 
                for mot in mots : 
                    if mot in non_sport : 
                        liste_elm.append(mot)
                    else : 
                        if last_sport in dico : 
                            dico[last_sport].extend(liste_elm)
                        else : 
                            last_sport = liste_elm
                        liste_elm = []
                        last_sport = mot 
                
                if last_sport in dico : 
                    dico[last_sport].extend(liste_elm)
                else : 
                    dico[last_sport] = liste_elm
    return dico

def clear_mot_clé(mot_clé) : 
    keys = mot_clé.keys()
    for key in keys : 
        liste = []
        mots = mot_clé[key]
        for mot in mots : 
            if mot == 'debut' or mot == 'fin' : 
                if 'date' in mots : 
                    mots.remove('date')
            if mot in liste : 
                mots.remove(mot)
            else : 
                liste.append(mot)
            mot_clé[key] = mots
    return mot_clé

def creation_phrases(mot_clé) : 
    keys = mot_clé.keys()
    text = ''
    phrase = ''
    for key in keys : 
        if key == '0' : 
            if 'epreuves' in  mot_clé[key] :
                liste_nom_sports = []
                for each in data : 
                    liste_nom_sports.append(data[each]['name'])
                noms = ', '.join(liste_nom_sports)
                phrase = 'Voici la liste des sports present aux JO 2024 : ' + noms
                     
        else : 
            nom = data[key]['name']
            phrase = f'Voici les éléments que vous avez demander sur le {nom} :'
            mots = mot_clé[key]
            print(mots)
            for mot in mots : 
                phrase = phrase
                mois = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin','juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']
                if mot == 'date' : 
                    dates = data[key]['date']
                    date_propre = []
                    for date in dates : 
                        date = date.split('/')
                        jour = date[0]
                        moi = mois[int(date[-1]) - 1]
                        date_propre.append(f'le {jour} {moi}')
                    date_propre = ', '.join(date_propre)
                
                    phrase = phrase + f' Les epreuves se dérouleront {date_propre} 2024.'
                elif mot == 'debut' : 
                    dates = data[key]['date']
                    date = dates[0].split('/')
                    jour = date[0]
                    moi = mois[int(date[-1]) - 1]
                    phrase = phrase + f' Les épreuves commenceront le {jour} {moi} 2024.'
                elif mot == 'fin' : 
                    dates = data[key]['date']
                    date = dates[1].split('/')
                    jour = date[0]
                    moi = mois[int(date[-1]) - 1]
                    phrase = phrase + f' Les épreuves se finiront le {jour} {moi} 2024.'
                elif mot == 'lieux' :
                    lieux = data[key]['lieux'] 
                    if  type(lieux) is list:
                        lieux = ', '.join(lieux)
                    phrase = phrase + f' Les epreuves se tiendront {lieux}.'
                elif mot == 'medaille' : 
                    medaille  = data[key]['nb_medailles']       
                    phrase  = phrase + f"La France a gagné {medaille[0]} medaille(s) dans ce sport dont "
                    if medaille[1] != 0 :
                        phrase = phrase +str( medaille[1]) + " medaille(s) d'or "
                    if medaille[2] != 0 :
                        if medaille[1] != 0 :
                            phrase += ", "
                        phrase = phrase + str(medaille[2]) + " medaille(s) d'argent "
                    if medaille[3] != 0 :
                        if medaille[1] != 0 or  medaille[2] != 0:
                            phrase += "et "
                        phrase = phrase + str(medaille[3]) + " medaille(s) de bronze "
                    phrase = phrase + '.'
                elif mot == 'epreuves' :
                    if 'epreuves'in data[key] :
                        epreuve = data[key][mot]
                        if  len(epreuve) > 1:
                            epreuve = ', '.join(epreuve)
                            phrase = phrase + f'les epreuves de ce sport sont {epreuve}'
                        else :
                            phrase = phrase + f'la seule épreuve de ce sport est {epreuve[0]}'
                     else :
                        phrase = phrase + 'Ce sport ne continent qu'une seule epreuve.'
            phrase= phrase + ''
        text += phrase
    if text == '' : 
    
        text = (f"Bonjour, Je suis un chatbot qui reponds à vos questions sur les Jeux Olympiques de Paris 2024. "
            "Je n est pas compris votre question. Veuillez me poser une question du type : "
            " Quelle est la date des epreuves de skateboard ? "
            " Où se déroule les épreuves de trampoline ?"
            " Combien de medaille a gagné la France au jeux olympiques d'aviron ?"
        )
    return text

def gestion_demande(question) : 
    return creation_phrases(clear_mot_clé(organisation_mot_clé(search_mot_clé(extraire_phrase(question)))))

if __name__ == '__main__' : 
    run = True 
    question = input()
    mot = search_mot_clé(extraire_phrase(question))
    print(mot)
    mot = organisation_mot_clé(mot)
    print(mot)
    print(gestion_demande(question))
