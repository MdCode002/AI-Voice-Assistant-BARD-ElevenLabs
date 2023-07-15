import os
from bardapi import Bard
from elevenlabs import generate, play, set_api_key
# KEY API ELEVENLABS
set_api_key("YOUR-API-KEY")
# KEY API BARD
os.environ['_BARD_API_KEY'] = "YOUR-API-KEY"

run = True
while run:
    input_text = input("\n\nEntrer votre message : ")

    input_text = input_text + \
        " (La réponse doit être courte et précise, sans utiliser les symboles * et -.)"
    print('\n merci de patienter \n')
    text = Bard().get_answer(input_text)['content']

    print(text+"\n")
    audio = generate(
        text,
        voice="Adam",
        model="eleven_multilingual_v1"
    )
    play(audio)
    choix = input("Entrer n pour quitter et y pour continuer : ")
    if choix == "y":
        run = True
    else:
        run = False
