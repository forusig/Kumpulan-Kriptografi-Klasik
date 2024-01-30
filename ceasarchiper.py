def filter_password(password):
    # Fungsi ini akan menyaring password untuk menghilangkan karakter non-alfabet
    filtered_password = ''.join(c for c in password if c.isalpha())
    return filtered_password

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Tentukan apakah karakter adalah huruf besar atau huruf kecil
            is_upper = char.isupper()
            
            # Konversi karakter ke indeks dalam alfabet (0-25)
            char_index = ord(char.lower()) - ord('a')
            
            # Geser karakter sesuai shift yang diberikan
            char_index = (char_index + shift) % 26
            
            # Konversi kembali ke karakter
            encrypted_char = chr(char_index + ord('a'))
            
            # Jika karakter asli adalah huruf besar, maka ubah karakter yang dienkripsi menjadi huruf besar juga
            if is_upper:
                encrypted_char = encrypted_char.upper()
            
            encrypted_text += encrypted_char
        else:
            # Jika karakter bukan huruf, tambahkan karakter aslinya
            encrypted_text += char
    
    return encrypted_text

# Fungsi untuk menghasilkan kata sandi yang telah dienkripsi
def encrypted_password(password, shift):
    filtered_password = filter_password(password)
    encrypted = caesar_encrypt(filtered_password, shift)
    return encrypted

# Contoh penggunaan:
password = "Ademaul4ni"
shift = 4
encrypted = encrypted_password(password, shift)
print(encrypted)  # Output yang diharapkan: "Zeypz"
