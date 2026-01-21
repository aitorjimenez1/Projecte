
game_context = {}

characters = {
    1:"Entrenador Pokémon Naranja",
    2:"Estudiante Pepe"
}

adventures = {
    1:{
        "nombre_aventura":"Aventura Pokémon",
        "descripcion_aventura":"Hoy es el día, el profesor Pokémon te dará a elegir 1 de entre 3 Pokémon como tu Pokémon inicial. Emprenderás tu aventura en este maravilloso mundo de Pokémon, tu objetivo es hacerte fuerte junto a tus Pokémon y volverte campeón de la Liga Pokémon.",
        "characters":list(characters.keys())},
    2:{
        "nombre_aventura":"El camino de la espada",
        "descripcion_aventura":"Eres un espadachín de nivel intermedio que sueña con llegar a la cima de la espada, convertirte en un maestro de la espada. Vives en un pequeño pueblo llamada pueblo Eridu, y eres el guardian de este pueblo.",
        "characters":list(characters.keys())},
    3:{
        "nombre_aventura":"¡Llego tarde a clase!",
        "descripcion_aventura":"Hoy tu alarma no sonó y te despiertas muy a gusto en la cama. Te levantas perezosamente y lo primero que haces es mirar el móvil, dandote cuenta que es lunes y que vas a llegar tarde a clase. Te sobresaltas y empiezas a prepararte a toda prisa para no llegar tarde.",
        "characters":list(characters.keys())}
}

id_by_steps = {
    #id: {
    #    "Description": "descripció del pas",
    #    "answers_in_step": (tupla amb els ids de les opcions posibles en aquest pas),
    #    "Final_Step": 0 si no és un pas final, 1 si és un pas final},

    1: {"Description": adventures[1]["descripcion_aventura"], "answers_in_step": (1011,1012), "Final_Step": 0},
    111: {"Description": "Decides no ir al laboratorio del profesor Pokémon, piensas que mejor adentrarte a la hierba alta y atrapar tu propio Pokémon. Experimentas el poder de los Pokémon y terminas muy mal herido. Para cuando alguien te encontró ya era muy tarde. FIN", "answers_in_step": (), "Final_Step": 1},
    112: {"Description": "Decides ir al laboratorio del profesor Pokémon a elegir tu Pokémon inicial. Una vez hecho, tu autoproclamado rival (el hijo del profesor) te reta a un combate Pokémon.", "answers_in_step": (1021,1022), "Final_Step": 0},
    121: {"Description": "Aceptas el desafío y tienes tu primer combate Pokémon. Acabas ganando, pero tu rival no se rinde y te jura que se hará más fuerte y te ganará.", "answers_in_step": (131,132), "Final_Step": 0},
    122: {"Description": "Rechazas el combate, el rival te llama aburrido y se va.", "answers_in_step": (131,132), "Final_Step": 0},
    131: {"Description": "Te vas directamente a desafiar a los líderes de gimnasio. Para conseguir las 8 medallas de gimnasio necesarios para participar en la Liga Pokémon", "answers_in_step": (1411), "Final_Step": 0},
    132: {"Description": "Te vas a capturar más Pokémon y a levelearlos", "answers_in_step": (1412,1422), "Final_Step": 0},
    1411: {"Description": "Vas muy de prisa y terminas yendo contra los líderes solo con tu Pokémon inicial al lvl 5. Te dan la paliza de tu vida y decides replantearte las cosas.", "answers_in_step": (131,132), "Final_Step": 0},
}


idAnswers_ByStep_Adventure = {
    #("ID de las respuestas por paso de la aventura", "ID del paso de la aventura (momento actual de la historia)"): {
    #    "Description": "descripció d'aquest pas",
    #    "Resolution_Anwer": 'Texte al camp resolution answer de la taula a la BBDD',
    #    "NextStep_Adventure": id del seguent pas},
    (1011, 1): {"Description": "Ir a la hierba alta a atrapar tu propio Pokémon inicial", "Resolution_Anwer": "Te vas directo a la hierba alta", "NextStep_Adventure": 111},
    (1012, 1): {"Description": "Ir al laboratorio del profesor Pokémon", "Resolution_Anwer": "No haces una estupidez y te diriges al laboratorio", "NextStep_Adventure": 112},
    (1021, 1): {"Description": "Aceptar", "Resolution_Anwer": "Empieza el combate", "NextStep_Adventure": 121},
    (1022, 1): {"Description": "Rechazar", "Resolution_Anwer": "Rechazas el combate", "NextStep_Adventure": 122}
}

replayAdventures = {}

#print(id_by_steps[122]["Description"])