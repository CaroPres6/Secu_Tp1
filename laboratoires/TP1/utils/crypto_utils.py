import random
import os
import sys
from pathlib import Path

# ajouter TP1 au path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.auth import load_csv, check_login, hash_password

# tp1 chiffrement
def create_permutation():
    alphabet = [chr(ord('a') + a) for a in range(26)]
    alpha_shuffled = alphabet.copy()
    random.shuffle(alpha_shuffled)
    return dict(zip(alphabet, alpha_shuffled))

def encrypt(text,shift,permutation):
    ciphertext = ""
    for char in text:
        if char.islower():
            # faire le shift
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # faire la permu.
            ciphertext += permutation[shifted]
        elif char.isupper():
            # faire le shift
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            shifted_lower = shifted.lower()
            permuted = permutation[shifted_lower]
            ciphertext += permuted.upper()
        else:
            ciphertext += char
    return ciphertext

def decrypt(cipher, shift, permutation):
    plaintext = ""
    # inverser permu.
    permu_reverse = {v: k for k, v in permutation.items()}
    for char in cipher:
        if char.islower():
            non_permuted = permu_reverse[char]
        # inverser shift
            original = chr((ord(non_permuted) - ord('a') - shift) % 26 + ord('a'))
            plaintext += original
        elif char.isupper():
            char_lower = char.lower()
            non_permuted = permu_reverse[char_lower]
            original = chr((ord(non_permuted) - ord('A') - shift) % 26 + ord('A'))
            plaintext += original
        else: 
            plaintext += char
    return plaintext

# tp2 passwords
def pt_1():
    # accède au répertoire et construit le chemin jusqu'au fichier voulu
    users_db = load_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'passwords_plain.csv'))
    if check_login('user02','mchawks0018@aim.com', users_db, mode='password_only'):
        print('Login réussi')
    else:
        print('Login échoué')
