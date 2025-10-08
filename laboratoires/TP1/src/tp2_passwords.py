import itertools
import os
import csv
import sys
from pathlib import Path

# ajouter TP1 au path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


from utils.auth import load_csv, check_login, hash_password

# fonction partie 1
def pt_1():
    # accède au répertoire et construit le chemin jusqu'au fichier voulu
    users_db = load_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_plain.csv'))
    if check_login('user02','mchawks0018@aim.com', users_db, mode='password_only'):
        print('Login réussi')
    else:
        print('Login échoué')

# appel fonction pour la partie 1
print('Début de la partie 1')
pt_1()
print('Fin de la partie 1')

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

# appel fonction pour la partie 2
print('Début de la partie 2')
hacked2 = brute_force()
print('Fin de la partie 2')

# fonction pour la partie 3
def create_pwds_hash_csv():
    input_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_plain.csv')
    output_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_hash.csv')
    
    usrs = load_csv(input_file)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['username', 'hashed']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for usr in usrs:
            username = usr['username']
            password = usr['password']
            hashed = hash_password(password)
            writer.writerow({'username': username, 'hashed': hashed})
    print(f"Hash écrits dans : {output_file}")
          
def attack_rainbow_table():
    usrs_db = load_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_hash.csv'))
    
    myspace_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'myspace.txt')
    with open(myspace_file, 'r', encoding='utf-8') as f:
        myspace_pwds = [line.strip() for line in f if line.strip()]
    
    hacked_pwds = {}
    
    for usr, pwd in itertools.product(usrs_db, myspace_pwds):
        username = usr['username']
        
        if username in hacked_pwds:
            continue
        
        if check_login(username, pwd, usrs_db, mode='hash_mode'):
            hacked_pwds[username] = pwd
            print(f'Hash piraté pour {username} : {pwd}')
    return hacked_pwds

# appel fonction pour la partie 3
print('Début de la partie 3')
create_pwds_hash_csv()
hacked3 = attack_rainbow_table()
print('Fin de la partie 3')

# fonctions pour la partie 4
def create_pwds_salty_hash_csv():
    input_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_plain.csv')
    output_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_salty_hash.csv')
    
    usrs = load_csv(input_file)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['username', 'salt', 'salty_hash']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for usr in usrs:
            username = usr['username']
            password = usr['password']
            salt, hashed = hash_password(password, salt=True)
            hex_salt = salt.hex()
            writer.writerow({'username': username, 'salt': hex_salt, 'salty_hash': hashed})

def salty_attack_rainbow_table():
    usrs_db = load_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_salty_hash.csv'))
    
    myspace_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'myspace.txt')
    with open(myspace_file, 'r', encoding='utf-8') as f:
        myspace_pwds = [line.strip() for line in f if line.strip()]
    
    hacked_pwds = {}
    
    for usr, pwd in itertools.product(usrs_db, myspace_pwds):
        username = usr['username']
        
        if username in hacked_pwds:
            continue
        
        hex_salt = usr['salt']
        salt = bytes.fromhex(hex_salt)
        usr_hash = usr['salty_hash']
        
        import hashlib
        hash_to_test = hashlib.sha256(salt + pwd.encode()).hexdigest()
        
        if hash_to_test == usr_hash:
            hacked_pwds[username] = pwd
            print(f'Hash salé piraté pour {username} : {pwd}')
    
    return hacked_pwds
# appel fonction pour la partie 4
print('Début de la partie 4')
create_pwds_salty_hash_csv()
hacked4 = salty_attack_rainbow_table()
print('Fin de la partie 4')
