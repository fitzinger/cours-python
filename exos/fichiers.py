# -*- coding: utf-8 -*-

# Cette ligne permet l'utilisation de codecs.decode(), c.f. ligne 21
import codecs

mystere = ["Gur Mra bs Clguba, ol Gvz Crgref\n\n",
           "Ornhgvshy vf orggre guna htyl.\n",
           "Rkcyvpvg vf orggre guna vzcyvpvg.\n"]

# On écrit ces chaînes de caractères dans le fichier "coded.txt"
f = open('coded.txt', mode='w')
f.writelines(mystere)
f.close()

# On relit le contenu du fichier "coded.txt" que l'on vient de créer
f = open('coded.txt', mode='r')
coded = f.read()
f.close()

# On décode le message mystérieux
decoded = codecs.decode(coded, encoding='rot13')

# On écrit le message décodé dans un autre fichier
f = open('decoded.txt', mode='w')
f.write(decoded)
f.close()

# Vous pouvez ensuite aller consulter le message décodé dans le fichier "decoded.txt"
