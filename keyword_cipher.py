# Assuming key and message to contain only lowercase English alphabet

def keyword_cipher(key, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    remaining_chars = []
    keyset = set(key)
    for char in alphabet:
        if char not in keyset:
            remaining_chars.append(char)
    cipher_alphabet = key + "".join(remaining_chars)

    cipher = []
    for char in message:
        cipher.append(cipher_alphabet[alphabet.index(char)])
    return "".join(cipher)
