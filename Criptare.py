def vernam_cipher(text, cheie):
    if len(text) != len(cheie):
        return "Eroare: Lungimea cheii trebuie să fie egală cu cea a mesajului!"
    
    rezultat = ""
    for i in range(len(text)):
        
        char_criptat = chr(ord(text[i]) ^ ord(cheie[i]))
        rezultat += char_criptat
        
    return rezultat


print("===== CIFRUL LUI VERNAM =====")

mesaj = input("Introduceți mesajul: ")
cheie = input(f"Introduceți cheia (exact {len(mesaj)} caractere): ")


criptat = vernam_cipher(mesaj, cheie)
print(f"Mesaj criptat: {criptat}")

decriptat = vernam_cipher(criptat, cheie)
print(f"Mesaj decriptat: {decriptat}")