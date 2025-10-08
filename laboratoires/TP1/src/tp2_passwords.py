import itertools
import os
import csv
import sys
from pathlib import Path

# ajouter TP1 au path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


from utils.auth import load_csv, check_login, hash_password
from utils.crypto_utils import pt_1, load_pw_from_csv, brute_force

# fonction partie 1
def pt_1():
    # accède au répertoire et construit le chemin jusqu'au fichier voulu
    users_db = load_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_plain.csv'))
    if check_login('user02','mchawks0018@aim.com', users_db, mode='password_only'):
        print('Login réussi')
    else:
        print('Login échoué')
# appel fonction pour la partie 1
pt_1()
# fonctions partie 2
def brute_force():
    users_db = load_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_plain.csv'))
    pwds_list = load_pw_from_csv('passwords_plain.csv')
    hacked_pwds = {}
    
    for usr, pwd in itertools.product(users_db, pwds_list):
        username = usr['username']
        
        if username in hacked_pwds:
            continue
            
        if check_login(username, pwd, users_db, mode='password_only'):
            hacked_pwds[username] = pwd
            print(f'Mot de passe piraté pour {username} : {pwd}')
    
    return hacked_pwds

def load_pw_from_csv(filename):
    pwds = []
    filepath = os.path.join(os.path.dirname(__file__), '..', 'data', filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # prendre seulement la colonne 'password'
            pwd = row['password'].strip()
            if pwd:
                pwds.append(pwd)
    
    return pwds
# partie 2
hacked = brute_force()

## avec salt impossible trouver password



# compare pw myspace avec pw plain
