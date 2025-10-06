import sys
from pathlib import Path

# ajouter TP1 au path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# si je mettais seulement from ..utils.crypto_utils import ..., ça me donnait des erreurs
from utils.crypto_utils import create_permutation, encrypt, decrypt

# initialisation des valeurs
permutation = create_permutation()
text = "helloworldthisismyplaintext"
shift = 3
# appel des fonctions de chiffrement et déchiffrement
cipher = encrypt(text, shift, permutation)
print(cipher)
plain = decrypt(cipher, shift, permutation)
print(plain)