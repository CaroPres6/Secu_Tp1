import random

# create_permutation() a implementer: 
def create_permutation():
    alphabet = [chr(ord('a') + a) for a in range(26)]
    alpha_shuffled = alphabet.copy()
    random.shuffle(alpha_shuffled)
    return dict(zip(alphabet, alpha_shuffled))

permutation = create_permutation()

text = "helloworldthisismyplaintext"
shift = 3

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
            # si c'était en upper remettre upper
        else:
            # garder spaces, ponctu
            ciphertext += char
    return ciphertext


def decrypt(cipher, shift, permutation):
    plaintext = ""
    # Inverser permu.
    permu_reverse = {v: k for k, v in permutation.items()}
    for char in cipher:
        if char.islower():
            non_permuted = permu_reverse[char]
        # Inverser shift
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


cipher = encrypt(text, shift, permutation)
print(cipher)
plain = decrypt(cipher, shift, permutation)
print(plain)