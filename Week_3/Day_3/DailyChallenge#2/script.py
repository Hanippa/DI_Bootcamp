# Instructions :

# Consider this list

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

#     Look at this result :

# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}

# You have to recreate the result using a translator module.

from translate import Translator
translator= Translator(from_lang="fr",to_lang="en")
translation = {}
for i in french_words:
    translation[i] = translator.translate(i)
print(translation)