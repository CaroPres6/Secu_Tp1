# quand tout est bien séparé dans crypto, retirer os,csv...
import os
import sys
from pathlib import Path
import csv

# ajouter TP1 au path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


from utils.auth import load_csv, check_login, hash_password
from utils.crypto_utils import pt_1, load_pw_from_csv

# appel fonction pour la partie 1
pt_1()

# partie 2


## avec salt impossible trouver password

# mettre cette fonction dans crypto_utils quand fini et
# faire appel fonction
def brute_force():
    users_db = load_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_plain.csv'))
    # mettre les psw dans liste or smtg...
    for usr in users_db:
        username = usr['username']
        for pwd in list :
            if check_login(username, pwd, users_db, mode = 'password_only'):
                print('Login réussi')
            else:
                print('Login échoué') 

# pour chq pw hash
# compare pw myspace avec pw plain
