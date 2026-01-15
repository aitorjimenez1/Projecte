characters = {
    1:"Entrenador Naranja",
    2:"Espadachín Sirius",
    3:"Estudiante Pepe"}

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
        "descripcion_aventura":"Hoy tu alarma no sonó y te despiertas muy agusto en la cama, te levantas perezosamente y lo primero que haces es mirar el móvil, dandote cuenta que es lunes y que vas a llegar tarde a clase, te sobresaltas y empiezas a prepararte a toda prisa para no llegar tarde.",
        "characters":list(characters.keys())}}

idAnswers_ByStep_Adventure = {
    """
    ("ID de las respuestas por paso de la aventura", "ID del paso de la aventura (momento actual de la historia)"): {
        "Description": "descripció d'aquest pas",
        "Resolution_Anwer": 'Texte al camp resolution answer de la taula a la BBDD', 
        "NextStep_Adventure": id del seguent pas}, 
    """
    }

id_by_steps = {
    """
    id: {
        "Description": "descripció del pas", 
        "answers_in_step": (tupla amb els ids de les opcions posibles en aquest pas), 
        "Final_Step": 0 si no és un pas final, 1 si és un pas final}, 
    """
    1: {'Description': 'Efectivamente, el puente es el c├ímino mas corto, no contabas con que el puente se descolgar├¡a, y no sobrevives a la caida. FIN', 'answers_in_step': (), 'Final_Step': 1},
    }

replayAdventures = {}