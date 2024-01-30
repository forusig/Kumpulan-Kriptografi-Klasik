def polyalphabet(plaintext, abjad, kunci):
    hasil = kunci+abjad
    result = "".join(dict.fromkeys(hasil))

    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            char = char.lower()
            encrypted_char = result[abjad.index(char)]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            
    return encrypted_text

def main():
    abjad = "abcdefghijklmnopqrstuvwxyz"
    kunci = "merdeka"
    plaintext = input("Masukkan teks yang ingin dienkripsi: ").lower()

    encrypted_text = polyalphabet(plaintext, abjad, kunci)
    print("Teks terenkripsi:", encrypted_text)

main()
