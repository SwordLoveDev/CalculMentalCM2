#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Code by Sword

#+---------------------------------------------------------------------+
#+   Importation des différentes bibliothèques utiles pour le script   +
#+---------------------------------------------------------------------+

import time
import os
import sys
import threading
from random import randint
from random import uniform

#+---------------------------------------------------------------------+
#+   banner = arrière plan du script quand on est menu principale      +
#+---------------------------------------------------------------------+

banner = """\033[1;00m\033[91m                                                  		
\033[96m  _____      _            _   __  __            _        _ 
\033[96m / ____|    | |          | | |  \/  |          | |      | |
\033[96m| |     __ _| | ___ _   _| | | \  / | ___ _ __ | |_ __ _| |
\033[96m| |    / _` | |/ __| | | | | | |\/| |/ _ \ '_ \| __/ _` | |
\033[96m| |___| (_| | | (__| |_| | | | |  | |  __/ | | | || (_| | |
\033[96m \_____\__,_|_|\___|\__,_|_| |_|  |_|\___|_| |_|\__\__,_|_|
                      \033[96mCodé par \033[91mSword                                   
\033[96m 
\033[96m                   \033[96mTapez \033[91maide\033[96m pour commencer !	

"""

#+---------------------------------------------------------------------+
#+            left = petit logo à côté de la zone de saisie            +
#+---------------------------------------------------------------------+

left = "\033[96m> \033[91m"

#+---------------------------------------------------------------------+
#+ aide = block pour afficher à l'utilisateur les commandes disponnible+
#+---------------------------------------------------------------------+

aide = """
              \033[00m \033[96m-> Commandes pour \033[91mCalcul Mental\033[96m <-\033[00m  
╔════════════════════════════════════════════════════════════════════╗
║ \033[91maddition        \033[00m| \033[96m Séquence de 10 questions sur les additions      \033[00m║
║ \033[91msoustraction    \033[00m| \033[96m Séquence de 10 questions sur les soustractions  \033[00m║
║ \033[91mmultiplication  \033[00m| \033[96m Séquence de 10 questions sur les multiplications\033[00m║
║ \033[91minfo            \033[00m| \033[96m Informations sur le logiciel                    \033[00m║
║ \033[91mclr             \033[00m| \033[96m Pour néttoyer le terminal                       \033[00m║
║ \033[91mquitter         \033[00m| \033[96m Pour quitter le logiciel                        \033[00m║
╚════════════════════════════════════════════════════════════════════╝\033[00m
"""

#+---------------------------------------------------------------------+
#+                     info = info sur le script                       +
#+---------------------------------------------------------------------+

info = """

  \033[00m \033[96m-> Informations sur \033[91mCalcul Mental\033[96m <-\033[00m

\033[00m[+]\033[96m Bonjour et bienvenue dans le script \033[91mCalcul Mental\033[96m !
\033[96mCe script propose un entrainement pour les \033[91mCE2\033[96m sur les \033[91mMathématiques\033[96m...
\033[96mCe logiciel est donc \033[91mcertifier\033[96m par les spécialistes de l'enseignement.

\033[00m[+]\033[96m A travers \033[91mCalcul Mental\033[96m, vous pourrez :
\033[00m- \033[96mVous entrainer sur les simples calculs mentals du niveau CE2
\033[00m- \033[96mEntrainez vos enfants dessus de menière autonnome
\033[00m- \033[96mEt donc devenir un Dieu en \033[91mMathématiques\033[96m

\033[00m[+]\033[96m Utilistaion de \033[91mCalcul Mental\033[96m :
\033[00m- \033[96mL'utiliser sous python3
\033[00m- \033[96mLe lancer dans un terminal sous linux avec la commande : \033[91mpython3 CalculMental.py\033[96m
\033[00m- \033[96mLe script est conçue pour être lancé dans un terminal

\033[00m[+]\033[96m Création de \033[91mCalcul Mental\033[96m :
\033[00m- \033[96mCréer le \033[91m07/25/2020\033[96m
\033[00m- \033[96mCodé entièrement par Sword
\033[00m- \033[96mVersion \033[91m1.0 Beta
"""

#+---------------------------------------------------------------------+
#+         Inscription de texte lors du démarrage du script            +
#+---------------------------------------------------------------------+

os.system ("clear")
print("\033[00m[+]\033[96m Bonjour et bienvenue dans le script \033[91mCalcul Mental\033[96m !")
time.sleep(3)
print("\033[00m[+]\033[96m Ce script propose un entrainement pour les \033[91mCE2\033[96m sur les \033[91mMathématiques\033[96m...")
time.sleep(4)
print("\033[00m[+]\033[96m Ce logiciel est donc \033[91mcertifier\033[96m par les spécialistes de l'enseignement.")
time.sleep(4)
os.system ("clear")
print(banner)

#+---------------------------------------------------------------------+
#+ Fonction addition pour l'éxercice des additions avec 10 questions   +
#+---------------------------------------------------------------------+

def additions():
	os.system ("clear")
	print("\033[96mVous avez lancé l'éxercice sur les \033[91madditions\033[96m, bonne chance !\033[91m")
	time.sleep(3)
	compteur = 0
	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 1\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 2\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 3\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 4\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 5\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 6\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 7\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 8\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 9\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 100))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 + v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 10\033[96m ->  \033[91m{0} \033[96m+\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT  !")

	print("\n\n\033[91mSEQUENCE SUR LES ADDITIONS TERMINER !")

	if compteur <= 5:
		print("\033[96mCe n'est pas \033[91mtrès bien\033[96m, ton résultat est de\033[91m", compteur,"/ 10\033[96m ! Tu peut mieux faire ! ")
	if compteur > 5:
		print("C'est \033[91mtrès bien\033[96m, ton résultat est de\033[91m", compteur,"/ 10\033[96m ! BRAVO ! ")
	
	exitadd = input("\n\033[00m[+]\033[96m Tape \033[91m'1'\033[96m et la touche \033[91m'ENTRER'\033[96m pour recommencer\n\033[00m[+]\033[96m Appuie sur la touche \033[91m'ENTRER'\033[96m pour quitter l'éxercice ...\033[91m\n\033[96m>\033[91m ")

	if exitadd == "":
		os.system ("clear")
		print(banner)
	elif exitadd == "ENTRER": 
		os.system ("clear")
		print(banner)
	elif exitadd == "1": 
		additions()
	return

#+---------------------------------------------------------------------+
#+Fonction soustraction pour l'éxercice des additions avec 10 questions+
#+---------------------------------------------------------------------+

def soustractions():
	os.system ("clear")
	print("\033[96mVous avez lancé l'éxercice sur les \033[91msoustractions\033[96m, bonne chance !\033[91m")
	time.sleep(3)
	compteur = 0
	a1 = int(uniform(50, 100))
	a2 = int(uniform(0, 49))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 1\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(40, 100))
	a2 = int(uniform(0, 39))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 2\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(60, 100))
	a2 = int(uniform(0, 39))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 3\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(50, 100))
	a2 = int(uniform(0, 49))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 4\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 100))
	a2 = int(uniform(0, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 5\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(40, 100))
	a2 = int(uniform(0, 39))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 6\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(50, 100))
	a2 = int(uniform(0, 49))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 7\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(20, 40))
	a2 = int(uniform(0, 19))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 8\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(50, 100))
	a2 = int(uniform(0, 49))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 9\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(70, 100))
	a2 = int(uniform(0, 69))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 - v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 10\033[96m ->  \033[91m{0} \033[96m-\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT  !")

	print("\n\n\033[91mSEQUENCE SUR LES ADDITIONS TERMINER !")

	if compteur <= 5:
		print("\033[96mCe n'est pas \033[91mtrès bien\033[96m, ton résultat est de\033[91m", compteur,"/ 10\033[96m ! Tu peut mieux faire ! ")
	if compteur > 5:
		print("C'est \033[91mtrès bien\033[96m, ton résultat est de\033[91m", compteur,"/ 10\033[96m ! BRAVO ! ")
	
	exitadd = input("\n\033[00m[+]\033[96m Tape \033[91m'1'\033[96m et la touche \033[91m'ENTRER'\033[96m pour recommencer\n\033[00m[+]\033[96m Appuie sur la touche \033[91m'ENTRER'\033[96m pour quitter l'éxercice ...\033[91m\n\033[96m>\033[91m ")

	if exitadd == "":
		os.system ("clear")
		print(banner)
	elif exitadd == "ENTRER": 
		os.system ("clear")
		print(banner)
	elif exitadd == "1": 
		soustractions()
	return

#+-----------------------------------------------------------------------+
#+Fonction mutliplication pour l'éxercice des additions avec 10 questions+
#+-----------------------------------------------------------------------+

def multiplications():
	os.system ("clear")
	print("\033[96mVous avez lancé l'éxercice sur les \033[91mmutliplications\033[96m, bonne chance !\033[91m")
	time.sleep(3)
	compteur = 0
	a1 = int(uniform(0, 10))
	a2 = int(uniform(0, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 1\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(1, 10))
	a2 = int(uniform(1, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 2\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 10))
	a2 = int(uniform(0, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 3\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(1, 10))
	a2 = int(uniform(1, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 4\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 10))
	a2 = int(uniform(0, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 5\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(1, 10))
	a2 = int(uniform(1, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 6\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 10))
	a2 = int(uniform(0, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 7\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(0, 10))
	a2 = int(uniform(0, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 8\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(1, 10))
	a2 = int(uniform(1, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 9\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT !")

	a1 = int(uniform(1, 10))
	a2 = int(uniform(1, 10))
	add = [a1, a2]
	v1 = add[0]
	v2 = add[1]
	qa1 = v1 * v2
	inputstring = "\n\033[00m[+]\033[96m Question \033[91mNUMERO 10\033[96m ->  \033[91m{0} \033[96mx\033[91m {1} \033[96m= \033[91m".format(v1, v2)
	rep1 = int(input(inputstring))
	if rep1 == qa1:
		compteur = compteur + 1 
		print("\033[96mBonne reponse ! La reponse était bien\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc maintenant \033[91m", compteur, "\033[96mPOINT !")
	else:
		print("\033[91mFAUX ! \033[96mLa reponse était\033[91m", qa1, "\033[96m!")
		print("\033[96mTu as donc toujours\033[91m", compteur, "\033[96mPOINT  !")

	print("\n\n\033[91mSEQUENCE SUR LES MULTIPLICATIONS TERMINER !")

	if compteur <= 5:
		print("\033[96mCe n'est pas \033[91mtrès bien\033[96m, ton résultat est de\033[91m", compteur,"/ 10\033[96m ! Tu peut mieux faire ! ")
	if compteur > 5:
		print("C'est \033[91mtrès bien\033[96m, ton résultat est de\033[91m", compteur,"/ 10\033[96m ! BRAVO ! ")
	
	exitadd = input("\n\033[00m[+]\033[96m Tape \033[91m'1'\033[96m et la touche \033[91m'ENTRER'\033[96m pour recommencer\n\033[00m[+]\033[96m Appuie sur la touche \033[91m'ENTRER'\033[96m pour quitter l'éxercice ...\033[91m\n\033[96m>\033[91m ")

	if exitadd == "":
		os.system ("clear")
		print(banner)
	elif exitadd == "ENTRER": 
		os.system ("clear")
		print(banner)
	elif exitadd == "1": 
		multiplications()
	return

#+---------------------------------------------------------------------+
#+   Boucle infinie qui permet de connaitre les commandes lancées par  +
#+     l'utilisateur pour en suite lancer les opérations demander      +
#+---------------------------------------------------------------------+

while True:
	sin = input(left).lower()
	if sin == "aide":
		print(aide)

	elif sin == "clr":
		os.system ("clear")
		print(banner)

	elif sin == "quitter":
		print("\033[96mMerci d'avoir utilisé \033[91mCalcul Mental\033[96m, à bientôt !")
		time.sleep(3)
		os.system ("clear")
		exit()

	elif sin == "addition":
		additions()

	elif sin == "soustraction":
		soustractions()

	elif sin == "multiplication":
		multiplications()

	elif sin == "info":
		print(info)

	else:
		print("\033[96mCommande pas trouvée, tapez \033[91maide\033[96m pour plus d'information !")
		

	
	
		
		



			
