# Base de donnée des sports olympiques

'''
    Ce fichier python sert de base de donnée pour le programme phrygibot
    Copyright (C) 2024  Spreng

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


'''
Exemple de formation du dictionnaire de chaque sports :
'sport' : {
        'name' : 'nom complet du sport',
        'epreuves' : ['epreuve 1', 'epreuve 2' , etc],
        'date' : ['jour 1', 'jour 2', etc],                 #chaques jours où se déroule l'épreuve est répertorié
        'lieux' : ['lieu 1', 'lieu 2', 'lieu 3', etc] ,
        'histoire' : ['1ère date d'apparition aux JO'],
        'nb_medailles' : [nombre_de_médailles_total, nombre_de_médailles_d_or, nombre_de_médailles_d_argent, nombre_de_médailles_de_bronze] #nombre de médailles pour l'équipe de france uniquement
        }
'''


data = {
    'athleti' : {
        'name' : 'athlétisme',
        'epreuves' : ['100m' ,'200m' ,'400m' , '800m' , '1500m' , '5000m' , '10000m' , '400m haies' , '3000m steeple' , 'relais 4x100m' , 'relais 4x400m' , 'saut en hauteur' , 'saut à la perche' , 'saut en longueur' , 'triple saut' , 'lancer de poids' , 'lancer de disque' , 'lancer de marteau' , 'lancer de javelot' , 'decathlon' , 'heptathlon' , '110m haies' , '100m haies' , '20km marche' , 'marche sur un marathon en relais mixte', 'marathon'],
        'date' : ['01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08', '11/08'],
        'lieux' : ['au stade de France (épreuve de piste)', 'hôtel de ville de Paris (au départ du marathon)', 'pont d\'Iéna (départ du 20km marche)'] ,
        'histoire' : ['1896'],
        'nb_medailles' : [71, 14, 27, 30]
        },
    'aviron' : {
        'name' : 'aviron',
        'epreuves' : ['skiff', 'deux de pointe', 'deux de couple', 'quatre de pointe sans barreur', 'quatre de couple', 'huite de pointe', 'deux de couple poids léger'],
        'date' : ['27/07', '28/07', '29/07', '30/07', '31/07', '01/08' '02/08','03/08'] ,
        'lieux' : 'au Stade nautique de Vaires-sur-Marne' ,
        'histoire' : ['1896'],
        'nb_medailles' : [36, 8, 15, 13]
        },
    'badminton' : {
        'name' : 'badminton',
        'epreuves' : ['simple', 'double'],
        'date' : ['27/07', '28/07', '29/07', '30/07', '31/07', '01/08' '02/08','03/08', '04/08', '05/08'] ,
        'lieux' : 'à l\'Arena Porte de la Chapelle' ,
        'histoire' : ['1992'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'basket' : {
        'name' : 'basketball',
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : ['à l\'Arena Bercy (phases finales des tournois)', 'au Stade Pierre Mauroy, Lille (phases préliminaires des tournois)'] ,
        'histoire' : ['1936'],
        'nb_medailles' : [5, 0, 4, 1]
        },
    'basket3*3' : {
        'name' : 'basketball 3x3',
        'date' : ['30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08'] ,
        'lieux' : 'à la Place de la Concorde' ,
        'histoire' : ['2020'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'boxe' : {
        'name' : 'boxe',
        'epreuves' : '7 catégories de poids qui n\'ont pas encore été définit.',
        'date' : ['27/07', '28/07','06/08','07/08'] ,
        'lieux' : ['au Stade Rolang-Garros (épreuves finales de boxe)', 'à l\'Arena Paris Nord (phases préliminaires)'] ,
        'histoire' : ['1904'],
        'nb_medailles' : [25, 6, 9, 10]
        },
    'canoe_sprint' : {
        'name' : 'canoë sprint',
        'epreuves' : ['canoë seul - 1000m', 'canoë seul - 200m', 'canoë double - 500m', 'kayak seul - 1000m', 'kayak seul - 500m', 'kayak double - 500m', 'kayak à quatre - 500m'],
        'date' : ['06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : 'au Stade nautique de Vaires-sur-Marne' ,
        'histoire' : ['1936'],
        'nb_medailles' : [15, 1, 4, 10]
        },
    'canoe_kayak_slalom' : {
        'name' : 'canoë-kayak slalom',
        'epreuves' : ['canoë seul', 'kayak seul', 'kayak cross'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08'] ,
        'lieux' : 'au Stade nautique de Vaires-sur-Marne' ,
        'histoire' : ['1936'],
        'nb_medailles' : [18, 7, 3, 8]
        },
    'cyclisme_piste' : {
        'name' : 'cyclisme sur piste',
        'epreuves' : ['vitesse individuelle', 'vitesse par équipe', 'keirin', 'poursuite par équipe', 'omnium', 'madison'],
        'date' : ['05/08','06/08','07/08','08/08', '09/08','10/08', '11/08'] ,
        'lieux' : 'au Vélodrome national de Saint-Quentin-en-Yvelines' ,
        'histoire' : ['1896'],
        'nb_medailles' : [67, 28, 21, 18]
        },
    'cyclisme_route' : {#erreur 
        'name' : 'cyclisme sur route',
        'epreuves' : ['épreuves contre-la-montre', 'épreuve en ligne'],
        'date' : ['27/07 (contre-la-montre)', '03/08 (en ligne, homme)', '04/07 (en ligne, femme)'] ,
        'lieux' : ['à l\'Esplanade des Invalides (départ du contre la montre)', 'au Trocadéro (course en ligne)'] ,
        'histoire' : ['1896'],
        'nb_medailles' : [18, 8, 4, 6]
        },
    'bmx_freestyle' : {
        'name' : 'BMX freestyle',
        'date' : ['30/07', '31/07'] ,
        'lieux' : 'à la place de la concorde' ,
        'histoire' : ['2020'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'bmx_racing' : {
        'name' : 'BMX racing',
        'date' : ['01/08','02/08'] ,
        'lieux' : 'au Stade BMX de Saint-Queantin-en-Yvelines' ,
        'histoire' : ['2008'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'mountain' : {
        'name' : 'mountain bike',
        'date' : ['28/07', '29/07'] ,
        'lieux' : 'à la Colline d\'Elancourt' ,
        'histoire' : ['1996'],
        'nb_medailles' : [6, 4, 1, 1]
        },
    'escrime' : {
        'name' : 'escrime',
        ' ' : ['épée individuelle', 'fleuret individuel', 'sabre individuel', 'épée par équipes', 'fleuret par équipes', 'sabre par équipes'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08'] ,
        'lieux' : 'au Grand Palais' ,
        'histoire' : ['1896'],
        'nb_medailles' : [123, 44, 43, 36]
        },
    'foot' : {
        'name' : 'football',
        'date' : ['24/07', '25/07', '26/07', '27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : ['au Parc des Princes', 'au Stade de Nantes', 'au Stade de Bordeaux', 'au Stade de Marseille', 'au Stade de Nice', 'au Stade Geoffroy-Guichard', 'au Stade de Lyon'] ,
        'histoire' : ['1900'],
        'nb_medailles' : [2, 1, 1, 0]
        },
    'golf' : {
        'name' : 'golf',
        'date' : ['01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : 'au Golf National' ,
        'histoire' : ['1900 (et 1904 puis revient en 2016)'],
        'nb_medailles' : [1, 0, 0, 1]
        },
    'gym_artistique' : {
        'name' : 'gymnastique artistique',
        'epreuves' : ['concours par équipe', 'concours général', 'exercices au sol', 'saut', 'barres asymétriques', 'poutre', 'cheval d\'arçons', 'anneaux', 'barres parallèles', 'barre fixe'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08'] ,
        'lieux' : 'à l\'Arena Bercy' ,
        'histoire' : ['1896'],
        'nb_medailles' : [22, 3, 10, 9]
        },
    'gym_rythm' : {
        'name' : 'gymnastique rythmique',
        'date' : ['08/08','09/08', '10/08'] ,
        'lieux' : 'à l\'Arena Porte de la Chapelle' ,
        'histoire' : ['1984'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'trampoline' : {
        'name' : 'trampoline',
        'date' : ['02/08'] ,
        'lieux' : 'à l\'Arena Bercy' ,
        'histoire' : ['2000'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'halter' : {
        'name' : 'haltérophilie',
        'epreuves' : ['49kg - femme', '59kg - femme', '71kg - femme', '81kg - femme', '+81kg - femme', '61kg - homme', '73kg - homme', '89kg - homme', '102kg - homme', '+102kg - homme'],
        'date' : ['07/08','08/08', '09/08','10/08', '11/08'] ,
        'lieux' : 'à l\'Arena Paris Sud' ,
        'histoire' : ['1896'],
        'nb_medailles' : [15, 9, 3, 3]
        },
    'hand' : {
        'name' : 'handball',
        'date' : ['25/07', '26/07', '27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08', '11/08'] ,
        'lieux' : ['au Stade Pierre Mauroy, Lille (phases finales)', 'à l\'Arena Paris Sud 6 (phases préliminaires)'] ,
        'histoire' : ['1936'],
        'nb_medailles' : [7, 4, 2, 1]
        },
    'hockey' : {
        'name' : 'hockey',
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08'] ,
        'lieux' : 'au Stade Yves-du-Manoir' ,
        'histoire' : ['1908'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'judo' : {
        'name' : 'judo',
        'epreuves' : ['7 epreuves individuels féminines :  -48kg, -52kg, -57kg, -63kg, -70kg, -78kg, +78kg', '7 epreuves individuels masculines : -60kg, -66kg, -73kg, -81kg, -90kg, -100kg, +100kg', 'une épreuve mixte par équipe'],
        'date' : ['27/07', '28/07', '29/07', '30/07', '31/07', '01/08', '02/08','03/08'] ,
        'lieux' : 'à l\'Arena Champ de Mars (à proximité de la Tour Eiffel)' ,
        'histoire' : ['1964'],
        'nb_medailles' : [57, 16, 13, 28]
        },
    'lutte' : {
        'name' : 'lutte',
        'epreuves' : ['lutte libre féminine (-50kg, -53kg, -57kg, -62kg, -68kg, -76kg)', 'lutte libre masculine (-57kg, -65kg, -74kg, -86kg, -97kg, -125kg)', 'lutte gréco-romaine masculine (-60kg, -67kg, -77kg, -87kg, -97kg, -130kg)'],
        'date' : ['05/08','06/08','07/08','08/08', '09/08','10/08', '11/08'] ,
        'lieux' : 'à l\Arena Champ de Mars' ,
        'histoire' : ['1896'],
        'nb_medailles' : [18, 4, 4, 10]
        },
    'pentha' : {
        'name' : 'penthatlon moderne',
        'epreuves' : 'individuel incluant équitation, laser-run, natation et deux épreuves d\'escrime différentes',
        'date' : ['08/08', '09/08','10/08', '11/08'] ,
        'lieux' : ['au Château de Versailles (pour l\'équitation, le bonus round escrime, la natation et le laser-run)', 'à l\'Arena Paris Nord (pour le tournois de classement d\escrime)']  ,
        'histoire' : ['1912'],
        'nb_medailles' : [4, 0, 2, 2]
        },
    'rugby' : {
        'name' : 'rugby à sept',
        'epreuves' : 'tournois de rugby à sept',
        'date' : ['24/07', '25/07', '26/07', '27/07', '28/07','29/07', '30/07'] ,
        'lieux' : 'au Stade de France' ,
        'histoire' : ['1900'],
        'nb_medailles' : [1, 0, 1, 0]
        },
    'natation' : {
        'name' : 'natation',
        'epreuves' : ['50m nage libre', '100m nage libre', '200m nage libre', '400m nage libre', '800m nage libre', '1 500m nage libre', '100m dos', '200m dos', '100m brasse', '200m brasse', '100m papillon', '200m papillon', '200m quatre nages individuel', '400m quatre nages individuel', 'relais 4x100m nage libre', 'relais 4x200m nage libre', 'relais 4x100m quatre nages ', 'relais mixte 4x100m quatre nages'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08'] ,
        'lieux' : 'à Paris La Défense Arena' ,
        'histoire' : ['1908'],
        'nb_medailles' : [46, 8, 16, 22]
        },
    'natation_artistique' : {
        'name' : 'natation artistique',
        'epreuves' : ['duo libre', 'duo technique', 'finale des duos', 'équipes libres', 'équipes techniques'],
        'date' : ['05/08','06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : 'au Centre Aquatique' ,
        'histoire' : ['1984'],
        'nb_medailles' : [1, 0, 0, 1]
        },
    'natation_marathon' : {
        'name' : 'natation marathon',
        'epreuves' : '10 km',
        'date' : ['08/08','09/08'] ,
        'lieux' : 'au Pont Alexandre III, dans la Seine (départ)' ,
        'histoire' : ['2008'],
        'nb_medailles' : [1, 0, 0, 1]
        },
    'plongeon' : {
        'name' : 'plongeon',
        'epreuves' : ['tremplin haut-vol 10m', 'tremplin haut-vol 10m synchronisé', 'tremplin 3m', 'tremplin 3m synchronisé'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : 'au Centre Aquatique' ,
        'histoire' : ['1904'],
        'nb_medailles' : [1, 0, 1, 0]
        },
    'waterpolo' : {
        'name' : 'water-polo',
        'date' : ['05/08','06/08','07/08','08/08', '09/08','10/08', '11/08'] ,
        'lieux' : ['au Centre aquatique (pour le tournois)', 'à Paris La Défense Arena (pour les finales)'] ,
        'histoire' : ['1900'],
        'nb_medailles' : [3, 1, 0, 2]
        },

    'equestre' : {
        'name' : 'sports équestres',
        'epreuves' : ['concours complet individuel', 'concours complet par équipes', 'dressage individuel', 'dressage par équipes', 'saut d’obstacle individuel', 'saut d’obstacle par équipes'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08'] ,
        'lieux' : 'au Château de Versailles' ,
        'histoire' : ['1900'],
        'nb_medailles' : [37, 14, 12, 11]
        },
    'taekw' : {
        'name' : 'taekwondo',
        'epreuves' : ['homme -58kg, -68kg, -80kg et +80kg', 'femme -49kg, -57kg, -67kg et +67kg'],
        'date' : ['07/08','08/08', '09/08','10/08'] ,
        'lieux' : 'au Grand Palais' ,
        'histoire' : ['1988'],
        'nb_medailles' : [8, 0, 3, 5]
        },
    'tennis' : {
        'name' : 'tennis',
        'epreuves' : ['simple', 'double'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08'] ,
        'lieux' : 'au Stade Roland-Garros' ,
        'histoire' : ['1896'],
        'nb_medailles' : [21, 5, 8, 8]
        },
    'ping' : {
        'name' : 'tennis de table',
        'epreuves' : ['simple', 'double (mixte)', 'par équipes'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : 'à l\'Arena Paris Sud' ,
        'histoire' : ['1988'],
        'nb_medailles' : [2, 0, 1, 1]
        },
    'tir' : {
        'name' : 'tir',
        'epreuves' : ['pistolet à air comprimé 10m', 'carabine à air comprimé 10m', 'carabine 50m 3 positions', 'skeet olympique', 'fosse olympique', 'pistolet rapide 25m'],
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08'] ,
        'lieux' : 'au Centre National de tir de Châteauroux' ,
        'histoire' : ['1896'],
        'nb_medailles' : [39, 12, 16, 11]
        },
    'tir_a_arc' : {
        'name' : 'tir à l\'arc',
        'epreuves' : ['individuel', 'par équipes'],
        'date' : ['25/07', '26/07', '27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08'] ,
        'lieux' : 'aux Invalides' ,
        'histoire' : ['1900'],
        'nb_medailles' : [25, 7, 11, 7]
        },
    'triat' : {
        'name' : 'triathlon',
        'epreuves' : ['individuel', 'en relais'],
        'date' : ['30/07', '31/07','05/08'] ,
        'lieux' : 'à partir du Pont Alexandre III' ,
        'histoire' : ['2000'],
        'nb_medailles' : [1, 0, 0, 1]
        },
    'voile' : {
        'name' : 'voile',
        'epreuves' : ['dériveur solitaire ILCA 6, skiff 49er FX, planche à voile IQ foil et formula kite (épreuves féminines)', 'dériveur solitaire ILCA 7, skiff 49er, planche à voile IQ foil et formula kite (épreuves masculines)', 'multicoque mixte Nacra 17 à foils et dériveur double mixte – 470 (épreuves mixtes)'],
        'date' : ['28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08'] ,
        'lieux' : 'à la Marina de Marseille' ,
        'histoire' : ['1900'],
        'nb_medailles' : [39, 13, 11, 15]
        },
    'volley' : {
        'name' : 'volleyball',
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08', '11/08'] ,
        'lieux' : 'à l\'Arena Paris Sud' ,
        'histoire' : ['1964'],
        'nb_medailles' : [1, 1, 0, 0]
        },
    'beach' : {
        'name' : 'volleyball de plage',
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08', '05/08','06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : 'au Stade Tour Eiffel' ,
        'histoire' : ['1992'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'breaking' : {
        'name' : 'break dance',
        'epreuves' : 'battle de breaking (style de danse)(non-mixte)',
        'date' : ['09/08','10/08'] ,
        'lieux' : 'à la Place de la Concorde' ,
        'histoire' : ['2024']
        },
    'escalade' : {
        'name' : 'escalade sportive',
        'epreuves' : ['combiné bloc-difficulté', 'vitesse'],
        'date' : ['05/08','06/08','07/08','08/08', '09/08','10/08'] ,
        'lieux' : 'au site d\escalade du Bourget' ,
        'histoire' : ['2020'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'surf' : {
        'name' : 'surf',
        'epreuves' : 'shortboard',
        'date' : ['27/07', '28/07','29/07', '30/07', '31/07', '01/08','02/08', '03/08','04/08'] ,
        'lieux' : 'à Teahupo’o, à Tahiti' ,
        'histoire' : ['2020'],
        'nb_medailles' : [0, 0, 0, 0]
        },
    'skate' : {
        'name' : 'skateboard',
        'epreuves' : ['skateboard street', 'skateboard park'],
        'date' : ['27/07', '28/07','06/08','07/08'] ,
        'lieux' : 'à la Place de la Concorde' ,
        'histoire' : ['2020'],
        'nb_medailles' : [0, 0, 0, 0]
        },
}
